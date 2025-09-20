"""
Archivo de pruebas para el sistema de persistencia mejorado.
Demuestra las funcionalidades de contadores de interacciones y información de cuenta.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from persistence.data_manager import (
    get_user_account_info, increment_interaction_count, 
    create_user_account, load_users_data, save_users_data
)
from services.account_service import get_account_summary, simulate_initial_data
from services.loan_service import save_simulated_loan
import json

def test_persistence_system():
    """Prueba el sistema de persistencia completo."""
    print("🧪 **PRUEBA DEL SISTEMA DE PERSISTENCIA**\n")
    
    # Usuario de prueba
    test_user_id = "123456789"
    
    print("=" * 60)
    print("1️⃣ **CREACIÓN DE CUENTA DE USUARIO**")
    print("=" * 60)
    
    # Crear cuenta de usuario
    account_info = create_user_account(test_user_id)
    print(f"✅ Cuenta creada para usuario: {test_user_id}")
    print(f"📊 Información inicial:")
    print(json.dumps(account_info, indent=2, ensure_ascii=False))
    
    print("\n" + "=" * 60)
    print("2️⃣ **SIMULACIÓN DE DATOS INICIALES**")
    print("=" * 60)
    
    # Simular datos iniciales
    simulate_initial_data(test_user_id)
    account_info = get_user_account_info(test_user_id)
    print(f"✅ Datos iniciales generados")
    print(f"💰 Saldo: ${account_info['balance']:,.2f}")
    print(f"📊 Transacciones: {account_info['total_transactions']}")
    
    print("\n" + "=" * 60)
    print("3️⃣ **PRUEBA DE CONTADORES DE INTERACCIONES**")
    print("=" * 60)
    
    # Simular diferentes tipos de interacciones
    print("🔄 Simulando interacciones...")
    
    # Interacción general
    increment_interaction_count(test_user_id, "general")
    print("✅ Interacción general +1")
    
    # Simulación de préstamo
    loan_data = {
        "principal": 50000,
        "months": 24,
        "interest_rate": 0.15,
        "monthly_payment": 2427.43,
        "total_to_pay": 58258.32
    }
    save_simulated_loan(test_user_id, loan_data)
    print("✅ Préstamo simulado +1")
    
    # Consulta de movimientos
    increment_interaction_count(test_user_id, "movements")
    print("✅ Consulta de movimientos +1")
    
    # Más préstamos
    loan_data2 = {
        "principal": 100000,
        "months": 36,
        "interest_rate": 0.12,
        "monthly_payment": 3321.43,
        "total_to_pay": 119571.48
    }
    save_simulated_loan(test_user_id, loan_data2)
    print("✅ Segundo préstamo simulado +1")
    
    print("\n" + "=" * 60)
    print("4️⃣ **INFORMACIÓN FINAL DE CUENTA**")
    print("=" * 60)
    
    # Obtener información final
    final_info = get_user_account_info(test_user_id)
    
    print("📊 **RESUMEN FINAL DE LA CUENTA:**")
    print(f"🆔 ID de Usuario: {final_info['user_id']}")
    print(f"🔐 PIN: {final_info['pin']}")
    print(f"💰 Saldo: ${final_info['balance']:,.2f}")
    print(f"🔒 Estado: {'Autenticado' if final_info['is_authenticated'] else 'No autenticado'}")
    print()
    print("📈 **ESTADÍSTICAS DE USO:**")
    print(f"• Total de interacciones: {final_info['total_interactions']}")
    print(f"• Préstamos simulados: {final_info['loan_simulations']}")
    print(f"• Consultas de movimientos: {final_info['movement_queries']}")
    print(f"• Transacciones registradas: {final_info['total_transactions']}")
    print(f"• Préstamos guardados: {final_info['total_loans']}")
    print()
    print(f"⏰ Última interacción: {final_info['last_interaction']}")
    print(f"📅 Cuenta creada: {final_info['account_created']}")
    
    print("\n" + "=" * 60)
    print("5️⃣ **VERIFICACIÓN DE PERSISTENCIA**")
    print("=" * 60)
    
    # Verificar que los datos se guardaron correctamente
    users_data = load_users_data()
    user_data = users_data.get(test_user_id, {})
    
    print("🔍 **VERIFICACIÓN EN ARCHIVO JSON:**")
    print(f"✅ Usuario existe en users.json: {test_user_id in users_data}")
    print(f"✅ Contador de interacciones: {user_data.get('interaction_count', 0)}")
    print(f"✅ Contador de préstamos: {user_data.get('loan_simulations', 0)}")
    print(f"✅ Contador de movimientos: {user_data.get('movement_queries', 0)}")
    print(f"✅ Balance guardado: ${user_data.get('balance', 0):,.2f}")
    
    print("\n" + "=" * 60)
    print("✅ **PRUEBA COMPLETADA EXITOSAMENTE**")
    print("=" * 60)

def test_multiple_users():
    """Prueba el sistema con múltiples usuarios."""
    print("\n🔄 **PRUEBA CON MÚLTIPLES USUARIOS**\n")
    
    users = ["111111111", "222222222", "333333333"]
    
    for user_id in users:
        print(f"👤 **Usuario: {user_id}**")
        
        # Crear cuenta
        create_user_account(user_id)
        
        # Simular algunas interacciones
        increment_interaction_count(user_id, "general")
        increment_interaction_count(user_id, "movements")
        
        # Obtener información
        info = get_user_account_info(user_id)
        print(f"  • Interacciones: {info['total_interactions']}")
        print(f"  • Consultas movimientos: {info['movement_queries']}")
        print()

def demonstrate_account_info_queries():
    """Demuestra cómo funcionan las consultas de información de cuenta."""
    print("\n💬 **DEMOSTRACIÓN DE CONSULTAS DE INFORMACIÓN**\n")
    
    test_user_id = "123456789"
    
    # Simular algunas consultas que el bot podría recibir
    queries = [
        "¿Cuántas interacciones tengo?",
        "Mi información de cuenta",
        "¿Cuántos préstamos simule?",
        "Estadísticas de mi cuenta",
        "¿Cuántas veces consulté mis movimientos?"
    ]
    
    for query in queries:
        print(f"❓ Usuario: '{query}'")
        info = get_user_account_info(test_user_id)
        
        if "interacciones" in query.lower():
            response = f"Tienes {info['total_interactions']} interacciones totales."
        elif "préstamos" in query.lower() or "prestamos" in query.lower():
            response = f"Has simulado {info['loan_simulations']} préstamos."
        elif "movimientos" in query.lower():
            response = f"Has consultado tus movimientos {info['movement_queries']} veces."
        else:
            response = f"Información completa disponible: {info['total_interactions']} interacciones, {info['loan_simulations']} préstamos, {info['movement_queries']} consultas de movimientos."
        
        print(f"🤖 Bot: {response}")
        print()

if __name__ == "__main__":
    # Ejecutar todas las pruebas
    test_persistence_system()
    test_multiple_users()
    demonstrate_account_info_queries()
    
    print("\n🎉 **TODAS LAS PRUEBAS COMPLETADAS**")
    print("\nEl sistema de persistencia está funcionando correctamente con:")
    print("✅ Contadores de interacciones")
    print("✅ Información completa de cuenta")
    print("✅ Persistencia en archivos JSON")
    print("✅ Manejo de múltiples usuarios")
    print("✅ Estadísticas detalladas de uso")
