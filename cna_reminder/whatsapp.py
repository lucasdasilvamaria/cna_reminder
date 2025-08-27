# whatsapp.py
import pyautogui
import pyperclip
import time

def send_message(message: str, turma_nome: str, livro_nome: str):
    print("[INFO] Copiando mensagem principal para a área de transferência...")
    pyperclip.copy(message)
    print("[INFO] Você tem 15 segundos para colocar o cursor no grupo do WhatsApp Desktop...")
    time.sleep(15)

    # Cola e envia a mensagem principal
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("enter")

    # Segunda mensagem automática
    segunda_msg = f"Enviar para a turma {livro_nome}."
    pyperclip.copy(segunda_msg)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("enter")

    print("[OK] Mensagens enviadas com sucesso!")
