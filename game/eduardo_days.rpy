default rachel_finish = False

label Tuesday_edu:

    play music "audio/bgm_intromusic.mp3" fadein 1.0 volume 0.3
    
    scene bg blank with dissolve

    centered "Tuesday"

    centered "6:40 AM"

    centered "You are now in the 110."

    play music "audio/bgm_walking.mp3" fadein 1.0 volume 0.3

    scene bg uni with dissolve

    character_name "Oh dear, it's full again..."

    character_name "It's already late, should I go until the next hour?"

    menu :
        "Take the Bus":
            #goto Tuesday_bus
            jump busTuesday

        "Skip the first class":
            #block of code to run
            scene bg blank with dissolve

            centered "*You returned home and waited for the next class.*"

            #$optional = 1

            jump classTuesday


label busTuesday:

    scene bg businterior
    

    character_name "*You are in the bus*"
    character_name "Everything is fine, I'm just late."
    character_name "I don't if it's me but I feel that everyday this is getting crowded."

    """*You push someone*"""

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
                character_name "Actually not, I've already seen you around here"
                
                $rachel_bus = 0

            "...":
                character_name "..."
                show rachel at right
                Rachel "Are you shy? Do not worry, haha"

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
        "oki":
            $ friendship_rachel += 3
            $ tension_rachel -= 2
            show rachel at right
            Rachel "Sabia que no te resisitirias ;)"
            Rachel "oki, veamos que hay que aprender"
            hide rachel
            $ rachel_clase = 1

        "prefiero hacerlo solo":
            $ friendship_rachel -= 2
            $ tension_rachel += 2 
            $ confidence_rachel -= 1
            show rachel at right
            Rachel "esta bien"
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
            "I'ts ok I'll do it with her":
                show rachel at right
                Rachel "Hi"
                Rachel "Let's start at once"
                $ tension_rachel += 2
                $ confidence_rachel -= 1
                jump Options1
            
            "I'm not interested":
                "As you wish"
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
    Rachel "Oki, we are going to do a exam"
    Rachel "isi pisi"
    hide rachel
    jump preguntas
    



label preGame:

    if finalTimeExamDialog == 0:
        Rachel "We did it! We passed the exam! 🥰"
        $ finalTimeExamDialog = 3
    
    if finalTimeExamDialog == 1:
        Rachel "We failed the exam! 😢"
        $ finalTimeExamDialog = 3

    if (friendship_rachel >= 2 and friendship_rachel < 5) and (confidence_rachel >= 2 and confidence_rachel < 5) and (tension_rachel >= 2 and tension_rachal < 5) and (tension_rachel > -2 and tension_rachal < 2):
        scene bg aula1
        show rachel at right
        Rachel "You are a good classmate, I'm so glad to see you"
        hide rachel
        jump preguntas

    

    if friendship_rachel >= 5 and confidence_rachel >= 5 and tension_rachel <= -3:

        if playGame > 0:

            scene bg aula1
            show rachel at right
            Rachel "That was funny 😂"
            Rachel "Hey what type of music do you like?"
            hide rachel
            menu:
                "xd":
                    show rachel at right
                    Rachel "a"
                "xd2":
                    show rachel at right
                    Rachel "A2"
                "otro":
                    $ musicFavorite = renpy.input("", length=9)
                    Rachel "[musicFavorite] ? that's quite interesting"
        
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
    

