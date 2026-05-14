# This file is part of Whiteboard submod by Friends of Monika.
# Report issues and ask questions at https://github.com/friends-of-monika/mas-whiteboard/issues


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="fom_whiteboard_topic",
            random=True
        )
    )

label fom_whiteboard_topic:
    m 3eub "Hey [mas_get_player_nickname()], quería mostrarte algo~"
    m 1sub "Últimamente he estado experimentando un poco con el código del juego, ¡y te hice...{w=0.3} una pizarra!"
    m 1hkb "No es gran cosa, lo sé, jajaja~"
    m 2eud "Pensé que podrías aburrirte un poco aquí sentado, así que se me ocurrió algo para entretenerte."

    if renpy.random.randint(0, 20) == 4: # https://xkcd.com/221/
        call fom_whiteboard_topic_yan

    m 3eub "Si tienes curiosidad por intentar dibujar algo, ¡avísame!"
    m 1hua "Espero que te guste~"
    return "derandom"

label fom_whiteboard_topic_yandere:
    # Yandere Monika Overhaul | Summer '26 =)
    $ style.say_dialogue = style.edited
    m 4csb "{cps=14}{color=#000}Para que puedas dibujar algo bonito mientras te miro...{/color}{/cps}{w=3}{nw}"
    $ style.say_dialogue = style.normal

    hide monika
    show yuri glitch zorder MAS_BACKGROUND_Z
    $ _history_list.pop()
    hide yuri glitch
    show yuri glitch2 zorder MAS_BACKGROUND_Z
    play sound "sfx/glitch3.ogg"
    pause 0.1
    hide yuri glitch2
    show yuri glitch zorder MAS_BACKGROUND_Z
    pause 0.3
    hide yuri glitch
    show monika 4rksdlb at i11 zorder MAS_MONIKA_Z
    hide monika
    show monika 4hksdlb at i11 zorder MAS_MONIKA_Z

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="fom_whiteboard_show",
            prompt="¿Puedo usar la pizarra?",
            category=["Pizarra"],
            pool=True,
            unlocked=True
        )
    )

label fom_whiteboard_show:
    # Disable the random topic hinting at the new topic when player actually
    # finds it first on their own
    $ mas_hideEVL("fom_whiteboard_topic", "EVL", derandom=True)

    if mas_getEVL_shown_count("fom_whiteboard_show") == 0:
        m 1eua "¡Claro!{w=0.3} dame un momento para traertelo.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    else:
        m 1hua "¡Oki doki!, enseguida lo traigo.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
 
    call spaceroom(hide_monika=True, scene_change=True, dissolve_all=True)

    if mas_getEVL_shown_count("fom_whiteboard_show") == 0:
        m "No quiero parecer grosera mirándote mientras dibujas, así que me quedaré a tu lado, ¿de acuerdo?~"
    else:
        m "¡Listo!"

    # Setup whiteboard canvas, calls canvas screen with dissolve and hides with dissolve
    $ whiteboard_canvas = store._fom_whiteboard.Whiteboard()
    $ label_init_ts = datetime.datetime.now()
    call screen fom_whiteboard_screen(whiteboard_canvas)
    $ label_time_spent = datetime.datetime.now() - label_init_ts

    # Dispose canvas and remove from global store
    $ whiteboard_canvas.dispose()
    $ del whiteboard_canvas

    if label_time_spent < datetime.timedelta(seconds=10):
        m "¿Ya terminaste? Jajaja~"
    else:
        m"Oh, ¿Ya terminaste?"

    m "¡Espero te hayas divertido!"
    m "Déjame llevarmelo ahora.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    call mas_transition_from_emptydesk("monika 3hua")

    m 3hua "Avísame si necesitas la pizarra blanca otra vez, [mas_get_player_nickname()]~"
    $ del label_init_ts, label_time_spent
    return
