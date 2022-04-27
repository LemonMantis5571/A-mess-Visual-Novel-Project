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
                background "images/UI/boxtext.png"
                text "Tamy's Confidence: [confidence_grettell]\n" + "Tamy's Friendship: [friendship_gretell]\n" + "Tamy's Tension: [tension_grettell]"     
                
            
        drag:
            drag_name "Nuria"
            xpos 0.6
            ypos 0.7
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Nuria's Confidence: [confidence_nuria]\n\n" + "Nuria's Friendship: [friendship_nuria]\n\n" + "Nuria's Tension: [tension_nuria]"


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
            
            

screen fnaf_screamer:

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
            button action [ToggleScreen("fnaf_screamer")]

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





                