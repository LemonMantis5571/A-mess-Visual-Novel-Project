default character_name = "Sherylda"
default chapter = "Chapter I: Pulse Check"
default heart_problems = 0
default censorship = 0

default confidence_nuria = 0
default friendship_nuria = 0
default tension_nuria = 0

default confidence_tamy = 0
default friendship_tamy = 0
default tension_tamy = 0

default route_nuria_stage = 0
default route_tamy_stage = 0
default tamy_unlocked = False
default ending_seen = False

default music_room_selected = "nuria_animal"
default track_unlocks = {
    "nuria_animal": True,
    "nuria_blackout": False,
    "tamy_afterdark": False,
    "tamy_homemage": False,
}
default track_results = {}

init python:
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("fonts/Lato-Bold.ttf", False, False)
