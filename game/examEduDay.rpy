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

    
#screen countdown:
    #timer 0.01 repeat True action If(time > 0, true = SetVariable("time", time - 0.01), false = [Hide('countdown'), Jump('finalTimeExamFailed')])
    #bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 300 at alpha_dissolve

label preguntas:
    $ fail_question = 0
    label menu1:
        #$ time = 5
        #$ timer_range = 5
        #$ timer_jump = 'menu1_slow' #esto no sirve xd
        #show screen countdown

        menu:
            "Say Statement"
            "Choice 1":
                show rachel
                #hide screen countdown
                Rachel "GG"
                
                jump menu2
            "Choice 2":
                show rachel
                #hide screen countdown
                Rachel "GG"
                $ fail_question += 1
                jump menu2
            "Choice 3":
                show rachel
                #hide screen countdown
                Rachel "GG"
                $ fail_question += 1
                jump menu2
            

    label menu2:
        #$ time = 5
        #$ timer_range = 5
        #$ timer_jump = 'menu2_slow'
        #show screen countdown

        menu:
            "Say Statement"
            "Choice 1":
                show rachel
                #hide screen countdown
                Rachel "GG"
                $ fail_question += 1
                jump menu3

            "Choice 2":
                show rachel
                #hide screen countdown
                Rachel "GG"
                $ fail_question += 1
                jump menu3
                

            "Choice 1":
                show rachel
                #hide screen countdown
                Rachel "GG"
                jump menu3

    label menu3:
        #$ time = 5
        #$ timer_range = 5
        #$ timer_jump = 'menu3_slow'

        #show screen countdown

        menu:
            "Say Statement"
            "Choice 1":
                show rachel
                hide screen countdown
                Rachel "GG"
                $ fail_question += 1
                jump menu4
                


            "Choice 2":
                show rachel
                hide screen countdown
                Rachel "GG"
                jump menu4
                


            "Choice 3":
                show rachel
                hide screen countdown
                Rachel "GG"
                $ fail_question += 1
                jump menu4

    label menu4:
        """$ time = 5
        $ timer_range = 5
        $ timer_jump = 'menu4_slow'
        show screen countdown"""

        menu:
            "Say Statement"
            "Choice 1":
                show rachel
                #hide screen countdown
                Rachel "GG"
                jump finalTimeExam



label finalTimeExamFailed:
    show rachel
    "¡Hola! ¿Cómo estás?"

    $ friendship_rachel += 1
    $ finalTimeExamDialog = 1

    jump preGame

label finalTimeExam:
    show rachel
    "¡Hola! ¿Cómo estás?2"

    $ friendship_rachel += 2
    $ confidence_rachel += 5
    $ finalTimeExamDialog = 0

    jump preGame