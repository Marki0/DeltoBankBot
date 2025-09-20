import json
import os
import math # Agregamos math para cálculos financieros más precisos

# Importamos las funciones para manejar datos
from persistence.data_manager import load_users_data, load_loans_data, save_loans_data, increment_interaction_count

def calculate_loan_payment(user_id: int, amount: float, months: int) -> dict:
    """
    Calcula la cuota y el total a pagar de un préstamo, adaptando la tasa
    de interés según el saldo simulado del usuario.
    """
    users = load_users_data()
    user_balance = users.get(str(user_id), {}).get("balance", 0)

    # Definimos las tasas de interés según el saldo
    # A mayor saldo, mejor tasa (menor interés)
    if user_balance > 40000:
        interest_rate = 0.10  # 10% anual para saldos altos
    elif user_balance > 20000:
        interest_rate = 0.15  # 15% anual para saldos medios
    else:
        interest_rate = 0.20  # 20% anual para saldos bajos
        
    monthly_rate = interest_rate / 12
    
    try:
        if months <= 0 or amount <= 0:
            raise ValueError("El número de cuotas y el monto deben ser mayores a 0.")
        
        # Fórmula de cálculo de cuota (sistema francés)
        monthly_payment = (amount * monthly_rate) / (1 - math.pow(1 + monthly_rate, -months))

    except (ZeroDivisionError, ValueError):
        return {"error": "El número de cuotas o el monto no son válidos."}
        
    total_to_pay = monthly_payment * months
    
    return {
        "monthly_payment": round(monthly_payment, 2),
        "total_to_pay": round(total_to_pay, 2),
        "interest_rate": interest_rate,
        "principal": amount,
        "months": months
    }

def save_simulated_loan(user_id: str, loan_data: dict) -> None:
    """
    Guarda los datos de un préstamo simulado y actualiza contadores.
    """
    # Cargar datos existentes
    data = load_loans_data()
    
    if str(user_id) not in data:
        data[str(user_id)] = []
    
    # Agregar timestamp al préstamo
    loan_data["timestamp"] = loan_data.get("timestamp", None)
    if not loan_data.get("timestamp"):
        from datetime import datetime
        loan_data["timestamp"] = datetime.now().isoformat()
    
    data[str(user_id)].append(loan_data)
    
    # Guardar datos
    save_loans_data(data)
    
    # Incrementar contador de interacciones
    increment_interaction_count(str(user_id), "loan")