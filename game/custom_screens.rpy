init python:
    def drag_placed(drags,drop):
        if not drop:
                return
        
        store.draggable = drags[0].drag_name
        store.droppable = drop.drop_name
        return True

init python:
    style.window.background = Frame("images/UI/boxtext.png", 100, 100)

screen StatusBox:
    fixed:
        drag:
            drag_name "Tamy"
            xpos 0.4
            ypos 0.5
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Tamy's Confidence: [confidence_tamy]\n" + "Tamy's Friendship: [friendship_tamy]\n" + "Tamy's Tension: [tension_tamy]"     

        drag:
            drag_name "Rachel"
            xpos 0.7
            ypos 0.8
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Rachel's Confidence: [confidence_rachel]\n" + "Rachel's Friendship: [friendship_rachel]\n" + "Rachel's Tension: [tension_rachel]"     
               
            
        drag:
            drag_name "Nuria"
            xpos 0.6
            ypos 0.7
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Nuria's Confidence: [confidence_nuria]\n" + "Nuria's Friendship: [friendship_nuria]\n" + "Nuria's Tension: [tension_nuria]"

        drag:
            drag_name "Music Game"
            xpos 0.5
            ypos 0.5
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Music taste status: \nMetal: [music_game_choice_nuria] \nPop-Synthwave: [music_game_choice_tamy]"
            
            

        button:
            hover_background "#00a"
            background "images/UI/1textbox.png"
            xpadding 140
            ypadding 120
            xpos 1640
            ypos 44
            yalign 0.5
            textbutton "Exit"  action [ToggleScreen("StatusBox"), Jump("Options")]

screen nuria_buttons:

    draggroup:
        drag:
            drag_name "phone"
            child "nuriaphone.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


screen fnaf_golden:

    draggroup:
        drag:
            drag_name "golden"
            child "images/UI/goldfreddy.png"
            xalign 0.5
            yalign 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            button action [ToggleScreen("fnaf_golden")]

screen afterdark:

    draggroup:
        drag:
            drag_name "mrkitty"
            child "images/UI/afterdark.png"
            xalign 0.5
            yalign 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            button action [ToggleScreen("afterdark")]

screen synthwave:

    draggroup:
        drag:
            drag_name "wave"
            child "images/UI/synthwave.png"
            xalign 0.5
            yalign 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            button action [ToggleScreen("synthwave")]

screen caldera:

    draggroup:
        drag:
            drag_name "sugar"
            child "images/UI/caldera.png"
            xalign 0.5
            yalign 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            button action [ToggleScreen("caldera")]
            
            

'''screen fnaf_screamer:

    draggroup:
        drag:
            drag_name "screamer"
            child "images/UI/screamer.png"
            xalign 0.5
            yalign 0.5
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            button action [ToggleScreen("fnaf_screamer")] '''

screen nuria_quit:
    button:
            background "images/UI/1textbox.png"
            xpadding 140
            ypadding 120
            xpos 1640
            ypos 44
            yalign 0.5
            textbutton "Quit"  action [ToggleScreen("nuria_quit"), Jump("nuriarepeat")]


screen nuria_quit_menu:
    button:
            background "images/UI/1textbox.png"
            xpadding 140
            ypadding 120
            xpos 1640
            ypos 44
            yalign 0.5
            textbutton "Quit"  action [ToggleScreen("nuria_quit_menu"), Jump("Options")]

screen guide_quit:
    button:
            background "images/UI/1textbox.png"
            xpadding 140
            ypadding 120
            xpos 1640
            ypos 44
            yalign 0.5
            textbutton "Quit"  action [ToggleScreen("guide_quit"), Jump("Options")]

'''
screen Music_Player:
    button:
        text "Music Controls"
        action ToggleScreen("music_controls") '''


screen thefeels_buttons:

    draggroup:
        drag:
            drag_name "phone"
            child "thefeels.png"
            xpos 450
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True          