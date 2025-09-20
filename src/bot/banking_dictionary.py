"""
Diccionario de palabras clave bancarias para procesamiento de lenguaje natural.
Contiene sinónimos, variaciones y expresiones comunes utilizadas en consultas bancarias.
"""

# Diccionario principal de intenciones y sus palabras clave
BANKING_INTENTS = {
    "balance": {
        "keywords": [
            "saldo", "balance", "cuánto", "cuanto", "monto", "total", "tengo", "plata", "dinero",
            "disponible", "disponibilidad", "fondos", "ahorro", "ahorros", "cuenta", "cuenta corriente",
            "caja de ahorro", "caja ahorro", "cuanto tengo", "cuánto tengo", "mi saldo", "ver saldo",
            "consultar saldo", "saldo actual", "dinero disponible", "plata disponible"
        ],
        "variations": [
            "¿cuánto dinero tengo?", "¿cuánta plata tengo?", "mi saldo actual", "ver mi balance",
            "¿tengo plata?", "¿hay dinero en mi cuenta?", "estado de cuenta", "consulta de saldo"
        ]
    },
    
    "transactions": {
        "keywords": [
            "movimientos", "transacciones", "historial", "resumen", "actividad", "operaciones",
            "compras", "gastos", "ingresos", "egresos", "últimos", "recientes", "pasados",
            "todos", "completo", "detalle", "detallado", "listado", "registro", "bitácora",
            "extracto", "estado de cuenta", "movimientos bancarios", "actividad de cuenta"
        ],
        "variations": [
            "¿qué movimientos tengo?", "mis últimas transacciones", "historial de compras",
            "ver mis gastos", "¿qué compré?", "mis ingresos", "todos mis movimientos",
            "resumen de actividad", "últimas operaciones", "gastos recientes"
        ]
    },
    
    "loans": {
        "keywords": [
            "préstamo", "prestamo", "crédito", "credito", "financiamiento", "financiación",
            "cuotas", "pago", "pagos", "mensual", "mensualidad", "mensualidades", "interés",
            "intereses", "tasa", "tasa de interés", "simular", "simulación", "calcular",
            "cotizar", "cotización", "solicitar", "solicitud", "banco", "personal",
            "hipotecario", "automotriz", "consumo", "libre inversión", "libre inversion"
        ],
        "variations": [
            "quiero un préstamo", "necesito crédito", "simular préstamo", "calcular cuotas",
            "¿cuánto pago por mes?", "tasa de interés", "préstamo personal", "crédito de consumo",
            "financiamiento automotriz", "préstamo hipotecario", "libre inversión"
        ]
    },
    
    "cards": {
        "keywords": [
            "tarjeta", "tarjetas", "tarjeta de crédito", "tarjeta credito", "débito", "debito",
            "visa", "mastercard", "american express", "amex", "classic", "gold", "platinum",
            "beneficios", "beneficio", "ventajas", "límite", "limite", "límite de crédito",
            "limite credito", "solicitar", "solicitud", "aplicar", "aplicación", "oferta",
            "ofertas", "promoción", "promociones", "cashback", "cash back", "puntos",
            "millas", "descuentos", "descuento"
        ],
        "variations": [
            "¿qué tarjetas tienen?", "tarjetas de crédito", "tarjeta de débito", "solicitar tarjeta",
            "beneficios de tarjeta", "límite de crédito", "tarjeta gold", "tarjeta platinum",
            "cashback", "puntos por compra", "descuentos con tarjeta"
        ]
    },
    
    "investments": {
        "keywords": [
            "plazo fijo", "plazofijo", "plazo fijo", "inversión", "inversion", "invertir",
            "rentabilidad", "rentable", "tasa", "tasa de interés", "intereses", "ganancia",
            "ganancias", "rendimiento", "ahorro", "ahorros", "capital", "capitalizar",
            "fondo común", "fondo común de inversión", "fci", "bonos", "acciones", "bolsa",
            "mercado", "riesgo", "conservador", "moderado", "agresivo"
        ],
        "variations": [
            "¿conviene plazo fijo?", "inversiones seguras", "dónde invertir", "mejor tasa",
            "fondo de inversión", "bonos del gobierno", "riesgo bajo", "inversión conservadora",
            "capitalizar ahorros", "hacer crecer dinero"
        ]
    },
    
    "transfers": {
        "keywords": [
            "transferir", "transferencia", "transferencias", "enviar", "enviar dinero",
            "mandar", "mandar plata", "enviar plata", "giro", "giros", "depósito",
            "deposito", "depositar", "depositar dinero", "ingresar", "ingresar dinero",
            "cbu", "alias", "cuenta destino", "cuenta de destino", "beneficiario",
            "destinatario", "recibir", "recibir dinero", "entrada", "salida"
        ],
        "variations": [
            "quiero transferir", "enviar dinero", "hacer transferencia", "depositar en cuenta",
            "recibir transferencia", "giro bancario", "transferencia nacional", "transferencia internacional"
        ]
    },
    
    "help": {
        "keywords": [
            "ayuda", "help", "soporte", "asistencia", "qué puedo", "que puedo", "opciones",
            "menú", "menu", "servicios", "servicio", "funciones", "funcionalidades",
            "comandos", "comando", "cómo", "como", "cómo funciona", "como funciona",
            "qué haces", "que haces", "para qué sirves", "para que sirves"
        ],
        "variations": [
            "¿qué puedes hacer?", "¿cómo te uso?", "menú de opciones", "servicios disponibles",
            "¿para qué sirves?", "necesito ayuda", "no entiendo", "¿qué opciones tengo?"
        ]
    },
    
    "schedule": {
        "keywords": [
            "horario", "horarios", "atención", "atencion", "abierto", "cerrado", "funciona",
            "cuándo", "cuando", "abren", "cierran", "días", "dias", "lunes", "martes",
            "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo",
            "feriado", "feriados", "sábados", "sabados", "domingos", "fin de semana",
            "hora", "horas", "mañana", "mañana", "tarde", "noche"
        ],
        "variations": [
            "¿A qué hora abren?", "¿Cuáles son los horarios?", "¿Están abiertos los sábados?",
            "¿A qué hora cierran?", "¿Funcionan los domingos?", "¿Qué días atienden?",
            "¿Cuándo están abiertos?", "Horarios de atención", "¿Está abierto ahora?",
            "¿Atienden los feriados?", "¿Cuándo cierran los viernes?"
        ]
    },
    
    "account_info": {
        "keywords": [
            "información", "informacion", "cuenta", "datos", "resumen", "estadísticas",
            "estadisticas", "contador", "contadores", "interacciones", "simulaciones",
            "mi cuenta", "datos de cuenta", "info", "información personal", "informacion personal",
            "cuántas veces", "cuantas veces", "veces", "número", "numero", "cantidad",
            "total", "totales", "cuántos", "cuantos", "cuántas", "cuantas"
        ],
        "variations": [
            "¿Cuántas veces consulté mi saldo?", "¿Cuántos préstamos simule?", "Mi información de cuenta",
            "¿Cuántas interacciones tengo?", "Resumen de mi cuenta", "Datos de mi cuenta",
            "¿Cuántas veces vi mis movimientos?", "Estadísticas de mi cuenta", "Contadores de uso"
        ]
    }
}

# Palabras de cortesía y expresiones comunes
COURTESY_WORDS = [
    "por favor", "gracias", "muchas gracias", "disculpa", "perdón", "hola", "buenos días",
    "buenas tardes", "buenas noches", "saludos", "quedo atento", "saludos cordiales"
]

# Saludos y despedidas
GREETINGS = [
    "hola", "hi", "hey", "buenos días", "buenas tardes", "buenas noches", 
    "saludos", "qué tal", "que tal", "cómo estás", "como estas",
    "buen día", "buen dia", "buena tarde", "buena noche", "buenas",
    "hola buenos días", "hola buenas tardes", "hola buenas noches",
    "buenos días", "buenas tardes", "buenas noches", "qué tal todo",
    "que tal todo", "cómo va", "como va", "todo bien", "todo ok"
]

FAREWELLS = [
    "chau", "chao", "adiós", "adios", "hasta luego", "nos vemos", "nos vemos pronto",
    "hasta pronto", "hasta la próxima", "hasta la proxima", "que tengas buen día",
    "que tengas buen dia", "que tengas buena tarde", "que tengas buena noche",
    "gracias por todo", "gracias por la ayuda", "muchas gracias", "perfecto",
    "perfecto gracias", "ok gracias", "ok, gracias", "listo", "listo gracias",
    "ya está", "ya esta", "listo gracias", "perfecto gracias", "ok perfecto",
    "gracias", "gracias totales", "gracias por todo", "chau gracias",
    "hasta luego gracias", "nos vemos gracias", "listo hasta luego"
]

# Respuestas de saludo
GREETING_RESPONSES = [
    "¡Hola! ¿En qué puedo ayudarte hoy?",
    "¡Hola! Bienvenido a tu asistente bancario. ¿En qué te puedo ayudar?",
    "¡Hola! Estoy aquí para ayudarte con tus consultas bancarias.",
    "¡Buenos días! ¿En qué puedo asistirte?",
    "¡Buenas tardes! ¿Qué consulta tienes para mí?",
    "¡Hola! Soy tu asistente bancario virtual. ¿Cómo puedo ayudarte?",
    "¡Hola! ¿Qué tal? ¿En qué puedo ayudarte?",
    "¡Buenos días! Estoy aquí para resolver tus consultas bancarias.",
    "¡Hola! ¿Cómo va todo? ¿En qué te puedo asistir?",
    "¡Buenas! Bienvenido, ¿qué necesitas saber hoy?"
]

# Respuestas de despedida
FAREWELL_RESPONSES = [
    "¡Hasta luego! Que tengas un excelente día.",
    "¡Chau! Estoy aquí cuando necesites ayuda.",
    "¡Hasta pronto! Cualquier consulta, no dudes en preguntarme.",
    "¡Que tengas un buen día! Hasta la próxima.",
    "¡Perfecto! Gracias por usar nuestro asistente bancario.",
    "¡Hasta luego! Recuerda que siempre estoy disponible para ayudarte.",
    "¡Perfecto! Que tengas un lindo día.",
    "¡Listo! Cualquier cosa, acá estoy.",
    "¡Chau! Fue un placer ayudarte.",
    "¡Hasta la próxima! Siempre disponible para tus consultas."
]

# Palabras de negación
NEGATION_WORDS = [
    "no", "nunca", "jamás", "tampoco", "ningún", "ninguna", "ninguno", "ningunas", "ningunos"
]

# Números escritos en español
NUMBER_WORDS = {
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
    "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
    "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
    "ochenta": 80, "noventa": 90, "cien": 100, "mil": 1000, "millón": 1000000
}

# Expresiones de tiempo
TIME_EXPRESSIONS = [
    "últimos", "recientes", "pasados", "anteriores", "hoy", "ayer", "esta semana",
    "este mes", "este año", "último mes", "último año", "pasado mes", "pasado año"
]

# Monedas y cantidades
CURRENCY_EXPRESSIONS = [
    "pesos", "peso", "$", "dólares", "dolar", "dolares", "usd", "euros", "euro",
    "miles", "millones", "mil", "millón", "millones"
]

def get_intent_keywords():
    """Retorna todas las palabras clave organizadas por intención."""
    return BANKING_INTENTS

def get_all_keywords():
    """Retorna una lista plana de todas las palabras clave."""
    all_keywords = []
    for intent_data in BANKING_INTENTS.values():
        all_keywords.extend(intent_data["keywords"])
        all_keywords.extend(intent_data["variations"])
    return all_keywords

def is_greeting(text: str) -> bool:
    """Detecta si el texto es un saludo."""
    text_lower = text.lower().strip()
    return any(greeting in text_lower for greeting in GREETINGS)

def is_farewell(text: str) -> bool:
    """Detecta si el texto es una despedida."""
    text_lower = text.lower().strip()
    return any(farewell in text_lower for farewell in FAREWELLS)

def get_random_greeting() -> str:
    """Retorna un saludo aleatorio."""
    import random
    return random.choice(GREETING_RESPONSES)

def get_random_farewell() -> str:
    """Retorna una despedida aleatoria."""
    import random
    return random.choice(FAREWELL_RESPONSES)

def find_intent_by_keywords(text: str) -> list:
    """
    Encuentra las intenciones que coinciden con las palabras clave en el texto.
    Retorna una lista de intenciones ordenadas por relevancia.
    """
    text_lower = text.lower()
    intent_scores = {}
    
    for intent, data in BANKING_INTENTS.items():
        score = 0
        
        # Puntúa por palabras clave
        for keyword in data["keywords"]:
            if keyword.lower() in text_lower:
                score += 2
        
        # Puntúa más por variaciones exactas
        for variation in data["variations"]:
            if variation.lower() in text_lower:
                score += 3
        
        if score > 0:
            intent_scores[intent] = score
    
    # Retorna intenciones ordenadas por puntuación
    return sorted(intent_scores.keys(), key=lambda x: intent_scores[x], reverse=True)

def clean_text(text: str) -> str:
    """
    Limpia el texto removiendo caracteres especiales y normalizando.
    """
    import re
    # Remover caracteres especiales excepto números y espacios
    cleaned = re.sub(r'[^\w\s\d]', ' ', text.lower())
    # Remover espacios múltiples
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned
