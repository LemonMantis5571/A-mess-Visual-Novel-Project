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
            Rachel "We arrived at the stop, get off we're late"
            hide rachel

            $rachel_bus = 1


        "Actually not":
            character_name "Actually not, I've already seen you around here"
            $rachel_bus = 0

        "...":
            character_name "..."
            show rachel at right
            Rachel "Are you shy? Do not worry, haha"
    
    if rachel_bus == 1:
        scene bg busllegada

        show rachel at right

        Rachel "If we walk faster we can get there in time"

        hide rachel

        "*Rachel goes faster and suddenly you see her outwalking you*"

        character_name "I'll see her in the classroom I guess.."

        #friend +1


    #elif rachel_bus == 0:
        #block of code to run
    #else:
        #block of code to run

            
        





label classTuesday:

    scene bg aula1

    character_name "What a great first class!"

    #aqui va a ir un personaje de profesor xd

    "Ok guys today we will do something different, we will see the parts of a computer "
    "Get in pairs and choose one of the parts you see here"

    show rachel at right

    #if optional == 1:
    #    Rachel "hi, i'm Rachel, I think everyone is here, do you want to join me?"
    #
        #menu labMinigame:
            #"Say Statement"
            #" ok":
                #show rachel at right
                #Rachel "great"
                #hide rachel

                #$decision = 1

            #"No, thanks":
                
                #show rachel at left
                #Rachel ":("
                #Rachel "it's okay"
                #hide rachel

                #$decision = 0

    #else:
    Rachel "Hi [character_name], come join me"

    hide rachel
    
    jump Options1

label Options1:
    
        
    scene bg mesa
    
    call screen selector1


screen selector1():

    vbox:
        align (1.0, 0.5)
        xsize 5
        spacing 20

        # Cambiamos los 'textbutton' por 'imagebutton',
        #   e indicamos la imagen básica: 'idle'
        #   y la imagen 'hover', cuando el ratón pasa por encima
        #imagebutton idle "ram"    hover "ram_hover"    action Jump("Ram")
        #imagebutton idle "motherboard"    hover "motherboard_hover"    action Jump("Motherboard")
        textbutton "ram"    action Jump("Ram")
        textbutton "motherboard"    action Jump("Motherboard")
        textbutton "cpu"    action Jump("cpu")
        textbutton "Continuar" action Jump("preGame")
        

    
label Ram:

    scene bg Tamy
    
    "RAM is the main memory of a device, the one where the data of the software you are using at the moment is temporarily stored."

    "It has two characteristics that makes the difference from sother types of storage. "

    "On the first hand it has enormous speed, and secondly the data is only stored temporarily."""

    jump Options1  
    
label Motherboard:

    scene bg Tamy
    "The motherboard is the main board on the internal structure of a computer where the electronic circuits, the processor, the memories and the main connections are located."

    "When we refer to the motherboard, we are talking about a type of technology that has been present since the beginning of the history of computers to this day."

    jump Options1

label cpu:

    scene bg Tamy
    "The CPU is the brain of the computer, we refer to the part of the computer in which direct commands that generate the different functions of the CPU that are controlled and originated."""

    "In the CPU all the calculations of the binary code of the computer are done. In general, it is the most important part of the system."
    jump Options1


    

label preGame:

    $decision = 1

    if decision == 1:
        scene bg aula1
        show rachel at right
        Rachel "Thank you for doing homework with me, while they come for me watch this game, it's very interesting :3"

        Rachel " You only have to touch the figures that have two or more of the same, simple right?"

        Rachel "Great, lets go"

        hide rachel

        jump initGame
    else:
        scene bg blank with dissolve

        centered "vas a casa a descansar para mañana"
    




        








    