init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_youtube",
            prompt="Voy a ver YouTube",
            category=['Vuelvo enseguida'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_youtube:
    if mas_isMoniNormal(higher=True):
        if (
            mas_isMoniHappy(higher=True)
            and random.randint(1,5) == 1
        ):
            m 1tta "¿Te importa si veo YouTube contigo [player]?"
        else:

            m 1eub "¡Oh! ¿Vas a ver YouTube?"

        m 1hua "¡Esto suena divertido!"
        m 1eua "¡Nos vemos pronto [player]!"

    elif mas_isMoniUpset():
        m 2esc "De acuerdo."

    elif mas_isMoniDis():
        m 6lkc "Tómate tu tiempo, solo..."
        m 6ekd "No olvides volver cuando termines... ¿ok?"
        m 6lka "De lo contrario."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_youtube"] = True
    return "idle"

label monika_idle_youtube_callback:

    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        m 1eua "¿Has terminado de ver YouTube por ahora, [player]?"
        m 1eub "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return
