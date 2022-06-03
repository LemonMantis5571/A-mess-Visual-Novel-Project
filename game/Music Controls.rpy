init python:
    def convert_float_into_time(t):
        i, f = divmod(t, 1)
        i = int(i)
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        return "{:02}:{:02}.{:02}".format(m, s, int(f*100))

screen music_controls:
    default soundis = False
    default p = None
    style_prefix "musiccontrols"
    drag:
        frame:
            if soundis:
                button:
                    text "⇲" size 35
                    action ToggleScreenVariable('soundis', True, False)
            else:
                xsize 600
                vbox:
                    spacing 5
                    timer .1 repeat True action SetScreenVariable("p",p)
                    if isinstance(renpy.music.is_playing(channel='music'), int):
                        if renpy.music.get_pos(channel='music'):
                            $ p = renpy.music.get_pos(channel='music')
                            vbox:
                                text renpy.music.get_playing(channel='music').split("/")[-1]
                                text "{} / {}".format(convert_float_into_time(renpy.music.get_pos(channel='music')), convert_float_into_time(renpy.music.get_duration(channel='music')))
                        else:
                            text "stopped"
                        bar value StaticValue(value=p, range=renpy.music.get_duration(channel='music')) xysize 500,40
                    bar value Preference("music volume") xysize 500,20
                    hbox:
                        button:
                            text "⟲" size 35
                            action ToggleMute('music')
                        button:
                            text "|| ||" size 25
                            action PauseAudio('music', value="toggle")
                        button:
                            text "⊠" size 35
                            action Stop('music')
                        button:
                            text "⇱" size 35
                            action ToggleScreenVariable('soundis', True, False)

style musiccontrols_button:
    xysize (60,60)