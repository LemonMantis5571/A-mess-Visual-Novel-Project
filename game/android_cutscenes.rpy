image splash = "images/bg afterdark.jpg"

define transition = Dissolve(2.0)

label splashscreen:
    scene black
    $renpy.pause(delay = 2, hard = True)
    show text "E2L Presents..." with dissolve
    play sound "audio/intro.mp3"
    $renpy.pause(delay = 3.5, hard = True)

    
    show text "Visual Novel Project: A mess..." with transition

    $renpy.pause(delay = 5, hard = True)

    scene black with dissolve
    $renpy.pause(delay = 1, hard = True)

    return