import os
import shutil
import schedule
import time
import pyautogui
from datetime import datetime

# Diretórios (modifique conforme necessário)
ORIGEM = 'C:/Users/SeuUsuario/Downloads'
DESTINO_BACKUP = 'C:/Backup/Downloads_Backup'

# Organiza arquivos por tipo
def organizar_arquivos():
    print(f"[{datetime.now()}] Organizando arquivos...")
    for arquivo in os.listdir(ORIGEM):
        caminho_completo = os.path.join(ORIGEM, arquivo)
        if os.path.isfile(caminho_completo):
            extensao = arquivo.split('.')[-1]
            pasta_destino = os.path.join(ORIGEM, extensao.upper())
            os.makedirs(pasta_destino, exist_ok=True)
            shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
    print("Arquivos organizados.")

# Faz backup da pasta de origem
def fazer_backup():
    print(f"[{datetime.now()}] Fazendo backup...")
    if not os.path.exists(DESTINO_BACKUP):
        os.makedirs(DESTINO_BACKUP)

    for item in os.listdir(ORIGEM):
        caminho_origem = os.path.join(ORIGEM, item)
        caminho_destino = os.path.join(DESTINO_BACKUP, item)
        if os.path.isdir(caminho_origem):
            shutil.copytree(caminho_origem, caminho_destino, dirs_exist_ok=True)
        else:
            shutil.copy2(caminho_origem, caminho_destino)
    print("Backup concluído.")

# Simula clique em um ponto específico da tela
def clicar_na_tela():
    print(f"[{datetime.now()}] Clicando automaticamente na tela...")
    x, y = 100, 200  # Altere conforme a posição desejada
    pyautogui.click(x, y)
    print("Clique realizado.")

# Agendando tarefas
schedule.every().day.at("10:00").do(organizar_arquivos)
schedule.every().day.at("10:05").do(fazer_backup)
schedule.every().day.at("10:10").do(clicar_na_tela)

print("Automação iniciada. Pressione Ctrl+C para encerrar.")

while True:
    schedule.run_pending()
    time.sleep(1)
