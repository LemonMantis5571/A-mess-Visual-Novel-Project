default character_name = "Sherylda"
default chapter = "World I: Frutiger Aero"
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

image bg class0 = "images/bg blank.webp"
image bg guide = "images/bg blank.webp"
image bg class1_frutiger = "images/bg blank.webp"
image bg class1_empty = "images/bg blank.webp"
image bg class1 = "images/bg blank.webp"
image bg class = "images/bg blank.webp"
image bg_nuria_frutiger = "images/bg blank.webp"
image bg afterdark = "images/bg blank.webp"
image bg homemage = "images/bg blank.webp"
image bg main_menu = "images/chapter1/bg main_menu.jpg"

init python:
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("fonts/Lato-Bold.ttf", False, False)
