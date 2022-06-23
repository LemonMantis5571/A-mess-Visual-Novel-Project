default rachel_finish = False
default EduChapter = "Chapter 2: Edu-Days"
label Tuesday_edu:
    
    play music "audio/bgm_intromusic.mp3" fadein 1.0 volume 0.3
    
    scene bg blank with dissolve

    centered "Tuesday"

    centered "6:40 AM"

    centered "You are now in the 110."

    play music "audio/bgm_walking.mp3" fadein 1.0 volume 0.3

    scene bg parada with dissolve

    character_name "Oh dear, it's full again..."

    character_name "Better wait for the next"

    jump busTuesday



label busTuesday:

    scene bg businterior

    character_name "*You are in the bus*"
    character_name "Everything is fine, I'm just late."
    character_name "At least the day is calm"

    """*they push you*"""

    if confidence_rachel < 5:
        show rachel at right

        Rachel "Omg sorry, wait a minute, are you [character_name]?"
        Rachel "I'm Rachel, we are on the same class."
        Rachel "What a coincidence, I'm also on the bus."

        hide rachel
        
        menu response:
            "Response"
            "Yes, what a surprise":
                character_name "Yes, what a surprise to see you here"
                character_name "We live near each other, I'm so glad to see you."
                show rachel at right
                Rachel "So, I'll see you more often then"
                Rachel "We arrived at the stop, hurry up we're late!"
                hide rachel
                $rachel_bus = 1


            "Actually not":
                show rachel2 at right
                character_name "Actually not, I've already seen you around here"
                Rachel "hmmm ok"
                hide rachel2
                $rachel_bus = 0

            "...":
                character_name "..."
                show rachel at right
                Rachel "Are you shy? Do not worry, haha"
                hide rachel

                $ rachel_bus = 2
        
        if rachel_bus == 1:
            scene bg busllegada

            show rachel at right

            Rachel "If we walk faster we can get there in time"

            hide rachel

            "*Rachel goes faster and suddenly you see her outwalking you*"

            character_name "I'll see her in the classroom I guess.."

            $ friendship_rachel += 2
            $ tension_rachel -= 1
            $ confidence_rachel += 1

        if rachel_bus == 0:
            scene bg busllegada
            show rachel at right
            Rachel "I supose that we're going to meet in the classroom"
            Rachel "See you there"
            $ tension_rachel += 2

        if rachel_bus == 2:
            scene bg busllegada
            show rachel at right
            Rachel "Let's go"

            "*She takes your hand and you start to walk faster*"

            Rachel "Hurry up! [character_name] we got a test today!"
            Rachel "I'll see you in the classroom"

            hide rachel

            $ friendship_rachel += 1

label classTuesday:

    scene bg aula1



    character_name "What a great first class!"

    #aqui va a ir un personaje de profesor xd

    "Ok guys today we will do something different, we will see the parts of a computer "
    "Get in pairs and choose one of the parts you see here"

    show rachel at right

    Rachel "Hi [character_name], come join me"

    hide rachel

    menu:
        "Alright":
            $ friendship_rachel += 3
            $ tension_rachel -= 2
            show rachel at right
            Rachel "I knew that you wouldn't resist {font=fonts/NotoEmoji-Bold.ttf}🥴{/font}"
            Rachel "Ok, let's see what we can do"
            hide rachel
            $ rachel_clase = 1

        "I prefer to do things on my own":
            $ friendship_rachel -= 2
            $ tension_rachel += 2 
            $ confidence_rachel -= 1
            show rachel at right
            Rachel "..."
            hide rachel
            $  rachel_clase = 0
    
    if rachel_clase == 1:
        jump Options1

    if rachel_clase == 0:
        
        "Are you going to work alone?"
        "It's ok if you want."
        "But listen..."
        "You are not going to do much without a team."

        menu:
            "I'ts ok I'll do with her":
                show rachel at right
                Rachel "Hi"
                Rachel "Let's start at once"
                $ tension_rachel += 2
                $ confidence_rachel -= 1
                jump Options1
            
            "I'm not interested":
                show rachel2 at right
                "I don't care about her.I don't want to check double"
                character_name "a"
                hide rachel2
                
                jump Options1

label Options1:
    
        
    scene bg mesa
    
    call screen selector1


screen selector1():

    vbox:
        align (1.0, 0.5)
        xpos 0.4
        ypos 0.5
        xsize 5
        spacing 20

        #imagebutton idle "ram"    hover "ram_hover"    action Jump("Ram")
        #imagebutton idle "motherboard"    hover "motherboard_hover"    action Jump("Motherboard")
        textbutton "RAM"    action Jump("Ram")
        textbutton "Motherboard"    action Jump("Motherboard")
        textbutton "CPU"    action Jump("cpu")
        textbutton "Continue" action Jump("exam")
        

    
label Ram:

    scene bg tamy
    
    show screen RAM_buttons
    show tamyt at left with hpunch
    Tamy "RAM is the main memory of a device, the one where the data of the software you are using at the moment is temporarily stored."

    Tamy "It has two characteristics that makes the difference from other types of storage. "

    Tamy "On the first hand it has enormous speed, and secondly the data is only stored temporarily."
    hide screen RAM_buttons
    hide tamyt
    jump Options1  
    
label Motherboard:

    scene bg tamy

    show tamyt at left with hpunch
    show screen Motherboard_buttons
    Tamy "The motherboard is the main board on the internal structure of a computer where the electronic circuits, the processor, the memories and the main connections are located."

    Tamy "When we refer to the motherboard, we are talking about a type of technology that has been present since the beginning of the history of computers to this day."
    hide screen Motherboard_buttons
    hide tamyt
    jump Options1

label cpu:

    scene bg tamy

    show tamyt at left with hpunch
    show screen CPU_buttons
    Tamy "The CPU is the brain of the computer, we refer to the part of the computer in which direct commands that generate the different functions of the CPU that are controlled and originated."

    Tamy "In the CPU all the calculations of the binary code of the computer are done. In general, it is the most important part of the system."
    hide screen CPU_buttons
    hide tamyt
    jump Options1


    
label exam:
    scene bg aula1
    show rachel at right
    Rachel "Okey, we are going to do an exam"
    hide rachel
    jump preguntas
    

label preGame:

    if finalTimeExamDialog == 0:
        Rachel "We did it! We passed the exam! {font=fonts/NotoEmoji-Bold.ttf}😎{/font}"
        $ finalTimeExamDialog = 3
    
    if finalTimeExamDialog == 1:
        Rachel "We failed the exam! {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
        $ finalTimeExamDialog = 3

    if (friendship_rachel >= 2 and friendship_rachel < 5) and (confidence_rachel >= 2 and confidence_rachel < 5) and (tension_rachel >= 2 and tension_rachal < 5) and (tension_rachel > -2 and tension_rachal < 2):
        scene bg aula1
        show rachel at right
        Rachel "You are a good classmate, I'm so glad to see you"
        hide rachel
        jump preguntas

    

    if friendship_rachel >= 5 and confidence_rachel >= 5 and tension_rachel <= -3:

        if playGame > 0:

            jump rachel_menu
        
        if playGame == 0:
            scene bg aula1
            show rachel at right
            Rachel "We do such a great team huh?"
            Rachel "Hmm."
            Rachel "Shall we play a game?"
            Rachel "I mean meanwhile they're coming."
            Rachel ":3"
            Rachel "You only have to touch the figures that have two or more of the same type, simple right?"
            Rachel "Great, lets go."

            hide rachel

            jump initGame
   

label rachel_menu:
    scene bg aula1
    show rachel at right
    stop music fadeout 1.0
   
    
    Rachel "Well, now what do we do?"
    hide rachel


    menu:
        "Play again":
            show rachel at right
            Rachel "Ok, let's play again"
            jump initGame

        "ask about your music":
            character_name "rachel, what  are you Listening?"
            show rachel at right
            Rachel "my music?"
            Rachel "I'm listening to... {font=fonts/NotoEmoji-Bold.ttf}🎶{/font}"
            Rachel "Look at it yourself"
            hide rachel

            menu:
                "WhatsappAudio20220903":
                    scene bg guide
                    play music "audio/rachel1.mp3" fadein 2.0 volume 0.5
                    pause
                    $ option_music_Rachel += 1
                    jump rachel_menu

                
                "WhatsappAudio20220901":
                    scene bg nuria
                    play music "audio/rachel2.mp3" fadein 2.0 volume 0.5
                    pause
                    $ option_music_Rachel += 1
                    jump rachel_menu

                    

                "WhatsappAudio20220904":
                    scene bg businterior
                    play music "audio/rachel3.mp3" fadein 2.0 volume 0.5
                    pause
                    $ option_music_Rachel += 1
                    jump rachel_menu 

                "return":
                    jump rachel_menu 

        "Talk":
            if option_music_Rachel >= 3 and opt_menu_talkRachel == True:
                Rachel "So, what do you think about my songs?"
                character_name "Good, I like them"
                Rachel "I have a lot more, but maybe tomorrow. "
                $ exitDay = True
                $ confidence_rachel += 2
                $ friendship_rachel += 5
                $ tension_rachel -= 2
                jump Byebye

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == False:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2

                        jump rachel_menu
                    
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu


            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == False:
                menu:
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == False:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2

                        jump rachel_menu

                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == False:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2

                        jump rachel_menu

                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == True:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2

                        jump rachel_menu
                    
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu


            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == False:
                menu:
                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu
 
            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == False:
                menu:
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu
 
            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == True:
                menu:
                    
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu

            #1 y 2 arriba

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == False:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2

                        jump rachel_menu
                    

                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        jump rachel_menu
 
            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == True:
                menu:

                    
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu

                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        jump rachel_menu

            # 1 y 3 
            # 2 y 3 arriba

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == True:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2

                        jump rachel_menu
                    
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        jump rachel_menu


            # unica opcion

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == False and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == True:
                menu:
                    "What's your phone brand?":
                        character_name "What's your phone brand?"
                        Rachel "It's a Xiaomi, Quality-Price XD"
                        character_name "..."
                        Rachel "It's a joke hahaha"
                        Rachel "but yeah, it's Xiaomi"

                        $ opt_menu_talkRachel_q1 = True
                        $ friendship_rachel += 2
                        $opt_menu_talkRachel = True

                        jump rachel_menu
                    
            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == False and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == True:
                menu:                    
                    "What do you do on your free time?":
                        character_name "What do you do on your free time?"
                        Rachel "Code, code and more code..."
                        Rachel "It's hard, but we are here for one reason :')"
                        character_name "Sad, this doesn't look how I expected {font=fonts/NotoEmoji-Bold.ttf}😔{/font}"
                        Rachel "Don't worry, I'll be here for you {font=fonts/NotoEmoji-Bold.ttf}🤗{/font}"
                        Rachel "You can do it"
                        Rachel "Don't be afraid if it's hard, just relax, distract with something and take back to the action."
                        Rachel "I believe in you {font=fonts/NotoEmoji-Bold.ttf}😁{/font}"

                        $ friendship_rachel += 5
                        $ confidence_rachel += 3
                        $ opt_menu_talkRachel_q2 = True
                        $opt_menu_talkRachel = True
                        
                        jump rachel_menu

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == False and opt_menu_talkRachel_q4 == True:
                menu:
                    "Which branch of computer science do you like the most?":
                        character_name "Which branch of computer science do you like the most?"
                        Rachel "I like a lot web development, but I also like the other branches"
                        Rachel "On the front end I like HTML, CSS and Javascript"
                        Rachel "It's awesome to be able to code in a browser"
                        character_name "Sounds good, I like it"

                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q3 = True
                        $opt_menu_talkRachel = True

                        jump rachel_menu

            if opt_menu_talkRachel == False and opt_menu_talkRachel_q1 == True and opt_menu_talkRachel_q2 == True and opt_menu_talkRachel_q3 == True and opt_menu_talkRachel_q4 == False:
                menu:
                    "What do you regularly eat here?":
                        character_name "What do you regularly eat here?"
                        Rachel "What is that?"
                        Rachel "JK, what I use to eat is a piece of bread and a chocolita"
                        Rachel "You won't need to eat until the next day B)"
                        character_name "Taking notes XD"


                        $ friendship_rachel += 2
                        $ confidence_rachel += 1
                        $ opt_menu_talkRachel_q4 = True
                        $opt_menu_talkRachel = True
                        jump rachel_menu
 
                    
        "Guide":
            jump Edu_days_guide

        "Go home":
            if exitDay == True:
                jump Byebye

            character_name "* I shouldn't go yet *"
            jump rachel_menu



label Byebye:
    character_name "I think is time to go"
    Rachel "Yep, you right, see you tomorrow [character_name]"
    Rachel "By the way, add me on Instagram"
    Rachel "To speak then?"
    character_name "ok"
    Rachel "ok, good bye"

    scene bg blank
    Centered "Thank you for playing this game"
    Centered "To be continued..."
    Centered "We promise.   "

    pause 25.0
    pause 25.0
    jump start_uni


            