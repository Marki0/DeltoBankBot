from services.account_service import get_user_balance, get_user_transactions, get_account_summary
from services.loan_service import calculate_loan_payment, save_simulated_loan
from bot.banking_dictionary import (
    find_intent_by_keywords, clean_text, COURTESY_WORDS, 
    NEGATION_WORDS, NUMBER_WORDS, TIME_EXPRESSIONS, CURRENCY_EXPRESSIONS,
    is_greeting, is_farewell, get_random_greeting, get_random_farewell
)
import re
import random

def extract_numbers_from_text(text: str) -> list:
    """Extrae números del texto, incluyendo números escritos."""
    numbers = []
    
    # Extraer números directamente
    direct_numbers = re.findall(r'\d+(?:\.\d+)?', text)
    numbers.extend([float(n) for n in direct_numbers])
    
    # Extraer números escritos
    words = text.lower().split()
    for word in words:
        if word in NUMBER_WORDS:
            numbers.append(NUMBER_WORDS[word])
    
    return numbers

def detect_courtesy_level(text: str) -> str:
    """Detecta el nivel de cortesía del usuario."""
    text_lower = text.lower()
    courtesy_count = sum(1 for word in COURTESY_WORDS if word in text_lower)
    
    if courtesy_count >= 2:
        return "high"
    elif courtesy_count == 1:
        return "medium"
    else:
        return "low"

def generate_courteous_response(base_response: str, courtesy_level: str) -> str:
    """Genera una respuesta con el nivel de cortesía apropiado."""
    if courtesy_level == "high":
        return f"Por supuesto, {base_response.lower()}. ¡Estoy aquí para ayudarte!"
    elif courtesy_level == "medium":
        return f"¡Por supuesto! {base_response}"
    else:
        return base_response

async def process_user_query(user_id: int, text: str) -> str:
    """
    Interpreta el mensaje del usuario usando NLP inteligente y devuelve 
    la respuesta apropiada con lógica conversacional avanzada.
    """
    # Limpiar y normalizar el texto
    cleaned_text = clean_text(text)
    original_text = text.lower()
    
    # Detectar saludos y despedidas primero
    if is_greeting(original_text):
        return get_random_greeting()
    
    if is_farewell(original_text):
        return get_random_farewell()
    
    # Detectar intenciones usando el diccionario NLP
    intents = find_intent_by_keywords(original_text)
    courtesy_level = detect_courtesy_level(original_text)
    
    # Si no se detecta intención clara, intentar lógica de fallback
    if not intents:
        return await handle_unclear_intent(original_text, courtesy_level)
    
    # Procesar según la intención principal detectada
    primary_intent = intents[0]
    
    if primary_intent == "balance":
        balance = get_user_balance(user_id)
        response = f"Tu saldo actual es de ${balance:.2f}"
        return generate_courteous_response(response, courtesy_level)
    
    elif primary_intent == "transactions":
        return await handle_transactions_query(user_id, original_text, courtesy_level)
    
    elif primary_intent == "loans":
        return await handle_loans_query(user_id, original_text, courtesy_level)
    
    elif primary_intent == "cards":
        return await handle_cards_query(original_text, courtesy_level)
    
    elif primary_intent == "investments":
        return await handle_investments_query(original_text, courtesy_level)
    
    elif primary_intent == "transfers":
        return await handle_transfers_query(user_id, original_text, courtesy_level)
    
    elif primary_intent == "help":
        return await handle_help_query(courtesy_level)
    
    elif primary_intent == "schedule":
        return await handle_schedule_query(courtesy_level)
    
    elif primary_intent == "account_info":
        return await handle_account_info_query(user_id, courtesy_level)
    
    else:
        return await handle_unclear_intent(original_text, courtesy_level)

async def handle_transactions_query(user_id: int, text: str, courtesy_level: str) -> str:
    """Maneja consultas sobre movimientos y transacciones."""
    transactions = get_user_transactions(user_id)
    
    if not transactions:
        response = "No hay movimientos registrados en tu cuenta"
        return generate_courteous_response(response, courtesy_level)
    
    # Detectar si quiere ver todos o solo algunos
    show_all = any(keyword in text for keyword in ["todos", "total", "completo", "todas", "historial completo"])
    show_count = 3 if not show_all else len(transactions)
    
    response = f"Aquí tienes un resumen de tus movimientos{' más recientes' if not show_all else ''}:\n\n"
    
    for i, t in enumerate(transactions[:show_count]):
        amount_text = f"+${t['amount']:.2f}" if t['amount'] > 0 else f"-${abs(t['amount']):.2f}"
        response += f"• {t['description']}: {amount_text}\n"
    
    if len(transactions) > show_count and not show_all:
        response += f"\n(Mostrando {show_count} de {len(transactions)} movimientos. Di 'todos' para ver el historial completo)"
    
    return generate_courteous_response(response, courtesy_level)

async def handle_loans_query(user_id: int, text: str, courtesy_level: str) -> str:
    """Maneja consultas sobre préstamos y créditos."""
    numbers = extract_numbers_from_text(text)
    
    if len(numbers) >= 2:
        amount = numbers[0]
        months = numbers[1]
        
        # Validaciones básicas
        if amount <= 0 or months <= 0:
            response = "El monto y las cuotas deben ser números positivos"
            return generate_courteous_response(response, courtesy_level)
        
        if amount > 5000000:  # Límite máximo simulado
            response = "El monto máximo para préstamos es de $5,000,000"
            return generate_courteous_response(response, courtesy_level)
        
        if months > 120:  # Máximo 10 años
            response = "El plazo máximo es de 120 cuotas (10 años)"
            return generate_courteous_response(response, courtesy_level)
        
        loan_data = calculate_loan_payment(user_id, amount, months)
        
        if "error" in loan_data:
            return generate_courteous_response(loan_data["error"], courtesy_level)
        
        save_simulated_loan(user_id, loan_data)
        
        response = f"📊 **Simulación de Préstamo**\n\n"
        response += f"💰 Monto: ${loan_data['principal']:,.2f}\n"
        response += f"📅 Cuotas: {loan_data['months']} meses\n"
        response += f"📈 Tasa anual: {loan_data['interest_rate'] * 100:.1f}%\n\n"
        response += f"💳 **Cuota mensual: ${loan_data['monthly_payment']:,.2f}**\n"
        response += f"💵 **Total a pagar: ${loan_data['total_to_pay']:,.2f}**\n"
        response += f"💸 **Intereses totales: ${loan_data['total_to_pay'] - loan_data['principal']:,.2f}**"
        
        return generate_courteous_response(response, courtesy_level)
    else:
        response = "Para simular un préstamo, necesito el monto y número de cuotas.\n\n"
        response += "Ejemplos:\n"
        response += "• 'Quiero un préstamo de 100000 en 24 cuotas'\n"
        response += "• 'Simular crédito de 500000 a 36 meses'\n"
        response += "• 'Préstamo personal 250000 en 12 cuotas'"
        return generate_courteous_response(response, courtesy_level)

async def handle_cards_query(text: str, courtesy_level: str) -> str:
    """Maneja consultas sobre tarjetas de crédito."""
    if "classic" in text:
        response = "💳 **Tarjeta Classic**\n\n"
        response += "✅ Límite inicial: $50,000\n"
        response += "✅ Beneficios en supermercados y farmacias\n"
        response += "✅ Ideal para gastos diarios\n"
        response += "✅ Sin costo de mantenimiento el primer año\n"
        response += "✅ Perfecta para estudiantes y jóvenes profesionales"
        
    elif "gold" in text:
        response = "💳 **Tarjeta Gold**\n\n"
        response += "✅ Límite hasta: $200,000\n"
        response += "✅ Seguro de viaje internacional\n"
        response += "✅ Acceso a salas VIP aeropuertos\n"
        response += "✅ Cashback del 1% en todas las compras\n"
        response += "✅ Requiere ingresos mínimos: $100,000/mes"
        
    elif "platinum" in text:
        response = "💳 **Tarjeta Platinum**\n\n"
        response += "✅ Límite premium: $500,000+\n"
        response += "✅ Asistencia personal 24/7\n"
        response += "✅ Acceso a eventos exclusivos\n"
        response += "✅ Cashback del 2% en todas las compras\n"
        response += "✅ Concierge service personalizado\n"
        response += "✅ Para clientes de alto nivel"
        
    else:
        response = "💳 **Nuestras Tarjetas de Crédito**\n\n"
        response += "🔸 **Classic**: Ideal para gastos diarios ($50K límite)\n"
        response += "🔸 **Gold**: Beneficios premium ($200K límite)\n"
        response += "🔸 **Platinum**: Experiencia exclusiva ($500K+ límite)\n\n"
        response += "¿Te gustaría conocer más detalles de alguna en particular?"
    
    return generate_courteous_response(response, courtesy_level)

async def handle_investments_query(text: str, courtesy_level: str) -> str:
    """Maneja consultas sobre inversiones y plazo fijo."""
    if "plazo fijo" in text or "plazofijo" in text:
        tasa_inflacion = 0.45
        tasa_plazo_fijo = 0.35
        
        response = "💰 **Análisis de Plazo Fijo**\n\n"
        response += f"📊 Tasa actual: {tasa_plazo_fijo:.1%} anual\n"
        response += f"📈 Inflación simulada: {tasa_inflacion:.1%} anual\n\n"
        
        if tasa_plazo_fijo > tasa_inflacion:
            response += "✅ **Recomendación: Favorable**\n"
            response += "La tasa supera la inflación, protegiendo tu capital."
        else:
            response += "⚠️ **Recomendación: Considera otras opciones**\n"
            response += "La tasa está por debajo de la inflación."
        
        response += "\n\n💡 **Alternativas**:\n"
        response += "• Fondos comunes de inversión (FCI)\n"
        response += "• Bonos del gobierno\n"
        response += "• Inversiones mixtas"
        
    else:
        response = "💼 **Opciones de Inversión Disponibles**\n\n"
        response += "🔹 **Plazo Fijo**: 35% anual - Inversión segura\n"
        response += "🔹 **FCI Conservador**: 40-45% anual - Riesgo bajo\n"
        response += "🔹 **FCI Moderado**: 50-60% anual - Riesgo medio\n"
        response += "🔹 **FCI Agresivo**: 70%+ anual - Riesgo alto\n\n"
        response += "¿Te interesa alguna opción en particular?"
    
    return generate_courteous_response(response, courtesy_level)

async def handle_transfers_query(user_id: int, text: str, courtesy_level: str) -> str:
    """Maneja consultas sobre transferencias."""
    balance = get_user_balance(user_id)
    
    response = "💸 **Transferencias Bancarias**\n\n"
    response += f"💰 Saldo disponible: ${balance:,.2f}\n\n"
    response += "🔹 **Transferencias Nacionales**:\n"
    response += "• Sin costo entre cuentas propias\n"
    response += "• $50 por transferencia a terceros\n\n"
    response += "🔹 **Transferencias Internacionales**:\n"
    response += "• $200 costo fijo\n"
    response += "• Tiempo: 1-3 días hábiles\n\n"
    response += "Para realizar una transferencia, necesitarás:\n"
    response += "• CBU o Alias del destinatario\n"
    response += "• Monto a transferir\n"
    response += "• Concepto de la operación"
    
    return generate_courteous_response(response, courtesy_level)

async def handle_help_query(courtesy_level: str) -> str:
    """Maneja consultas de ayuda."""
    response = "🤖 **Asistente Bancario - Servicios Disponibles**\n\n"
    response += "💰 **Consulta de Saldo**\n"
    response += "• '¿Cuánto tengo?' / 'Mi saldo'\n\n"
    response += "📊 **Movimientos**\n"
    response += "• 'Mis movimientos' / 'Últimas transacciones'\n\n"
    response += "💳 **Préstamos**\n"
    response += "• 'Quiero un préstamo de X en Y cuotas'\n\n"
    response += "🏦 **Tarjetas**\n"
    response += "• 'Tarjetas disponibles' / 'Tarjeta Gold'\n\n"
    response += "📈 **Inversiones**\n"
    response += "• 'Plazo fijo' / 'Inversiones disponibles'\n\n"
    response += "💸 **Transferencias**\n"
    response += "• 'Transferencias' / 'Enviar dinero'\n\n"
    response += "🕐 **Horarios**\n"
    response += "• '¿A qué hora abren?' / 'Horarios de atención'\n\n"
    response += "¿En qué puedo ayudarte específicamente?"
    
    return generate_courteous_response(response, courtesy_level)

async def handle_schedule_query(courtesy_level: str) -> str:
    """Maneja consultas sobre horarios de atención del Banco Delta."""
    response = "🏦 **Banco Delta - Horarios de Atención**\n\n"
    response += "🕐 **Horarios:**\n"
    response += "• **Lunes a Viernes**: 10:00 a 15:00 hs\n"
    response += "• **Sábados**: Cerrado\n"
    response += "• **Domingos**: Cerrado\n"
    response += "• **Feriados**: Cerrado\n\n"
    response += "📞 **Atención al Cliente:**\n"
    response += "• **Lunes a Viernes**: 08:00 a 18:00 hs\n"
    response += "• **Sábados**: 09:00 a 13:00 hs\n\n"
    response += "🤖 **Asistente Virtual (Este bot):**\n"
    response += "• **Disponible 24/7** para consultas básicas\n\n"
    response += "💡 **Nota**: Para operaciones complejas, te recomendamos acercarte a nuestras sucursales en horario de atención."
    
    return generate_courteous_response(response, courtesy_level)

async def handle_account_info_query(user_id: int, courtesy_level: str) -> str:
    """Maneja consultas sobre información de cuenta del usuario."""
    account_info = get_account_summary(user_id)
    
    response = "👤 **Información de tu Cuenta**\n\n"
    response += f"🆔 **ID de Usuario**: {account_info['user_id']}\n"
    response += f"🔐 **PIN**: {account_info['pin']}\n"
    response += f"💰 **Saldo Actual**: ${account_info['balance']:,.2f}\n"
    response += f"🔒 **Estado**: {'Autenticado' if account_info['is_authenticated'] else 'No autenticado'}\n\n"
    
    response += "📊 **Estadísticas de Uso:**\n"
    response += f"• **Total de interacciones**: {account_info['total_interactions']}\n"
    response += f"• **Préstamos simulados**: {account_info['loan_simulations']}\n"
    response += f"• **Consultas de movimientos**: {account_info['movement_queries']}\n"
    response += f"• **Transacciones registradas**: {account_info['total_transactions']}\n"
    response += f"• **Préstamos guardados**: {account_info['total_loans']}\n\n"
    
    if account_info['last_interaction']:
        from datetime import datetime
        try:
            last_interaction = datetime.fromisoformat(account_info['last_interaction'].replace('Z', '+00:00'))
            response += f"⏰ **Última interacción**: {last_interaction.strftime('%d/%m/%Y %H:%M')}\n"
        except:
            response += f"⏰ **Última interacción**: {account_info['last_interaction']}\n"
    
    if account_info['account_created']:
        try:
            account_created = datetime.fromisoformat(account_info['account_created'].replace('Z', '+00:00'))
            response += f"📅 **Cuenta creada**: {account_created.strftime('%d/%m/%Y %H:%M')}\n"
        except:
            response += f"📅 **Cuenta creada**: {account_info['account_created']}\n"
    
    return generate_courteous_response(response, courtesy_level)

async def handle_unclear_intent(text: str, courtesy_level: str) -> str:
    """Maneja consultas no claras o no entendidas."""
    # Detectar si contiene números (posible consulta de préstamo)
    numbers = extract_numbers_from_text(text)
    if len(numbers) >= 2:
        return await handle_loans_query(None, text, courtesy_level)
    
    # Respuestas contextuales
    if any(word in text for word in ["dinero", "plata", "pesos", "$"]):
        response = "¿Te refieres a tu saldo actual o a alguna consulta específica sobre dinero?"
    elif any(word in text for word in ["cuenta", "banco", "servicio"]):
        response = "¿Necesitas información sobre tu cuenta, servicios bancarios o algo específico?"
    else:
        responses = [
            "No estoy seguro de entender tu consulta. ¿Podrías ser más específico?",
            "¿En qué puedo ayudarte? Puedo consultar tu saldo, movimientos, préstamos y más.",
            "No logro entender completamente. ¿Te refieres a saldo, movimientos, préstamos o tarjetas?"
        ]
        response = random.choice(responses)
    
    return generate_courteous_response(response, courtesy_level)