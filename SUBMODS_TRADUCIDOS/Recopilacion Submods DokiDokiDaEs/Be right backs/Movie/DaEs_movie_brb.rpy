init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_movie",
            prompt="Do you want to watch a movie?",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_movie:
    if mas_isMoniNormal(higher=True):
        if (
            mas_isMoniHappy(higher=True)
            and random.randint(1,5) == 1
        ):
            m 1tta "Oh how exciting [player]!"
        else:

            m 1eub "I'm looking forward to seeing what you've picked [player]!"

        m 1hua "I wonder what genre you have in mind?"
        m 3hub "Either way I'm sure it will be fun watching anything with you,{w=0.5}{nw} "
        extend 3wublb "don't you think?~"
        m 1eua "See you soon [player]!"

    elif mas_isMoniUpset():
        m 2esc "Ok."

    elif mas_isMoniDis():
        m 6lkc "Take your time, just..."
        m 6ekd "Don't forget to come back when you're done... Ok?"
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_movie"] = True
    return "idle"

label monika_idle_movie_callback:

    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        m 1eua "I really enjoyed watching that with you [player]!"
        m 1eub "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return
