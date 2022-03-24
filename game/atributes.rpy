#Nuria Atributes

default confidence_nuria = 0  
default friendship_nuria =0
default tension_nuria = 0

#Grettell Atributes

default confidence_grettell = 0  
default friendship_gretell = 0
default tension_grettell = 0



#Atributes
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