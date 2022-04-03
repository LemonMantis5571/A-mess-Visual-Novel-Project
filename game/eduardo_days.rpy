label Tuesday_edu:

    play music "audio/bgm_intromusic.mp3" fadein 1.0 volume 0.3
    
    scene bg blank with dissolve

    centered "Tuesday"

    centered "6:40 AM"

    centered "You are now in the 110."

    play music "audio/bgm_walking.mp3" fadein 1.0 volume 0.3

    scene bg uni with dissolve

    character_name "oh dear, it's full again "

    character_name "It's already late, should I go until the next hour?"

    menu :
        "Ir en el bus lleno":
            #goto Tuesday_bus
            jump busTuesday

        "No ir a la primera clase":
            #block of code to run
            scene bg blank with dissolve

            centered "regresas a casa a esperar la siguiente clase"

            jump classTuesday


label busTuesday:

    scene bg  with dissolve

    character_name "I'm going to the bus"

label classTuesday:

    scene bg busLlegada with dissolve

    character_name "Mucho mejor xd"
    
            
    




        








    