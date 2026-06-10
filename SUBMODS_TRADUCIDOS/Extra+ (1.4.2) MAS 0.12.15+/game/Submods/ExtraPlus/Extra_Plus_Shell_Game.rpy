#===========================================================================================
# MINIGAME#1 (PENDIENTE DE REVISION) SHELL GAME ...
#===========================================================================================
#====Shell Game
default persistent.sg_max_score = 0

image extra_sg_cup:
    xanchor 0.5 yanchor 0.5
    contains:
        "extra_cup"
        xalign 0.5 yalign 0.5
image extra_sg_cup_hover:
    contains:
        "extra_cup_hover"
        xalign 0.5 yalign 0.5
image extra_sg_cup_idle:
    contains:
        "extra_cup_idle"
        xalign 0.5 yalign 0.5
image extra_sg_ball:
    xanchor 0.5 yanchor 0.5
    contains:
        "extra_ball"
        xalign 0.5 yalign 0.5

screen shell_game_minigame():
    #Displays the shell game minigame interface, letting the player pick a cup and quit the game.
    zorder 50
    style_prefix "hkb"
    use extra_no_click()
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="sg") repeat True

    # Buttons must follow the REAL cup positions after shuffling
    for i in range(3):
        imagebutton:
            xanchor 0.5 yanchor 0.5
            xpos store.ep_sg.cup_coordinates[i]
            ypos 250
            idle "extra_sg_cup_idle"
            hover "extra_sg_cup_hover"
            focus_mask "extra_sg_cup_hover"
            action SGVerification(i, store.ep_sg.ball_position, "sg_check_label")
    
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton _("Salir") action [Hide("shell_game_minigame"), Jump("shell_game_result")]

init -5 python in ep_sg:
    cup_skin = randomize_cup_skin()
    target_shuffles = 4
    ball_position = 1
    current_turn = 1
    shuffle_cups = 0
    cup_speed = 0.9 
    difficulty = 1 # 1-Easy, 2-Normal, 3-Hard, 4-Progressive
    correct_answers = 0
    comment = False
    cup_choice = None
    original_cup = [0, 1, 2]
    cup_coordinates = [695, 925, 1155]
    cup_coordinates_real = [695, 925, 1155]
    #====Comments by moni on standard difficulties
    _compliments = [
        _("¡Bien hecho, [player]!"),
        _("¡Impresionante, sigue así!"),
        _("¡Lo estás haciendo genial!"),
        _("¡Excelente ojo, [player]!"),
        _("¡Buena atrapada!"),
        _("¡Estás progresando!"),
        _("¡Bravo, [player]!"),
        _("¡Excepcional!"),
        _("¡Muy bien!"),
        _("¡Nada se te escapa, ¿eh?!"),
        _("¡Lo estás haciendo fantástico!"),
        _("¡Lo estás haciendo increíble!"),
    ]
    _failures = [
        _("¡Oh, esa no!"),
        _("¡Esa no es, [player]!"),
        _("¡Inténtalo de nuevo!"),
        _("¡No te dejes engañar por tus ojos!"),
        _("¡Sigue practicando, [player]!"),
        _("¡Lo conseguirás la próxima vez!"),
        _("¡Mejor suerte en la próxima ronda!"),
        _("¡No te rindas!"),
        _("¡Casi!"),
        _("Esa no era la respuesta correcta, pero estás cerca."),
        _("Lo siento, [player], esa no es."),
        _("¡No pierdas de vista la pelotita!")
    ]

label minigame_sg:
    show monika 1eub at t11
    if not renpy.seen_label("checkpoint_minigame_sg") and not renpy.seen_label("shell_game_result"):
        m 1etb "¿Quieres jugar al Juego de encuentra la pelotita conmigo, [player]?"
        m 1sua "Es un juego de observación y concentración. ¡Creo que te gustará!"
        m 1eua "Las reglas son simples: esconderé una pelota debajo de uno de estos vasos y los moveré."
        m 1hub "Solo tienes que adivinar bajo qué vaso está la pelota."
        m 1eub "Si adivinas correctamente, anotas un punto!"

label checkpoint_minigame_sg:
    if renpy.seen_label("shell_game_result"):
        m 1eta "¿Quieres jugar al Juego de encuentra la pelotita otra vez, [player]?"
        if persistent.sg_max_score == 0:
            m 1eka "Por cierto, quería disculparme..."
            m 3lkb "Acabo de darme cuenta de que había un error en mi código que estaba evitando que tu puntuación máxima se guardara correctamente."
            m 1hubsb "¡Lo he arreglado ya! Así que a partir de ahora, estaré llevando un registro de tu récord."
            m "¡Buena suerte estableciendo un nuevo récord!"
        else:
            m 1sua "¡Genial! ¡Veamos si puedes superar tu récord de [persistent.sg_max_score] respuestas correctas seguidas!"

    m 1hua "De acuerdo, ¿en qué dificultad quieres jugar?{nw}"
    menu:
        "De acuerdo, ¿en qué dificultad quieres jugar?{fast}"
        "Fácil":
            m 1eua "¿Vas a jugar algo fácil, [player]?"
            extend 1hua " ¡Bien!"
            python:
                ep_sg.cup_speed = 0.85
                ep_sg.difficulty = 1
                ep_sg.target_shuffles = 4
        "Normal":
            m 3eub "¿Quieres empezar con un juego casual? "
            extend 3hub "¡Suena bien!"
            python:
                ep_sg.cup_speed = 0.5
                ep_sg.difficulty = 2
                ep_sg.target_shuffles = 6
        "Difícil":
            m 3etb "¿Estas con confianza?"
            m 1hub "¡Jajaja, así me gusta! ¡Vamos!"
            python:
                ep_sg.cup_speed = 0.25
                ep_sg.difficulty = 3
                ep_sg.target_shuffles = 8
        "Progresivo":
            m 1ttb "¿Un desafío, eh? ¡Me gusta tu espíritu!"
            m 1hub "¡Empecemos fácil y hagamos que sea más difícil a medida que avancemos!"
            python:
                ep_sg.cup_speed = 0.7
                ep_sg.difficulty = 4
                ep_sg.target_shuffles = 3

    python:
        store.ep_button.hide_zoom_button()
        # Disable chibi dragging during minigame
        ep_sg.saved_drag_state = persistent.enable_drag_chibika
        persistent.enable_drag_chibika = False
        # Reset stats for a new game session
        ep_sg.current_turn = 1
        ep_sg.correct_answers = 0

label sg_init_game:
    $ config.allow_skipping = False
    show monika 1eua at t21
    pause 0.2

    show extra_sg_cup zorder 12 as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos -400
        easein_bounce 0.5 ypos 250

    show extra_sg_cup zorder 12 as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show extra_sg_cup zorder 12 as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    pause 1.0

    show extra_sg_ball zorder 12 behind cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 335

    show extra_sg_cup as cup_2:
        linear 0.5 ypos 110

    m 1lub "La pelota siempre empieza por debajo del centro del hoyo." # REVISAR TRADUCCION A LA HORA D JUGAR, SI SE ENTIENDE O NO

    show extra_sg_cup as cup_2:
        linear 0.5 ypos 250

    m 1hub "¡Observa con atención dónde está!"

    hide extra_sg_ball

    show extra_sg_cup as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos 250

    show extra_sg_cup as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 250

    show extra_sg_cup as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos 250

    python:
        ep_sg.cup_coordinates_real[0] = 695
        ep_sg.cup_coordinates_real[1] = 925
        ep_sg.cup_coordinates_real[2] = 1155

        ep_sg.original_cup[0] = 0
        ep_sg.original_cup[1] = 1
        ep_sg.original_cup[2] = 2
        
        # Initialize cup identity tracking
        ep_sg.cup_index_real = [0, 1, 2]

        ep_sg.ball_position = 1
        disable_esc()
        mas_MUMURaiseShield()
        afm_pref = renpy.game.preferences.afm_enable
        renpy.game.preferences.afm_enable = False
    show screen score_minigame(game="sg")

label sg_loop_game:
    show monika 1eua
    show screen extra_no_click
    python:
        move_cup_1, move_cup_2 = renpy.random.sample(range(3), 2)

        # Swap visual positions
        temp_cup_position = ep_sg.cup_coordinates_real[move_cup_2]
        ep_sg.cup_coordinates_real[move_cup_2] = ep_sg.cup_coordinates_real[move_cup_1]
        ep_sg.cup_coordinates_real[move_cup_1] = temp_cup_position

        # Swap cup identities
        temp_cup_index = ep_sg.cup_index_real[move_cup_2]
        ep_sg.cup_index_real[move_cup_2] = ep_sg.cup_index_real[move_cup_1]
        ep_sg.cup_index_real[move_cup_1] = temp_cup_index

        # FIX: Update ball position based on cup identities
        if ep_sg.cup_index_real[move_cup_1] == ep_sg.ball_position:
            ep_sg.ball_position = ep_sg.cup_index_real[move_cup_2]
        elif ep_sg.cup_index_real[move_cup_2] == ep_sg.ball_position:
            ep_sg.ball_position = ep_sg.cup_index_real[move_cup_1]

    $ renpy.pause(ep_sg.cup_speed, hard="True")

    play sound sfx_cup_shuffle

    show extra_sg_cup as cup_1:
        ease ep_sg.cup_speed xpos ep_sg.cup_coordinates_real[0]

    show extra_sg_cup as cup_2:
        ease ep_sg.cup_speed xpos ep_sg.cup_coordinates_real[1]

    show extra_sg_cup as cup_3:
        ease ep_sg.cup_speed xpos ep_sg.cup_coordinates_real[2]

    if ep_sg.shuffle_cups != (ep_sg.target_shuffles - 1):
        $ ep_sg.shuffle_cups += 1
        jump sg_loop_game

    pause 1.0

    show screen shell_game_minigame

    "Selecciona un vaso:"

label sg_check_label:

    hide screen shell_game_minigame

    show extra_sg_cup as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos 250

    show extra_sg_cup as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 250

    show extra_sg_cup as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos 250
    python:
        ep_sg.cup_coordinates_real[0] = 695
        ep_sg.cup_coordinates_real[1] = 925
        ep_sg.cup_coordinates_real[2] = 1155
        cup_dialogues = ["izquierdo", "del centro", "derecho"]
        chosen_cup_dialogue = cup_dialogues[ep_sg.cup_choice]

    m 1eub "Elegiste el vaso [chosen_cup_dialogue]..."

    call sg_reveal_cup(ep_sg.cup_choice, is_chosen=True)

    if ep_sg.comment:
        m 1sub "[renpy.substitute(renpy.random.choice(ep_sg._compliments))]"
    else:
        m 1hub "[renpy.substitute(renpy.random.choice(ep_sg._failures))]"

    if ep_sg.cup_choice != ep_sg.ball_position:
        m 1lub "El vaso correcto era..."
        call sg_reveal_cup(ep_sg.ball_position, is_chosen=False)
        m 1hua "¡Este!"

    show extra_sg_cup as cup_1:
        linear 0.5 xpos ep_sg.cup_coordinates[0] ypos 250

    show extra_sg_cup as cup_2:
        linear 0.5 xpos ep_sg.cup_coordinates[1] ypos 250

    show extra_sg_cup as cup_3:
        linear 0.5 xpos ep_sg.cup_coordinates[2] ypos 250

    pause 1.0

    hide extra_sg_ball
    python:
        ep_sg.current_turn += 1
        ep_sg.shuffle_cups = 0
        ep_sg.ball_position = 1
        # Reset cup identity tracking
        ep_sg.cup_index_real = [0, 1, 2]
        if ep_sg.difficulty == 4 and ep_sg.current_turn % 6 == 0:
            ep_sg.cup_speed = max(0.15, ep_sg.cup_speed - 0.05)
            ep_sg.target_shuffles += 1
    jump sg_loop_game
    return

label sg_reveal_cup(cup_index, is_chosen):
    if cup_index == 0:
        show extra_sg_cup as cup_1:
            linear 0.5 ypos 110
        if cup_index == ep_sg.ball_position:
            show extra_sg_ball zorder 12 behind cup_1:
                xpos ep_sg.cup_coordinates[0] ypos 335
    elif cup_index == 1:
        show extra_sg_cup as cup_2:
            linear 0.5 ypos 110
        if cup_index == ep_sg.ball_position:
            show extra_sg_ball zorder 12 behind cup_2:
                xpos ep_sg.cup_coordinates[1] ypos 335
    elif cup_index == 2:
        show extra_sg_cup as cup_3:
            linear 0.5 ypos 110
        if cup_index == ep_sg.ball_position:
            show extra_sg_ball zorder 12 behind cup_3:
                xpos ep_sg.cup_coordinates[2] ypos 335

    if is_chosen and cup_index == ep_sg.ball_position:
        $ ep_sg.correct_answers += 1
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label shell_game_result:
    hide screen score_minigame
    python:
        new_high_score = (ep_sg.correct_answers > persistent.sg_max_score)
        # Fix logic: current_turn starts at 1 and increments after each round.
        # If user quits immediately, current_turn is 1 (0 played).
        # If user plays 1 round, current_turn becomes 2.
        rounds_played = max(0, ep_sg.current_turn - 1)
        
        enable_esc()
        mas_MUMUDropShield()
        renpy.game.preferences.afm_enable = afm_pref

    hide extra_sg_ball
    show extra_sg_cup as cup_1:
        xpos ep_sg.cup_coordinates[0] ypos 250
        easeout_expo 0.5 ypos -400
    show extra_sg_cup as cup_2:
        xpos ep_sg.cup_coordinates[1] ypos 250
        pause 0.1
        easeout_expo 0.5 ypos -400
    show extra_sg_cup as cup_3:
        xpos ep_sg.cup_coordinates[2] ypos 250
        pause 0.2
        easeout_expo 0.5 ypos -400

    pause 0.8
    hide cup_1
    hide cup_2
    hide cup_3
    hide screen extra_no_click
    show monika at t11

    # The player didn't play any rounds.
    if rounds_played == 0:
        m 1hka "¿Al final no querías jugar?"
        m 1eua "No pasa nada, quizás tengas ganas la próxima vez."
        m 1dub "Te estaré esperando, [player]."

    # The player didn't get any correct.
    elif ep_sg.correct_answers == 0:
        m 1eka "[player], ¿te encuentras bien?"
        m 1ekb "ugamos [rounds_played] rondas y no acertaste ninguna."
        m 1etd "¿Estabas un poco distraído, tal vez?"
        if ep_sg.difficulty == 4: # Dialogue for Progressive
            m 3eka "El modo progresivo puede ser complicado al principio. ¡La velocidad aumenta muchísimo!"
            m 3hua "No te preocupes, seguro que dominarás el juego."
        else:
            m 1hua "Está bien, todos tenemos días malos. ¡Hagamos algo que te anime!"

    # Perfect score!
    elif ep_sg.correct_answers == rounds_played:
        m 2sub "¡Guau, una puntuación perfecta! ¡Las acertaste todas!"
        if new_high_score:
            m 1hubsa "¡Es un nuevo récord! ¡Felicidades, [player]! Me siento muy orgullosa de ti."
        else:
            m 1hubsb "Igualaste tu récord perfecto. ¡Tu concentración es increíble!"
        m 3eub "Tienes unos ojos realmente afilados, Jejeje~"

    # Mixed result (some correct, some failed).
    else:
        m 1eua "¡Qué buena partida, [player]!"
        if new_high_score:
            m 1hubsb "¡Has batido un nuevo récord de  [ep_sg.correct_answers]! ¡Genial!"
            m 1eua "A pesar de algunos errores, has conseguido superar tu mejor marca. ¡Eso sí que es progreso!"
        else:
            m 1hua "Has acertado [ep_sg.correct_answers] veces. ¡Buen trabajo!"
            if ep_sg.difficulty == 4: # Dialogue for Progressive
                m 3hua "Mantener el ritmo del modo progresivo es difícil, ¡pero aguantaste mucho tiempo!"
            else:
                m 3hub "Es solo cuestión de práctica. ¡Sé que pronto superarás tu récord de [persistent.sg_max_score] victorias!"
        
        m 1hubsa "Bueno, gracias por jugar conmigo. ¡Me lo he pasado genial!"
        
        if rounds_played > 50:
            m 3eka "Y también, por favor, descansa la vista un rato. Hemos estado jugando bastante tiempo..."
            m 1dub "Siempre me preocupo por tu salud, [player]."

    window hide
    python:
        if ep_sg.correct_answers > persistent.sg_max_score:
            persistent.sg_max_score = ep_sg.correct_answers
        ep_sg.current_turn = 1 # Reset to 1 for next session
        ep_sg.correct_answers = 0
        ep_sg.shuffle_cups = 0
        # Reset speed and shuffles based on difficulty (not hardcoded)
        # This ensures next game starts with correct values for the difficulty
        if ep_sg.difficulty == 1:  # Easy
            ep_sg.cup_speed = 0.85
            ep_sg.target_shuffles = 4
        elif ep_sg.difficulty == 2:  # Normal
            ep_sg.cup_speed = 0.5
            ep_sg.target_shuffles = 6
        elif ep_sg.difficulty == 3:  # Hard
            ep_sg.cup_speed = 0.25
            ep_sg.target_shuffles = 8
        elif ep_sg.difficulty == 4:  # Progressive
            ep_sg.cup_speed = 0.7
            ep_sg.target_shuffles = 3
        
        # Restore chibi dragging state
        persistent.enable_drag_chibika = ep_sg.saved_drag_state
        
    jump close_extraplus
    return