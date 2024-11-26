from utils import clear_screen, notify, play_sound
from timer import countdown
from animations import loading_animation

def pomodoro_cycle(work_duration, short_break, long_break, cycles):
    """Gestiona el ciclo completo del temporizador Pomodoro."""
    completed_sessions = 0

    for cycle in range(cycles):
        clear_screen()
        print(f"--- Ciclo {cycle + 1} de {cycles} ---")
        
        # Sesión de trabajo
        print("Inicio de la sesión de trabajo:")
        countdown(work_duration * 60, "work")
        completed_sessions += 1
        
        # Descanso corto
        if cycle < cycles - 1:  # No hacer descanso corto después del último ciclo
            notify("¡Tiempo de descanso corto!")
            play_sound()
            print("¡Tiempo de descanso corto!")
            countdown(short_break * 60, "break")
            loading_animation(5)  # Animación de transición

    # Descanso largo
    notify("¡Ciclos de trabajo completados! Tiempo de descanso largo.")
    play_sound()
    print("¡Tiempo de descanso largo!")
    countdown(long_break * 60, "long_break")
    loading_animation(10)  # Animación de transición más larga

    print(f"Total de sesiones completadas: {completed_sessions}")
