
init python:
    class ins_post:
        def __init__(self, user, title, image, time):
            self.user = user
            self.title = title
            self.image = image
            self.time_stamp = time
            self.likes = []
            self.seen = []
            self.Comments_shown = False
            self.comments = []
        def toggle_comments(self):
            self.Comments_shown = not self.Comments_shown
    class ins_user:
        def __init__(self, name, image = "no_avatar"):
            self.name = name
            self.image = image
            self.posts = []
            self.following = []
        def post(self, title = "No title", image = "no_image", time = "1:00 tuesday june 14"):
            p = ins_post(self, title, image, time)
            self.posts.append(p)

    class ins_feed:
        def __init__(self):
            self.user = None
            self.other_users = []
            self.page = "Feed"
            self.feed = []

            self.posting_step = "Write a title."
            self.post_image = None
            self.post_title = "No title"
            self.comment = ""
        def get_feed(self):
            self.feed = []
            for j in self.user.following:
                for i in j.posts:
                    self.feed.append(i)
            renpy.random.shuffle(self.feed)
        def set_page(self, page):
            self.page = page
            Hide("insto")()
            Show("insto")()

        def send_comment(self, post):
            post.comments.append([self.user, self.comment])
            self.comment = ""
        def start_posting(self, step):
            self.posting_step = step
        def set_image(self, image):
            self.post_image = image
            self.posting_step = "Write a title."
        def set_title(self, title):
            self.post_title = title
        def send_post(self):
            if self.post_image:
                self.user.post(self.post_title, self.post_image)
            else:
                self.user.post(self.post_title)
            self.page = "Me"
            self.post_image = None
            self.post_title = "No title"
        def heart(self, post):
            if not self.user in post.likes:
                post.likes.append(self.user)
            else:
                post.likes.remove(self.user)
        def follow(self, user):
            if not user in self.user.following:
                self.user.following.append(user)
                try:
                    self.other_users.remove(user)
                except:
                    pass
            else:
                try:
                    self.user.following.remove(user)
                except:
                    pass
                if not user in self.other_users:
                    self.other_users.append(user)
        def follow_suggestions(self):
            s = []
            if len(self.other_users):
                for i in range(3):
                    u = renpy.random.choice(self.other_users)
                    if not u in self.user.following and not u in s:
                        s.append(u)
            return s

default all_images_for_aya = [
    "queen",
    "nuriainsto",
    "dyneside",
    "invisions",
]
default instopost = ins_feed()
screen insto(g = instopost, set = all_images_for_aya):
    on "show" action Function(g.get_feed)
    frame:
        xysize(600,900) padding(0,0) background "insto_bg" align .5,.5

        frame: # Top bar
            ysize 100 xfill True background "#111d" yalign 0.0
            button:
                align 0.0,.5 background "#222" xysize 40,40
                text "⬅" font "DejaVuSans.ttf" align .5,.5
                action Function(g.set_page, "Feed")

            button:
                align 0.2,.5 background "#222" xysize 40,40
                text "X" font "DejaVuSans.ttf" align .5,.5
                action Jump("Options")

            button align 1.0,.5:
                text _("My wall") size 22
                action Function(g.set_page, "Me")
            if g.page == "Feed":
                text "InstoPost" align .5,.5
            elif g.page in ["Me", "Me posting"]:
                text "Your wall" align .5,.5
            else:
                vbox align .5,.5 spacing 8:
                    text g.page.name size 20 align .5,.5
                    button background "#0009" padding 8,8:
                        align .5,.5
                        if g.page in g.user.following:
                            text _("Un-follow") size 20
                        else:
                            text _("Follow") size 20
                        action Function(g.follow, g.page)

        viewport:
            draggable True scrollbars None mousewheel True yinitial 0.0 align .5,0.0
            xfill False
            yfill False
            yalign 1.0
            ymaximum 770 yoffset 110
            vbox spacing 10:
                if g.page == "Feed":
                    timer .1 action 
                    for i in reversed(g.feed):
                        use insto_post_body(i, g)
                    frame xsize 556 background "#0009":
                        vbox align .5,.5:
                            text _("End of your feed") align .5,.5 size 22
                            $ suggestions = g.follow_suggestions()
                            if len(suggestions):
                                text _("Follow more people to get more. Here's few suggestions:") align .5,.5 size 22
                                for i in suggestions:
                                    button:
                                        hbox spacing 10:
                                            add i.image
                                            text i.name yalign .5
                                        action Function(g.set_page, i)
                elif g.page == "Me":
                    frame xsize 556 background "#0009" padding 20,20:
                        button xalign .5 background "#0009" padding 20,20:
                            text _("Post something") size 24
                            action Function(g.set_page, "Me posting")

                    for i in reversed(g.user.posts):
                        use insto_post_body(i, g)
                    frame xsize 556 background "#0009":
                        text _("You have started here.") align .5,.5 size 22
                elif g.page == "Me posting":
                    if g.posting_step == "Choose an image.":
                        frame xsize 556 background "#0009" padding 8,8:
                            vbox:
                                for i in set:
                                    button:
                                        text i
                                        action Function(g.set_image, i)
                    elif g.posting_step == "Write a title.":
                        if g.post_image:
                            $ img = g.post_image.lower()
                        else:
                            $ img = None
                        
                        frame xsize 556 background "#0009" padding 8,8 align .5,.5:
                            vbox align .5,.5 spacing 8:
                                if img:
                                    button:
                                        align .5,.5
                                        add img at zoom(image_fit(img, (400,600)))
                                        action Function(g.start_posting, "Choose an image.")
                                else:
                                    button xalign .5 background "#0009" padding 20,20:
                                        text _("Select or capture an image") size 24
                                        action Function(g.start_posting, "Choose an image.")
                                frame background "#0009" padding 8,8 xfill True:
                                    input:
                                        value FieldInputValue(g, "post_title")

                                button background "#0009" padding 8,8 align .5,.5:
                                    text _("Send")
                                    action Function(g.send_post)


                else:
                    for i in reversed(g.page.posts):
                        use insto_post_body(i, g)
                    frame xsize 556 background "#0009":
                        text _("No more posts available.") align .5,.5 size 22

style instopost_frame:
    background "#0009" xfill True

screen insto_post_body(p, g):
    style_prefix "instopost"
    $ img = p.image.lower()
    frame:
        xsize 556 background "#0009" padding 8,8
        vbox spacing 4:
            fixed fit_first True:
                vbox:
                    button:
                        hbox spacing 10:
                            add p.user.image
                            vbox yalign .5:
                                text p.user.name color "#6babff" size 24
                                text p.time_stamp color "#b0b3b8" size 20
                        action Function(g.set_page, p.user)
                    text p.title
                    add img at zoom(image_fit(img, (540,900)))
                button align .5,1.0:
                    text _("open") size 20
                    action Show("insto_image", i = img)
                button align 1.0,1.0:
                    fixed fit_first True:
                        if g.user in p.likes:
                            add "insto_heart"
                        else:
                            add "insto_heart_gray"
                        text str(len(p.likes)) size 16 align .5,.4
                    action Function(g.heart, p)
                button align .0,1.0:
                    hbox spacing 10:
                        text str(len(p.comments)) size 24
                        text _("Comments") size 24
                    action Function(p.toggle_comments)
            if p.Comments_shown:
                for i in p.comments:
                    frame:
                        vbox:
                            button:
                                action Function(g.set_page, p.user)
                                hbox spacing 10:
                                    add i[0].image
                                    text i[0].name color "#6babff" size 24 align .0,.5
                            text i[1] size 24
                frame:
                    vbox:
                        hbox spacing 10:
                            add g.user.image
                            text g.user.name color "#6babff" size 24 align .0,.5
                        frame padding 8,8:
                            input:
                                value FieldInputValue(g, "comment") size 24
                        button padding 8,8 align 1.0,.5:
                            text _("Send") size 24
                            action Function(g.send_comment, p)




screen insto_image(i):
    button:
        align .5,.5
        at insto_image_animation
        add i at zoom(image_fit(i, (600,900)))
        action Hide("insto_image")
transform insto_image_animation:
    zoom 0.01
    ease .2 zoom 1




transform zoom(z):
    zoom z

# We need some users
default aya_user = ins_user(
    name = "[character_name]",
    image = "aya_avatar"
)
default rin_user = ins_user(
    name = "@Aminoaciduria",
    image = "rin_avatar"
)
default mayo_user = ins_user(
    name = "@MayoNyan",
    image = "mayo_avatar"
)
default chepito = ins_user(
    name = "@Chepito",
    image = "chepito_avatar"
)
default guy_101 = ins_user(
    name = "@Daniel Ortega"
)
default the_real_president = ins_user(
    name = "@Herradora"
)

default pita = ins_user(
    name = "@pita"
)

label insto_example:
    
    # Specify the default user
    $ instopost.user = aya_user
    # she follows few friends
    $ instopost.follow(rin_user)
    $ instopost.follow(chepito)
    $ instopost.follow(mayo_user)
    # add some other users to our app
    $ instopost.other_users = [guy_101, the_real_president,pita]

    # Adding some post to people's timeline
    #$ mayo_user.post(_("Koi and tea..."),"piqselscom-id-oigzk")
    #$ mayo_user.post(_("Snow?"),"cat-5932474__480")
    #$ mayo_user.post(_("I want a big kitty"),"lion-3012515__340")

    $ rin_user.post(_("Bought a new guitar"),"nuriainsto")
    $ rin_user.post(_("Recently met dyneside!"),"dyneside")
    $ rin_user.post(_("This album is gonna be nuts"),"invisions")
    $ rin_user.post(_("One day I'll met them"),"queen")

    $ chepito.post(_("Here with my friends having a fun time"),"tapineo")

    #$ guy_101.post(_("Am I handsome."),"meme-4656855__480")
    #$ guy_101.post(_("Give me your number girl"),"suit-673697__480")
    #$ guy_101.post(_("This can be you"),"woman-438399__480")

    #$ the_real_president.post(_("Follow me and I'll give you a car."))
    #$ pita.post(_("Donate today and this puppy gets to live."), "cavalier-king-charles-spaniel-5952324__480")
    #$ pita.post(_("Donate to find this puppy a home."), "dog-1037702__480")
    # there are a number of ways to add comments to a specific post, here's one
    #$ pita.posts[-1].comments.append([mayo_user, _("Can I adopt a puppy?")])
    #$ pita.posts[-1].comments.append([pita, _("Unfortunately we don't offer that service. But you can donate and we will find them a home.")])
    #$ pita.posts[-1].comments.append([mayo_user, _("Why?")])

    #$ pita.post(_("This homeless puppy needs your donation."), "rottweiler-869017__340")
    #$ pita.post(_("If you donate we can feed this puppy."), "cocker-spaniel-2785074__480")
    #$ pita.post(_("These 3 puppies have no home, please donate.."), "animals-1509196__340")






    # let's try to give posts some likes
    python:
        for j in instopost.other_users:
            for i in j.posts:
                for u in [rin_user, mayo_user, guy_101, aya_user]:
                    like = renpy.random.choice([0,1])
                    if like:
                        if not u in i.likes:
                            i.likes.append(u)

    call screen insto
    return
