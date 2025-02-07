# Twitch Live Notifier & Chat Bot

Este projeto monitora um canal da Twitch e, quando a live começa, abre automaticamente a página da transmissão no navegador. Após 1 minuto, ele executa um script para enviar uma mensagem no chat do canal.

## 📌 Funcionalidades
- Monitora automaticamente a transmissão de um canal específico da Twitch.
- Abre a live no navegador assim que detectada.
- Aguarda 1 minuto e envia uma mensagem no chat via API da Twitch.
- Registra logs das atividades do script.
- Impede múltiplas execuções simultâneas.

---

## 🛠️ Requisitos
- Python 3.x
- Conta de desenvolvedor na Twitch
- Credenciais da API da Twitch (Client ID e Client Secret)
- Biblioteca `requests` instalada

Instale as dependências com:
```sh
pip install requests
```

---

## 🚀 Configuração
### 1️⃣ **Obtenha suas credenciais da API da Twitch**
1. Acesse [Twitch Developer Console](https://dev.twitch.tv/console/apps)
2. Crie um novo aplicativo.
3. Defina o tipo como **Confidencial** para obter um Client Secret.
4. Copie o **Client ID** e o **Client Secret**.

### 2️⃣ **Configure o script**
Abra `twitchChecker.py` e edite as seguintes variáveis:
```python
CLIENT_ID = "seu_client_id"
CLIENT_SECRET = "seu_client_secret"
CHANNEL_NAME = "nome_do_canal"
CHECK_INTERVAL = 1800  # Tempo em segundos entre verificações
```

---

## 📜 Scripts
### `twitchChecker.py`
Este é o script principal que monitora a live e abre a Twitch no navegador.

**Execução:**
```sh
python twitchChecker.py
```

### `twitch_chat.py`
Este script é chamado pelo `twitchChecker.py` para enviar uma mensagem no chat da Twitch.

**Execução manual:**
```sh
python twitch_chat.py
```

---

## ⏳ Automação no Windows
### Opção 1: Agendando a Tarefa no Windows
1. Abra o **Agendador de Tarefas**.
2. Crie uma nova tarefa.
3. Configure para rodar `twitchChecker.bat` no login do usuário.
4. Salve e ative a tarefa.

### Opção 2: Criando um Arquivo `.bat`
Crie um arquivo `twitchChecker.bat` no mesmo diretório do script:
```bat
@echo off
cd /d "C:\caminho\para\o\projeto"
python twitchChecker.py
exit
```
Adicione esse arquivo ao **Iniciar** do Windows.

---

## 📝 Logs
O script registra logs de execução no arquivo `twitch_checker.log`.

---

## 📌 Observações
- Certifique-se de que `twitchChecker.py` tem permissão para acessar a internet.
- O script pode falhar se o Client ID ou Secret estiverem errados.

---

## 📜 Licença
Este projeto é de código aberto. Sinta-se livre para modificar e melhorar!

---

Desenvolvido por FletserW 🚀

