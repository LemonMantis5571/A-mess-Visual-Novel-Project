init python:
    import copy
    import time as _pytime
    store = renpy.store

    renpy.music.register_channel("preview", mixer="music_room_mixer", loop=False)
    renpy.music.register_channel("rhythm", mixer="music", loop=False)

    RHYTHM_SONGS = {
        "nuria_animal": {
            "id": "nuria_animal",
            "title": "Animal in Me",
            "artist": "Nuria Route",
            "character": "Nuria",
            "audio": "audio/metal1.mp3",
            "background": "bg animal",
            "difficulty": "2/5",
            "length": 16.4,
            "description": "Nuria's first chart. Sharp hits, simple pressure.",
            "unlock_text": "Unlocked from the start.",
            "notes": [
                {"time": 1.00, "lane": 0}, {"time": 1.40, "lane": 1}, {"time": 1.80, "lane": 2}, {"time": 2.20, "lane": 3},
                {"time": 2.80, "lane": 0}, {"time": 3.00, "lane": 1}, {"time": 3.20, "lane": 2}, {"time": 3.40, "lane": 3},
                {"time": 4.10, "lane": 1}, {"time": 4.55, "lane": 0}, {"time": 5.00, "lane": 2}, {"time": 5.45, "lane": 3},
                {"time": 6.10, "lane": 0}, {"time": 6.50, "lane": 2}, {"time": 6.90, "lane": 1}, {"time": 7.30, "lane": 3},
                {"time": 8.10, "lane": 0}, {"time": 8.55, "lane": 1}, {"time": 9.00, "lane": 2}, {"time": 9.45, "lane": 3},
                {"time": 10.10, "lane": 3}, {"time": 10.50, "lane": 2}, {"time": 10.90, "lane": 1}, {"time": 11.30, "lane": 0},
                {"time": 12.10, "lane": 0}, {"time": 12.30, "lane": 2}, {"time": 12.50, "lane": 1}, {"time": 12.70, "lane": 3},
                {"time": 13.50, "lane": 1}, {"time": 14.00, "lane": 0}, {"time": 14.50, "lane": 2}, {"time": 15.00, "lane": 3},
            ],
        },
        "nuria_blackout": {
            "id": "nuria_blackout",
            "title": "Blackout",
            "artist": "Nuria Route",
            "character": "Nuria",
            "audio": "audio/metal3.mp3",
            "background": "bg blackout",
            "difficulty": "3/5",
            "length": 18.2,
            "description": "Nuria's second chart. Denser bursts and a faster center lane.",
            "unlock_text": "Clear Animal in Me.",
            "notes": [
                {"time": 1.10, "lane": 0}, {"time": 1.45, "lane": 2}, {"time": 1.80, "lane": 1}, {"time": 2.15, "lane": 3},
                {"time": 2.90, "lane": 0}, {"time": 3.15, "lane": 1}, {"time": 3.40, "lane": 2}, {"time": 3.65, "lane": 3},
                {"time": 4.30, "lane": 2}, {"time": 4.55, "lane": 1}, {"time": 4.80, "lane": 0}, {"time": 5.05, "lane": 1},
                {"time": 5.30, "lane": 2}, {"time": 5.55, "lane": 3}, {"time": 6.10, "lane": 0}, {"time": 6.45, "lane": 3},
                {"time": 7.00, "lane": 1}, {"time": 7.35, "lane": 2}, {"time": 7.70, "lane": 1}, {"time": 8.05, "lane": 0},
                {"time": 8.70, "lane": 3}, {"time": 9.05, "lane": 2}, {"time": 9.40, "lane": 1}, {"time": 9.75, "lane": 0},
                {"time": 10.40, "lane": 0}, {"time": 10.65, "lane": 2}, {"time": 10.90, "lane": 3}, {"time": 11.15, "lane": 1},
                {"time": 11.80, "lane": 0}, {"time": 12.15, "lane": 1}, {"time": 12.50, "lane": 2}, {"time": 12.85, "lane": 3},
                {"time": 13.60, "lane": 1}, {"time": 13.85, "lane": 2}, {"time": 14.10, "lane": 1}, {"time": 14.35, "lane": 3},
                {"time": 15.00, "lane": 0}, {"time": 15.35, "lane": 1}, {"time": 15.70, "lane": 2}, {"time": 16.05, "lane": 3},
            ],
        },
        "tamy_afterdark": {
            "id": "tamy_afterdark",
            "title": "Afterdark",
            "artist": "Tamy Route",
            "character": "Tamy",
            "audio": "audio/blezz1.mp3",
            "background": "bg afterdark",
            "difficulty": "2/5",
            "length": 16.8,
            "description": "Tamy's first chart. Longer pauses, cleaner timing.",
            "unlock_text": "Meet Tamy after clearing Nuria's first chart.",
            "notes": [
                {"time": 1.20, "lane": 1}, {"time": 1.80, "lane": 2}, {"time": 2.40, "lane": 1}, {"time": 3.00, "lane": 0},
                {"time": 3.60, "lane": 2}, {"time": 4.20, "lane": 3}, {"time": 4.80, "lane": 2}, {"time": 5.40, "lane": 1},
                {"time": 6.10, "lane": 0}, {"time": 6.70, "lane": 1}, {"time": 7.30, "lane": 2}, {"time": 7.90, "lane": 3},
                {"time": 8.60, "lane": 3}, {"time": 9.20, "lane": 2}, {"time": 9.80, "lane": 1}, {"time": 10.40, "lane": 0},
                {"time": 11.10, "lane": 1}, {"time": 11.70, "lane": 2}, {"time": 12.30, "lane": 1}, {"time": 12.90, "lane": 3},
                {"time": 13.60, "lane": 0}, {"time": 14.20, "lane": 1}, {"time": 14.80, "lane": 2}, {"time": 15.40, "lane": 3},
            ],
        },
        "tamy_homemage": {
            "id": "tamy_homemage",
            "title": "Homemage",
            "artist": "Tamy Route",
            "character": "Tamy",
            "audio": "audio/blezz2.mp3",
            "background": "bg homemage",
            "difficulty": "3/5",
            "length": 18.0,
            "description": "Tamy's second chart. Repeating patterns and a steadier climb.",
            "unlock_text": "Clear Afterdark.",
            "notes": [
                {"time": 1.00, "lane": 0}, {"time": 1.35, "lane": 1}, {"time": 1.70, "lane": 2}, {"time": 2.05, "lane": 3},
                {"time": 2.60, "lane": 1}, {"time": 2.95, "lane": 2}, {"time": 3.30, "lane": 1}, {"time": 3.65, "lane": 0},
                {"time": 4.20, "lane": 2}, {"time": 4.55, "lane": 3}, {"time": 4.90, "lane": 2}, {"time": 5.25, "lane": 1},
                {"time": 5.80, "lane": 0}, {"time": 6.15, "lane": 2}, {"time": 6.50, "lane": 3}, {"time": 6.85, "lane": 1},
                {"time": 7.40, "lane": 1}, {"time": 7.75, "lane": 0}, {"time": 8.10, "lane": 1}, {"time": 8.45, "lane": 2},
                {"time": 9.00, "lane": 3}, {"time": 9.35, "lane": 2}, {"time": 9.70, "lane": 1}, {"time": 10.05, "lane": 0},
                {"time": 10.60, "lane": 0}, {"time": 10.95, "lane": 1}, {"time": 11.30, "lane": 2}, {"time": 11.65, "lane": 3},
                {"time": 12.20, "lane": 2}, {"time": 12.55, "lane": 1}, {"time": 12.90, "lane": 2}, {"time": 13.25, "lane": 3},
                {"time": 13.80, "lane": 1}, {"time": 14.15, "lane": 0}, {"time": 14.50, "lane": 1}, {"time": 14.85, "lane": 2},
                {"time": 15.40, "lane": 3}, {"time": 15.75, "lane": 2}, {"time": 16.10, "lane": 1}, {"time": 16.45, "lane": 0},
            ],
        },
    }

    def sync_music_progress():
        for song_id in RHYTHM_SONGS:
            if song_id not in store.track_unlocks:
                store.track_unlocks[song_id] = False
            if song_id not in store.track_results:
                store.track_results[song_id] = {
                    "grade": "-",
                    "score": 0,
                    "accuracy": 0.0,
                    "accuracy_text": "--",
                    "cleared": False,
                }

    def unlock_track(song_id):
        sync_music_progress()
        store.track_unlocks[song_id] = True

    def ordered_song_ids():
        sync_music_progress()
        return [song_id for song_id in RHYTHM_SONGS if store.track_unlocks.get(song_id, False)]

    def locked_song_ids():
        sync_music_progress()
        return [song_id for song_id in RHYTHM_SONGS if not store.track_unlocks.get(song_id, False)]

    def selected_song():
        sync_music_progress()
        return RHYTHM_SONGS[store.music_room_selected]

    def open_music_room():
        sync_music_progress()
        if store.track_unlocks.get(store.music_room_selected, False):
            preview_music_song(store.music_room_selected)
        else:
            stop_preview_music()

    def preview_music_song(song_id=None):
        sync_music_progress()
        if song_id is not None:
            store.music_room_selected = song_id
        if not store.track_unlocks.get(store.music_room_selected, False):
            renpy.notify("Track locked.")
            return
        renpy.music.stop(channel="rhythm")
        renpy.music.play(RHYTHM_SONGS[store.music_room_selected]["audio"], channel="preview", fadein=0.2)

    def stop_preview_music():
        renpy.music.stop(channel="preview", fadeout=0.2)

    def format_time(value):
        value = max(0, int(value))
        return "{:01d}:{:02d}".format(value // 60, value % 60)

    def music_position_text():
        pos = renpy.music.get_pos(channel="preview") or 0.0
        return format_time(pos)

    def best_grade(song_id):
        sync_music_progress()
        return store.track_results.get(song_id, {}).get("grade", "-")

    def unlock_text(song_id):
        if store.track_unlocks.get(song_id, False):
            return "Status: unlocked"
        return "Status: locked - " + RHYTHM_SONGS[song_id]["unlock_text"]

    def unlocked_track_count():
        sync_music_progress()
        return len([song_id for song_id, unlocked in store.track_unlocks.items() if unlocked])

    def route_label(name):
        if name == "nuria":
            stage = store.route_nuria_stage
            if stage == 0:
                return "Not met"
            if stage == 1:
                return "First chart pending"
            if stage == 2:
                return "Second chart pending"
            return "Route complete"

        stage = store.route_tamy_stage
        if stage == 0:
            return "Locked" if not store.tamy_unlocked else "Met"
        if stage == 1:
            return "First chart pending"
        if stage == 2:
            return "Second chart pending"
        return "Route complete"

    def store_last_result(song_id):
        sync_music_progress()
        result = rhythm_state.build_result()
        current = store.track_results.get(song_id, {})
        if result["score"] >= current.get("score", 0):
            store.track_results[song_id] = result

    def lane_key_text(lane):
        return ["D", "F", "J", "K"][lane]

    # ---------- color helpers ----------
    def judgment_color(j):
        if j == "PERFECT":
            return "#6dffa0"
        if j == "GOOD":
            return "#ffe66d"
        return "#ff5c5c"

    def lane_glow_color(lane):
        base = ["#e25f5f", "#e2a65f", "#4ca7d9", "#8c6fe8"]
        return base[lane] + "55"


    class RhythmGameState(object):
        lane_count = 4
        lane_width = 140
        lane_gap = 12
        lane_top = 84
        lane_height = 760
        hit_line_y = 760
        note_height = 28
        note_speed = 420.0
        pre_spawn = 1.60
        # Ren'Py input/audio timing is not strict enough for arcade-tight windows.
        # Keep this forgiving so visual alignment matters more than frame-perfect input.
        perfect_window = 0.14
        good_window = 0.25
        miss_window = 0.38
        input_offset = 0.04
        lane_colors = ["#e25f5f", "#e2a65f", "#4ca7d9", "#8c6fe8"]

        def __init__(self):
            self.song_id = None
            self.song = None
            self.notes = []
            self.last_judgment = ""
            self.judgment_time = 0.0
            self.score = 0
            self.combo = 0
            self.max_combo = 0
            self.perfect = 0
            self.good = 0
            self.miss = 0
            self.finished = False
            self.running = False
            self.lane_flash_times = [0.0, 0.0, 0.0, 0.0]

        def start(self, song_id):
            stop_preview_music()
            self.song_id = song_id
            self.song = RHYTHM_SONGS[song_id]
            self.notes = []
            for note in self.song["notes"]:
                note_data = copy.deepcopy(note)
                note_data["judged"] = False
                self.notes.append(note_data)
            self.last_judgment = ""
            self.judgment_time = 0.0
            self.score = 0
            self.combo = 0
            self.max_combo = 0
            self.perfect = 0
            self.good = 0
            self.miss = 0
            self.finished = False
            self.running = True
            self.lane_flash_times = [0.0, 0.0, 0.0, 0.0]
            renpy.music.stop(channel="preview")
            renpy.music.play(self.song["audio"], channel="rhythm", fadein=0.1)

        def current_time(self):
            if not self.running:
                return 0.0
            return max(0.0, renpy.music.get_pos(channel="rhythm") or 0.0)

        def lane_x(self, lane):
            total_width = (self.lane_width * self.lane_count) + (self.lane_gap * (self.lane_count - 1))
            left = (1920 - total_width) // 2
            return left + lane * (self.lane_width + self.lane_gap)

        def judge_note(self, note, delta):
            note["judged"] = True
            delta = abs(delta)
            if delta <= self.perfect_window:
                self.perfect += 1
                self.combo += 1
                self.max_combo = max(self.max_combo, self.combo)
                self.score += 1000 + (self.combo * 5)
                self.last_judgment = "PERFECT"
                self.judgment_time = _pytime.time()
                return

            if delta <= self.good_window:
                self.good += 1
                self.combo += 1
                self.max_combo = max(self.max_combo, self.combo)
                self.score += 600 + (self.combo * 3)
                self.last_judgment = "GOOD"
                self.judgment_time = _pytime.time()
                return

            self.register_miss(note)

        def register_miss(self, note=None):
            if note is not None:
                note["judged"] = True
            self.miss += 1
            self.combo = 0
            self.last_judgment = "MISS"
            self.judgment_time = _pytime.time()

        def tick(self):
            if not self.running or self.finished:
                return

            now = self.current_time() + self.input_offset
            for note in self.notes:
                if note["judged"]:
                    continue
                if now - note["time"] > self.miss_window:
                    self.register_miss(note)
                    continue
                break

            if now >= self.song["length"] and all(note["judged"] for note in self.notes):
                self.finish()

        def hit_lane(self, lane):
            if not self.running or self.finished:
                return

            self.lane_flash_times[lane] = _pytime.time()

            now = self.current_time() + self.input_offset
            candidates = []

            for note in self.notes:
                if note["judged"] or note["lane"] != lane:
                    continue
                delta = note["time"] - now
                if abs(delta) <= self.miss_window:
                    candidates.append((abs(delta), delta, note))
                    continue
                if delta > self.miss_window:
                    break

            if candidates:
                _, delta, note = min(candidates, key=lambda item: item[0])
                self.judge_note(note, delta)
                return

            self.register_miss()

        def flash_active(self, lane):
            return (_pytime.time() - self.lane_flash_times[lane]) < 0.12

        def judgment_visible(self):
            return (_pytime.time() - self.judgment_time) < 0.55

        def progress(self):
            if not self.song:
                return 0.0
            now = self.current_time()
            return min(1.0, max(0.0, now / self.song["length"]))

        def visible_notes(self):
            now = self.current_time()
            visible = []
            for note in self.notes:
                if note["judged"]:
                    continue
                delta = note["time"] - now
                if delta < -self.miss_window or delta > self.pre_spawn:
                    continue
                y = self.hit_line_y - (delta * self.note_speed)
                closeness = max(0.0, 1.0 - abs(delta) / self.pre_spawn)
                visible.append({
                    "lane": note["lane"],
                    "x": self.lane_x(note["lane"]),
                    "y": y,
                    "color": self.lane_colors[note["lane"]],
                    "closeness": closeness,
                })
            return visible

        def accuracy(self):
            total = self.perfect + self.good + self.miss
            if not total:
                return 0.0
            weighted_hits = (self.perfect * 1.0) + (self.good * 0.7)
            return weighted_hits / total

        def grade(self):
            acc = self.accuracy()
            if acc >= 0.95 and self.miss <= 1:
                return "S"
            if acc >= 0.88:
                return "A"
            if acc >= 0.78:
                return "B"
            if acc >= 0.68:
                return "C"
            return "D"

        def cleared(self):
            return self.grade() in ("S", "A", "B", "C")

        def finish(self):
            self.finished = True
            self.running = False
            renpy.music.stop(channel="rhythm", fadeout=0.2)

        def build_result(self):
            accuracy = self.accuracy()
            return {
                "song_id": self.song_id,
                "score": self.score,
                "grade": self.grade(),
                "accuracy": accuracy,
                "accuracy_text": "{:.0%}".format(accuracy),
                "cleared": self.cleared(),
                "max_combo": self.max_combo,
            }


default rhythm_state = RhythmGameState()


# ──────────────────────────────────────
#  ATL transforms
# ──────────────────────────────────────

transform hit_line_pulse:
    alpha 0.7
    ease 0.45 alpha 1.0
    ease 0.45 alpha 0.7
    repeat

transform hud_slide_left:
    xoffset -360
    alpha 0.0
    easein 0.5 xoffset 0 alpha 1.0

transform hud_slide_right:
    xoffset 360
    alpha 0.0
    easein 0.5 xoffset 0 alpha 1.0

transform judgment_pop:
    anchor (0.5, 0.5)
    zoom 1.6
    alpha 1.0
    yoffset 0
    easein 0.12 zoom 1.0
    pause 0.15
    ease 0.35 alpha 0.0 yoffset -50

transform combo_wobble:
    subpixel True
    xoffset 0
    ease 0.18 xoffset 4
    ease 0.18 xoffset -4
    ease 0.18 xoffset 2
    ease 0.18 xoffset 0
    repeat

transform lane_btn_idle:
    zoom 1.0
    alpha 0.85

transform lane_btn_hover:
    zoom 1.03
    alpha 1.0

transform progress_grow(w):
    xsize 0
    linear 0.15 xsize w


# ──────────────────────────────────────
#  Rhythm game screen
# ──────────────────────────────────────

screen rhythm_game(g=rhythm_state):
    modal True
    timer 0.016 repeat True action [Function(g.tick), If(g.finished, true=Return(g.build_result()), false=NullAction())]

    # --- background ---
    add Transform(g.song["background"], fit="contain", xysize=(1920, 1080), xalign=0.5, yalign=0.5)

    frame:
        background "#05060fcc"
        xfill True
        yfill True

    # --- progress bar at top ---
    $ prog_px = int(1920 * g.progress())
    frame:
        xpos 0
        ypos 0
        xsize 1920
        ysize 5
        background "#2a1028"
    frame:
        xpos 0
        ypos 0
        xsize max(1, prog_px)
        ysize 5
        background "#EC8FD0"

    # --- lane columns ---
    for lane in range(g.lane_count):
        # main column body
        frame:
            xpos g.lane_x(lane)
            ypos g.lane_top
            xsize g.lane_width
            ysize g.lane_height
            background "#1a0a1abb"

        # lane flash overlay (on key press)
        if g.flash_active(lane):
            frame:
                xpos g.lane_x(lane)
                ypos g.lane_top
                xsize g.lane_width
                ysize g.lane_height
                background lane_glow_color(lane)

        # hit line (pulsing)
        frame:
            xpos g.lane_x(lane)
            ypos g.hit_line_y
            xsize g.lane_width
            ysize 6
            at hit_line_pulse
            background g.lane_colors[lane]

        # thin lane border lines
        frame:
            xpos g.lane_x(lane)
            ypos g.lane_top
            xsize 2
            ysize g.lane_height
            background g.lane_colors[lane] + "33"
        frame:
            xpos g.lane_x(lane) + g.lane_width - 2
            ypos g.lane_top
            xsize 2
            ysize g.lane_height
            background g.lane_colors[lane] + "33"

    # --- falling notes ---
    for note in g.visible_notes():
        # glow halo behind note (grows as note approaches hit line)
        $ glow_extra = int(12 * note["closeness"])
        $ glow_alpha = "44" if note["closeness"] > 0.6 else "22"
        frame:
            xpos note["x"] - glow_extra // 2
            ypos int(note["y"]) - glow_extra // 2
            xsize g.lane_width + glow_extra
            ysize g.note_height + glow_extra
            background note["color"] + glow_alpha

        # main note body (rounded-ish via inner highlight)
        frame:
            xpos note["x"]
            ypos int(note["y"])
            xsize g.lane_width
            ysize g.note_height
            background note["color"]

        # slight inner shine on top half
        frame:
            xpos note["x"] + 4
            ypos int(note["y"]) + 2
            xsize g.lane_width - 8
            ysize g.note_height // 2 - 2
            background "#ffffff18"

    # --- judgment popup (floating center) ---
    if g.judgment_visible() and g.last_judgment:
        text g.last_judgment:
            at judgment_pop
            xalign 0.5
            ypos 420
            size 64
            bold True
            color judgment_color(g.last_judgment)
            outlines [(3, "#000000cc", 0, 0)]

    # --- HUD left panel ---
    frame:
        at hud_slide_left
        background "#2a1028e8"
        xpos 40
        ypos 40
        xsize 380
        ysize 240
        padding (24, 20)

        vbox:
            spacing 8
            text "[g.song['title']]" size 32 bold True color "#ffffff"
            text "[g.song['character']]  |  [g.song['difficulty']]" size 18 color "#d4a0c8"
            null height 4

            hbox:
                spacing 20
                vbox:
                    spacing 4
                    text "Score" size 16 color "#d4a0c8"
                    text "[g.score]" size 28 bold True color "#EC8FD0"
                vbox:
                    spacing 4
                    text "Accuracy" size 16 color "#d4a0c8"
                    text "[g.build_result()['accuracy_text']]" size 28 bold True color "#EC8FD0"

    # --- HUD right panel ---
    frame:
        at hud_slide_right
        background "#2a1028e8"
        xpos 1490
        ypos 40
        xsize 390
        ysize 240
        padding (24, 20)

        vbox:
            spacing 6

            hbox:
                spacing 18
                vbox:
                    spacing 2
                    text "Combo" size 16 color "#d4a0c8"
                    if g.combo >= 10:
                        text "[g.combo]" at combo_wobble size 36 bold True color "#ffe66d"
                    else:
                        text "[g.combo]" size 36 bold True color "#f5f7fb"
                vbox:
                    spacing 2
                    text "Max" size 16 color "#d4a0c8"
                    text "[g.max_combo]" size 36 bold True color "#f5f7fb"

            null height 4

            hbox:
                spacing 16
                text "P [g.perfect]" size 18 color "#6dffa0"
                text "G [g.good]" size 18 color "#ffe66d"
                text "M [g.miss]" size 18 color "#ff5c5c"

            null height 6

            hbox:
                spacing 8
                text "Keys: D  F  J  K" size 16 color "#9a8094"
                textbutton "Quit" text_size 16 text_color "#EC8FD0" text_hover_color "#FFC0CB":
                    action [Function(g.finish), Return(g.build_result())]

    # --- lane hit buttons ---
    for lane in range(g.lane_count):
        button:
            xpos g.lane_x(lane)
            ypos 855
            xsize g.lane_width
            ysize 85
            background "#2a1028"
            hover_background g.lane_colors[lane]
            action Function(g.hit_lane, lane)

            text lane_key_text(lane):
                align (0.5, 0.5)
                size 28
                bold True
                color "#f5f7fb"

    # --- keyboard bindings ---
    key "d" action Function(g.hit_lane, 0)
    key "f" action Function(g.hit_lane, 1)
    key "j" action Function(g.hit_lane, 2)
    key "k" action Function(g.hit_lane, 3)


label play_rhythm_song(song_id):
    $ sync_music_progress()
    $ rhythm_state.start(song_id)
    call screen rhythm_game()
    return _return
