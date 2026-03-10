label start:
    scene bg blank
    $ sync_music_progress()
    jump start_uni


label traveling:
    stop music fadeout 1.0
    scene bg blank with dissolve
    centered "*Monday morning*"
    centered "*The bus ride to Lincoln feels half real, half haunted.*"
    play music "audio/bgm_walking.mp3" fadein 1.0 volume 0.3
    scene bg zumen with slideawayleft
    character_name "If I miss first period again, Miss Isela is going to skin me alive."
    character_name "At least the city still sounds awake."
    centered "*You reach Lincoln and force yourself through the gate.*"
    jump lincoln


label lincoln:
    $ chapter = "Chapter I: Pulse Check"

    scene bg class1 with dissolve
    play music "audio/bgm_class.mp3" fadein 1.0 volume 0.3
    "The room is already full."
    scene bg class0
    show isela at left
    Isela "Good morning, [character_name]. Late. Again."
    Isela "Sit down before I decide to count this as a speech."
    hide isela
    scene bg class1
    character_name "Everyone looks different today."
    character_name "Not quieter. Sharper."
    character_name "Like every desk has its own metronome."
    jump class_hub


label class_hub:
    $ sync_music_progress()
    if route_nuria_stage >= 3 and route_tamy_stage >= 3 and not ending_seen:
        jump class_ending

    scene bg class1
    play music "audio/bgm_class.mp3" fadein 1.0 volume 0.3

    "What do you want to do?"
    menu:
        "Talk to Nuria":
            jump nuria_route

        "Talk to Tamy":
            if tamy_unlocked:
                jump tamy_route
            else:
                scene bg class0
                show tamyt at left
                Tamy "Not yet."
                Tamy "You still sound like static."
                hide tamyt
                jump class_hub

        "Open music room":
            call screen music_room(in_game=True)
            if _return and _return not in ("__back__", True, False) and _return in RHYTHM_SONGS:
                $ selected_chart = _return
                call play_rhythm_song(selected_chart)
                $ store_last_result(selected_chart)
            jump class_hub

        "Status":
            call screen StatusBox
            jump class_hub

        "Guide":
            jump guide


label nuria_route:
    scene bg class0

    if route_nuria_stage == 0:
        show nuria at right
        Nuria "You look like somebody who hears songs from outside the room."
        Nuria "That is useless."
        Nuria "If you want to know me, keep up with mine."
        character_name "So I do not just listen?"
        Nuria "No."
        Nuria "You play."
        $ route_nuria_stage = 1
        hide nuria
        jump class_hub

    if route_nuria_stage == 1:
        show nuriat at right
        Nuria "First pulse. \"Animal in Me\"."
        Nuria "Do not fake confidence. Hit on time."
        hide nuriat
        call play_rhythm_song("nuria_animal")
        $ result = _return
        $ store_last_result("nuria_animal")
        if result["cleared"]:
            scene bg class0
            show nuria_blush at right
            Nuria "You stayed with it."
            Nuria "That was not terrible."
            $ confidence_nuria += 4
            $ friendship_nuria += 3
            $ tension_nuria = max(0, tension_nuria - 1)
            $ route_nuria_stage = 2
            $ tamy_unlocked = True
            $ unlock_track("nuria_blackout")
            $ unlock_track("tamy_afterdark")
            hide nuria_blush
        else:
            scene bg class0
            show nuria_angry at right
            Nuria "No. You drifted."
            Nuria "Practice it in the music room and come back."
            $ tension_nuria += 1
            hide nuria_angry
        jump class_hub

    if route_nuria_stage == 2:
        show nuriat at right
        Nuria "Second pulse. \"Blackout\"."
        Nuria "This one is what I sound like before I say anything."
        hide nuriat
        call play_rhythm_song("nuria_blackout")
        $ result = _return
        $ store_last_result("nuria_blackout")
        if result["cleared"]:
            scene bg class0
            show nuria at right
            Nuria "Fine."
            Nuria "Now you get it."
            Nuria "Loud is only the shell."
            Nuria "Tamy will talk to you now. Tell her I allowed it."
            $ confidence_nuria += 5
            $ friendship_nuria += 5
            $ tension_nuria = max(0, tension_nuria - 2)
            $ route_nuria_stage = 3
            hide nuria
        else:
            scene bg class0
            show nuria_angry at right
            Nuria "Still not there."
            Nuria "When your hands stop hesitating, come back."
            $ tension_nuria += 1
            hide nuria_angry
        jump class_hub

    show nuria at right
    Nuria "I already said what matters."
    Nuria "Use the music room if you want a better grade."
    hide nuria
    jump class_hub


label tamy_route:
    scene bg class0

    if route_tamy_stage == 0:
        show tamyt at right
        Tamy "Nuria said you can keep tempo."
        Tamy "That lowers my suspicion a little."
        Tamy "I do not like noise. I like precision."
        Tamy "Meet me on my first chart."
        $ route_tamy_stage = 1
        $ unlock_track("tamy_afterdark")
        hide tamyt
        jump class_hub

    if route_tamy_stage == 1:
        show tamyt at right
        Tamy "\"Afterdark.\""
        Tamy "Hold steady. Do not rush the gaps."
        hide tamyt
        call play_rhythm_song("tamy_afterdark")
        $ result = _return
        $ store_last_result("tamy_afterdark")
        if result["cleared"]:
            scene bg class0
            show tamy at right
            Tamy "That was cleaner."
            Tamy "You actually listen with your hands."
            $ confidence_tamy += 4
            $ friendship_tamy += 4
            $ tension_tamy = max(0, tension_tamy - 1)
            $ route_tamy_stage = 2
            $ unlock_track("tamy_homemage")
            hide tamy
        else:
            scene bg class0
            show tamyt at right
            Tamy "Too early. Too late. Too nervous."
            Tamy "Try again after practicing."
            $ tension_tamy += 1
            hide tamyt
        jump class_hub

    if route_tamy_stage == 2:
        show tamyt at right
        Tamy "\"Homemage.\""
        Tamy "This is the one I do not put on for strangers."
        hide tamyt
        call play_rhythm_song("tamy_homemage")
        $ result = _return
        $ store_last_result("tamy_homemage")
        if result["cleared"]:
            scene bg class0
            show tamy at right
            Tamy "All right."
            Tamy "You are not a stranger now."
            Tamy "Maybe this class is less unbearable with you in it."
            $ confidence_tamy += 5
            $ friendship_tamy += 5
            $ tension_tamy = max(0, tension_tamy - 2)
            $ route_tamy_stage = 3
            hide tamy
        else:
            scene bg class0
            show tamyt at right
            Tamy "You missed the shape of it."
            Tamy "Practice before you ask again."
            $ tension_tamy += 1
            hide tamyt
        jump class_hub

    show tamy at right
    Tamy "We are good."
    Tamy "Improve your grades if you want, but the route is done."
    hide tamy
    jump class_hub


label class_ending:
    $ ending_seen = True
    stop music fadeout 1.0
    scene bg class1 with dissolve
    play music "audio/bgm_intromusic.mp3" fadein 1.0 volume 0.3
    character_name "The room sounds different now."
    character_name "Not softer."
    character_name "Just less closed."
    show nuria at right
    Nuria "You kept tempo."
    hide nuria
    show tamy at left
    Tamy "And did not panic."
    hide tamy
    show isela at left
    Isela "If all of you are finished having invisible emotional breakthroughs, open your notebooks."
    hide isela
    character_name "Maybe this mess finally has a rhythm."
    return
