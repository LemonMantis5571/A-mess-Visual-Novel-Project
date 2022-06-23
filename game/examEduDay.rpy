init python:
    import time

    timer_range = 0
    timer_jump = 0
    time = 0

    '''transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0'''

label preguntas:
    
    label menu1:


        menu:
            "the ram is..."
            "is the main memory of a device":
                show rachel
                Rachel "Good :3"
                
                jump menu2
            "The Crane of chepito":
                show rachel
                Rachel "hmmmmm ok?"
                $ fail_question += 1
                jump menu2
            "don't know":
                show rachel
                Rachel "hmmmmm ok"
                $ fail_question += 1
                jump menu2
            

    label menu2:


        menu:
            "The motherboard is..."
            "My mom's board":
                show rachel
                #hide screen countdown
                Rachel "Really?"
                $ fail_question += 1
                jump menu3

            "the main board on the external structure of a computer":
                show rachel
                #hide screen countdown
                Rachel "Really?"
                $ fail_question += 1
                jump menu3
                

            "the main board on the internal structure of a computer":
                show rachel
                #hide screen countdown
                Rachel "You know him a lot"
                jump menu3

    label menu3:

        menu:
            "What is the CPU?"
            "is the brain of the computer":
                show rachel
                hide screen countdown
                Rachel "..."
                $ fail_question += 1
                jump finalTimeExam          

            "don't know":
                show rachel
                hide screen countdown
                Rachel "Great, finished!"
                jump finalTimeExam

            "This is not xd":
                show rachel
                hide screen countdown
                Rachel "..."
                $ fail_question += 1
                jump finalTimeExam
                

label finalTimeExam:
    show rachel

    if fail_question =>2:
        Rachel "We will do it better to next"
    else:
        Rachel "It wasn't so difficult "

    $ friendship_rachel += 2
    $ confidence_rachel += 5
    $ finalTimeExamDialog = 0

    jump preGame