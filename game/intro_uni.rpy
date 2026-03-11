# ──────────────────────────────────────
#  Intro / Setup – with real scenes
# ──────────────────────────────────────

transform intro_fade_in:
    alpha 0.0
    easein 0.6 alpha 1.0


screen content_warning_screen:
    modal True
    default health_answer = None
    default censor_answer = None

    frame:
        background "#1a0a1ad8"
        xfill True
        yfill True

    frame:
        at intro_fade_in
        background "#2e1630ee"
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 480
        padding (40, 32)

        vbox:
            spacing 18
            text "Before we start" size 38 bold True color "#ffffff" xalign 0.5

            null height 6

            text "This game contains flashing visuals, sudden audio cues, and intense scenes." size 22 color "#ffffff" xalign 0.5 text_align 0.5

            null height 14

            frame:
                background "#3a1a38ee"
                xfill True
                padding (24, 18)

                vbox:
                    spacing 14

                    text "Do you have heart problems or photosensitivity?" size 24 color "#ffffff"
                    hbox:
                        spacing 20
                        xalign 0.5
                        textbutton "Yes — enable safe mode":
                            text_size 22
                            if health_answer == 1:
                                background "#ffe66d44"
                                text_color "#ffffff"
                                text_bold True
                            else:
                                text_color "#ffffff"
                            text_hover_color "#ffffff"
                            padding (16, 8)
                            action SetScreenVariable("health_answer", 1)
                        textbutton "No — full experience":
                            text_size 22
                            if health_answer == 0:
                                background "#6dffa044"
                                text_color "#ffffff"
                                text_bold True
                            else:
                                text_color "#ffffff"
                            text_hover_color "#ffffff"
                            padding (16, 8)
                            action SetScreenVariable("health_answer", 0)

            frame:
                background "#3a1a38ee"
                xfill True
                padding (24, 18)

                vbox:
                    spacing 14

                    text "Disable strong visual scares?" size 24 color "#ffffff"
                    hbox:
                        spacing 20
                        xalign 0.5
                        textbutton "Yes — keep it mild":
                            text_size 22
                            if censor_answer == 1:
                                background "#ffe66d44"
                                text_color "#ffffff"
                                text_bold True
                            else:
                                text_color "#ffffff"
                            text_hover_color "#ffffff"
                            padding (16, 8)
                            action SetScreenVariable("censor_answer", 1)
                        textbutton "No — bring it on":
                            text_size 22
                            if censor_answer == 0:
                                background "#6dffa044"
                                text_color "#ffffff"
                                text_bold True
                            else:
                                text_color "#ffffff"
                            text_hover_color "#ffffff"
                            padding (16, 8)
                            action SetScreenVariable("censor_answer", 0)

            null height 4

            $ can_continue = health_answer is not None and censor_answer is not None

            textbutton "Continue":
                xalign 0.5
                text_size 28
                text_color "#ffffff"
                text_hover_color "#ffffff"
                sensitive can_continue
                action Return((health_answer, censor_answer))


label start_uni:
    scene bg main_menu
    centered "{size=26}{color=#ffffff}Talya is already waiting for you on the main menu threshold.{/color}{/size}"

    # ── Content warning / accessibility ──
    call screen content_warning_screen
    $ heart_problems = _return[0]
    $ censorship = _return[1]

    # ── Name input ──
    scene bg main_menu
    show secret at center with dissolve
    Talya "Before you enter, answer me properly."
    Talya "What should they call you in this world?"
    $ entered = renpy.input("Enter your name, or leave blank for {b}Sherylda{/b}.", length=12).strip()
    if entered:
        $ character_name = entered
    else:
        $ character_name = "Sherylda"
    Talya "Good."
    Talya "I will remember [character_name]."

    # ── Intro scene with Talya ──
    stop music fadeout 0.5
    play music "audio/bgm_unimusic.mp3" fadein 1.5 volume 0.3
    scene bg main_menu with dissolve

    centered "{size=28}{color=#ffffff}Somewhere between the last bell and the first silence...{/color}{/size}"

    show secret at left with dissolve

    Talya "So you came back."
    Talya "Or maybe you never really left."

    character_name "Who are you?"

    Talya "Someone who listens when others just hear noise."
    Talya "Lincoln does not stay one thing for long."
    Talya "It slips from world to world, and each one has its own rhythm."
    Talya "The first world is bright, glossy, impossible to trust."
    Talya "Frutiger Aero."
    Talya "Every person here still has a pulse that says more than their words."

    show secret at center with easeinleft

    Talya "There are two people you should know."
    Talya "Nuria. She is a wall of distortion, but there is a melody underneath."
    Talya "And Tamy. She speaks in precision, but the gaps between her words are louder."

    character_name "What am I supposed to do?"

    Talya "Listen. Not just with your ears."
    Talya "With your hands."
    Talya "Each of them has rhythm charts. If you can keep tempo, they let you in."

    Talya "Confidence, friendship, and tension still shape how they react."
    Talya "But now those values shift when you survive the beat and answer honestly."

    Talya "If you get lost, talk to the guide or open the music room."
    Talya "And pay attention to the world around you."
    Talya "That changes too."
    Talya "This is the interview."
    Talya "I ask. You answer. Then the world opens."

    Talya "One more thing, [character_name]."
    Talya "Do not rush the silence between the notes."
    Talya "That is where the truth lives."

    hide secret with dissolve

    centered "{size=24}{color=#ffffff}Talya walks away before you can respond.{/color}{/size}"
    centered "{size=24}{color=#ffffff}The morning bus is waiting.{/color}{/size}"

    jump traveling
