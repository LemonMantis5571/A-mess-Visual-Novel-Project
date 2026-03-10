# ──────────────────────────────────────
#  Status Box – consistent warm palette
# ──────────────────────────────────────

transform status_fade_in:
    alpha 0.0
    easein 0.4 alpha 1.0

screen StatusBox:
    modal True

    frame:
        background "#1a0a1ad8"
        xfill True
        yfill True

    frame:
        at status_fade_in
        background "#2e1630ee"
        xalign 0.5
        yalign 0.5
        xsize 1320
        ysize 760
        padding (40, 32)

        vbox:
            spacing 20

            text "Route Status" size 42 bold True color "#EC8FD0"

            hbox:
                spacing 30

                # nuria card
                frame:
                    background "#3a1a38ee"
                    xsize 580
                    ysize 280
                    padding (24, 20)

                    vbox:
                        spacing 8
                        text "Nuria" size 32 bold True color "#8cff66"
                        text "Stage: [route_label('nuria')]" size 22 color "#d4a0c8"
                        null height 4
                        hbox:
                            spacing 16
                            vbox:
                                text "Confidence" size 16 color "#9a8094"
                                text "[confidence_nuria]" size 26 bold True color "#ffffff"
                            vbox:
                                text "Friendship" size 16 color "#9a8094"
                                text "[friendship_nuria]" size 26 bold True color "#ffffff"
                            vbox:
                                text "Tension" size 16 color "#9a8094"
                                text "[tension_nuria]" size 26 bold True color "#ffffff"
                        null height 4
                        hbox:
                            spacing 10
                            text "Animal in Me" size 18 color "#9a8094"
                            text "[best_grade('nuria_animal')]" size 18 bold True color "#EC8FD0"
                            text "Blackout" size 18 color "#9a8094"
                            text "[best_grade('nuria_blackout')]" size 18 bold True color "#EC8FD0"

                # tamy card
                frame:
                    background "#1a1a38ee"
                    xsize 580
                    ysize 280
                    padding (24, 20)

                    vbox:
                        spacing 8
                        text "Tamy" size 32 bold True color "#6666ff"
                        text "Stage: [route_label('tamy')]" size 22 color "#a0a8d4"
                        null height 4
                        hbox:
                            spacing 16
                            vbox:
                                text "Confidence" size 16 color "#808aaa"
                                text "[confidence_tamy]" size 26 bold True color "#ffffff"
                            vbox:
                                text "Friendship" size 16 color "#808aaa"
                                text "[friendship_tamy]" size 26 bold True color "#ffffff"
                            vbox:
                                text "Tension" size 16 color "#808aaa"
                                text "[tension_tamy]" size 26 bold True color "#ffffff"
                        null height 4
                        hbox:
                            spacing 10
                            text "Afterdark" size 18 color "#808aaa"
                            text "[best_grade('tamy_afterdark')]" size 18 bold True color "#EC8FD0"
                            text "Homemage" size 18 color "#808aaa"
                            text "[best_grade('tamy_homemage')]" size 18 bold True color "#EC8FD0"

            # music room summary
            frame:
                background "#1a0a1aee"
                xfill True
                ysize 230
                padding (24, 20)

                vbox:
                    spacing 8
                    text "Music Room" size 28 bold True color "#EC8FD0"
                    text "Unlocked tracks: [unlocked_track_count()] / [len(RHYTHM_SONGS)]" size 22 color "#ffffff"
                    text "Selected track: [RHYTHM_SONGS[music_room_selected]['title']]" size 22 color "#d4a0c8"
                    text "Current goal: [chapter]" size 22 color "#ffffff"
                    text "Clear charts with a C grade or higher to move the story." size 18 color "#9a8094"

            textbutton "Back":
                xalign 1.0
                text_size 24
                text_color "#EC8FD0"
                text_hover_color "#FFC0CB"
                action Return()
