# ──────────────────────────────────────
#  Music Room – consistent warm palette
# ──────────────────────────────────────

init python:
    def mr_select_chart():
        stop_preview_music()
        return store.music_room_selected

    def mr_go_back():
        stop_preview_music()
        return "__back__"

transform mr_bg_drift:
    subpixel True
    zoom 1.0
    xalign 0.5
    yalign 0.5

transform mr_panel_fade:
    alpha 0.0
    easein 0.35 alpha 1.0

transform mr_track_hover:
    xoffset 0
    easein 0.15 xoffset 8

transform mr_track_idle:
    xoffset 8
    easein 0.15 xoffset 0

transform mr_timer_pulse:
    alpha 0.7
    ease 0.6 alpha 1.0
    ease 0.6 alpha 0.7
    repeat


screen music_room(in_game=False):
    tag menu
    modal True
    on "show" action Function(open_music_room)
    on "hide" action Function(stop_preview_music)
    timer 0.1 action NullAction() repeat True

    $ song = selected_song()
    $ unlocked = track_unlocks.get(music_room_selected, False)
    $ result = track_results.get(music_room_selected, {})

    # animated background
    add Transform(song["background"], fit="contain", xysize=(1920, 1080)) at mr_bg_drift

    # dark overlay
    frame:
        background "#1a0a1add"
        xfill True
        yfill True

    hbox:
        spacing 26
        xalign 0.5
        yalign 0.5

        # ── left panel: track list ──
        frame:
            at mr_panel_fade
            background "#2a1028ee"
            xsize 420
            ysize 820
            padding (24, 24)

            vbox:
                spacing 14
                text "Music Room" size 36 color "#EC8FD0" bold True
                text "Practice unlocked charts and preview character themes." size 18 color "#d4a0c8"

                null height 8

                viewport:
                    draggable True
                    mousewheel True
                    ymaximum 660

                    vbox:
                        spacing 8
                        for song_id in ordered_song_ids():
                            $ row_song = RHYTHM_SONGS[song_id]
                            $ is_selected = song_id == music_room_selected
                            button:
                                xfill True
                                if is_selected:
                                    background "#EC8FD044"
                                else:
                                    background "#ffffff0a"
                                hover_background "#EC8FD033"
                                padding (14, 10)
                                action [
                                    SetVariable("music_room_selected", song_id),
                                    Function(preview_music_song, song_id)
                                ]

                                hbox:
                                    spacing 10
                                    yalign 0.5
                                    text "[row_song['title']]" size 22 color "#ffffff"
                                    text "[best_grade(song_id)]" size 20 color "#EC8FD0" bold True

                        null height 6
                        for song_id in locked_song_ids():
                            $ row_song = RHYTHM_SONGS[song_id]
                            button:
                                xfill True
                                background "#ffffff06"
                                padding (14, 10)
                                action SetVariable("music_room_selected", song_id)

                                hbox:
                                    spacing 10
                                    yalign 0.5
                                    text "[row_song['title']]" size 22 color "#666677"
                                    text "LOCKED" size 18 color "#555566"

        # ── right panel: track details ──
        frame:
            at mr_panel_fade
            background "#2e1630ee"
            xsize 980
            ysize 820
            padding (28, 28)

            vbox:
                spacing 18

                # Preserve the background aspect ratio in the header preview.
                frame:
                    background "#120914"
                    xsize 924
                    ysize 240
                    xalign 0.5
                    padding (0, 0)

                    add Transform(song["background"], fit="contain", xysize=(924, 240), xalign=0.5, yalign=0.5)

                hbox:
                    spacing 20

                    # song info
                    vbox:
                        spacing 8
                        xsize 580
                        text "[song['title']]" size 40 bold True color "#ffffff"
                        text "[song['character']]  |  [song['artist']]" size 22 color "#d4a0c8"

                        hbox:
                            spacing 16
                            text "Difficulty [song['difficulty']]" size 22 color "#EC8FD0"
                            text "Grade [result.get('grade', '-')]" size 22 color "#EC8FD0" bold True

                        null height 4
                        text "[song['description']]" size 20 color "#c8b0c0"
                        text "[unlock_text(song['id'])]" size 18 color "#9a8094"

                    # preview stats
                    frame:
                        background "#1a0a1aee"
                        xsize 300
                        ysize 200
                        padding (18, 16)

                        vbox:
                            spacing 8
                            text "Preview" size 26 bold True color "#EC8FD0"
                            text "[music_position_text()] / [format_time(song['length'])]" at mr_timer_pulse size 22 color "#ffffff"
                            text "Best score [result.get('score', 0)]" size 20 color "#d4a0c8"
                            text "Accuracy [result.get('accuracy_text', '--')]" size 20 color "#d4a0c8"

                # controls bar
                frame:
                    background "#3a1a38ee"
                    xfill True
                    padding (20, 18)

                    vbox:
                        spacing 12
                        text "Volume" size 22 color "#EC8FD0"
                        bar value Preference("music_room_mixer volume") xmaximum 600

                        hbox:
                            spacing 14

                            textbutton "Preview":
                                sensitive unlocked
                                text_size 22
                                text_color "#ffffff"
                                text_hover_color "#FFC0CB"
                                action Function(preview_music_song, music_room_selected)

                            textbutton "Stop":
                                text_size 22
                                text_color "#ffffff"
                                text_hover_color "#FFC0CB"
                                action Function(stop_preview_music)

                            if in_game:
                                textbutton "Select Chart":
                                    sensitive unlocked
                                    text_size 22
                                    text_color "#EC8FD0"
                                    text_hover_color "#FFC0CB"
                                    action Function(mr_select_chart)

                            textbutton "Back":
                                text_size 22
                                text_color "#ffffff"
                                text_hover_color "#FFC0CB"
                                action Function(mr_go_back)
