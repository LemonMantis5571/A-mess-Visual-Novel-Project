init python:
    import random
    import time
    from palabras import palabras
    random.seed(time.clock())

    def get_a_word():
        #f = open(renpy.loader.transfn("resources/sgb-words.txt"),"r")
        #words = f.readlines(  )
        words = palabras
        selected = random.randint(0, len(words)-1)
        return words[selected].strip()
    class lingo_game:
        def __init__(self):
            self.word_string = ""
            self.word = []
            self.input = []
            self.y = 0
            self.x = 0
            self.won = False
        def set_word(self, word = None):
            if not word:
                word = get_a_word()
            self.word_string = word
            self.word = []
            for i in word:
                self.word.append(i.upper())
            self.input = [
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
            ]
            self.y = 0
            self.x = 0
            self.won = False

        def send(self, letter):
            if self.x < 5 and self.y < 5:
                self.input[self.y][self.x] = letter
                self.move(1)
        def move(self, value):
            if self.x < 6 and self.y < 5:
                self.x += value
                if self.x < 0:
                    self.x = 0
                elif self.x > 5:
                    self.x = 5
        def back(self):
            if self.y < 5 and not self.won:
                self.move(-1)
                self.input[self.y][self.x] = None
        def enter(self):
            if self.y < 5 and not self.won:
                if self.word == self.input[self.y]:
                    self.won = True
                else:
                    self.y += 1
                    self.x = 0
default alphabet = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
    ]

default lingo_game_handler = lingo_game()
screen lingo(word = None, g = lingo_game_handler, resetting = False):
    modal True
    timer .01 action Function(g.set_word, word)
    fixed fit_first True align .5,.5:
        at fade(.2)
        vbox spacing 10:
            for m,y in enumerate(g.input):
                hbox spacing 10:
                    for n,x in enumerate(y):
                        frame:
                            xysize 70,70
                            if m < g.y:
                                if x == g.word[n]:
                                    background "#0f0d"
                                elif x in g.word:
                                    background "#fc0d"
                                else:
                                    background "#666d"
                            else:
                                if g.won and m == g.y:
                                    background "#0f0d"
                                else:
                                    background "#fff9"

                            if x:
                                text x align .5,.5 color "#000"
                            if g.y == m:
                                if g.x == n:
                                    frame:
                                        background "#fff9"
    
    default osk = 210
    fixed fit_first True align .5,1.0:
        at osk_offset(osk)
        frame xsize 660 background None padding 0,0:
            hbox align .5,.5 spacing 10:
                hbox spacing 10 box_wrap True box_wrap_spacing 10:
                    for i in alphabet:
                        button xysize 60,60 background "#fff9":
                            text i align .5,.5 color "#000"
                            action Function(g.send, i) keysym [i.lower(), i]

                vbox spacing 10:
                    button xysize 130,60 background "#fff9":
                        text "⌦" align .5,.5 color "#000" at flip
                        action Function(g.back) keysym "K_BACKSPACE"
                    button xysize 130,60 background "#fff9":
                        text "⏎" align .5,.5 color "#000"
                        action Function(g.enter) keysym "K_RETURN"

        hbox align 1.0,.0 offset 49,-70 spacing 10:
            if resetting:
                button xysize 60,60 background "#fff9":
                    text "⟲" align .5,.5 color "#000"
                    action Function(g.set_word)
            button xysize 60,60 background "#fff9":
                text "⌨" align .5,.5 color "#000"
                action ToggleScreenVariable("osk", -40, 210)
    key "K_LEFT" action Function(g.move, -1)
    key "K_RIGHT" action Function(g.move, 1)
    key "K_BACKSPACE" action Function(g.back)
    key "K_RETURN" action Function(g.enter)

    if g.won:
        frame padding 40,40 background "#fff9" align .5,.92:
            vbox spacing 20:
                text "Great job, let's move on." color "#000"
                hbox spacing 10 align .5,.5:
                    if resetting:
                        button background "#fff9" padding 40,40:
                            text "Retry" color "#000"
                            action Function(g.set_word)
                    button background "#fff9" padding 40,40:
                        text "Next" color "#000"
                        action Return(["won", g.word_string, g.y+1])
    elif g.y > 4:
        frame padding 40,40 background "#fff9" align .5,.92:
            vbox spacing 20:
                text "Huh, not that easy it seems." color "#000"
                hbox spacing 10 align .5,.5:
                    if resetting:
                        button background "#fff9" padding 40,40:
                            text "Retry" color "#000"
                            action Function(g.set_word)
                    button background "#fff9" padding 40,40:
                        text "Next" color "#000"
                        action Return(["lost", g.word_string])


transform osk_offset(y):
    ease .4 yoffset y
transform flip():
    xzoom -1
transform fade(t):
    alpha 0
    linear t alpha 1

label lingo_example:
    "Lets start with a word we choose. This time \"lingo\""
    call screen lingo("lingo")
    "Easy when you know the answer right?"
    "Let's try with a random word from a list of 80."
    call screen lingo
    $ word = _return[1]
    if _return[0] == "won":
        $ tries = _return[2]
        if tries < 4:
            "Impressive! guessed \"[word]\" in [tries] attempts."
        else:
            "Guessed \"[word]\" in [tries] attempts. Not bad."
    else:
        "Couldn't guess it? it was: \"[word]\"."
    "At least you tried."
    "the word was \"[word]\""
    $ Wordle_Finish = True
    jump tamy_options
    #call screen lingo(resetting = True)
    #$ word = _return[1]