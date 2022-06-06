# The script of the game goes in this file.

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
# The game starts here.

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

default game_code_uni = "0188U" #The code of the game 

default game_code_lincoln  = "0198L" #The code of the game

default game_code = 0

define nuria_init_dialogue = False

define feel = 0

default Tamy_Takes_You = False
#Tamy Atributes
default tamy_unlocked = 0

#Playlist Conditionals
default Spotify = 0

default character_name = "Sherylda"

default Wordle_Finish = False

label start:
    # The game starts here.
    scene bg blank
    
    $ game_code = renpy.input("Enter your pass-code:", length=5)

    screen input:

        window:

            style "nvl_window"
            
            text prompt xalign 0.5 yalign 0.4
            input id "input" xalign 0.5 yalign 0.5

        use quick_menu

    if game_code == game_code_lincoln:
        jump start_lincoln

    elif game_code == game_code_uni:
        jump start_uni
    
    else:
        jump start
    
label start_lincoln:
    play music "audio/bgm_intromusic.mp3" fadein 1.0 volume 0.3
    scene bg opening

    
    Meifeng "*sigh*"
    show meifeng at left
    Blezz "*sigh*"
    show blezz at right

    Meifeng "I'm Meifeng, a student From Lincoln English Academy."
    hide blezz
    hide meifeng
    show blezz
    Blezz "I'm Blezz, and me too.."
    hide blezz

    show meifeng at left

    Meifeng """
     I'll give you a little introduction to this particular game.

     In this game you will have the oportunity to apreciate a concept of the current level 6 to level 9 class in lincoln academy.

     The game consist in listening to the 4 music of each character that will be displayed in the class.

     Each character is a mix of my perspective of each personality from everyone in the room.

     The protagonist, aka YOU will be asking for a touch of their headset and discover what they are listening to.

     The main plot is to daydream about what music tells for every character in the game.

     Yes is a short game as you can tell.

     So, don't waste more time and jump to the action!

     """

    Meifeng "Oops!, i forgot something!"
    Meifeng "What's your name?. "
    
    $ character_name = renpy.input("Insert your name below", length=9)

    Meifeng "Nice to meet you [character_name]."
    Meifeng "Get good."
    
label traveling:

    stop music fadeout 1.0
    scene bg blank with dissolve
    centered "*Sunday morning*"
    centered "*You path towards to the Zumen.*"
    play music "audio/bgm_walking.mp3" fadein 1.0 volume 0.3
    scene bg zumen
    "*You arrive and see the vendings stores around there...*"

    character_name "*.*"
    character_name "*..*"
    character_name "*...*"

    character_name "*I need to hurry up!, Teacher Isela is going to be mad at me!*"

    "*You take the 112 Bus and ready to go.*"


    label prelincoln:

    scene bg blank

    centered "*You arrive to the entrance...*"

    scene bg lincoln
    
    character_name "So, Im finally here..."
    character_name "I didn't even take breakfast too."
    character_name "This day seems doomed already."

    "What to do next?"
    menu:
         "Get back to home, this day taste like a expired chocolita.":
            show isela at right
            Isela "Where are you going??!!, get back here and enter the class..."
            character_name "I guess i'm done..."
            jump lincoln

         "Enter the class.":
            jump lincoln
    

label lincoln:
    $ chapter = "Chapter I: The English Class" 
    scene bg blank
    centered "*You enter the class*"

    scene bg class1

    play music "audio/bgm_class.mp3" fadein 1.0 volume 0.3
    "I wonder why is everybody looking at me in that way..."
    scene bg class0
    show isela at left
    Isela "Good morning, you late... again..."
    Isela "[character_name], you better have a good excuse this time..."
    scene bg class1
    character_name "I -I mean..."
    Isela "Anyways, let's start with memorizes!"
    hide isela
    character_name "Douh."
    character_name "Why everyone has  headphones now?."
    extend " I'm a bit confused."
    character_name "I wonder what are they listening to."
    character_name "Maybe i can get a touch."

label Options:
    play music "audio/bgm_class.mp3" fadein 1.0 volume 0.3
    scene bg class1
    hide screen nuria_buttons
    hide screen nuria_quit
    hide screen nuria_quit_menu
    "What to do now?."

    
    menu Talk_Grind:
        "Listen to your own Spotify playlist":
            
            if Spotify == 0:
                menu:
                    "Cartoon On & On":
                        stop music fadeout 1.0
                        scene bg cartoon with dissolve
                        play music "audio/preset.mp3" fadein 2.0 volume 0.2
                        "..."
                        hide window
                        pause
                        character_name "I don't know why, but this song bring me memories."
                        character_name "It feels like a summer day in 2015."
                        character_name "What a year..."
                        character_name "Anyways."
                        stop music fadeout 1.0
                        jump Options

                    "Get back":
                        jump Options

            elif Spotify == 1:
                menu:
                    "Cartoon On & On":
                        stop music fadeout 1.0
                        scene bg cartoon with dissolve
                        play music "audio/preset.mp3" fadein 2.0 volume 0.2
                        hide window
                        pause
                       
                        stop music fadeout 1.0
                        jump Options
                    
                    "Twice - The Feels":
                        stop music fadeout 1.0
                        scene bg class1
                        show screen thefeels_buttons
                        play music "audio/thefeels.mp3" fadein 2.0 volume 0.2
                        hide window
                        pause

                        stop music fadeout 1.0
                        hide screen thefeels_buttons
                        jump Options

                    "Get back":
                        jump Options
                


        "Get new songs":
            if music_game_choice_nuria>50:
                menu:
                    "The feels Twice":
                        "Oh, look it seems you have unlocked a new song."
                        "You have unlocked the feels twice."
                        $ Spotify = 1
                        jump Options    

                    "????":
                        "You haven't unlocked it yet"
                        "*Maybe I can unlock news if I listen to the others songs for a while*"
                        jump Options

                    "????":
                        "You haven't unlocked it yet"
                        "*Maybe I can unlock news if I listen to the others songs for a while*"
                        jump Options
            
            elif music_game_choice_nuria<50:
                menu:
                    "????":
                        "You haven't unlocked it yet"
                        "*Maybe I can unlock news if I listen to the others songs for a while*"
                        jump Options

                    "????":
                        "You haven't unlocked it yet"
                        "*Maybe I can unlock news if I listen to the others songs for a while*"
                        jump Options

                    "????":
                        "You haven't unlocked it yet"
                        "*Maybe I can unlock news if I listen to the others songs for a while*"
                        jump Options

                    "????":
                        "You haven't unlocked it yet"
                        jump Options




        "Talk with people in the class":
            if Tamy_Takes_You == False:
                    if tamy_unlocked == 0:
                        menu:
                            "Talk to Nuria":
                                if nuria_init_dialogue == True:
                                    jump Nuria_Music
                                else:
                                    jump Nuria

                            "Talk to Tamy":
                                scene bg class0
                                show tamyt
                                Tamy "Hey, [character_name]!"
                                Tamy "I'm Tamy."
                                Tamy "I'll like to talk with you but im busy right now"
                                Tamy "You should come back later."
                                jump Options
                        
                    if tamy_unlocked >= 1:
                        menu:
                            
                            "Talk to Nuria":
                                    jump Nuria_Music


                            "Talk to Tamy":
                                if Tamy_knowledge == True:
                                    jump tamy_options  #Tamy_knowledge == True
                                jump Tamy
                    
            if Tamy_Takes_You == True:
                menu:
                    "Talk to Nuria":
                        jump Nuria_Music
                    
                    "Talk to Tamy":
                        jump tamy_options
                    
                    "Talk to the teacher":
                        scene bg class0
                        show isela
                        Isela "Hey, [character_name]!"
                        Isela "Don't be late next time."
                        Isela "So guys this is the class for today"
                        Isela "Do you have any questions?"
                        character_name "I have-I have a question."
                        Isela "So no one."
                        Isela "Alright, see you next day."
                        hide Isela
                        scene bg lincoln
                        show tamyt at left
                        Tamy "So, do we go to the university?"
                        hide tamyt
                        show tamy at left
                        character_name "Yessir."
                        hide tamy
                        show tamyt at left
                        Tamy "Ok, let's go."
                        jump Tuesday_edu
           

        "Status":
            jump status
        
        "Guide":
            jump guide


label Nuria:
    $ nuria_init_dialogue = True

    scene bg class0
    "*You aproach to Nuria*"
    character_name "Sup bro."
    show nuria
    Nuria "Sup? trash."
    show nuriat
    Nuria "I mean [character_name]."
    Nuria "Wth u looking for?"
    hide nuriat
    show nuria
    character_name "I'm just wondering if i can get some tunes."
    hide nuria

    show nuriat

    Nuria "Yeah, why not?"
    Nuria "I mean I have a superior music taste..."
    hide nuriat
    show nuria

    jump Nuria_Music

label Nuria_Music:
    hide screen nuria_quit
    stop music fadeout 1.0
    scene bg nuria with dissolve
    "*You put on the headphones*"
    "What to listen now?."
    hide window
    show screen nuria_buttons with pixellate
    show nuria at right
    show screen nuria_quit_menu


menu:

    "Animal in Me":
        hide screen nuria_buttons
        hide nuria
        scene bg animal with dissolve
        play music "audio/metal1.mp3" fadein 3.0 volume 0.3
        hide window
        
        pause
        show nuriat at right
        Nuria "Savage right?"
        Nuria "For me it's like exposing what i'm in reality."
        Nuria "Well, i'm not a animal for sure haha, but i like to be wild."
        character_name "That was a pretty bad joke."
        Nuria "xD."
        if feel == 0:
            $ feel = renpy.input("What does this music makes you feel?", length=8)
            Nuria "[feel], huh?."
            Nuria "You're a weirdo."
            Nuria "Anyway..."
        Nuria "Last time you said that [feel]"
        hide nuriat
        show nuria at right
        show screen nuria_quit


    "Suite 8":
        scene bg suite8 with dissolve
        show nuria at right
        play music "audio/metal2.mp3" fadein 3.0 volume 0.3
        $ music_game_choice_nuria += renpy.random.randint(1,10)
        hide window
        pause
        
        jump nuriarepeat

    "Blackout":
        scene bg blackout with dissolve
        show nuria at right
        play music "audio/metal3.mp3" fadein 3.0 volume 0.3
        $ music_game_choice_nuria += renpy.random.randint(1,10)
        hide window
        pause
        jump nuriarepeat



    "Faith in 1984":
        scene bg faith with dissolve
        show nuria at right
        play music "audio/metal4.mp3" fadein 3.0 volume 0.3
        $ music_game_choice_nuria += renpy.random.randint(1,10)
        hide window
        pause
        jump nuriarepeat


    "Falling Down + Heathens":
        scene bg falling with dissolve
        show nuria at right
        play music "audio/metal5.mp3" fadein 3.0 volume 0.3
        $ music_game_choice_nuria += renpy.random.randint(1,10)
        hide window
        pause
        jump nuriarepeat
    
    "Talk":
        hide screen nuria_quit_menu
        $ tamy_unlocked += 1
        if Nuria_finish == True:
            call Nuria_finished_chapt1
            
        call atributes_nuria
        $ music_game_choice_nuria += renpy.random.randint(1,10)
        jump Nuria_Music



label nuriarepeat:
        hide screen nuria_quit
        if feel != 0:
            character_name "That was [feel]."
            character_name "*Hmm, so she likes metal a lot.*"

        character_name "*Hmm, so she likes metal a lot.*"
        stop music fadeout 0.1
        jump Nuria_Music




label status:
    "*Here's the status from every classmate*"
    menu:
        "Character Status":
            call screen StatusBox
        
        "Back Menu":
            jump Options #TODO: Add music status
        


            


label Tamy:

    scene bg class0
    "*You aproaches to Tamy*"

    character_name "Hi."

    show tamyt
    Tamy "*Disgusting sound* so you are [character_name]."
    hide tamyt
    show tamy
    Tamy "*Eats*"
    character_name "Im just wondering if-"
    hide tamy
    show tamyt
    
    Tamy "Yeah I know, you wanna listen to my playlist."
    character_name "Huh, how do you.."
    
    Tamy "You talk too loud... you know?"

    character_name "..."

    Tamy """
    But for you disgrace, my phone broke when i was coming here.

    You shall come to my house to listen.

    Just wait me after class and we ready to go.

    """
    hide tamyt
    character_name "Aight."
    hide tamyt
    "*You waited for 3 hours*"
    show tamyt
    Tamy "so, here we go."

    scene bg tamy with dissolve

    character_name "Very nice house."
    show tamyt
    Tamy "yep, I bought it yesterday."

    character_name "what?"

    Tamy "Anyway just turn on the radio."

    character_name "Radio?, aren't we using spooderfy?"

    Tamy "That's for losers lol."

    character_name "*Ashamed face*"

    hide tamyt


    
    "*You turn on the radio*"
    "What radio station to listen now?."

label tamy_options:
    stop music fadeout 1.0
    play music "audio/bgm_class.mp3" fadein 1.0 volume 0.3
    $ Tamy_knowledge = True     # This is to make sure that the player can't repeat the dialogue.
    scene bg tamy with dissolve
    show tamy

    menu:
        "Radio.net":
            scene bg afterdark with dissolve
            show tamy
            play music "audio/blezz1.mp3" fadein 1.0 volume 0.3
            
            $ music_game_choice_tamy += renpy.random.randint(1,10)
            # call screen Music_Player
            hide tamy
            show screen afterdark
            hide window
            pause
            hide screen afterdark
            jump tamy_options
        
        "98.5 FM":
            scene bg homemage with dissolve
            show tamy
            play music "audio/blezz2.mp3" fadein 1.0 volume 0.3
            $ music_game_choice_tamy += renpy.random.randint(1,10)
            hide tamy
            show screen synthwave
            hide window
            pause
            hide screen synthwave
            stop music fadeout 1.0
            jump tamy_options

        "CBC Radio ONE":
            scene bg maroon with dissolve
            show tamy
            play music "audio/blezz3.mp3" fadein 1.0 volume 0.3
            $ music_game_choice_tamy += renpy.random.randint(1,10)
            hide tamy
            show screen caldera
            hide window
            pause
            hide screen caldera
            jump tamy_options

        "Shekinah Radio":
            hide tamy
            if childish == 0:
                play music "audio/screamer.mp3"  volume 0.15
                show screamer:
                    parallel:
                        0.2 #tiempo de espera
                        xalign 0.5 yalign 0 #centrar la imagen en el eje x
                        ease 0.25 zoom 2.0 #animación donde la imagen hace un zoom al doble
                    parallel:
                        alpha 0 #opacidad 0
                        0.2 #t. de espera
                        linear 0.15 alpha 1.0 #comienza a mostrarse
                        1.0 #t. de espera
                        linear 0.10 alpha 0 #empieza a desaparecer
                    parallel:
                        dizzy(1.5,0.01) #animación de la imagen
                window auto hide
                pause 1.0
                window auto show

            hide screen fnaf_screamer
            $ childish += 1

            stop music fadeout 1.0
            scene bg fnaf with dissolve
            show screen fnaf_golden
            show tamy
            play music "audio/blezz4.mp3" fadein 1.0 volume 0.3
            $ music_game_choice_tamy += renpy.random.randint(1,10)
            hide tamy
            hide window
            pause
            hide screen fnaf_golden
            jump tamy_options

        "Talk":
            if Tamy_University_trip == True:
                jump Tamy_Taking_Action
            show tamyt
            #make a dialogue with tamy
            Tamy """
            And when I awoke at night.  That's when I knew who she was.  
            That she was a dreamer.  
            someone who could play any instrument.  
            any color you could imagine.  
            everyone I ever loved, in all their expressions.  
            """


            Tamy "*You are not supposed to talk to me*"
            Tamy "*I am not supposed to talk to you*"
            Tamy "Joking! I am just a little childish with you."
            #tamy takes you to the university

            Tamy "So you are [character_name]."
            Tamy "I might have seen you in the university."
            character_name "..."
            character_name "Oh really?"

            Tamy "Yes, like 5 times so far."
            character_name "That's scary."

            Tamy "So, why you are here?"
            character_name "I just want to meet new people"
            Tamy "Interesting"

            Tamy "All of them are students on the same university as your's"
            character_name "How the heck I didn't know?"

            Tamy "Maybe you should start to see fowards from your own feet"
            character_name "..."
            character_name "Can you take me there?"

            Tamy "I'm not sure."
            Tamy "Taking you as a person that I just met 5 mins ago."
            Tamy "To my friends..."
            Tamy "Let me think a bit about it"
            $ Tamy_University_trip = True
            jump tamy_options




        "Quit":
            jump Options


label Tamy_Taking_Action:
    if Wordle_Finish == True and Nuria_final_dialogue == True:
        scene bg tamy with dissolve
        show tamyt
        Tamy "I'm not sure if I should tell you this, but I've been thinking about you."
        Tamy "Maybe I can introduce you to my friends."
        Tamy "Wait for me at the stop Tomorow."
        if confidence_tamy == 0 and friendship_tamy == 0 and tension_tamy == 0:
           $ confidence_tamy += 5
           $ friendship_tamy += 5
        $ Tamy_Takes_You = True
        $ tamy_unlocked -= 2
        hide tamyt
        jump tamy_options
    
    if Adult == True:
            menu:
                "What's up?":
                    jump Tamy_Dialogues
                
                "Take me to the university":
                    scene bg tamy with dissolve
                    show tamyt
                    Tamy "I'm not quite sure that we should go to the university together, I just met you!"
                    Tamy "Definitively that's not gonna happen"
                    hide tamyt
                    jump tamy_options

                "Maybe I should go alone to the University":
                    "Where are you going?"
                    "?"
                    "??"
                    "???"
                    "????"
                    $renpy.pause(delay = 2.5, hard = True)
                    hide tamyt
                    hide tamy
                    play music "audio/screamer.mp3"  volume 0.15
                    show jeff:
                            parallel:
                                0.2 #tiempo de espera
                                xalign 0.5 yalign 0 #centrar la imagen en el eje x
                                ease 0.25 zoom 2.0 #animación donde la imagen hace un zoom al doble
                            parallel:
                                alpha 0 #opacidad 0
                                0.2 #t. de espera
                                linear 0.15 alpha 1.0 #comienza a mostrarse
                                1.0 #t. de espera
                                linear 0.10 alpha 0 #empieza a desaparecer
                            parallel:
                                dizzy(1.5,0.01) #animación de la imagen

                    window auto hide
                    pause 1.0
                    window auto show
                    $ Adult = False
                    hide jeff
                    jump tamy_options

    menu:
        "What's up?":
            jump Tamy_Dialogues
                
        "Take me to the university":
            scene bg tamy with dissolve
            show tamyt
            Tamy "I'm not quite sure that we should go to the university together, I just met you!"
            Tamy "Definitively that's not gonna happen"
            hide tamyt
            jump tamy_options



label Tamy_Dialogues:
    hide tamyt
    hide tamy
    show tamyt
    Tamy "Hey, [character_name]."
    Tamy "Shall we play a game?"
    character_name "..."
    character_name "I don't know."
    Tamy "A wordle Game."
    Tamy "It's gonna be fun."
    Tamy "Trust Me."
    
    menu:
        "I'm Ready":
            jump lingo_example
        
        "No":
            scene bg tamy with dissolve
            show tamyt
            Tamy "You are so boring!!!"
            Tamy "Looser!"
            jump tamy_options
    





