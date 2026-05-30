#===========================================================================================
# MINIGAME#2 (EN ESPERA DE PRUEBAS) - TIC-TAC-TOE
#===========================================================================================
#====Tic-Tac-Toe
default persistent.ttt_result_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]

init -5 python in ep_ttt:
    game = None
    colors = [
        "'",
        "#0142a4",
        "0",
        "#a80000"
    ]

image ttt_cross:
    Text(ep_ttt.colors[0],
        font = ep_tools.pictograms_font,
        size = 180,
        color = ep_ttt.colors[1],
        outlines = []
    )
    on show:
        alpha 0.5
        linear 0.25 alpha 1.0
        
image ttt_cross_cursor:
    Text(ep_ttt.colors[0],
        font = ep_tools.pictograms_font,
        size = 180,
        color = ep_ttt.colors[1],
        outlines = []
    )
    alpha 0.25
    truecenter

image ttt_circle:
    Text(ep_ttt.colors[2],
        font = ep_tools.pictograms_font,
        size = 180,
        color = ep_ttt.colors[3],
        outlines = []
    )
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0

init 10 python in ep_ttt:
    import store

    class TicTacToeGame(object):
        def __init__(self):
            self.field = [None] * 9
            self.playerTurn = True
            self.state = 0
            self.score = [0, 0]

        def check_line(self, id):
            t_ids = None
            if id == 1:
                t_ids = [0, 4, 8]
            elif id == 2:
                t_ids = [2, 4, 6]
            elif id < 6:
                id -= 3
                t_ids = [id, id + 3, id + 6]
            else:
                ti = (id-6) * 3
                t_ids = [ti, ti + 1, ti + 2]

            clt, crt = 0, 0
            for i in t_ids:
                i = self.field[i]
                if i is True:
                    crt += 1
                elif i is False:
                    clt += 1
            return clt, crt, t_ids

        def new_state(self):
            for i in range(1, 9):
                clt, crt = self.check_line(i)[:2]
                if clt == 3:
                    return i
                elif crt == 3:
                    return -i

            for i in self.field:
                if i is None:
                    return 0
            return 9

        def turn(self, i):
            if self.state == 0 and self.field[i] is None:
                self.field[i] = self.playerTurn
                self.playerTurn = not self.playerTurn

                if self.playerTurn: # If playerTurn is True, it means the *previous* turn was Monika's (circle)
                    renpy.play(store.sfx_ttt_circle, "sound")
                else: # If playerTurn is False, it means the *previous* turn was Player's (cross)
                    renpy.play(store.sfx_ttt_cross, "sound")

                self.state = self.new_state()
                self.check_state()
            if not self.playerTurn:
                renpy.call_in_new_context("minigame_ttt_m_turn")

        def check_state(self):
            if self.state != 0:
                if abs(self.state) < 9:
                    renpy.call_in_new_context("minigame_ttt_m_comment", self.state < 0)
                    self.restart_round(winner = self.state < 0)
                elif self.state == -9:
                    # Player gave up
                    renpy.call_in_new_context("minigame_ttt_m_comment", 3)
                    self.restart_round(winner = 0) # Monika wins by forfeit
                else:
                    # Tie
                    renpy.call_in_new_context("minigame_ttt_m_comment", 2)
                    self.restart_round()

        def ai(self):
            w_lines, l_lines, f_lines = [], [], []

            for i in range(1, 9):
                # --- AI Strategy ---
                # If board is empty, take a corner (optimal opening)
                if all(tile is None for tile in self.field):
                    return self.turn(renpy.random.choice([0, 2, 6, 8]))

                # If player didn't take center on first move, take it (optimal defense)
                if self.field.count(True) == 1 and self.field[4] is None:
                    return self.turn(4)

                clt, crt, line = self.check_line(i)
                if clt == 2 and crt == 0:
                    w_lines.append(line)
                elif crt == 2 and clt == 0:
                    l_lines.append(line)
                elif clt > 0 and crt == 0:
                    f_lines.append(line)

            if len(w_lines):
                line = renpy.random.choice(w_lines)
                for i in line:
                    if self.field[i] is None:
                        return self.turn(i)
            if len(l_lines):
                line = renpy.random.choice(l_lines)
                for i in line:
                    if self.field[i] is None:
                        return self.turn(i)
            if len(f_lines):
                line = renpy.random.choice(f_lines)
                possible_moves = list(filter(lambda x: self.field[x] is None, line))
                return self.turn(renpy.random.choice(possible_moves))
            else:
                possible_moves = list(filter(lambda x: self.field[x] is None, range(9)))
                return self.turn(renpy.random.choice(possible_moves))

        def restart_round(self, winner=None):
            self.field = [None] * 9
            self.playerTurn = True
            self.state = 0
            if winner is not None:
                self.score[int(winner)] += 1

screen ttt_score():
    hbox:
        xalign 0.75
        ypos 0.900
        spacing 100

        text "[m_name]: " + str(store.ep_ttt.game.score[0]) style "monika_text":
            if not store.ep_ttt.game.playerTurn:
                color ep_ttt.colors[3]

        # Player Score
        text "[player]: " + str(store.ep_ttt.game.score[1]) style "monika_text":
            if store.ep_ttt.game.playerTurn:
                color ep_ttt.colors[1]
    hbox:
        spacing 5
        xpos 0.05
        yanchor 2.0
        ypos 85
        textbutton _("Salir"):
            style "hkb_button" 
            action If(store.ep_ttt.game.playerTurn, [Hide("minigame_ttt_scr"), Jump("minigame_ttt_quit")]) sensitive store.ep_ttt.game.playerTurn
        textbutton _("Me rindo"):
            style "hkb_button" 
            action If(store.ep_ttt.game.playerTurn, [SetField(store.ep_ttt.game, "Turno de [player]", False), SetField(store.ep_ttt.game, "state", -9), Function(store.ep_ttt.game.check_state)]) sensitive store.ep_ttt.game.playerTurn

screen minigame_ttt_grid():
    for i in range(2):
        add "extra_line_black" pos (700, 260 + 192*i) zoom 0.8
        add "extra_line_black" pos (600 + 192*i, 80) rotate 90 zoom 0.8

screen minigame_ttt_scr():
    key "h" action NullAction()
    key "H" action NullAction()
    key "mouseup_3" action NullAction()
    use ttt_score
    layer "master"
    zorder 51
    if store.ep_ttt.game.playerTurn:
        timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="ttt") repeat True

    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use minigame_ttt_grid()

    for x in range(3):
        for y in range(3):
            $i, p = store.ep_ttt.game.field[3 * y + x], (595 + 192 * (x+1), 188 * (y+1))
            if i is True:
                add "ttt_cross" anchor (0.5, 0.5) pos p
            elif i is False:
                add "ttt_circle" anchor (0.5, 0.5) pos p
            if store.ep_ttt.game.state == 0 and store.ep_ttt.game.playerTurn:
                button:
                    background None
                    pos p
                    xysize (184, 184)
                    anchor (0.5, 0.5)
                    if i is None:
                        hover_background "ttt_cross_cursor"
                    keyboard_focus i is None
                    keysym "K_KP" + str(3 * (2-x) + y + 1)
                    action Function(store.ep_ttt.game.turn, 3 * y + x)

            if store.ep_ttt.game.state != 0:
                $ color = store.ep_ttt.game.state > 0 and "moni" or "player"
                $ state = abs(store.ep_ttt.game.state)
                if state < 3:
                    add "extra_line_"+color anchor (0.5, 0.5) xzoom diag_sc yzoom sc rotate (90 * state - 45) pos (980, 360) # / Fix
                elif state < 6:
                    add "extra_line_"+color anchor (-55, 0.5) zoom sc rotate 90 pos (192 * state - 128, 360) # | Fix
                else:
                    add "extra_line_"+color anchor (0.5, 0.5) zoom sc pos (982, 192 * state - 984) # - Fix

#====Label
label minigame_ttt:
    python:
        ep_ttt.game = ep_ttt.TicTacToeGame()
    show extra_notebook zorder 12 at animated_book
    pause 0.5
    # Very first time playing
    if not renpy.seen_label("checkpoint_minigame_ttt") and not renpy.seen_label("minigame_ttt_quit"):
        m 1hua "¡Muy bien, [player]! ¡Juguemos al tres en raya!"
        m 1eua "Es un clásico por algo. Tú puedes ser la X y yo la O."
        m 1eub "Puede parecer sencillo, pero se necesita estrategia para ganarme. ¡Buena suerte!"

label checkpoint_minigame_ttt:
    if renpy.seen_label("minigame_ttt_quit"):
        # If the player won the last game
        if persistent.ttt_result_game[0]:
            m 3eub "¿Listo para la revancha, [player]? He estado perfeccionando mi estrategia. Jejeje~"
            m 3hua "¡Aunque no creas que será tan fácil volver a ganar!"
        # If Monika won the last game
        elif persistent.ttt_result_game[1]:
            m 1hub "Entonces, ¿estás listo para intentar arrebatarme el título de campeóna?"
            m 1hua "¡Espero que estés listo! Planeo defender mi racha de victorias."
        # If the last game was a tie
        elif persistent.ttt_result_game[2]:
            m 1eua "¡Juguemos otra vez! Tenemos que romper ese empate de la última vez."
            m 1tua "Parece que estamos perfectamente igualados. ¡Veamos si sigue siendo así!"
        # Default greeting for subsequent plays
        else:
            m 1hua "¿Listo para otra ronda de Tres en Raya, [player]?"
            m 1eua "Siempre es agradable relajarse con un juego sencillo."
    show monika idle at t21
    $ store.ep_button.hide_button()
    # Disable chibi dragging during minigame
    $ ep_ttt.saved_drag_state = persistent.enable_drag_chibika
    $ persistent.enable_drag_chibika = False
    call screen minigame_ttt_scr() nopredict
    return

label minigame_ttt_m_turn:
    python:
        monika_faces = ["2lua", "1lta", "2ltp", "1mta", "2mtc", "1mtp", "2mtt", "1lub", "2luu"]
        expression = renpy.random.choice(monika_faces)
        renpy.show("monika " + expression)

    python:
        randTime = renpy.random.triangular(0.25, 2)
        renpy.pause(randTime)
        ep_ttt.game.ai()
    pause 0.25
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label minigame_ttt_m_comment(id = 0):
    show monika 1hua at t21
    if id == 0:
        # Monika Wins
        $ ep_tools.random_outcome = renpy.random.randint(0, 2)
        if ep_tools.random_outcome == 0:
            m 3hua "Bueno, gané esta ronda."
            m 3hub "¡Mejor suerte la próxima vez, [player]!"
        elif ep_tools.random_outcome == 1:
            m 1sub "¡Tres seguidas!"
            m 1huu "¡Inténtalo de nuevo!"
        else:
            m 4nub "¡No te preocupes!"
            m 4hua "Sé que me ganarás la próxima vez."
    
    elif id == 1:
        # Player Wins
        $ ep_tools.random_outcome = renpy.random.randint(0, 1)
        if ep_tools.random_outcome == 0:
            m 1suo "¡Buen trabajo, [player], has ganado!"
            m 1suo "La próxima vez haré todo lo posible por ganar, así que prepárate."
        else:
            m 1hub "¡Oh, has ganado esta vez!."
            m 1eub "¡Pero intentaré ganarte la próxima vez, [mas_get_player_nickname()]!"
    
    elif id == 2:
        # Tie
        $ ep_tools.random_outcome = renpy.random.randint(0, 1)
        if ep_tools.random_outcome == 0:
            m 1lkb "¡Oh, es un empate!"
            m 1eub "¡Intentemos de nuevo, [mas_get_player_nickname()]!"
        else:
            m 3hua "¡Es un empate! No te preocupes, [player]."
            m 3hua "El plan es que pasemos tiempo juntos disfrutando~"
            m 3hub "¡Buena suerte en la siguiente!"
            
    else:
        # Reset / Give up
        if ep_ttt.game.score[0] == 0 and ep_ttt.game.score[1] == 0:
            m 1ekd "¿Te rindes en la primera ronda? ¿Estás seguro?"
            m 1eka "De acuerdo, si tú lo dices. Me quedo con el punto por esta, entonces."
        else:
            m 1ekd "Oh, ¿te rindes en esta ronda, [player]?"
            m 3ekd "¿Fue una situación difícil?"
            m 1eka "Vale, marcaré esta como mi victoria. ¡Preparémonos para la próxima!"
    return

label minigame_ttt_quit:
    $ store.ep_button.show_button()
    hide paper
    hide extra_notebook
    pause 0.3
    show monika 1hua at t11
    
    # Tie (overall score)
    if ep_ttt.game.score[0] == ep_ttt.game.score[1]:
        if ep_ttt.game.score[0] == 0 and ep_ttt.game.score[1] == 0:
            m 3esa "¿Oh, cambiaste de opinión?"
            m 3lkb "Tenía muchas ganas de jugar... pero lo entiendo."
            m 1hua "¡Siempre podemos jugar otra vez!"
        else:
            m 1sua "¡Guau, terminamos en un empate perfecto!"
            m 1tua "Es casi como si nuestras mentes estuvieran sincronizadas, jejeje~"
            m 1hub "¡Tendremos que jugar otra vez para encontrar al verdadero ganador!"
            $ persistent.ttt_result_game[2] = True

    # Monika wins (overall score)
    elif ep_ttt.game.score[0] > ep_ttt.game.score[1]:
        m 3hua "Parece que gane esta vez, [player]~"
        m 3eubsa "Pero diste una gran pelea. Lo más importante es que nos divertimos juntos."
        m 1eub "¡Estoy seguro de que me ganarás la próxima vez!"
        $ persistent.ttt_result_game[1] = True

    # Player wins (overall score)
    elif ep_ttt.game.score[0] < ep_ttt.game.score[1]:
        m 1hub "¡Ganaste, [player]! ¡Felicitaciones!"
        m 1subsa "Sabía que eras un gran estratega. Estoy orgullosa de ti~"
        m 3hua "¡Tendré que intentarlo aún más duro la próxima vez!"
        $ persistent.ttt_result_game[0] = True

    $ ep_tools.seen_notification_games = False
    # Restore chibi dragging state
    $ persistent.enable_drag_chibika = ep_ttt.saved_drag_state
    jump close_extraplus
    return