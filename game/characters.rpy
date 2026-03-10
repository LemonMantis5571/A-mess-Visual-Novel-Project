# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Meifeng = Character("Meifeng", color="#FFD700")
define Blezz = Character("Blezz", color="#ff99cc")
define Isela = Character("Miss Isela", color="#b3b3ff")
define Grettell = Character("Grettell", color="#ff00ff")
define Nuria = Character("Nuria", color="#8cff66",  what_slow_cps=30, what_slow_abortable=False)
define Tamy  = Character("Tamy", color="#6666ff",  what_slow_cps=30, what_slow_abortable=False)
define Rachel = Character("Rachel", color="#ff6666",  what_slow_cps=30, what_slow_abortable=False)
define Yves = Character("Yves", color="#ff66ff",  what_slow_cps=30, what_slow_abortable=False)
define Talya = Character("Talya", color="#ff00ff", what_slow_cps=30, what_slow_abortable=False)
define Ozuna = Character("Ozuna", color="#ff12ff", what_slow_cps=45, what_slow_abortable=False)
define guide = Character("Juan Caldera", color="#FFD700", what_slow_cps=30, what_slow_abortable=False)

transform dizzy(m, t):
    subpixel True
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat
