

#Nuria Atributes

default confidence_nuria = 0  
default friendship_nuria =0
default tension_nuria = 0

#Grettell Atributes

default confidence_tamy = 0  
default friendship_tamy = 0
default tension_tamy = 0

# Rachel Atributes

default confidence_rachel = 0
default friendship_rachel = 0
default tension_rachel = 0

default option_music_Rachel = 0

default exitDay = False

default music_game_choice_rachel = 0

default opt_menu_talkRachel = False
default opt_menu_talkRachel_q1 = False
default opt_menu_talkRachel_q2 = False
default opt_menu_talkRachel_q3 = False
default opt_menu_talkRachel_q4 = False


# fin de opciones de rachel

#Music game atributes

default music_game_choice_nuria = 0
default music_game_choice_tamy = 0



default taste = 0

default Tamy_University_trip = False

init python:
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("fonts/Lato-Bold.ttf", False, False)


#Adult game atributes
default heart_problems = 0
default censorship = 0                
default childish = 0

#Atributes

default Nuria_finish = False
default Nuria_final_dialogue = False
default Tamy_knowledge = False

label atributes_nuria: 
    hide screen nuria_quit_menu
    $ randomnum = renpy.random.randint(1,2) # (randomize between 1 and 2)

    if friendship_nuria>=25 and tension_nuria<=5 and confidence_nuria>=25:
        $ Nuria_finish = True

    if randomnum==1 and confidence_nuria<45:

        show nuria
        Nuria "How things are going???"
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
                $ confidence_nuria += 5
                $ friendship_nuria += 5
                $ tension_nuria -= 3

            "You such an agressive person you know?":
                hide nuriat
                show nuria_angry at right
                Nuria "I'm gonna show what a true agressive person is."
                Nuria "Just get out!"
                Nuria "Dumb!"
                $ confidence_nuria -= 3
                $ tension_nuria += 5
                $ friendship_nuria -= 4

            "I like you":
                Nuria "*Blushes*"
                hide nuriat
                show nuria_blush at right
                Nuria "..."
                Nuria "So cute."
                hide nuria_blush
                show nuriat at right
                Nuria "You'll never stand a chance with me."
                Nuria "No cap." 
                hide nuriat
                $ friendship_nuria +=4
                $ tension_nuria -= 2
                $ confidence_nuria += 4  

            "My mom prepared me some chicken sandwich":
                character_name "You want a taste of it?"
                Nuria "I don't want anything from you."
                Nuria "But I'll take it anyways."
                hide nuriat
                show nuria_sandwich at right
                Nuria "Omg this is so good."
                Nuria "Dammn."
                menu:
                    "I said a piece... not all.":
                        Nuria "You such a fool."
                        $ confidence_nuria +=3
                        $ friendship_nuria +=3
                        $ tension_nuria -= 1 
                        
                    "I swear I hate you":
                        Nuria "Who do you think you are??"
                        Nuria "Trash."
                        show nuria_angry at right with dissolve
                        $ confidence_nuria -=4
                        $ friendship_nuria -=4
                        $ tension_nuria += 4

                    "*Cries in KFC*":
                        Nuria "Are you really crying?"
                        Nuria "What a mommysitter."
                        
                        $ confidence_nuria +=5
                        $ friendship_nuria += 5
                        $ tension_nuria -= 6
        jump Nuria_Music                  

    elif randomnum==2 and confidence_nuria<45:
        Nuria "OMG this class is so boring bruh."
        hide nuria
        show nuriat
        Nuria "I rather be making my next single."
        Nuria "..."
        Nuria "What are you looking at?"
        character_name "Nothing."
        Nuria "Yes, you better see nothing."
        Nuria "..."
        Nuria "You still here?"
        character_name "Yes."
        Nuria "Well, I'm bored."
        if taste == 0:
            Nuria "May i ask what's your favorite type of music?"
            $ taste = renpy.input(" ", length=8)
            Nuria "[taste], that's interesting."
            Nuria "Mine is metal."
        Nuria "I'm gonna make a song about you."
        Nuria "[taste] right?"
        character_name "Yeah."
        hide nuriat
        menu:
            "We can hear metal together":
                show nuria_blush at right
                Nuria "..."
                Nuria "Of course not."
                Nuria "Mine is so underground."
                hide nuria_blush
                $ confidence_nuria +=4
                $ friendship_nuria +=4
                $ tension_nuria -= 1 

            "You that's edgy":
                show nuria_angry at right
                Nuria "I'm sorry?"
                Nuria "B."
                Nuria "You such a disgusting person."
                $ confidence_nuria -=10
                $ friendship_nuria -=10
                $ tension_nuria += 5
                hide nuria_angry
            
            "Maybe you can guide me through that genre":
                show nuriat at right
                Nuria "Or maybe you should stay with your Babytv's songs."
                Nuria "That's all i will say."
                $ friendship_nuria +=4
                $ tension_nuria -= 1
                $ confidence_nuria += 4  
                hide nuriat at right

        jump Nuria_Music
   


label Nuria_finished_chapt1:
        if Nuria_final_dialogue == True:
            jump Nuria_finalized
        show nuria
        Nuria "I'm glad you're here."
        Nuria "You are not that bad as I think."
        #Make a Friendship dialogue script with Nuria
        Nuria "So, what do you want to talk about?"
        Nuria "Do you want to talk about the others?"
        Nuria "Or do you want to talk about your own life?"
        Nuria "Anyway, I'm not sure what to say."
        Nuria "About Tamy¿?!"
        Nuria "Well, she's a good person."
        character_name "What about the rest of the class?"
        Nuria "I only know her."
        Nuria "You should go to the university if you want to know more about the others."
        Nuria "Maybe Tamy can take you there."
        hide nuriaf
        $ Nuria_final_dialogue = True
        $ Tamy_University_trip = True
        jump Nuria_finalized
        
    

label Nuria_finalized:
        show nuria
        Nuria "You should go the University, maybe you can get more information about the others."
        Nuria "I'm sure you'll find them."
        Nuria "Tamy can take you in there."
    
        hide nuria
        jump Nuria_Music

