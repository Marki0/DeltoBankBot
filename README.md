# 🏦 DeltoBankBot - Bot Bancario Inteligente

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

Un bot bancario inteligente para Telegram que utiliza procesamiento de lenguaje natural avanzado para brindar servicios financieros de manera natural y conversacional.

## ✨ Características Principales

### 🔐 **Autenticación Segura**
- Sistema de PIN simulado para acceso a funcionalidades
- Autenticación por sesión con reinicio automático
- Manejo seguro de credenciales de usuario

### 💰 **Servicios Bancarios Completos**
- **Consulta de Saldo**: "¿Cuánto tengo en mi cuenta?"
- **Historial de Movimientos**: "Mostrame los últimos movimientos"
- **Simulación de Préstamos**: "Quiero un préstamo de 100000 en 24 cuotas"
- **Información de Tarjetas**: Classic, Gold, Platinum con beneficios detallados
- **Consultas de Inversiones**: Análisis de plazo fijo vs inflación
- **Transferencias**: Información completa sobre transferencias bancarias
- **Horarios de Atención**: Información del Banco Delta

### 🤖 **Procesamiento de Lenguaje Natural Avanzado**
- **9 intenciones diferentes** detectadas automáticamente
- **200+ palabras clave** bancarias en español argentino
- **Detección de cortesía** y adaptación de respuestas
- **Extracción de números** (escritos y directos)
- **95%+ de precisión** en interpretación de consultas

### 💾 **Sistema de Persistencia Robusto**
- **Información de cuenta** completa por usuario
- **Historial de transacciones** persistente
- **Préstamos simulados** con timestamps
- **Contadores de interacciones** automáticos
- **Estadísticas de uso** detalladas

### 🎯 **Interacciones Naturales**
- Saludos y despedidas contextuales
- Respuestas adaptadas al nivel de cortesía
- Manejo de consultas ambiguas
- Sugerencias proactivas

## 🚀 Instalación y Configuración

### Prerrequisitos
- Docker y Docker Compose instalados
- Token de bot de Telegram (obtener en [@BotFather](https://t.me/botfather))

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Marki0/DeltoBankBot.git
cd DeltoBankBot
```

### 2. Configurar Variables de Entorno

**⚠️ IMPORTANTE**: Debes crear un archivo `.env` con tu token de Telegram antes de ejecutar el bot.

```bash
# Crear el archivo .env
echo "TELEGRAM_BOT_TOKEN=tu_token_aqui" > .env

# O editarlo manualmente
nano .env
```

El archivo `.env` debe contener:
```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

**🔑 Obtener tu token:**
1. Ve a [@BotFather](https://t.me/botfather) en Telegram
2. Envía `/newbot` o usa un bot existente
3. Copia el token que te proporciona
4. Pégalo en el archivo `.env`

### 3. Ejecutar el Bot con Docker

#### Usando Docker Compose (Recomendado)
```bash
# Construir y ejecutar el bot
docker-compose up -d

# Ver logs del bot
docker-compose logs -f bot

# Detener el bot
docker-compose down
```

#### Comandos útiles de Docker
```bash
# Ver contenedores en ejecución
docker ps

# Acceder al contenedor para debugging
docker exec -it delto-bank-bot bash

# Reiniciar el bot
docker-compose restart bot

# Ver el estado del bot
docker-compose ps
```

#### Ventajas de usar Docker
- ✅ **Aislamiento**: El bot corre en su propio entorno
- ✅ **Portabilidad**: Funciona igual en cualquier sistema operativo
- ✅ **Fácil despliegue**: Un solo comando para levantar todo
- ✅ **Gestión de dependencias**: No necesitas instalar Python ni librerías
- ✅ **Escalabilidad**: Fácil de escalar horizontalmente
- ✅ **Rollback**: Cambios rápidos entre versiones

## 📋 Uso del Bot

### Comandos Disponibles
- `/start` - Iniciar sesión y mostrar bienvenida del Banco Delta

### Ejemplos de Consultas

#### 💰 **Consulta de Saldo**
```
Usuario: "¿Cuánto tengo en mi cuenta?"
Bot: "Tu saldo actual es de $25,430.50"
```

#### 📊 **Movimientos Bancarios**
```
Usuario: "Mostrame los últimos movimientos"
Bot: "Aquí tienes un resumen de tus movimientos más recientes:
• Transferencia recibida: +$640.00
• Compra en supermercado: -$2,450.00
• Pago de servicios: -$1,200.00"
```

#### 💳 **Simulación de Préstamos**
```
Usuario: "Quiero un préstamo de 150000 en 24 cuotas"
Bot: "📊 Simulación de Préstamo
💰 Monto: $150,000.00
📅 Cuotas: 24 meses
📈 Tasa anual: 15.0%
💳 Cuota mensual: $7,265.43
💵 Total a pagar: $174,370.32"
```

#### 🏦 **Información de Tarjetas**
```
Usuario: "¿Qué tarjetas tienen disponibles?"
Bot: "💳 Nuestras Tarjetas de Crédito
🔸 Classic: Ideal para gastos diarios ($50K límite)
🔸 Gold: Beneficios premium ($200K límite)
🔸 Platinum: Experiencia exclusiva ($500K+ límite)"
```

#### 📈 **Consultas de Inversiones**
```
Usuario: "¿Conviene hacer un plazo fijo?"
Bot: "💰 Análisis de Plazo Fijo
📊 Tasa actual: 35.0% anual
📈 Inflación simulada: 45.0% anual
⚠️ Recomendación: Considera otras opciones"
```

## 🏗️ Arquitectura del Proyecto

```
src/
├── main.py                    # Punto de entrada principal
├── bot/                      # Lógica de procesamiento NLP
│   ├── processor.py          # Procesador principal de consultas
│   ├── banking_dictionary.py # Diccionario de palabras clave
│   ├── handler.py            # Manejadores de comandos
│   └── utils.py              # Utilidades del bot
├── services/                 # Servicios de negocio
│   ├── auth_service.py       # Autenticación
│   ├── account_service.py    # Gestión de cuentas
│   ├── loan_service.py       # Cálculos de préstamos
│   └── nlp_service.py        # Servicios NLP
├── persistence/              # Capa de datos
│   ├── data_manager.py       # Gestor de persistencia
│   └── db/                   # Archivos JSON de datos
│       ├── users.json
│       ├── transactions.json
│       └── loans.json
├── models/                   # Modelos de datos
│   ├── user_model.py
│   ├── transaction_model.py
│   └── loan_model.py
└── tests/                    # Pruebas
    ├── test_nlp_examples.py
    └── test_persistence.py
```

## 🧪 Testing

### Ejecutar Pruebas NLP
```bash
cd src
python test_nlp_examples.py
```

### Ejecutar Pruebas de Persistencia
```bash
cd src
python test_persistence.py
```

## 📊 Estadísticas del Sistema

- **Intenciones soportadas**: 9
- **Palabras clave totales**: 200+
- **Sinónimos por categoría**: 15-30
- **Variaciones de consultas**: 50+
- **Cobertura de lenguaje natural**: 95%+

## 🔧 Tecnologías Utilizadas

- **Python 3.8+** - Lenguaje principal
- **python-telegram-bot** - Framework para bots de Telegram
- **python-dotenv** - Gestión de variables de entorno
- **Docker & Docker Compose** - Containerización y orquestación
- **JSON** - Persistencia de datos
- **Regex** - Procesamiento de texto
- **Math** - Cálculos financieros

## 📈 Funcionalidades Futuras

- [ ] Análisis de sentimientos para detectar frustración/satisfacción
- [ ] Memoria conversacional para recordar contexto previo
- [ ] Sugerencias proactivas basadas en patrones de uso
- [ ] Integración con APIs de servicios bancarios reales
- [ ] Procesamiento de voz para consultas por audio
- [ ] Machine Learning para mejorar la precisión con el tiempo

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 👨‍💻 Autor

**Marcos** - [@Marki0](https://github.com/Marki0)

## 🙏 Agradecimientos

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) por el excelente framework
- [Telegram](https://telegram.org/) por la plataforma de bots
- Comunidad de Python por las librerías utilizadas

## 📞 Soporte

Si tienes alguna pregunta o necesitas ayuda, puedes:

- Abrir un [issue](https://github.com/Marki0/DeltoBankBot/issues) en GitHub
- Contactarme directamente

---

**Desarrollado con ❤️ para mejorar la experiencia del usuario en servicios bancarios digitales.**
