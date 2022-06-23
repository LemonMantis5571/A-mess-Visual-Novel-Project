

init python:
    def icons_update(st):
        global is_animating
        global icons_to_animate

        if is_animating:
            for i, icon in enumerate(icons_to_animate):
                t = Transform(child= icon.hover_image)

                if icon.zoom < 0.7 and icon.zoomIn == True:
                    icon.zoom += 0.01
                    t.zoom = icon.zoom
                    t.update()
                    icon.set_child(t)
                    icon.posx -= 0.5
                    icon.posy -= 0.5
                    icon.x = icon.posx
                    icon.y = icon.posy
                elif icon.zoom >= 0.7 and icon.zoomIn == True:
                    icon.zoomIn = False
                    icon.zoomOut = True
                elif icon.zoom > 0.5 and icon.zoomOut == True:
                    icon.zoom -= 0.01
                    t.zoom = icon.zoom
                    t.update()
                    icon.set_child(t)
                    icon.posx += 0.5
                    icon.posy += 0.5
                    icon.x = icon.posx
                    icon.y = icon.posy
                else:
                    icon.zoomOut = False
                    icon.zoomIn = True
                    t.zoom = 0.5
                    t.child = icon.idle_image
                    t.update()
                    icon.set_child(t)
                    icons_to_animate.pop(i)

            if len(icons_to_animate) != 0:
                return 0
            else:
                is_animating = False
                return None
        else:
            return None

    def icons_events(event, x, y, st):
        if event.type == 1025:
            if event.button == 1:
                for icon in icons_list:
                    if icon is not None:
                        if icon.x <= x <= (icon.x + icon_size) and icon.y <= y <= (icon.y + icon_size):
                            findMatches(icon = icon, deleteOnMatch = True)
                            break

    def findMatches(icon, deleteOnMatch):
        matches = []
        matches.append(icon)

        for icon in matches:
            #Match right
            if icon.index + 1 < grid_size and icons_list[icon.index + 1] is not None:
                if icon.icon_type == icons_list[icon.index + 1].icon_type and (icon.index + 1) % icons_per_row != 0 and icons_list[icon.index + 1] not in matches:
                    matches.append(icons_list[icon.index + 1])
            #Match down
            if icon.index <= grid_size - icons_per_row - 1 and icons_list[icon.index + icons_per_row] is not None:
                if icon.icon_type == icons_list[icon.index + icons_per_row].icon_type and icons_list[icon.index + icons_per_row] not in matches:
                    matches.append(icons_list[icon.index + icons_per_row])
            #Match left
            if icon.index - 1 >= 0 and icons_list[icon.index - 1] is not None:
                if icon.icon_type == icons_list[icon.index - 1].icon_type and icon.index % icons_per_row != 0 and icons_list[icon.index - 1] not in matches:
                    matches.append(icons_list[icon.index - 1])
            #Match up
            if icon.index >= icons_per_row and icons_list[icon.index - icons_per_row] is not None:
                if icon.icon_type == icons_list[icon.index - icons_per_row].icon_type and icons_list[icon.index - icons_per_row] not in matches:
                    matches.append(icons_list[icon.index - icons_per_row])

        if len(matches) != 1 and deleteOnMatch == True:
            deleteMatches(matches)
        elif deleteOnMatch == False:
            animateOnMatch(matches)

    def animateOnMatch(matches):
        global icons_to_animate
        global is_animating
        for icon in matches:
            icons_to_animate.append(icon)
        is_animating = True
        icons.redraw(0)

    def deleteMatches(matches):
        global score
        for icon in matches:
            icons_list[icon.index] = None
            icon.destroy()
            score += point

        renpy.restart_interaction()
        icons.redraw(0)
        shiftIcons()

    def shiftIcons():
        for i, icon in enumerate(reversed(icons_list)):
            rindex = (grid_size - 1) - i

            if icon is None and rindex >= icons_per_row:
                rm = 0
                while icons_list[rindex - (icons_per_row * rm)] is None and rindex - (icons_per_row * rm) >= icons_per_row:
                    rm += 1
                if icons_list[rindex - (icons_per_row * rm)] is not None:
                    icons_list[rindex - (icons_per_row * rm)].y += (icon_size * rm) + (icon_padding * rm)
                    icons_list[rindex] = icons_list[rindex - (icons_per_row * rm)]
                    icons_list[rindex - (icons_per_row * rm)] = None
                    icons_list[rindex].index = rindex

        for i in range(grid_size - icons_per_row, grid_size - 1):
            if icons_list[i] is None:
                cm = 0
                while icons_list[i + cm] is None and i + cm < grid_size - 1:
                    cm += 1
                if icons_list[i + cm] is not None:
                    icons_list[i + cm].x -= (icon_size * cm) + (icon_padding * cm)
                    icons_list[i] = icons_list[i + cm]
                    icons_list[i + cm] = None
                    icons_list[i].index = i
                    for icon in range(grid_size / icons_per_row):
                        if icons_list[(i + cm) - (icons_per_row * icon)] is not None:
                            icons_list[(i + cm) - (icons_per_row * icon)].x -= (icon_size * cm) + (icon_padding * cm)
                            icons_list[i - (icons_per_row * icon)] = icons_list[(i + cm) - (icons_per_row * icon)]
                            icons_list[(i + cm) - (icons_per_row * icon)] = None
                            icons_list[i - (icons_per_row * icon)].index -= cm

        icons.redraw(0)
        renpy.retain_after_load()
        hint(hintButton = False)

    def hint(hintButton):
        match = False
        for icon in icons_list:
            if icon is not None:
                #Match right
                if icon.index + 1 < grid_size and icons_list[icon.index + 1] is not None:
                    if icon.icon_type == icons_list[icon.index + 1].icon_type and (icon.index + 1) % icons_per_row != 0:
                        if hintButton:
                            findMatches(icon = icon, deleteOnMatch = False)
                        else:
                            match = True
                        break
                #Match down
                if icon.index <= grid_size - icons_per_row - 1 and icons_list[icon.index + icons_per_row] is not None:
                    if icon.icon_type == icons_list[icon.index + icons_per_row].icon_type:
                        if hintButton:
                            findMatches(icon = icon, deleteOnMatch = False)
                        else:
                            match = True
                        break
                #Match left
                if icon.index - 1 >= 0 and icons_list[icon.index - 1] is not None:
                    if icon.icon_type == icons_list[icon.index - 1].icon_type and icon.index % icons_per_row != 0:
                        if hintButton:
                            findMatches(icon = icon, deleteOnMatch = False)
                        else:
                            match = True
                        break
                #Match up
                if icon.index >= icons_per_row and icons_list[icon.index - icons_per_row] is not None:
                    if icon.icon_type == icons_list[icon.index - icons_per_row].icon_type:
                        if hintButton:
                            findMatches(icon = icon, deleteOnMatch = False)
                        else:
                            match = True
                        break

        if not match and not hintButton:
            global icons_list
            for icon in icons_list:
                if icon is not None:
                    icon.destroy()
            icons_list = []
            icons.redraw(0)
            renpy.jump("setup_icons")

screen gameOver:
    python:
        score_type = ""

        for type in scoring:
            if scoring[type][0] <= score <= scoring[type][1]:
                score_type = type
                break

    modal True

    frame:
        background "#00000050"
        xfill True
        yfill True
        frame:
            background "#877d6b"
            xysize (500, 250)
            padding (2, 2)
            align (0.5, 0.5)
            frame:
                background "#f6f1e7"
                xfill True
                yfill True

                text "Game Over!" size 30 color "#000000" align (0.5, 0.1)
                text "Your score is: [score]" size 18 color "#000000" align (0.5, 0.4)
                text "You got a [score_type] score" size 18 color "#000000" align (0.5, 0.5)
                button:
                    background "#FFFFFF"
                    xysize (120, 50)
                    align (0.5, 0.8)
                    textbutton _("Win") align (0.5, 0.5) action Jump("Hola")
                    
                        
                    

transform half_size:
    zoom 0.5

label setup_icons:
    python:
        for i in range(grid_size):
            rand_image = icon_images[renpy.random.randint(0,4)]
            idle_path = "Icons/{}.png".format(rand_image)
            hover_path = "Icons/{}_hover.png".format(rand_image)
            idle_image = Image(idle_path)
            hover_image = Image(hover_path)
            icons_list.append(icons.create(Transform(child= idle_image, zoom = 0.5)))
            icons_list[-1].index = i
            icons_list[-1].icon_type = rand_image
            icons_list[-1].idle_image = idle_image
            icons_list[-1].hover_image = hover_image
            icons_list[-1].zoom = 0.5
            icons_list[-1].posx = 0.0
            icons_list[-1].posy = 0.0
            icons_list[-1].zoomIn= True
            icons_list[-1].zoomOut = False

    call screen SameGame

screen scoreUI:
    timer 0.1 action If(round(countdownTime) > 0, true = SetVariable("countdownTime", countdownTime - 0.1), false = Show("gameOver")) repeat If(round(countdownTime) > 0, true = True, false = False)
    frame:
        align (0.01, 0.01)
        background "#877d6b"
        xysize (250, 50)
        padding (2, 2)
        frame:
            background "#f6f1e7"
            xfill True
            yfill True
            grid 4 1:
                xfill True
                spacing 0
                image "UI/coin-icon.png" xalign 1.0 at half_size
                text "[score]" align(0.0, 0.5) color "#000000"
                image "UI/clock-icon.png" xalign 1.0 at half_size
                text "{:.0f}".format(countdownTime) align(0.0, 0.5) color "#000000"

screen SameGame:
    $frame_xsize = (icons_per_row * icon_size) + (icons_per_row * icon_padding) + icon_padding + 4
    $frame_ysize = ((grid_size / icons_per_row) * icon_size) + ((grid_size / icons_per_row) * icon_padding) + icon_padding + 4

    frame:
        background "#FFFFFF50"
        xalign 0.2
        yalign 0.5
        xsize frame_xsize
        ysize frame_ysize

        $crow = 0
        $ccolumn = 0

        for icon in icons_list:
            $xp = (icon_size * ccolumn) + (icon_padding * ccolumn)
            $yp = (icon_size * crow) + (icon_padding * crow)

            image "Icons/grid-cell.png" xpos xp ypos yp zoom 0.5
            if icon is not None:
                if not is_animating:
                    $icon.x = xp
                    $icon.y = yp
                    $icon.posx = xp
                    $icon.posy = yp
                else:
                    $icon.x = icon.posx
                    $icon.y = icon.posy

            python:
                if ccolumn % (icons_per_row - 1) != 0 or ccolumn == 0:
                    ccolumn += 1
                else:
                    ccolumn = 0
                    crow += 1

        add icons

    button:
        xysize (120, 40)
        pos (0.25, 0.80)
        background "#FFFFFF"
        action If(is_animating == False, true= Function(hint, hintButton = True, _update_screens = False), false= NullAction())
        text "Hint" color "#000000" size 20 align (0.5, 0.5)

label initGame:
    $grid_size = 100
    $icon_size = 50
    $icon_padding = 2
    $icons_per_row = 10
    $icons = SpriteManager(update = icons_update, event= icons_events)
    $icon_images = ["icon_1", "icon_2", "icon_3", "icon_4", "icon_5"]
    $icons_list = []
    $countdownTime = 100.0
    $point = 5
    $score = 0
    $scoring = {"low" : [0, 1000], "medium" : [1001, 2000], "high" : [2001, 3000]}
    $icons_to_animate = []
    $is_animating = False

    scene bg aula1
    show rachel at right
    show screen scoreUI
    jump setup_icons

    return


label Hola:
    scene bg uni
    hide screen gameOver
    hide screen scoreUI

    show rachel at right
    Rachel "That was fun "
    Rachel "It was a great day but I'll go home, see you"
    
    character_name "Goodbye"

    hide rachel

    $ playGame =+ 1

    jump preGame