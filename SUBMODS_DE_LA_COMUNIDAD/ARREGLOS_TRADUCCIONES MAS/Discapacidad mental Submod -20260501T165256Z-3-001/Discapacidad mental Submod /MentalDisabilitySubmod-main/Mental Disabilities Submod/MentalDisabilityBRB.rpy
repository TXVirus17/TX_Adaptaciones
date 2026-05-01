# comentario aleatorio para cuando el jugador regresa y se ha calmado, si deciden no desahogarse con Monika
# Lo siento PencilMario, hasta que pueda dejarlo como quiero, la revisión tendrá que esperar.
init python:
    RandomCalmDownWelcome = ["¡Pasemos más tiempo juntos!",
    "¡Hagamos que el resto de tu día sea mejor, juntos!",
    "¿Qué querés hacer ahora?",
    "Espero que podamos disfrutar el resto de nuestro día juntos."
    ]

    RandomCalmDownWelcomeQuip = random.choice(RandomCalmDownWelcome)
#TRADUCCION HECHA POR ALKAID

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_calmdown_idle",
            prompt="Voy a calmarme",
            category=['vuelvo enseguida'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label mental_calmdown_idle:
    m 1euc "¿Necesitás calmarte, [player]?"
    m "¡Espero no haberte molestado!"
    m 3euc "¿Bueno, te gustaría decirme por qué estás molesto, [player]?{nw}"
    menu:
        m "¿Bueno, te gustaría decirme por qué estás molesto, [player]?"
        "Sí.":
            $ PlayerAskedMonikaToVent = True
            m 1eua "Adelante, contame todo por qué estás molesto, [player]."
            m "Voy a mostrar un aviso para que me digas cuando hayas terminado de hablar. No te interrumpo."
            menu:
                "Terminé de hablar Monika...":
                    jump mental_calmdown_idle_callback
        "No, gracias.":
            $ PlayerAskedMonikaToVent = False
            m 1euc "Oh, está bien."
            m 3hub "Estaré aquí esperándote, [player]!"

    # Configurar la etiqueta de devolución de llamada
    $ mas_idle_mailbox.send_idle_cb("mental_calmdown_idle_callback")
    # Luego los datos de inactividad
    $ persistent._mas_idle_data["mental_idle_calmdown"] = True
    return "idle"

label mental_calmdown_idle_callback:

    m 3eud "¿Te has calmado, [player]?"
    menu:
        "Sí.":
            if PlayerAskedMonikaToVent == True:
                m 1eua "Me alegra haber podido ayudarte a calmarte un poco, [player]."
            else:
                m 1eua "Me alegra que te hayas calmado, [player]."
        "No.":
            m 1euc "Incluso si no pudiste calmarte completamente, ponerse en un ambiente más tranquilo puede ayudarte a calmarte más."
            m 3eub "¡Como este lugar!"
    m 1eub "Sabés, realmente desearía poder hacer más..."
    m 3euc "Aunque no pueda estar físicamente."
    extend 3eua "¡Siempre estaré aquí para vos en tu computadora!"
    m 1rusdlc "O al menos hasta que haya una forma de salir de tu computadora."
    m 1eua "De todos modos, [RandomCalmDownWelcomeQuip]"

    return
