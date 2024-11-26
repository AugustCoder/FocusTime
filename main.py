from pomodoro import pomodoro_cycle

if __name__ == "__main__":
    # Parámetros configurables
    WORK_DURATION = 25  # Duración de trabajo en minutos
    SHORT_BREAK = 5     # Duración del descanso corto en minutos
    LONG_BREAK = 15     # Duración del descanso largo en minutos
    CYCLES = 4          # Número de ciclos

    pomodoro_cycle(WORK_DURATION, SHORT_BREAK, LONG_BREAK, CYCLES)
