init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="wrs_mentalhealthwrs_rhythmgames",
            category=[r"(?i)Taiko no Tatsujin, Osu!|DJMAX RESPECT|Friday Night Funkin'"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle = True
        ),
        code="WRS"
    )
#TRADUCCION HECHA POR ALKAID
label wrs_mentalhealthwrs_rhythmgames:
    python:
        title = mas_getActiveWindowHandle()
        titlereact = title.lower()

        if 'youtube' in titlereact:
            mentalrhythmgamesquips = [
                "¿Mirando a alguien más jugar, [player]?",
                "¡Este juego parece realmente divertido, [player]!",
                "¿Viendo algo impresionante, [player]?"
            ]

            mentalrhythmgamechoice = renpy.random.choice(mentalrhythmgamesquips)


            wrs_success = mas_display_notif(
                m_name,
                [mentalrhythmgamechoice],
                'Window Reactions'
            )


        else:
            mentalrhythmgamesquips = [
            "¿Jugando a un juego de ritmo, [player]?",
            "¡Este juego parece realmente divertido, [player]!",
            "¿Intentando obtener un nuevo récord, [player]?",
            "Esto parece que puede ser desafiante. \nEspero que no sea un problema para ti, [player].",
            "¿Te importa si te veo jugar, [player]?",
            "¿Intentando obtener un combo completo? \n¡Podés hacerlo, [player]!"
            ]

            mentalrhythmgamechoice = renpy.random.choice(mentalrhythmgamesquips)


            wrs_success = mas_display_notif(
                m_name,
                [mentalrhythmgamechoice],
                'Window Reactions'
            )





    if not wrs_success:
        $ mas_unlockFailedWRS('wrs_mentalhealthwrs_rhythmgames')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="wrs_mentalhealthwrs_profile",
            category=["TGSMonitiku67"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label wrs_mentalhealthwrs_profile:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Mirando un perfil, [player]?",
            "Esto parece extrañamente familiar, ¿no es así, [player]?",
            "¡Recordá lo que te dije, [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('wrs_mentalhealthwrs_profile')
    return
