# FocusTime "Pomodoro"

🎯 FocusTime es una herramienta minimalista y funcional de gestión del tiempo basada en la técnica Pomodoro. Diseñada para mantenerte enfocado mientras trabajas en ciclos temporales, esta herramienta combina simplicidad y estilo para la CLI.

### ¿Cómo funciona?

- Trabaja durante 25 minutos en una tarea específica.
- Toma un descanso corto de 5 minutos.
- Repite este ciclo 4 veces.
- Después del cuarto ciclo, toma un descanso largo de 15 minutos o   más.

### Estructura del Proyecto

La aplicación está organizada en múltiples módulos para facilitar su mantenimiento y extensión:

```python

pomodoro/
│
├── main.py             # Punto de entrada principal.
├── utils.py            # Funciones utilitarias (notificaciones, sonidos, limpieza).
├── animations.py       # Animaciones minimalistas y estéticas.
├── timer.py            # Lógica del temporizador (countdown, barra de progreso).
└── pomodoro.py         # Gestión principal del ciclo Pomodoro.


```

### Cómo Usarlo

Clona el repositorio:

```bash
git clone <URL del repositorio>
cd pomodoro
```
Ejecuta el archivo principal:

```bash
Copiar código
python main.py
```

Personaliza la configuración inicial directamente en main.py:

```bash
WORK_DURATION: Duración de las sesiones de trabajo (en minutos).
SHORT_BREAK: Duración de los descansos cortos (en minutos).
LONG_BREAK: Duración de los descansos largos (en minutos).
CYCLES: Número de ciclos antes del descanso largo.
```

### Mejoras Futura

- Compatibilidad con Windows.
- Integración con Google Calendar para programar sesiones.
- Guardado de estadísticas en un archivo local o base de datos.
