import os
import google.cloud.dialogflow_v2 as dialogflow

# Substitua pelo caminho real do seu arquivo JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\kauan\\OneDrive\\Documentos\\Agente IA - Code\\assistentevirtual-nwhs-ced6af972d20.json"

def detect_intent_texts(project_id, session_id, text, language_code):
    """Envia um texto para o Dialogflow e recebe a resposta"""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    # Criando entrada de texto para a consulta
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    # Detectando intenção
    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text

# Testando com uma pergunta
if __name__ == "__main__":
    project_id = "assistentevirtual-nwhs"  # Substitua pelo ID do seu projeto Dialogflow
    session_id = "123456"  # ID da sessão (pode ser qualquer número)
    pergunta = "Oi, como você está?"  # Texto que será enviado ao bot

    resposta = detect_intent_texts(project_id, session_id, pergunta, "pt-BR")
    print("Resposta do Dialogflow:", resposta)
