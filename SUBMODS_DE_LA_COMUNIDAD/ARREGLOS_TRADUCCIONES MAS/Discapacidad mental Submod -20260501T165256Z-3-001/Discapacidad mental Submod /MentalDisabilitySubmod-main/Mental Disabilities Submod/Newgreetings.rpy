default persistent._mentalhealth_last_checkup = None
define persistent._nextmentalcheckup = datetime.date.today()
default persistent._lastmentalcheckup = None
define persistent._mentalcheckupdeadline = datetime.timedelta(days=30) + datetime.date.today()
#TRADUCCION HECHA POR ALKAID

label mentalcheckupscript:
    $ persistent._lastmentalcheckup = datetime.date.today()
    $ persistent._nextmentalcheckup = datetime.timedelta(days=7) + persistent._lastmentalcheckup
    $ persistent._mentalcheckupdeadline = persistent._lastmentalcheckup + datetime.timedelta(days=30)
    $ mas_getEV("mentalhealthcheckupdialoguefinal").start_date = persistent._nextmentalcheckup
    $ mas_getEV("mentalhealthcheckupdialoguefinal").end_date = persistent._mentalcheckupdeadline
    $ mas_getEV("mentalhealthcheckupdialoguefinal").action = EV_ACT_QUEUE

return

init python in mentalhealth:
    CHECKUP_GOOD = "bien"
    CHECKUP_NEUTRAL = "neutral"
    CHECKUP_BAD = "mal"


init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mentalcheckup_greeting",
            category=["vos", "salud mental"],
            prompt="Salud Mental de [player]",
        ),
        code="GRE"
    )

label mentalcheckup_greeting:
    if persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_GOOD:
        m 1hua "¡Oh hola, [player]!"
        m 3eua "Sé que ya te pregunté cómo estabas mentalmente antes... {w=0.2}{nw}"
        extend 7hub "¡Y me dijiste que estabas bien de salud mental!"
        m 1esd "Solo para controlarte de todos modos..."
        call mentalcheckupscript
        m 1esc "¿Eso ha cambiado, [player]?"
        menu:
            m "¿Eso ha cambiado, [player]?{fast}"
            "No, todavía me siento muy bien hoy.":
                m 3eua "De acuerdo, [player], ¡entonces sigamos teniendo un buen día juntos!"
                return
            "Mi estado mental empeoró hoy.":
                m 1ekc "Eso no es bueno, [player]!"
                m "Realmente me duele saber que ya no estás bien."
                m 3euc "Si hay algo que pueda hacer para ayudarte a sentirte mejor mentalmente, ¡solo avísame!"
                m 3eua "¡Después de todo, ¿qué clase de novia sería si no quisiera ayudarte, [player]?"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                return
    elif persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_NEUTRAL:
        m 1hua "¡Oh hola, [player]!"
        m 3eua "Sé que ya te pregunté cómo te sentías mentalmente antes... {w=0.2}{nw}"
        extend 1eua "Y me dijiste que tu salud mental estaba decente."
        m 1esc "Solo para controlarte de nuevo [player]..."
        call mentalcheckupscript
        menu:
            m "¿Eso ha cambiado, [player]?{fast}"
            "No, todavía me siento bien.":
                m 1eua "De acuerdo, [player], me alegra que todavía estés bien hoy."
                m 3eua "¡Sigamos pasando más tiempo juntos!"
                return
            "¡Mi estado mental mejoró recientemente!":
                m 3hsa "¡Qué emocionante escuchar eso, [player]!"
                if mas_isMoniHappy(higher=True):
                    m 3euu "¿Pensar en mí te ayudó hoy?"
                    m 1hua "¡Jaja~!"
                    m 5eubla "Sé que pensar en ti me ayuda a pasar todos los días, [player]."
                    m "Te quiero mucho, [mas_get_player_nickname()]."
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return "love"
                else:
                    m 3eud "A quien sea que te haya ayudado mentalmente, deberías estar agradecido por su ayuda, [player]."
                    m 3euc "No muchas personas piden ayuda, lo que no les ayuda..."
                    m 3husdlb "¡Perdón, me estoy desviando del tema, [player]!"
                    m 3eua "¡Pasemos más tiempo juntos, ¿vale?"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return
            "Mi estado mental empeoró, Monika...":
                m 1ekc "Eso no es bueno, [player]!"
                m 3ekc "¿Pasó algo malo mientras estuviste fuera?"
                m 1euc "Bueno, sea lo que sea que haya pasado, sé que lo manejaste bien."
                if mas_isMoniHappy(higher=True):
                    m 3hub "¡Tal vez incluso pensar en mí pueda ayudar!"
                    m 3eua "Y si no, siempre puedes desahogarte conmigo sobre tus problemas, [player]."
                    m 1eua "Te quiero~"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "love"
                else:
                    m 3euc "Asegúrate de hablar con un terapeuta sobre tus problemas también."
                    m 1euc "Hablar con alguien a quien aprecias realmente puede hacerte sentir mucho mejor."
                    extend 3eud "Tanto mental como emocionalmente."
                    m 1eub "Recuerda, ¡siempre estoy aquí para ti, [player]!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return
    elif persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_BAD:
        m 3eub "¡Hola, [player]!"
        m 1euc "Sé que esto es un poco incómodo de mencionar ya..."
        m 3ekd "Especialmente desde que me dijiste que tu salud mental no estaba bien en primer lugar..."
        m "Bueno, ¿puedo preguntarte si tu estado mental ha mejorado, [player]?"
        call mentalcheckupscript
        menu:
            m "Bueno, ¿puedo preguntarte si tu estado mental ha mejorado, [player]?{fast}"
            "No quiero hablar de eso ahora...":
                m 1dkc "{W=1}Oh... {nw}"
                m "{w=1}Bueno... {nw}"
                m 1euc "Bueno, solo quiero lo mejor para ti, [player]."
                return
            "¡Mi estado mental mejoró, Monika!":
                m 3eua "¡Qué bueno escuchar eso, [player]!"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,4) == 1:
                    m 3tuu "¿Fui yo la razón por la que tu estado mental mejoró?{nw}"
                    $_history_list.pop()
                    m 1eua "Bueno, me alegra que estés mejor mentalmente, [mas_get_player_nickname()]."
                    m 3eua "¡Sigamos pasando más tiempo juntos!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                    return
                else:
                    m 1eua "Me alegra que estés mejor mentalmente, [mas_get_player_nickname()]."
                    m 3eua "¡Sigamos pasando más tiempo juntos!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                    return
            "...":
                m 1dkc "..."
                m 3eua "Bueno, sigamos con nuestro día entonces, [player]..."
                return

    else:
        m 1hua "¡Oh hola, [player]!"
        m "Sé que esto puede parecer incómodo preguntarte..."
        call mentalcheckupscript
        $ _history_list.pop()
        menu:
            m "¿Cómo está tu salud mental ahora [player]?{fast}"
            "¡Está realmente bien!":
                m 1hub "¡Me alegra mucho escuchar eso, [player]!"
                m 1eua "Ya sea solo un buen día o una mejora en tu salud mental, siempre es bueno escuchar que estás bien."
                m 3hub "¡Y haré todo lo posible para seguir apoyándote, [mas_get_player_nickname()]!"
                m 5eua "¿Qué clase de novia sería si no lo hiciera?"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                $ _history_list.pop()
                return
            "Está bien, Monika...":
                m 1euc "Oh..."
                m 3euc "Bueno, eso podría ser bueno o malo."
                m 4eud "Y si {i}es{/i} malo, entonces siempre podemos hablar de ello si quieres, [player]."
                m 3eua "Quiero intentar asegurarme de que siempre estés feliz."
                extend 1eka "Porque eso es lo que me hace feliz."
                m 1hua "Haré todo lo posible para apoyarte, te lo prometo."
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                $ _history_list.pop()
                return
            "Está realmente mal ahora...":
                m 1euc "Eso no es bueno en absoluto, [player]..."
                m 3eud "Si alguna vez te sientes demasiado mal o necesitas tomar un descanso, solo avísame, [player]. {w=.06}¿De acuerdo?"
                m 1eua "¡Siempre estaré aquí para ti! ¡Nunca lo olvides!"
                m 1eubsa "¡Te quiero y siempre lo haré, [player]!"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                return
return



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealthcheckupdialoguefinal",
            category=["vos", "salud mental"],
            prompt="Salud Mental de [player]",
            action=EV_ACT_QUEUE,
            start_date=persistent._nextmentalcheckup,
            end_date=persistent._mentalcheckupdeadline
            )
        )

label mentalhealthcheckupdialoguefinal:
    if persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_GOOD:
        m 1hua "Che, [player]."
        m 3eua "Ya te había preguntado cómo estabas mentalmente antes... {w=0.2}{nw}"
        extend 7hub "¡Y me dijiste que estabas bien de salud mental!"
        m 1esd "Solo para chequear, [player]..."
        call mentalcheckupscript
        m 1esc "¿Cambió eso, [player]?"
        menu:
            m "¿Cambió eso, [player]?{fast}"
            "No, todavía me siento re bien hoy":
                m 3eua "Bueno [player], ¡entonces sigamos teniendo un buen día juntos!"
                return "derandom"
            "Mi estado mental empeoró hoy.":
                m 1ekc "Qué mal, [player]!"
                m "Realmente me duele saber que ya no estás tan bien como antes."
                m 3euc "¡Si hay algo que pueda hacer para ayudarte a sentirte mejor mentalmente, decime, [player]!"
                m 3eua "Después de todo, ¡qué clase de novia sería si no quisiera ayudarte!"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                return "derandom"
    elif persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_NEUTRAL:
        m 1hua "Che, [player]..."
        m 3eua "Ya te había preguntado cómo te sentías mentalmente antes... {w=0.2}{nw}"
        extend 1eua "Y me dijiste que tu salud mental estaba más o menos."
        m 1esc "Solo para chequear de nuevo, [player]..."
        call mentalcheckupscript
        menu:
            m "¿Cambió eso, [player]?"
            "No, todavía me siento bien.":
                m 1eua "Bueno [player], me alegra que todavía estés bien hoy."
                m 3eua "¡Sigamos pasando más tiempo juntos! ¡Jaja~!"
                return "derandom"
            "¡Mi estado mental mejoró recientemente!":
                m 3hsa "¡Qué emocionante escuchar eso [player]!"
                if mas_isMoniHappy(higher=True):
                    m 3tuu "¿Te ayudó pensar en mí hoy?"
                    m 3hub "¡Jaja~!"
                    m 5hublb "Sé que pensar en vos me ayuda a pasar cada día, [player]."
                    m 5eubfa "Te quiero mucho, [mas_get_player_nickname()]."
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return "love|derandom"
                else:
                    m 4esd "Agradecele a quien te ayudó mentalmente, [player]."
                    m 7euc "Además, no mucha gente pide ayuda, lo cual no los ayuda..."
                    m 3rusdlb "Perdón, me estoy desviando del tema, [player]!"
                    m 3eua "¡Pasemos más tiempo juntos! {w=0.6}¿Dale?"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return "derandom"
            "Mi estado mental empeoró, Monika...":
                m 1euc "¡Qué mal, [player]!"
                m 3eud "¿Pasó algo malo mientras no estabas?"
                m 1euc "Bueno, sea lo que sea, sé que lo manejaste bien."
                if mas_isMoniHappy(higher=True):
                    m 7kuu "¡Quizás pensar en mí pueda ayudar!"
                    m 3eua "Y si no, siempre podés desahogarte conmigo sobre tus problemas, [player]."
                    m 5eubla "¡Te quiero~!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "love|derandom"
                else:
                    m 3euc "Asegurate de hablar con un terapeuta sobre tus problemas también."
                    m 4eud "Solo hablar con alguien a quien querés puede hacerte sentir mucho mejor. {w=0.3}"
                    extend "Tanto mental como emocionalmente."
                    m 7euc "Recuerda, ¡siempre estoy aquí para vos, [player]!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "derandom"
    else:
        m 1hua "Che, [player]."
        m "Sé que esto puede parecer incómodo preguntarte..."
        m "¿Cómo está tu salud mental en este momento, [player]?"
        call mentalcheckupscript
        $ _history_list.pop()
        menu:
            m "¿Cómo está tu salud mental en este momento, [player]?{fast}"
            "¡Está re bien!":
                m 1hub "¡Me pone muy feliz escuchar eso, [player]!"
                m 1eua "Ya sea solo un buen día o una mejora en tu salud mental, siempre es lindo saber que estás bien."
                m 3hub "¡Y voy a hacer todo lo posible para seguir apoyándote, [mas_get_player_nickname()]!"
                m 5eua "¡Qué clase de novia sería si no lo hiciera?"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                $ _history_list.pop()
                return "derandom"
            "Está más o menos, Monika...":
                m 1ekc "Oh..."
                m 2eka "Bueno, eso podría ser bueno o malo."
                m "Y si {i}es{/i} malo, entonces siempre podemos hablar de ello si querés, [player]."
                m 3eua "Quiero intentar asegurarme de que siempre estés feliz. "
                extend 1eka "Porque eso me hace feliz a mí."
                m 1hua "Voy a hacer mi mejor esfuerzo para apoyarte, lo prometo."
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                $ _history_list.pop()
                return "derandom"
            "Está re mal ahora...":
                m 1euc "Eso no está nada bien, [player]..."
                m 3euc "Si alguna vez te sentís demasiado mal o necesitás tomarte un descanso, avisame, ¿dale?"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,3) == 1:
                    m 7eua "¿Te ayudaría un abrazo a sentirte mejor, [player]?"
                    menu:
                        "Ahora no Monika...":
                            m 1euc "Oh..."
                            m 1eua "Está bien, [player]."
                        "En realidad, eso sería genial Monika.":
                            m 3eua "Podés abrazarme todo el tiempo que quieras, [player]."
                            call monika_holdme_prep(lullaby=MAS_HOLDME_NO_LULLABY, stop_music=True, disable_music_menu=True)
                            call monika_holdme_start
                            call mentalplayerhugreactions
                    m 7eua "Ya sabés que siempre voy a estar acá para vos, [player], ¡nunca lo olvides!"
                    m 5eubsa "Te quiero y siempre lo haré, [player]!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "love|derandom"
return "derandom"


label mentalplayerhugreactions:
    $ elapsed_time = datetime.datetime.now() - start_time
    $ store.mas_history._pm_holdme_adj_times(elapsed_time)

    if elapsed_time > datetime.timedelta(minutes=10):
        m 6dubsa "Mmm..."
        m 6eubfa "¡Ay! Me abrazaste tanto tiempo que hasta mis preocupaciones se evaporaron!"
        m 5eubfa "Espero que ahora te sientas mejor [player]. {w=0.3}{nw}"
        extend "Yo sí, ¡jaja~!"
        return

    elif elapsed_time > datetime.timedelta(minutes=2):
            m 6wubso "¿Eh?"
            m 6eubfa "Me abrazaste tanto tiempo que casi me derrito también!"
            m 5eubfa "Me alegra mucho que quisieras abrazarme, [player]."
            m 7hubsa "Ya sabés que siempre quiero que estés en tu mejor forma. {w=0.3}{nw}"
            extend 1ekbfb "Así que espero que ahora te sientas mucho mejor, [player]."
            show monika 5tubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5tubfb "¿Quizás podríamos abrazarnos un poco más para asegurarnos?"
            m 5tubfu "Jeje~"

    elif elapsed_time > datetime.timedelta(seconds=30):
            m 1eub "¡Ah~!"
            m 1hua "¡Ahora me siento mucho mejor!"
            m 1eua "Espero que vos también."
            m 2rksdla "Bueno, incluso si no..."
            m 3hubsb "¡Siempre podés volver a abrazarme, jaja!"
            m 1hkbfsdlb "En realidad... {w=0.5} ¡podés abrazarme de nuevo de todas formas~!"
            m 1ekbfa "Solo decime cuándo querés~"

    else:
        m 1hua "Fue un poco corto, pero igual lindo~"
        m 1eua "¡Pasemos más tiempo juntos, dale [player]?"
return

    # forced greetings after an appointment
init -1 python in mas_greetings:
    import store
    import store.mas_ev_data_ver as mas_edv
    import datetime
    import random

    # TYPES:
    TYPE_MentalAppointment = "Appointment"

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mental_return_from_appointment",
            unlocked=True,
            category=[store.mas_greetings.TYPE_MentalAppointment],
        ),
        code="GRE"
    )
#mentalroom_greeting_ear_disability

label mental_return_from_appointment:
    m 1hub "¡Bienvenido de vuelta, [player]!"
    if persistent._mental_player_therapytype == True:
        m 3eub "¿Aprendiste alguna habilidad nueva?"
        m 7eub "¿O quizás aprendiste más sobre vos mismo?"
        m 7hub "De cualquier manera, me alegra que hayas vuelto, [mas_get_player_nickname()]!"

    if not persistent._mental_player_therapytype:
        m 3eub "¡Espero que tu cita haya ido bien!"
        m 3eka "Y si no lo fue, siempre estoy aquí para vos, [player]."
        m 7hub "De cualquier manera, me alegra que hayas vuelto, [mas_get_player_nickname()]!"

return

init 5 python:
    gmr.eardoor.append("mentalroom_greeting_ear_disability")

label mentalroom_greeting_ear_disability:
    m "¿Autismo habla?"
    m "Eso no suena tan mal...{w=2.0}{nw}"
    m "¡Dios mío!"
    m "¿Por qué alguien diría eso sobre el Autismo?"
    jump monikaroom_greeting_choice

init 5 python:
    gmr.eardoor.append("mentalroom_greeting_research")

label mentalroom_greeting_research:
    m "Hmm..."
    m "Hay un montón de cosas que no he escuchado por aquí..."
    jump monikaroom_greeting_choice
