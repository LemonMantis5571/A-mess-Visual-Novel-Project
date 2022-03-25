label  start_uni:
    play music "audio/bgm_unimusic.mp3" fadein 1.0 volume 0.3
    scene bg uni with dissolve

    show secret
    Talya "Hello there."
    Talya "So, you are a UNI Student."
    Talya "You may ask what are you doing here."
    Talya "Well I'm here to help you."
    Talya "I'm Talya, your guide in this adventure. "
    #make dialogue of a music game introduction
    Talya "I'm going to show you how to play this game."
    Talya "You will have to choose between two paths."
    Talya "Being a good person is the best path."
    Talya "Being a bad person is the second best path."
    Talya "Well, not that bad, right?"
    Talya "Aight, in this game you'll experiment the personality of every character."
    Talya "From music taste to programming preferences."
    Talya "Your main goal is..."
    Talya "Be yourself."
    Talya "So, tell me your name."
    menu:
        "Ok":
         $ character_name = renpy.input("Insert your name below", length=9)

        "I prefer a random nickname":
            Talya "Ok, I'll call you..."
            Talya "..."
            stop music fadeout 1.0
            Talya "Ozuna!"
            hide secret
            play music "audio/ozuna.mp3" fadein 1.0 volume 0.3
            show ozuna at right with dissolve
            "Ozuna!?"
            show secret at left
            Talya "Yes."
            hide ozuna
            show ozunat at right with dissolve
            Ozuna "ax2+bx+c=0"
            $ character_name = "Ozuna" 

    hide ozuna
    Talya "Nice to meet you, [character_name]."
    Talya "So, lets start with your first choice."

    jump traveling


