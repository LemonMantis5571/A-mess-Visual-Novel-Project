init python:
    import copy
    import time as _pytime
    store = renpy.store

    renpy.music.register_channel("preview", mixer="music_room_mixer", loop=False)
    renpy.music.register_channel("rhythm", mixer="music", loop=False)

    def build_long_chart(base_notes, section_starts, lane_shifts, time_scales, accent_every=None, accent_start_section=99):
        chart = []
        base_start = base_notes[0]["time"]

        for section_index, section_start in enumerate(section_starts):
            lane_shift = lane_shifts[section_index % len(lane_shifts)]
            time_scale = time_scales[section_index % len(time_scales)]

            for note_index, note in enumerate(base_notes):
                lane = (note["lane"] + lane_shift) % 4
                note_time = section_start + ((note["time"] - base_start) * time_scale)
                chart.append({
                    "time": round(note_time, 2),
                    "lane": lane,
                })

                if accent_every and section_index >= accent_start_section and note_index % accent_every == (accent_every - 1):
                    chart.append({
                        "time": round(note_time + (0.12 * time_scale), 2),
                        "lane": (lane + 1 + (section_index % 2)) % 4,
                    })

        chart.sort(key=lambda item: item["time"])
        return chart

    NURIA_ANIMAL_BASE_NOTES = [
        {"time": 1.00, "lane": 0}, {"time": 1.40, "lane": 1}, {"time": 1.80, "lane": 2}, {"time": 2.20, "lane": 3},
        {"time": 2.80, "lane": 0}, {"time": 3.00, "lane": 1}, {"time": 3.20, "lane": 2}, {"time": 3.40, "lane": 3},
        {"time": 4.10, "lane": 1}, {"time": 4.55, "lane": 0}, {"time": 5.00, "lane": 2}, {"time": 5.45, "lane": 3},
        {"time": 6.10, "lane": 0}, {"time": 6.50, "lane": 2}, {"time": 6.90, "lane": 1}, {"time": 7.30, "lane": 3},
        {"time": 8.10, "lane": 0}, {"time": 8.55, "lane": 1}, {"time": 9.00, "lane": 2}, {"time": 9.45, "lane": 3},
        {"time": 10.10, "lane": 3}, {"time": 10.50, "lane": 2}, {"time": 10.90, "lane": 1}, {"time": 11.30, "lane": 0},
        {"time": 12.10, "lane": 0}, {"time": 12.30, "lane": 2}, {"time": 12.50, "lane": 1}, {"time": 12.70, "lane": 3},
        {"time": 13.50, "lane": 1}, {"time": 14.00, "lane": 0}, {"time": 14.50, "lane": 2}, {"time": 15.00, "lane": 3},
    ]

    NURIA_BLACKOUT_BASE_NOTES = [
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
    ]

    RHYTHM_SONGS = {
        "nuria_animal": {
            "id": "nuria_animal",
            "title": "Animal in Me",
            "artist": "Nuria Route",
            "character": "Nuria",
            "audio": "audio/metal1.mp3",
            "background": "bg_nuria_frutiger",
            "difficulty": "4/5",
            "length": 105.0,
            "description": "Nuria's first full chart. Sharp hits, longer stamina, much tighter timing.",
            "unlock_text": "Unlocked from the start.",
            "perfect_window": 0.15,
            "good_window": 0.25,
            "miss_window": 0.35,
            "notes": build_long_chart(
                NURIA_ANIMAL_BASE_NOTES,
                [1.0, 14.6, 28.0, 41.0, 53.8, 66.4, 78.8, 91.0],
                [0, 1, 0, 2, 1, 3, 2, 0],
                [1.00, 0.98, 0.96, 0.94, 0.92, 0.90, 0.88, 0.86],
                accent_every=8,
                accent_start_section=3,
            ),
        },
        "nuria_blackout": {
            "id": "nuria_blackout",
            "title": "Blackout",
            "artist": "Nuria Route",
            "character": "Nuria",
            "audio": "audio/metal3.mp3",
            "background": "bg_nuria_frutiger",
            "difficulty": "5/5",
            "length": 99.0,
            "description": "Nuria's second full chart. Dense phrases, longer pressure, and unforgiving windows.",
            "unlock_text": "Clear Animal in Me.",
            "perfect_window": 0.12,
            "good_window": 0.20,
            "miss_window": 0.30,
            "notes": build_long_chart(
                NURIA_BLACKOUT_BASE_NOTES,
                [1.0, 13.8, 26.2, 38.2, 50.0, 61.6, 73.0, 84.4],
                [0, 1, 2, 1, 3, 2, 0, 3],
                [0.98, 0.96, 0.94, 0.92, 0.90, 0.88, 0.86, 0.84],
                accent_every=6,
                accent_start_section=2,
            ),
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

    def grade_color(grade):
        palette = {
            "S": "#ffe66d",
            "A": "#6dffa0",
            "B": "#8cc8ff",
            "C": "#f3c87c",
            "D": "#ff7a7a",
            "-": "#f5f7fb",
        }
        return palette.get(grade, "#f5f7fb")

    def timing_color(offset):
        if offset is None:
            return "#f5f7fb"
        delta = abs(offset)
        if delta <= 0.05:
            return "#6dffa0"
        if delta <= 0.12:
            return "#ffe66d"
        return "#ff7a7a"


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
        perfect_window = 0.20
        good_window = 0.35
        miss_window = 0.50
        input_offset = 0.04
        lane_colors = ["#e25f5f", "#e2a65f", "#4ca7d9", "#8c6fe8"]

        def __init__(self):
            self.song_id = None
            self.song = None
            self.notes = []
            self.total_notes = 0
            self.judged_notes = 0
            self.last_judgment = ""
            self.last_offset = None
            self.last_lane = None
            self.judgment_time = 0.0
            self.combo_pop_time = 0.0
            self.score = 0
            self.combo = 0
            self.max_combo = 0
            self.perfect = 0
            self.good = 0
            self.miss = 0
            self.finished = False
            self.running = False
            self.result_snapshot = None
            self.lane_flash_times = [0.0, 0.0, 0.0, 0.0]
            self.sparks = []

        def start(self, song_id):
            stop_preview_music()
            self.song_id = song_id
            self.song = RHYTHM_SONGS[song_id]
            self.perfect_window = self.song.get("perfect_window", type(self).perfect_window)
            self.good_window = self.song.get("good_window", type(self).good_window)
            self.miss_window = self.song.get("miss_window", type(self).miss_window)
            self.notes = []
            self.total_notes = len(self.song["notes"])
            self.judged_notes = 0
            for note in self.song["notes"]:
                note_data = copy.deepcopy(note)
                note_data["judged"] = False
                self.notes.append(note_data)
            self.last_judgment = ""
            self.last_offset = None
            self.last_lane = None
            self.judgment_time = 0.0
            self.combo_pop_time = 0.0
            self.score = 0
            self.combo = 0
            self.max_combo = 0
            self.perfect = 0
            self.good = 0
            self.miss = 0
            self.finished = False
            self.running = True
            self.result_snapshot = None
            self.lane_flash_times = [0.0, 0.0, 0.0, 0.0]
            self.sparks = []
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

        def mark_judged(self, note):
            if note is not None and not note["judged"]:
                note["judged"] = True
                self.judged_notes += 1

        def judge_note(self, note, delta):
            self.mark_judged(note)
            self.last_offset = delta
            self.last_lane = note["lane"]
            abs_delta = abs(delta)

            if abs_delta <= self.perfect_window:
                self.perfect += 1
                self.combo += 1
                self.max_combo = max(self.max_combo, self.combo)
                self.score += 1000 + (self.combo * 5)
                self.last_judgment = "PERFECT"
                self.judgment_time = _pytime.time()
                hit_y = self.hit_line_y - (delta * self.note_speed)
                self.sparks.append({"lane": note["lane"], "x": self.lane_x(note["lane"]) + self.lane_width // 2, "y": hit_y + self.note_height // 2, "time": self.judgment_time, "type": "PERFECT"})
                if self.combo >= 5:
                    self.combo_pop_time = self.judgment_time
                return

            if abs_delta <= self.good_window:
                self.good += 1
                self.combo += 1
                self.max_combo = max(self.max_combo, self.combo)
                self.score += 600 + (self.combo * 3)
                self.last_judgment = "GOOD"
                self.judgment_time = _pytime.time()
                hit_y = self.hit_line_y - (delta * self.note_speed)
                self.sparks.append({"lane": note["lane"], "x": self.lane_x(note["lane"]) + self.lane_width // 2, "y": hit_y + self.note_height // 2, "time": self.judgment_time, "type": "GOOD"})
                if self.combo >= 5:
                    self.combo_pop_time = self.judgment_time
                return

            self.register_miss(note, lane=note["lane"])

        def register_miss(self, note=None, lane=None):
            self.mark_judged(note)
            self.miss += 1
            self.combo = 0
            self.last_judgment = "MISS"
            self.last_offset = None
            self.last_lane = lane
            self.judgment_time = _pytime.time()

        def tick(self):
            if not self.running or self.finished:
                return

            now = self.current_time() + self.input_offset
            for note in self.notes:
                if note["judged"]:
                    continue
                if now - note["time"] > self.miss_window:
                    self.register_miss(note, lane=note["lane"])
                    continue
                break

            if now >= self.song["length"] and self.judged_notes >= self.total_notes:
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

            self.register_miss(lane=lane)

        def flash_active(self, lane):
            return (_pytime.time() - self.lane_flash_times[lane]) < 0.12

        def judgment_visible(self):
            return (_pytime.time() - self.judgment_time) < 0.55

        def combo_visible(self):
            return self.combo >= 5 and (_pytime.time() - self.combo_pop_time) < 0.45

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

        def active_sparks(self):
            now = _pytime.time()
            self.sparks = [s for s in self.sparks if now - s["time"] < 0.25]
            return self.sparks

        def accuracy(self):
            total = self.perfect + self.good + self.miss
            if not total:
                return 0.0
            weighted_hits = (self.perfect * 1.0) + (self.good * 0.7)
            return weighted_hits / total

        def accuracy_text(self):
            return "{:.0%}".format(self.accuracy())

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
            self.result_snapshot = self.build_result()
            renpy.music.stop(channel="rhythm", fadeout=0.2)

        def timing_text(self):
            if self.last_judgment == "MISS":
                return "Missed window"
            if self.last_offset is None:
                return "On beat"
            ms = int(round(abs(self.last_offset) * 1000))
            if ms == 0:
                return "On beat"
            if self.last_offset > 0:
                return "{}ms early".format(ms)
            return "{}ms late".format(ms)

        def remaining_notes(self):
            return max(0, self.total_notes - self.judged_notes)

        def build_result(self):
            if self.result_snapshot is not None:
                return dict(self.result_snapshot)

            accuracy = self.accuracy()
            return {
                "song_id": self.song_id,
                "score": self.score,
                "grade": self.grade(),
                "accuracy": accuracy,
                "accuracy_text": self.accuracy_text(),
                "cleared": self.cleared(),
                "max_combo": self.max_combo,
                "perfect": self.perfect,
                "good": self.good,
                "miss": self.miss,
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

transform combo_burst:
    anchor (0.5, 0.5)
    zoom 1.35
    alpha 0.0
    on show:
        alpha 0.0
        easein 0.08 alpha 1.0 zoom 1.0
        pause 0.1
        ease 0.22 alpha 0.0 yoffset -24

transform spark_burst:
    anchor (0.5, 0.5)
    zoom 1.0
    alpha 0.85
    easeout 0.25 zoom 1.8 alpha 0.0

transform results_pop:
    alpha 0.0
    zoom 0.96
    easein 0.18 alpha 1.0 zoom 1.0

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

    frame:
        background "#120914dd"
        xalign 0.5
        ypos 18
        xsize 500
        ysize 78
        padding (24, 12)

        hbox:
            spacing 28
            xalign 0.5
            yalign 0.5

            vbox:
                spacing 2
                text "Grade" size 16 color "#d4a0c8" xalign 0.5
                text "[g.grade()]" size 28 bold True color grade_color(g.grade()) xalign 0.5

            vbox:
                spacing 2
                text "Time" size 16 color "#d4a0c8" xalign 0.5
                text "[format_time(g.current_time())] / [format_time(g.song['length'])]" size 24 color "#ffffff" xalign 0.5

            vbox:
                spacing 2
                text "Notes Left" size 16 color "#d4a0c8" xalign 0.5
                text "[g.remaining_notes()]" size 24 bold True color "#ffffff" xalign 0.5

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
            ysize 26
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

    # --- hit sparks (visual hit feedback) ---
    for spark in g.active_sparks():
        $ spark_color = g.lane_colors[spark["lane"]] if spark["type"] == "PERFECT" else "#ffffff"
        frame:
            xpos spark["x"]
            ypos int(spark["y"])
            xsize g.lane_width
            ysize g.note_height
            at spark_burst
            background spark_color

    # --- judgment popup (floating center) ---
    if g.judgment_visible() and g.last_judgment:
        vbox:
            xalign 0.5
            ypos 410
            spacing 4

            text g.last_judgment:
                at judgment_pop
                xalign 0.5
                size 64
                bold True
                color judgment_color(g.last_judgment)
                outlines [(3, "#000000cc", 0, 0)]

            text "[g.timing_text()]":
                xalign 0.5
                size 24
                bold True
                color timing_color(g.last_offset)
                outlines [(2, "#000000aa", 0, 0)]

    if g.combo_visible():
        text "[g.combo] combo":
            at combo_burst
            xalign 0.5
            ypos 510
            size 34
            bold True
            color "#ffffff"
            outlines [(2, "#000000aa", 0, 0)]

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
                    text "[g.accuracy_text()]" size 28 bold True color "#EC8FD0"

            null height 6
            text "[g.timing_text()]" size 18 color timing_color(g.last_offset)

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
                textbutton "Quit" text_size 16 text_color "#ffffff" text_hover_color "#ffffff":
                    action [Function(g.finish), Return(g.build_result())]

    # --- lane hit buttons ---
    for lane in range(g.lane_count):
        $ lane_button_bg = (g.lane_colors[lane] + "55") if g.flash_active(lane) else "#2a1028"
        button:
            xpos g.lane_x(lane)
            ypos 855
            xsize g.lane_width
            ysize 85
            background lane_button_bg
            hover_background g.lane_colors[lane]
            action Function(g.hit_lane, lane)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 2

                text lane_key_text(lane):
                    xalign 0.5
                    size 28
                    bold True
                    color "#f5f7fb"

                text "Lane [lane + 1]":
                    xalign 0.5
                    size 14
                    color "#ffffffcc"

    # --- keyboard bindings ---
    key "d" action Function(g.hit_lane, 0)
    key "f" action Function(g.hit_lane, 1)
    key "j" action Function(g.hit_lane, 2)
    key "k" action Function(g.hit_lane, 3)


screen rhythm_results(song, result):
    modal True
    tag menu

    add Transform(song["background"], fit="contain", xysize=(1920, 1080), xalign=0.5, yalign=0.5)

    frame:
        background "#04050ddd"
        xfill True
        yfill True

    frame:
        at results_pop
        background "#1a0a1af2"
        xalign 0.5
        yalign 0.5
        xsize 980
        ysize 620
        padding (38, 34)

        vbox:
            spacing 18

            hbox:
                spacing 28

                vbox:
                    spacing 4
                    xsize 620
                    text "[song['title']]" size 38 bold True color "#ffffff"
                    text "[song['character']]  |  [song['artist']]" size 22 color "#d4a0c8"
                    text ("Chart cleared." if result["cleared"] else "Keep practicing and try again.") size 20 color "#ffffff"

                frame:
                    background "#120914"
                    xsize 220
                    ysize 160
                    xalign 1.0
                    yalign 0.5

                    text "[result['grade']]":
                        xalign 0.5
                        yalign 0.5
                        size 92
                        bold True
                        color grade_color(result["grade"])

            hbox:
                spacing 20

                frame:
                    background "#2a1028"
                    xsize 430
                    ysize 220
                    padding (22, 18)

                    vbox:
                        spacing 10
                        text "Performance" size 26 bold True color "#ffffff"
                        text "Score  [result['score']]" size 22 color "#ffffff"
                        text "Accuracy  [result['accuracy_text']]" size 22 color "#ffffff"
                        text "Max combo  [result['max_combo']]" size 22 color "#ffffff"

                frame:
                    background "#2a1028"
                    xsize 430
                    ysize 220
                    padding (22, 18)

                    vbox:
                        spacing 10
                        text "Hit Breakdown" size 26 bold True color "#ffffff"
                        text "Perfect  [result['perfect']]" size 22 color "#6dffa0"
                        text "Good  [result['good']]" size 22 color "#ffe66d"
                        text "Miss  [result['miss']]" size 22 color "#ff7a7a"

            text "Retry to refine your score, or continue back to the story." size 20 color "#ffffff"

            hbox:
                spacing 18
                xalign 1.0

                textbutton "Retry":
                    text_size 24
                    text_color "#ffffff"
                    text_hover_color "#ffffff"
                    action Return("retry")

                textbutton "Continue":
                    text_size 24
                    text_color "#ffffff"
                    text_hover_color "#ffffff"
                    action Return("continue")


label play_rhythm_song(song_id):
    $ sync_music_progress()
    $ retry_song = True
    $ final_result = None

    while retry_song:
        $ rhythm_state.start(song_id)
        call screen rhythm_game()
        $ result = _return
        call screen rhythm_results(RHYTHM_SONGS[song_id], result)
        if _return != "retry":
            $ final_result = result
            $ retry_song = False

    return final_result
