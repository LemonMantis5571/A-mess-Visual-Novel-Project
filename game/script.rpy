# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Meifeng = Character("Meifeng", color="#FFD700")
define Blezz = Character("Blezz", color="#ff99cc")
define Isela = Character("Miss Isela", color="#b3b3ff")
define Grettell = Character("Grettell", color="#ff00ff")
define Nuria = Character("Nuria", color="#8cff66")
define Tamy  = Character("Tamy", color="#6666ff")
define Rachel = Character("Rachel", color="#ff6666")
define Yves = Character("Yves", color="#ff66ff")
# The game starts here.

#Nuria Atributes

default confidence_nuria = 0  
default friendship_nuria =0
default tension_nuria = 0

#Grettell Atributes

default confidence_grettell = 0  
default friendship_gretell = 0
default tension_grettell = 0



#Tamy Atributes
default tamy_unlocked = 0

#Playlist Conditionals
default Spotify = 0

default character_name = "Sherylda"


label start:
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
    
    character_name "So, Im finally here... its dope."
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

    scene bg blank
    centered "*You enter the class*"

    scene bg class1

    play music "audio/bgm_class.mp3" fadein 1.0 volume 0.3
    "*I arrived the class... I wonder why everybody is looking at me in that way..."
    show isela at left
    Isela "Good morning, you late... again..."
    Isela "[character_name], you better have a good excuse this time..."
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
                        "*Music Playing*"
                        character_name "I don't know why, but this song bring me memories."
                        character_name "It feels like a summer day in 2015."
                        character_name "What a year..."
                        character_name "Anyways."
                        stop music fadeout 1.0
                        jump Options
                    "Get back":
                        jump Options    

        "Get new songs":
            menu:
                "????":
                    "You haven't unlocked it yet"
                    jump Options

                "????":
                    "You haven't unlocked it yet"
                    jump Options

                "????":
                    "You haven't unlocked it yet"
                    jump Options

                "????":
                    "You haven't unlocked it yet"
                    jump Options
            




        "Talk with people in the class":
            if tamy_unlocked == 0:
                menu:
                    "Talk to Grettell":
                        jump Grettell

                    "Talk to Nuria":
                        jump Nuria
                
            if tamy_unlocked >= 1:
                menu:
                    "Talk to Grettell":
                            jump Grettell

                    "Talk to Nuria":
                            jump Nuria

                    "Talk to Tamy":
                            jump Tamy
        
        "Status":
            jump status


label Grettell:
 scene bg class0
 "*You aproaches to Grettell*"

 character_name "Hi."

 show grettell

 Grettell "H-hi what's going on-on? [character_name]."

 character_name "Im just wondering if i can listen to your music."

 Grettell """
 NO!

 NO!

 NO!

 NO!

 ...

 OK

 Maybe a bit. ><
 
 
 
 """
 

 "*You put the headphones on*"
 "What to listen now?."
 menu:
    "Wolves in the dark":
        play music "audio/Grettell.mp3" fadein 1.0 volume 0.3
        "*Music Starts to play*"
        "*You start to feel inspiration*"
        hide grettell
        show bg wolf with dissolve
        show grettell at right
        menu:
            "Get Back":
                character_name "*That was Dope*"
                stop music fadeout 1.0
                jump Options


label Nuria:
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

    Nuria "Yup, why not?"
    Nuria "I mean i have superior taste of music..."
    hide nuriat
    show nuria

    jump Nuria_Music

label Nuria_Music:
"*You put the headphones on*"
stop music fadeout 1.0
scene bg nuria with dissolve

"What to listen now?."
show nuria at right

menu:

    "Animal in Me":
        hide nuria
        scene bg animal with dissolve
        play music "audio/metal1.mp3" fadein 3.0 volume 0.3
        "*Music Starts to play*"
        show nuriat at right
        Nuria "Savage or nah?"
        Nuria "For me it's like exposing what i'm in reality."
        Nuria "Well, i'm not a animal for sure haha, but i like to be wild."
        Nuria "Maybe you can tell me."
        $ feel = renpy.input("Describe in a word what does this music feel.", length=8)
        Nuria "[feel], huh?."
        Nuria "You're a weirdo."
        Nuria "Anyway..."
        hide nuriat
        show nuria at right
        jump nuriarepeat


    "Suite 8":
        scene bg suite8 with dissolve
        show nuria at right
        play music "audio/metal2.mp3" fadein 3.0 volume 0.3
        "*Music Starts to play*"
        
        jump nuriarepeat

    "Blackout":
        scene bg blackout with dissolve
        show nuria at right
        play music "audio/metal3.mp3" fadein 3.0 volume 0.3
        "*Music Starts to play*"
        jump nuriarepeat



    "Faith in 1984":
        scene bg faith with dissolve
        show nuria at right
        play music "audio/metal4.mp3" fadein 3.0 volume 0.3
        "*Music Starts to play*"
        jump nuriarepeat


    "Falling Down + Heathens":
        scene bg falling with dissolve
        show nuria at right
        play music "audio/metal5.mp3" fadein 3.0 volume 0.3
        "*Music Starts to play*"
        jump nuriarepeat
    
    "Talk":
        $ tamy_unlocked += 1
        call atributes_nuria from _call_atributes_nuria
        jump Nuria_Music

    "Quit":
        jump Options


label nuriarepeat:
    menu:
         "Get Back":
            character_name "That was Dope."
            stop music fadeout 0.1
            jump Nuria_Music


label atributes_nuria: 
    $ randomnum = renpy.random.randint(1,2) # (randomize between 1 and 2)

    if randomnum==1 and confidence_nuria<45:
        show nuria

        Nuria "How my life is going???"
        hide nuria
        show nuriat
        Nuria "Well, things are..."
        Nuria "Don't mess with my life you dumb."
        character_name "I'm trying to start a conversation with you."
        Nuria "Just get out of my sight."
        menu:
            "I liked a song of your playlist":
                Nuria "..."
                Nuria "Really?"
                character_name "Yeah."
                Nuria "hmm."
                Nuria "that's good."
                hide nuriat
                $ confidence_nuria += 3
                $ friendship_nuria += 2
                $ tension_nuria -= 3

            "You such an agressive person you know?":
                show nuria_angry at right
                Nuria "I'm gonna show what a true agressive person is."
                Nuria "Just get out!"
                Nuria "Dumb!"
                $ confidence_nuria -= 3
                $ tension_nuria += 5
                $ friendship_nuria -= 4

            "I like you":
                Nuria "*Blushes*"
                show nuria_blush at right
                Nuria "..."
                Nuria "Get low you dumb."
                hide nuria_blush
                show nuriat at right
                Nuria "You'll never stand a chance with me."
                Nuria "No cap." 
                hide nuriat
                $ friendship_nuria +=2
                $ tension_nuria -= 2
                $ confidence_nuria += 2  

            "My mom prepared me some chicken sandwich":
                character_name "You want a taste of it?"
                Nuria "I don't want anything from you."
                Nuria "But i'll take it anyways."
                hide nuriat
                show nuria_sandwich at right
                Nuria "Omg this is so good."
                Nuria "Dammn."
                menu:
                    "I said a piece... not all.":
                        Nuria "You such a fool."
                        $ confidence_nuria +=2
                        $ friendship_nuria +=1
                        $ tension_nuria -= 1 
                        
                    "I swear i hate you":
                        Nuria "Who do you think you are??"
                        Nuria "Trash."
                        show nuria_angry at right with dissolve
                        $ confidence_nuria -=3
                        $ friendship_nuria -=2
                        $ tension_nuria += 4

                    "*Cries in KFC*":
                        Nuria "Are you really crying?"
                        Nuria "What a mommysitter."
                        
                        $ confidence_nuria -=1
                        $ friendship_nuria += 5
                        $ tension_nuria -= 6

    elif randomnum==2 and confidence_nuria<45:
        Nuria "OMG this class is so boring bruh."
        hide nuria
        show nuriat
        Nuria "I rather be programming the next Smash bros."
        Nuria "What are you looking at?"
        character_name "Nothing."
        Nuria "You better see nothing."
        Nuria "..."
        Nuria "You still here?"
        character_name "Yes."
        Nuria "May i ask what's your favorite type of music?"
        $ taste = renpy.input(" ", length=8)
        Nuria "[taste], that's interesting."
        Nuria "Mine is metal."
        hide nuriat
        menu:
            "We can hear metal together":
                show nuria_blush at right
                Nuria "..."
                Nuria "Of course not."
                Nuria "Mine is too hard for weak people as you."
                hide nuria_blush
                $ confidence_nuria +=2
                $ friendship_nuria +=1
                $ tension_nuria -= 1 

            "You that's edgy":
                show nuria_angry at right
                Nuria "I'm sorry?."
                Nuria "What did you just say?."
                Nuria "You such a desilutional person."
                $ confidence_nuria -=2
                $ friendship_nuria -=1
                $ tension_nuria += 5
                hide nuria_angry
            
            "Maybe you can guide me through that genre":
                show nuriat at right
                Nuria "Simple Plan - The las one standing."
                Nuria "That's all i will say."
                $ friendship_nuria +=3
                $ tension_nuria -= 1
                $ confidence_nuria += 4  
                hide nuriat at right
     
    return

label status:
    "*Here's the status from every classmate*"
    menu:
        "Grettell":
            """
            Grettell's Confidence: [confidence_grettell]

            Grettell's Tension: [tension_grettell]

            Grettell's Friendship: [friendship_gretell]
            """
            jump Options

        "Nuria":
            """
            Nuria's Confidence: [confidence_nuria]

            Nuria's Tension: [tension_nuria]

            Nuria's Friendship: [friendship_nuria]

            """
            jump Options
        
        "Back Menu":
            jump Options

            


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
    
    Tamy "Yeah I know , u want to listen to my playlist."
    character_name "Huh, how do you.."
    
    Tamy "You talk too loud... u know?"

    character_name "..."

    Tamy """
    But for you disgrace, i do not have my music player here.

    U shall come to my house to listen.

    Just wait me after class and we ready to go.

    """
    hide tamyt
    character_name "Aight."
    hide tamyt
    "*You wait for 3 hours*"
    show tamyt
    Tamy "so, here we go."

    scene bg tamy with dissolve

    character_name "Very nice house."
    show tamyt
    Tamy "yep, i bought it yesterday."

    character_name "what"

    Tamy "Anyway just turn the radio on."

    character_name "Radio?, aren't we using spooderfy?"

    Tamy "That's for losers lol."

    character_name "*Sad face*"

    hide tamyt


    
    "*You turn the radio on*"
    "What radio station to listen now?."

label tamy_options:
    scene bg tamy with dissolve
    show tamy
    menu:
        "Radio.net":
            scene bg afterdark with dissolve
            show tamy
            play music "audio/blezz1.mp3" fadein 1.0 volume 0.3
            "*Music Starts to play*"
            hide tamy

            menu:
                "Get Back":
                    character_name "*That was Dope*"
                    stop music fadeout 1.0
                    jump tamy_options
        
        "98.5 FM":
            scene bg homemage with dissolve
            show tamy
            play music "audio/blezz2.mp3" fadein 1.0 volume 0.3
            "*Music Starts to play*"
            
            hide tamy
            menu:
                "Get Back":
                    character_name "*That was Dope*"
                    stop music fadeout 1.0
                    jump tamy_options

        "CBC Radio ONE":
            scene bg maroon with dissolve
            show tamy
            play music "audio/blezz3.mp3" fadein 1.0 volume 0.3
            "*Music Starts to play*"
            hide tamy
            menu:
                "Get Back":
                    character_name "*That was Dope*"
                    stop music fadeout 1.0
                    jump tamy_options

        "Shekinah Radio":
            scene bg fnaf with dissolve
            show tamy
            play music "audio/blezz4.mp3" fadein 1.0 volume 0.3
            "*Music Starts to play*"
            hide tamy
            menu:
                "Get Back":
                    character_name "*That was Dope*"
                    stop music fadeout 1.0
                    jump tamy_options

        "Quit":
            jump Options
