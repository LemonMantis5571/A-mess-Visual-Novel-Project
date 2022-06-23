

define Eduguide = Character("Herradora", color="#8a0303", what_slow_cps=30, what_slow_abortable=False)

label Edu_days_guide:
    scene bg blank
    stop music fadeout 1.0
    play music "audio/demonic.mp3" fadein 2.0 volume 0.5
    scene bg eduguide with pixellate

    Eduguide "You again huh."
    Eduguide "The final ARC."
    hide eduguide

label Edu_days_options:
    hide eduguide
    "Select an option."
    show eduguide at left with hpunch
    Eduguide "Bienvenido a la convocatoria de geometria."
    menu:
        "Im stuck.":
            show eduguide with dissolve
            Eduguide "So you are stuck in [EduChapter]'s chapter."
            Eduguide "Maybe you should try to find a way out."
            show eduguide at right with move
            Eduguide "Try to talk and listen to all their songs"
            Eduguide "(?)"
            Eduguide "If you max out status points, maybe you can unlock new paths in the history."
            Eduguide "Press any key to continue."
            hide eduguide
            jump Edu_days_options
        

        "How do I save the game?":
            show eduguide with dissolve
            Eduguide "You can save the game by pressing the save key in the options below the screen."
            Eduguide "You can also load the game by pressing the load key."
            show eduguide at right with move
            Eduguide "Very simple to use."
            jump Edu_days_options
        
        "How do I change the music?":
            show eduguide at right with move
            Eduguide "You can change the music by unlocking them in the main history."
            Eduguide "As you are progressing, you will unlock an option to change whenever you want."
            jump Edu_days_options
            

        "How do I change the character?":
            show eduguide at right with dissolve
            Eduguide "The only way to change character is to create a new game file."
            jump Edu_days_options
        
        "Quit":
                jump rachel_menu
