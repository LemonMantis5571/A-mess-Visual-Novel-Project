label guide:
    scene bg blank
    stop music fadeout 1.0
    play music "audio/guide.mp3" fadein 1.0 volume 0.2
    scene bg guide with pixellate
    show guide at left

    guide "You do not progress by listening passively anymore."
    guide "Each route advances when you clear the rhythm charts attached to that character."
    guide "The default lane keys are D, F, J and K."
    guide "You can also tap the lane buttons on screen."

    menu:
        "How do I progress?":
            guide "Clear Nuria's first chart to unlock Tamy."
            guide "Clear both charts for a character to finish that route."
            guide "The music room lets you preview tracks and practice unlocked charts."
            jump guide

        "What counts as a clear?":
            guide "You need at least a C grade."
            guide "Perfect and Good hits raise score and combo."
            guide "Too many misses will break the clear."
            jump guide

        "Back":
            hide guide
            jump class_hub
