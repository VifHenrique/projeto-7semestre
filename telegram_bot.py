import os
import logging
import google.cloud.dialogflow_v2 as dialogflow
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio
import nest_asyncio  # Solução para evitar conflitos no loop de eventos

# Aplicar correção para Windows e Jupyter Notebook
nest_asyncio.apply()

# Configuração do Token do Telegram
TOKEN = "8109078178:AAGtxhyppDkmpLdOCDQkpgfT7tSLihPXYK8"

# Configuração do Dialogflow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\kauan\\OneDrive\\Documentos\\Agente IA - Code\\assistentevirtual-nwhs-ced6af972d20.json"
PROJECT_ID = "assistentevirtual-nwhs"

# Configuração de Logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Função para enviar mensagens ao Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code="pt-BR"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

# Função que responde mensagens no Telegram
async def responder(update: Update, context: CallbackContext):
    user_message = update.message.text
    chat_id = update.message.chat_id
    resposta = detect_intent_texts(PROJECT_ID, str(chat_id), user_message)
    await update.message.reply_text(resposta)

# Função para iniciar o bot
async def iniciar(update: Update, context: CallbackContext):
    await update.message.reply_text("Olá! Eu sou seu bot. Envie uma mensagem para começar!")

# Configuração do Bot no Telegram
async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", iniciar))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot iniciado...")
    await app.run_polling()

# Executando no Windows sem conflitos
if __name__ == "__main__":
    asyncio.run(main())  # Agora rodando sem problemas









