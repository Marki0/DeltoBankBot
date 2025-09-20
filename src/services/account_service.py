import random
from persistence.data_manager import (
    load_users_data, save_users_data, load_transactions_data, save_transactions_data,
    increment_interaction_count, get_user_account_info, create_user_account
)

def get_user_balance(user_id):
    """Obtiene el saldo simulado de un usuario."""
    users = load_users_data()
    user_data = users.get(str(user_id), {})
    return user_data.get("balance", 0)

def get_user_transactions(user_id):
    """Obtiene una lista de transacciones simuladas y actualiza contadores."""
    transactions = load_transactions_data()
    
    # Incrementar contador de consultas de movimientos
    increment_interaction_count(str(user_id), "movements")
    
    return transactions.get(str(user_id), [])

def simulate_initial_data(user_id):
    """Genera saldo y transacciones iniciales simuladas para un nuevo usuario."""
    # Crear cuenta de usuario si no existe
    create_user_account(str(user_id))
    
    users = load_users_data()
    transactions = load_transactions_data()

    # Genera un saldo inicial aleatorio
    balance = random.randint(1000, 50000)
    users[str(user_id)]["balance"] = balance
    
    # Simula 5 transacciones si el usuario no tiene ninguna
    if str(user_id) not in transactions:
        transactions[str(user_id)] = []
        transaction_types = ["Compra en línea", "Supermercado", "Servicios públicos", "Transferencia recibida"]
        for i in range(5):
            amount = random.randint(-1000, 1000)
            if amount < 0:
                description = random.choice(transaction_types)
            else:
                description = "Transferencia recibida"
            
            transactions[str(user_id)].append({
                "id": i + 1,
                "amount": amount,
                "description": description,
                "date": "2025-09-19" # Fecha estática
            })
    
    save_users_data(users)
    save_transactions_data(transactions)

def get_account_summary(user_id):
    """Obtiene un resumen completo de la cuenta del usuario."""
    return get_user_account_info(str(user_id))