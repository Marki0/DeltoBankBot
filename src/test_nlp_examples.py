"""
Archivo de pruebas para demostrar las capacidades de NLP del bot bancario.
Contiene ejemplos de consultas en lenguaje natural que el bot puede procesar.
"""

from bot.processor import process_user_query
from bot.banking_dictionary import find_intent_by_keywords
import asyncio

# Ejemplos de consultas en lenguaje natural
TEST_QUERIES = {
    "balance": [
        "¿Cuánto dinero tengo?",
        "Mi saldo actual",
        "¿Cuánta plata tengo disponible?",
        "Ver mi balance",
        "¿Tengo dinero en mi cuenta?",
        "Estado de mi cuenta",
        "Consulta de saldo por favor"
    ],
    
    "transactions": [
        "Mis últimos movimientos",
        "¿Qué compré recientemente?",
        "Ver todas mis transacciones",
        "Historial completo de gastos",
        "Mis últimas 5 compras",
        "Resumen de actividad de mi cuenta",
        "¿Cuáles fueron mis últimos egresos?"
    ],
    
    "loans": [
        "Quiero un préstamo de 100000 en 24 cuotas",
        "Simular crédito personal de 500000 a 36 meses",
        "¿Cuánto pagaría por un préstamo de 250000 en 12 cuotas?",
        "Necesito financiamiento de 750000 en 48 cuotas",
        "Préstamo de 150000 en 18 meses",
        "Simular préstamo personal 300000 en 24 cuotas"
    ],
    
    "cards": [
        "¿Qué tarjetas tienen disponibles?",
        "Información sobre la tarjeta Gold",
        "Tarjeta Classic beneficios",
        "Solicitar tarjeta Platinum",
        "¿Cuáles son los límites de las tarjetas?",
        "Tarjetas de crédito disponibles"
    ],
    
    "investments": [
        "¿Conviene hacer un plazo fijo?",
        "Inversiones seguras disponibles",
        "¿Qué tasa tiene el plazo fijo?",
        "Fondos de inversión conservadores",
        "¿Dónde puedo invertir mi dinero?",
        "Opciones de inversión de bajo riesgo"
    ],
    
    "transfers": [
        "¿Cómo hago una transferencia?",
        "Enviar dinero a otra cuenta",
        "Transferencias nacionales",
        "¿Cuánto cuesta enviar dinero?",
        "Giro bancario internacional",
        "Depositar dinero en otra cuenta"
    ],
    
    "help": [
        "¿Qué puedes hacer?",
        "Ayuda",
        "¿Para qué sirves?",
        "Servicios disponibles",
        "¿Cómo te uso?",
        "Menú de opciones"
    ],
    
    "schedule": [
        "¿A qué hora abren?",
        "¿Cuáles son los horarios?",
        "¿Están abiertos los sábados?",
        "¿A qué hora cierran?",
        "¿Funcionan los domingos?",
        "¿Qué días atienden?",
        "¿Cuándo están abiertos?",
        "Horarios de atención",
        "¿Está abierto ahora?",
        "¿Atienden los feriados?"
    ],
    
    "account_info": [
        "¿Cuántas veces consulté mi saldo?",
        "¿Cuántos préstamos simule?",
        "Mi información de cuenta",
        "¿Cuántas interacciones tengo?",
        "Resumen de mi cuenta",
        "Datos de mi cuenta",
        "¿Cuántas veces vi mis movimientos?",
        "Estadísticas de mi cuenta",
        "Contadores de uso",
        "Información personal"
    ],
    
    "courteous": [
        "Por favor, ¿podrías decirme mi saldo?",
        "Muchas gracias, ¿cuánto tengo disponible?",
        "Disculpa, ¿podrías ayudarme con un préstamo?",
        "Hola, gracias por la atención. ¿Qué tarjetas tienen?",
        "Buenos días, ¿conviene hacer un plazo fijo?"
    ],
    
    "greetings": [
        "Hola",
        "Buenos días",
        "Buenas tardes",
        "¿Qué tal?",
        "¿Cómo estás?",
        "Buenas",
        "¡Hola!",
        "¿Qué tal todo?",
        "Todo bien",
        "¿Cómo va?"
    ],
    
    "farewells": [
        "Chau",
        "Adiós",
        "Hasta luego",
        "Gracias",
        "Perfecto gracias",
        "Listo",
        "Ok gracias",
        "Hasta pronto",
        "Nos vemos",
        "Gracias por todo"
    ],
    
    "complex": [
        "Hola, por favor necesito saber cuánto tengo y también quiero simular un préstamo de 200000 en 30 cuotas",
        "Buenos días, ¿podrías decirme mis últimos movimientos y qué tarjetas tienen disponibles?",
        "Gracias, necesito información sobre inversiones seguras y también sobre transferencias internacionales"
    ]
}

async def test_query_intent_detection():
    """Prueba la detección de intenciones."""
    print("🔍 **PRUEBA DE DETECCIÓN DE INTENCIONES**\n")
    
    for intent, queries in TEST_QUERIES.items():
        print(f"📋 **{intent.upper()}**:")
        for query in queries:
            detected_intents = find_intent_by_keywords(query.lower())
            primary_intent = detected_intents[0] if detected_intents else "No detectado"
            print(f"  • '{query}' → {primary_intent}")
        print()

async def test_natural_language_processing():
    """Prueba el procesamiento de lenguaje natural completo."""
    print("🤖 **PRUEBA DE PROCESAMIENTO DE LENGUAJE NATURAL**\n")
    
    # Usuario simulado
    test_user_id = 12345
    
    # Probar diferentes tipos de consultas
    test_cases = [
        "Hola, ¿cuánto dinero tengo en mi cuenta?",
        "Por favor, ¿podrías mostrarme mis últimos movimientos?",
        "Quiero simular un préstamo de 150000 en 24 cuotas",
        "¿Qué tarjetas de crédito tienen disponibles?",
        "¿Conviene hacer un plazo fijo actualmente?",
        "¿Cómo puedo hacer transferencias?",
        "Gracias, ¿qué servicios ofrecen?",
        "¿Podrías ayudarme con información sobre inversiones?",
        "Necesito un crédito de 300000 en 36 meses",
        "¿Cuál es el límite de la tarjeta Gold?",
        "¿A qué hora abren?",
        "Horarios de atención",
        "¿Cuántas interacciones tengo?",
        "Mi información de cuenta",
        "Hola",
        "Buenos días",
        "Chau",
        "Gracias por todo"
    ]
    
    for i, query in enumerate(test_cases, 1):
        print(f"**Consulta {i}:** '{query}'")
        try:
            response = await process_user_query(test_user_id, query)
            print(f"**Respuesta:** {response}")
        except Exception as e:
            print(f"**Error:** {e}")
        print("-" * 80)
        print()

async def test_greetings_and_farewells():
    """Prueba específicamente saludos y despedidas."""
    print("👋 **PRUEBA DE SALUDOS Y DESPEDIDAS**\n")
    
    test_user_id = 12345
    
    # Probar saludos
    print("**SALUDOS:**")
    greeting_examples = [
        "Hola", "Buenos días", "Buenas tardes", "¿Qué tal?", "¿Cómo estás?",
        "Buenas", "¡Hola!", "¿Qué tal todo?", "Todo bien", "¿Cómo va?"
    ]
    
    for greeting in greeting_examples:
        print(f"  Usuario: '{greeting}'")
        try:
            response = await process_user_query(test_user_id, greeting)
            print(f"  Bot: {response}")
        except Exception as e:
            print(f"  Error: {e}")
        print()
    
    print("**DESPEDIDAS:**")
    farewell_examples = [
        "Chau", "Adiós", "Hasta luego", "Gracias", "Perfecto gracias",
        "Listo", "Ok gracias", "Hasta pronto", "Nos vemos", "Gracias por todo"
    ]
    
    for farewell in farewell_examples:
        print(f"  Usuario: '{farewell}'")
        try:
            response = await process_user_query(test_user_id, farewell)
            print(f"  Bot: {response}")
        except Exception as e:
            print(f"  Error: {e}")
        print()

async def test_edge_cases():
    """Prueba casos límite y consultas ambiguas."""
    print("⚠️ **PRUEBA DE CASOS LÍMITE**\n")
    
    test_user_id = 12345
    
    edge_cases = [
        "No entiendo nada",
        "Préstamo de 0 en 0 cuotas",
        "Quiero un préstamo de 10000000 en 200 cuotas",
        "Tarjeta inexistente",
        "Mi saldo y también quiero un préstamo de 100000 en 12 cuotas"
    ]
    
    for query in edge_cases:
        print(f"**Consulta:** '{query}'")
        try:
            response = await process_user_query(test_user_id, query)
            print(f"**Respuesta:** {response}")
        except Exception as e:
            print(f"**Error:** {e}")
        print("-" * 50)
        print()

def print_dictionary_stats():
    """Muestra estadísticas del diccionario bancario."""
    from bot.banking_dictionary import BANKING_INTENTS, get_all_keywords
    
    print("📊 **ESTADÍSTICAS DEL DICCIONARIO BANCARIO**\n")
    
    total_keywords = 0
    for intent, data in BANKING_INTENTS.items():
        keywords_count = len(data["keywords"]) + len(data["variations"])
        total_keywords += keywords_count
        print(f"🔹 **{intent}**: {keywords_count} palabras clave")
    
    print(f"\n📈 **Total de palabras clave**: {total_keywords}")
    print(f"📈 **Intenciones soportadas**: {len(BANKING_INTENTS)}")

async def main():
    """Función principal para ejecutar todas las pruebas."""
    print("🚀 **SISTEMA DE PRUEBAS - BOT BANCARIO INTELIGENTE**\n")
    print("=" * 80)
    
    # Estadísticas del diccionario
    print_dictionary_stats()
    print("\n" + "=" * 80)
    
    # Prueba de saludos y despedidas
    await test_greetings_and_farewells()
    print("=" * 80)
    
    # Prueba de detección de intenciones
    await test_query_intent_detection()
    print("=" * 80)
    
    # Prueba de procesamiento completo
    await test_natural_language_processing()
    print("=" * 80)
    
    # Prueba de casos límite
    await test_edge_cases()
    
    print("✅ **Todas las pruebas completadas**")

if __name__ == "__main__":
    # Ejecutar las pruebas
    asyncio.run(main())
