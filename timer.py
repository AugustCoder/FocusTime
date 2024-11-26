import time
from animations import display_focus_mode

def format_timer(seconds):
    """Formatea el temporizador en minutos y segundos."""
    mins, secs = divmod(seconds, 60)
    return f"{mins:02}:{secs:02}"

def display_progress_bar(current, total, bar_length=40):
    """Muestra una barra de progreso dinámica."""
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    return bar

def countdown(seconds, phase):
    """Realiza una cuenta regresiva con barra de progreso."""
    total_time = seconds
    display_focus_mode(phase)
    while seconds > 0:
        timer = format_timer(seconds)
        bar = display_progress_bar(total_time - seconds, total_time)
        print(f"\r{timer} |{bar}| {total_time - seconds}/{total_time} segundos", end='')
        time.sleep(1)
        seconds -= 1
    print("\r¡Tiempo terminado!                      ")
