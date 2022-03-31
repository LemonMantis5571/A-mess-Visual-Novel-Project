image splash = "images/bg afterdark.jpg"

define transition = Dissolve(2.0)

label splashscreen:
    scene black
    with Pause(2)
    show text "E2L Presents..." with dissolve
    play sound "audio/intro.mp3"
    with Pause(3.5)

    
    show text "Visual Novel Project: A mess..." with transition

    with Pause(5)

    scene black with dissolve
    with Pause(1)

    return