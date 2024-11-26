import os
import subprocess

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('clear')

def notify(message):
    """Envía una notificación al escritorio."""
    subprocess.run(['notify-send', message])

def play_sound():
    """Reproduce un sonido de notificación."""
    sound_path = '/usr/share/sounds/freedesktop/stereo/complete.oga'  # Ajusta según tu sistema
    subprocess.run(['paplay', sound_path])
