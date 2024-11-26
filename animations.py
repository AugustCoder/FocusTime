import time

def display_focus_mode(phase):
    """Muestra un indicador minimalista de la fase actual."""
    icons = {
        "work": "🕒 Trabajando...",
        "break": "🛋️ Descansando...",
        "long_break": "☕ Tiempo de relajación..."
    }
    print(f"\n{icons.get(phase, '🌟')}")

def loading_animation(duration=5):
    """Muestra una animación minimalista para descanso."""
    frames = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            print(f"\r{frame} Relájate un momento...", end="")
            time.sleep(0.2)
    print("\r¡Listo!                              ")
