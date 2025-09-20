import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Importamos las funciones que acabamos de crear
from services.auth_service import authenticate_user, is_authenticated
from persistence.data_manager import load_users_data, save_users_data
from services.account_service import simulate_initial_data

from bot.processor import process_user_query

# Configuración básica de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje cuando se emite el comando /start y reinicia la sesión."""
    user_id = update.effective_user.id
    
    users_data = load_users_data()
    # Si el usuario no existe, lo creamos
    if str(user_id) not in users_data:
        users_data[str(user_id)] = {"pin": "1234", "is_authenticated": False}
    # Si el usuario ya existe, reiniciamos su estado a no autenticado
    else:
        users_data[str(user_id)]["is_authenticated"] = False
    
    save_users_data(users_data)
    
    # Generamos datos iniciales si es la primera vez del usuario
    simulate_initial_data(user_id)

    # Bienvenida personalizada del Banco Delta
    welcome_message = """🏦 **¡Bienvenido al Banco Delta!**

¡Hola! Soy tu asistente bancario virtual de Banco Delta. Estoy aquí para ayudarte con todas tus consultas financieras.

🕐 **Nuestros horarios de atención:**
• Lunes a Viernes: 10:00 a 15:00 hs
• Sábados, Domingos y Feriados: Cerrado
       Bot 24/7 Dispoible.
💳 **Servicios disponibles:**
• Consulta de saldo y movimientos
• Simulación de préstamos
• Información de tarjetas
• Consultas sobre inversiones
• Transferencias bancarias

Para acceder a tu cuenta, por favor ingresa tu PIN simulado."""
    
    await update.message.reply_text(welcome_message)
# ... (código anterior)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja los mensajes de texto para autenticación y funcionalidades."""
    user_id = update.effective_user.id
    text = update.message.text.lower()

    if not is_authenticated(user_id):
        if authenticate_user(user_id, text):
            await update.message.reply_text("PIN correcto. ¡Bienvenido! ¿En qué puedo ayudarte?")
        else:
            await update.message.reply_text("PIN incorrecto. Inténtalo de nuevo.")
    else:
        # Ahora, el procesamiento de la consulta se delega al procesador
        response = await process_user_query(user_id, text)
        await update.message.reply_text(response)



def main() -> None:
    """Inicia el bot."""
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN no está configurado.")
        return

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()