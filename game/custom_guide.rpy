#Screens
label guide:
    scene bg blank
    stop music fadeout 1.0
    play music "audio/guide.mp3" fadein 2.0 volume 0.2
    scene bg guide with pixellate
    
    guide "This is the guide screen."
    guide "You can press the enter key to skip the text."
    guide "You can press the escape key to go back to the main menu."
    guide "Press any key to continue."
    hide guide

label guide_options:
    hide guide
    "Select an option."
    show guide with hpunch
    menu:
        "Im stuck.":
            show guide with dissolve
            guide "So you are stuck in [chapter]'s chapter."
            guide "Maybe you should try to find a way out."
            show guide at right with move
            guide "Like listening the songs multiple times."
            guide "(?)"
            guide "If you max out status points, maybe you can unlock new paths in the history."
            guide "Press any key to continue."
            jump guide_options
        

        "How do I save the game?":
            show guide with dissolve
            guide "You can save the game by pressing the save key in the options below the screen."
            guide "You can also load the game by pressing the load key."
            show guide at right with move
            guide "Very simple to use."
            jump guide_options
        
        "How do I change the music?":
            show guide at right with move
            guide "You can change the music by unlocking them in the main history."
            guide "As you are progressing, you will unlock an option to change whenever you want."
            jump guide_options
            

        "How do I change the character?":
            show guide at right with dissolve
            guide "The only way to change character is to create a new game file."
            jump guide_options

        "Quit.":
           hide guide
           stop music fadeout 1.0
           jump Options

'''label traveling:
        scene bg blank
        stop music fadeout 1.0
        scene bg traveling with dissolve
        show traveling at right with dissolve
        traveling "You are now in a city."
        traveling "You can go to the university or to the KFC."
        traveling "Which do you choose?"
        menu:
            "Go to the university":
                $ university = 1
                jump university
            "Go to the KFC":
                $ university = 0
                jump university
        hide traveling
    '''
