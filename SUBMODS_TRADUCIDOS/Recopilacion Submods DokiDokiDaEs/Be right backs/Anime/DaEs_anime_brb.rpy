init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_anime",
            prompt="I'm going to go watch some anime",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_anime:
    if mas_isMoniNormal(higher=True):
        if (
            mas_isMoniHappy(higher=True)
            and random.randint(1,5) == 1
        ):
            m 1tta "Mind if I watch with you [player]?"
        else:

            m 1eub "Oh! You're going to watch some anime?"

        m 1hua "Hope you enjoy your show!"
        m 3hub "When I cross over we can watch anime together,{w=0.5}{nw} "
        extend 3wublb "doesn't that sound romantic?~"
        m 1eua "See you soon [player]!"

    elif mas_isMoniUpset():
        m 2esc "Ok."

    elif mas_isMoniDis():
        m 6lkc "Take your time, just..."
        m 6ekd "Don't forget to come back when you're done... Ok?"
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_anime"] = True
    return "idle"

label monika_idle_anime_callback:

    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        m 1eua "Finished watching for now, [player]?"
        m 1eub "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return
