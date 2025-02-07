import socket
import time

# 🔧 Configurações
SERVER = "irc.chat.twitch.tv"
PORT = 6667  # Porta padrão do IRC
TOKEN = "oauth:wz4lzt6dbqhd6cfbzdekzr0clabayt"  # ⚠️ Seu token OAuth (inclua 'oauth:' no começo)
USERNAME = "FletserW"  # ⚠️ Seu nome de usuário na Twitch
CHANNEL = "#trixxiemix"  # ⚠️ Nome do canal (comece com #, ex: "#FletserW")

# Conectar ao servidor IRC da Twitch
sock = socket.socket()
sock.connect((SERVER, PORT))
sock.send(f"PASS {TOKEN}\r\n".encode("utf-8"))
sock.send(f"NICK {USERNAME}\r\n".encode("utf-8"))
sock.send(f"JOIN {CHANNEL}\r\n".encode("utf-8"))

# Aguardar conexão estável
time.sleep(2)

# Enviar mensagem no chat
message = "oiii  trixxi5Oila "
sock.send(f"PRIVMSG {CHANNEL} :{message}\r\n".encode("utf-8"))
print(f"✅ Mensagem enviada no chat de {CHANNEL}: {message}")

# Fechar conexão
sock.close()
