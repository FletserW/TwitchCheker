import requests
import time
import webbrowser
import os
import subprocess  # Para executar o script do chat

# Verificar se esta em execução
LOCK_FILE = "twitch_checker.lock"

if os.path.exists(LOCK_FILE):
    print("O script já está rodando!")
    exit()

# Criar o arquivo de bloqueio
with open(LOCK_FILE, "w") as lock:
    lock.write("Rodando")

try:
    # Código principal do Twitch Checker
    print("Executando o Twitch Checker...")
    # (coloque seu código aqui)
finally:
    # Remover o arquivo de bloqueio quando o script encerrar
    os.remove(LOCK_FILE)

# Criar um log para saber se esta em exexução
LOG_FILE = "twitch_checker.log"

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

log_message("Iniciando o Twitch Checker...")

# Configurações
CLIENT_ID = "wj8h3e5u68p8fzmmabekecrv8uecws"
CLIENT_SECRET = "54yzyjxjgvv04az3sv0p6hujiwl8b7"
CHANNEL_NAME = "trixxiemix"
CHECK_INTERVAL = 600  # Tempo em segundos entre verificações
CHAT_SCRIPT = "twitch_chat.py"  # Nome do script do chat

# Obtém o token de acesso
def get_access_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    return response.json().get("access_token")

# Verifica se a live está online
def is_live(access_token):
    url = f"https://api.twitch.tv/helix/streams?user_login={CHANNEL_NAME}"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return bool(data["data"])

# Loop de monitoramento
if __name__ == "__main__":
    token = get_access_token()
    while True:
        if is_live(token):
            print(f"A live de {CHANNEL_NAME} começou! 🎥")
            
            # Abre a live no navegador
            webbrowser.open(f"https://www.twitch.tv/{CHANNEL_NAME}")
            
            # Espera 1 minuto antes de mandar mensagem no chat
            print("⏳ Esperando 1 minuto antes de enviar mensagem no chat...")
            time.sleep(60)
            
            # Executa o script que envia mensagem no chat
            print("💬 Enviando mensagem no chat...")
            subprocess.run(["python", CHAT_SCRIPT])

            break  # Sai do loop após detectar a live
        else:
            print(f"A live de {CHANNEL_NAME} ainda não começou... ⏳")
        time.sleep(CHECK_INTERVAL)