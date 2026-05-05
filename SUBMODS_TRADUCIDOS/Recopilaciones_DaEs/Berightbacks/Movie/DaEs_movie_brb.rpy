init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_movie",
            prompt="¿Quieres ver una película?",
            category=['Vuelvo enseguida'],
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
            m 1tta "¡Oh, qué emocionante  [player]!"
        else:

            m 1eub "Tengo muchas ganas de ver lo que has elegido. [player]!"

        m 1hua "¿Qué género tienes en mente?"
        m 3hub "De cualquier manera, estoy segura de que será divertido ver cualquier cosa contigo,{w=0.5}{nw} "
        extend 3wublb "¿No crees?~"
        m 1eua "¡Nos vemos pronto [player]!"

    elif mas_isMoniUpset():
        m 2esc "De acuerdo."

    elif mas_isMoniDis():
        m 6lkc "Tómate tu tiempo, solo..."
        m 6ekd "No olvides volver cuando termines... ¿Esta bien?"
        m 6lka "De lo contrario."
    else:

        m 6ckc "..."

    $ persistent._mas_idle_data["monika_idle_movie"] = True
    return "idle"

label monika_idle_movie_callback:

    if mas_isMoniNormal(higher=True):
        $ wb_quip = mas_brbs.get_wb_quip()
        m 1eua "¡Me encantó ver eso contigo [player]!"
        m 1eub "[wb_quip]"
    else:

        call mas_brb_generic_low_aff_callback

    return
