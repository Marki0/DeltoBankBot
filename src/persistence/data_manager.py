import json
import os
from datetime import datetime

DB_DIR = "src/persistence/db/"
USERS_DB = os.path.join(DB_DIR, "users.json")
TRANSACTIONS_DB = os.path.join(DB_DIR, "transactions.json")
LOANS_DB = os.path.join(DB_DIR, "loans.json")

def load_users_data():
    """Carga los datos de los usuarios desde el archivo JSON."""
    if not os.path.exists(USERS_DB):
        return {}
    try:
        with open(USERS_DB, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está vacío o malformado, devuelve un diccionario vacío
        return {}

def save_users_data(data):
    """Guarda los datos de los usuarios en el archivo JSON."""
    with open(USERS_DB, "w") as f:
        json.dump(data, f, indent=4)

def load_transactions_data():
    """Carga los datos de las transacciones desde el archivo JSON."""
    if not os.path.exists(TRANSACTIONS_DB) or os.stat(TRANSACTIONS_DB).st_size == 0:
        return {}
    with open(TRANSACTIONS_DB, "r") as f:
        return json.load(f)

def save_transactions_data(data):
    """Guarda los datos de las transacciones en el archivo JSON."""
    with open(TRANSACTIONS_DB, "w") as f:
        json.dump(data, f, indent=4)

def load_loans_data():
    """Carga los datos de los préstamos desde el archivo JSON."""
    if not os.path.exists(LOANS_DB) or os.stat(LOANS_DB).st_size == 0:
        return {}
    try:
        with open(LOANS_DB, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_loans_data(data):
    """Guarda los datos de los préstamos en el archivo JSON."""
    with open(LOANS_DB, "w") as f:
        json.dump(data, f, indent=4)

def get_user_account_info(user_id: str) -> dict:
    """Obtiene información completa de la cuenta del usuario."""
    users = load_users_data()
    transactions = load_transactions_data()
    loans = load_loans_data()
    
    user_data = users.get(user_id, {})
    user_transactions = transactions.get(user_id, [])
    user_loans = loans.get(user_id, [])
    
    # Contar interacciones
    interaction_count = user_data.get("interaction_count", 0)
    loan_simulations = user_data.get("loan_simulations", 0)
    movement_queries = user_data.get("movement_queries", 0)
    
    return {
        "user_id": user_id,
        "pin": user_data.get("pin", "1234"),
        "balance": user_data.get("balance", 0),
        "is_authenticated": user_data.get("is_authenticated", False),
        "total_interactions": interaction_count,
        "loan_simulations": loan_simulations,
        "movement_queries": movement_queries,
        "total_transactions": len(user_transactions),
        "total_loans": len(user_loans),
        "last_interaction": user_data.get("last_interaction", None),
        "account_created": user_data.get("account_created", None)
    }

def increment_interaction_count(user_id: str, interaction_type: str = "general") -> None:
    """Incrementa el contador de interacciones del usuario."""
    users = load_users_data()
    
    if user_id not in users:
        users[user_id] = {
            "pin": "1234",
            "is_authenticated": False,
            "balance": 0,
            "interaction_count": 0,
            "loan_simulations": 0,
            "movement_queries": 0,
            "last_interaction": datetime.now().isoformat(),
            "account_created": datetime.now().isoformat()
        }
    
    # Incrementar contador general
    users[user_id]["interaction_count"] = users[user_id].get("interaction_count", 0) + 1
    
    # Incrementar contador específico
    if interaction_type == "loan":
        users[user_id]["loan_simulations"] = users[user_id].get("loan_simulations", 0) + 1
    elif interaction_type == "movements":
        users[user_id]["movement_queries"] = users[user_id].get("movement_queries", 0) + 1
    
    # Actualizar última interacción
    users[user_id]["last_interaction"] = datetime.now().isoformat()
    
    save_users_data(users)

def create_user_account(user_id: str) -> dict:
    """Crea una nueva cuenta de usuario con información completa."""
    users = load_users_data()
    
    if user_id not in users:
        users[user_id] = {
            "pin": "1234",
            "is_authenticated": False,
            "balance": 0,
            "interaction_count": 0,
            "loan_simulations": 0,
            "movement_queries": 0,
            "last_interaction": datetime.now().isoformat(),
            "account_created": datetime.now().isoformat()
        }
        save_users_data(users)
    
    return get_user_account_info(user_id)