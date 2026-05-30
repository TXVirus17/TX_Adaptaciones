#===========================================================================================
# MINIGAME#3(EN REVISIÓN): ROCK PAPER SCISSORS
#===========================================================================================
#====Rock Paper Scissors
default persistent.psr_result_game = [False, False, False] #Player, Monika and Tie. Quit [FFF]
default persistent.rps_player_history = []

screen RPS_mg():
    #Shows the Rock-Paper-Scissors minigame interface, with buttons for each choice and a quit button.
    zorder 50
    timer store.ep_tools.games_idle_timer action Function(store.ep_tools.show_idle_notification, context="rps") repeat True

    # Monika's card back
    imagebutton idle "extra_card_back":
        action NullAction()
        xalign 0.7
        yalign 0.1

    # Player's choices
    $ x_positions = [0.5, 0.7, 0.9]
    for i, choice in enumerate(ep_rps.choices):
        imagebutton:
            idle choice.image
            hover choice.image at hover_card
            action [SetField(ep_rps, "your_choice", choice.value), Hide("RPS_mg"), Jump("rps_loop")]
            xalign x_positions[i]
            yalign 0.7

    # Quit button
    vbox:
        xpos 0.86
        yanchor 1.0
        ypos 0.950
        textbutton _("Salir") style "hkb_button" action Jump("rps_quit")

init python in ep_rps:
    import store
    
    class RPSChoice(object):
        """
        Represents a single choice in the Rock, Paper, Scissors game.
        """
        def __init__(self, name, value, image, beats):
            """
            Initializes a new RPSChoice.

            Args:
                name (str): The display name of the choice (e.g., "Rock").
                value (int): The numerical identifier for the choice (1: Rock, 2: Paper, 3: Scissors).
                image (str): The name of the image displayable for this choice.
                beats (int): The numerical value of the choice that this one beats.
            """
            self.name = name
            self.value = value
            self.image = image
            self.beats = beats

    your_choice = 0
    player_wins = 0
    moni_wins = 0
    choices = [RPSChoice("Rock", 1, "extra_rock", 3), RPSChoice("Paper", 2, "extra_paper", 1), RPSChoice("Scissors", 3, "extra_scissors", 2)]

    # Lookup dictionary for counter moves: key = move to beat, value = move that beats it
    # Rock(1) is beaten by Paper(2), Paper(2) is beaten by Scissors(3), Scissors(3) is beaten by Rock(1)
    counter_lookup = {1: 2, 2: 3, 3: 1}

    def getMonikaChoice():
        """
        Determines Monika's choice based on the player's history.
        """
        history = store.persistent.rps_player_history
        history_len = len(history)  # Cache length to avoid multiple calls
        
        # If there's not much history, or with a 30% chance, play randomly.
        if history_len < 3 or renpy.random.randint(1, 100) <= 30:
            return renpy.random.randint(1, 3)

        # --- AI Logic ---
        
        # 1. Frequency Analysis: What is the player's most common move?
        # We count how many times the player has chosen each option.
        rock_count = history.count(1)
        paper_count = history.count(2)
        scissors_count = history.count(3)

        # Find the most frequent move.
        player_most_frequent_move = 0
        max_count = -1
        if rock_count > max_count:
            max_count = rock_count
            player_most_frequent_move = 1
        if paper_count > max_count: # Use 'if' instead of 'elif' to handle ties, defaulting to the last one checked.
            max_count = paper_count
            player_most_frequent_move = 2
        if scissors_count > max_count:
            max_count = scissors_count
            player_most_frequent_move = 3

        # Monika chooses the counter to the player's most frequent move using lookup
        counter_move = counter_lookup[player_most_frequent_move]


        # 2. Anti-Repetition Pattern: If the player repeated their last move, they are less likely to repeat it a third time.
        # For example, if they played Rock, Rock, they are now more likely to play Paper or Scissors.
        # Monika can play Scissors, which beats Paper and ties with Scissors, making it a safe bet.
        if history_len >= 2 and history[-1] == history[-2]:
            last_move = history[-1]
            # The move that beats the player's last move.
            move_that_beats_player = counter_lookup[last_move]
            # Monika chooses the move that beats 'move_that_beats_player'.
            # This is a strategy to cover the player's two most likely options.
            smart_bet = counter_lookup[move_that_beats_player]
            # There's a 50% chance she'll use this strategy instead of the frequency analysis.
            if renpy.random.randint(1, 2) == 1:
                return smart_bet
        
        # Fallback to the counter move if the anti-repetition logic wasn't used
        return counter_move

label minigame_rps:
    $ mas_MUMURaiseShield()
    show extra_card_back zorder 12:
        xalign 0.7
        yalign 0.1
        yoffset -900
        easein 0.5 yoffset 0
    show extra_rock zorder 12:
        xalign 0.5
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.1
    show extra_paper zorder 12:
        xalign 0.7
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.2
    show extra_scissors zorder 12:
        xalign 0.9
        yalign 0.7
        yoffset 900
        easein 0.5 yoffset 0
    pause 0.3

    # Very first time playing
    if not renpy.seen_label("checkpoint_minigame_rps") and not renpy.seen_label("rps_quit"):
        m 1hua "¡Piedra, papel o tijera, [player]! ¿Listo para probar suerte?"
        m 1eua "Veamos a quién favorece el destino hoy. ¡Buena suerte!"
        m 1eub "¡Veamos a quién favorece el destino hoy! ¡Buena suerte!"

label checkpoint_minigame_rps:
    if renpy.seen_label("rps_quit"):
        # If the player won the last game
        if persistent.psr_result_game[0]:
            m 3eub "¿Listo para la revancha, [player]? He estado pensando en mi estrategia. Jejeje~"
            m 3hua "¡Esta vez no te lo pondré tan fácil!"
        # If Monika won the last game
        elif persistent.psr_result_game[1]:
            m 1hub "¿Estás listo para desafiar al campeón de nuevo?"
            m 1hua "¡Espero que estés listo! Tengo planeado mantener mi racha de victorias."
        # If the last game was a tie
        elif persistent.psr_result_game[2]:
            m 1eua "¡Juguemos otra vez! Tenemos que romper ese empate de la última vez."
            m 1tua "Parece que estamos perfectamente sincronizados. ¡Veamos si eso todavía es cierto!"
        # Default greeting for subsequent plays
        else:
            m 1hua "¿Listo para otra ronda de Piedra, Papel o Tijera, [player]?"
            m 1eua "Siempre es bueno relajarse con un juego simple."

    hide extra_card_back
    hide extra_rock
    hide extra_paper
    hide extra_scissors
    # Disable chibi dragging during minigame
    $ ep_rps.saved_drag_state = persistent.enable_drag_chibika
    $ persistent.enable_drag_chibika = False
    show screen score_minigame(game="rps")
    show monika idle at t21
    call screen RPS_mg nopredict
    return

label rps_loop:
    # Limit history to last 100 moves to prevent save file bloat
    # Only append valid choices (1=Rock, 2=Paper, 3=Scissors)
    if ep_rps.your_choice in (1, 2, 3):
        $ persistent.rps_player_history.append(ep_rps.your_choice)
        if len(persistent.rps_player_history) > 100:
            $ persistent.rps_player_history = persistent.rps_player_history[-100:]
    $ monika_choice_val = ep_rps.getMonikaChoice()
    $ renpy.restart_interaction()
    $ player_choice = ep_rps.choices[ep_rps.your_choice - 1]
    $ monika_choice = ep_rps.choices[monika_choice_val - 1]

    # Show player's and Monika's choices
    show extra_card_back as monika_card_back zorder 12:
        xalign 0.7
        yalign 0.1

    # Show all choices at their default positions
    show extra_rock zorder 12:
        xalign 0.5 yalign 0.7
    show extra_paper zorder 12:
        xalign 0.7 yalign 0.7
    show extra_scissors zorder 12:
        xalign 0.9 yalign 0.7

    # Adjust yoffset for player's choice
    if player_choice.value == 1: # Rock
        show extra_rock:
            yoffset -20
    elif player_choice.value == 2: # Paper
        show extra_paper:
            yoffset -20
    elif player_choice.value == 3: # Scissors
        show extra_scissors:
            yoffset -20

    m 1eub "Piedra,{w=0.3} Papel,{w=0.3} Tijera{w=0.3}!{nw}"
    hide monika_card_back with dissolve

    # Show Monika's choice
    show expression monika_choice.image as monika_choice_display zorder 12 with dissolve:
        xalign 0.7
        yalign 0.1

    # Determine winner and show dialogue
    if monika_choice.value == player_choice.value:
        # Tie
        if player_choice.value == 1: # Rock
            m 3hub "¡Piedra contra piedra! ¡Jajaja!"
            m 1hua "Es un empate."
        elif player_choice.value == 2: # Paper
            m 1eub "¡Elegimos papel!"
            m 1tua "¡Estamos empatados! Deberías dejar de leer mi mente, [mas_get_player_nickname()]~"
            m 1hub "Jajaja~"
        elif player_choice.value == 3: # Scissors
            m 2hkb "¡Dos pares de tijeras hacen un empate, [player]!"
            m 2hub "Es divertido que pensáramos en lo mismo, Jejeje~"

    elif player_choice.beats == monika_choice.value:
        # Player wins
        $ ep_rps.player_wins += 1
        if player_choice.value == 1: # Rock vs Scissors
            m 1hksdrb "¡Piedra rompe tijeras!"
            m 1hua "Me venciste, [player]!"
        elif player_choice.value == 2: # Paper vs Rock
            m 1lkb "¡Papel cubre piedra!"
            m 1lub "Ganaste, [player]."
        elif player_choice.value == 3: # Scissors vs Paper
            m 1hssdrb "¡Tijeras cortan papel!"
            m 1eua "¡La victoria es tuya!"

    else:
        # Monika wins
        $ ep_rps.moni_wins += 1
        if monika_choice.value == 1: # Rock vs Scissors (Player)
            m 1mub "Adiós a tus tijeras, [player]~"
            m 1mub "¡No pudiste vencerme! ¡Jajaja~!"
        elif monika_choice.value == 2: # Paper vs Rock (Player)
            m 1dub "¡Papel cubre piedra!"
            m 1tub "Lo siento [player], perdiste esta vez!"
        elif monika_choice.value == 3: # Scissors vs Paper (Player)
            m 3eub "¡Tijeras cortan papel!"
            m 3hua "Lo siento, [player], perdiste."

    hide monika_choice_display
    show monika idle at t21
    $ ep_rps.your_choice = 0
    jump hide_images_rps
    return

label rps_quit:
    $ mas_MUMUDropShield()
    hide screen score_minigame
    
    show extra_card_back zorder 12:
        xalign 0.7 yalign 0.1
    show extra_rock zorder 12:
        xalign 0.5 yalign 0.7
    show extra_paper zorder 12:
        xalign 0.7 yalign 0.7
    show extra_scissors zorder 12:
        xalign 0.9 yalign 0.7
    
    show extra_card_back:
        easeout 0.6 yoffset -1300
    show extra_rock:
        easeout 0.6 yoffset 1300
    pause 0.1
    
    show extra_paper:
        easeout 0.6 yoffset 1300
    pause 0.2
    
    show extra_scissors:
        easeout 0.6 yoffset 1300
    pause 0.3
    
    hide extra_card_back
    hide extra_rock
    hide extra_paper
    hide extra_scissors
    
    $ ep_rps.your_choice = 0
    jump rps_result
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label rps_result:
    show monika idle at t11
    #Tie
    if ep_rps.moni_wins == ep_rps.player_wins:
        if ep_rps.moni_wins == 0 and ep_rps.player_wins == 0:
            m 1etd "¿No quieres jugar?jnjm "
            m 1eka "Pensé que querías jugar conmigo desde hace un rato..."
            m 3hua "Pero no te preocupes, entiendo si cambias de opinión."
            m 3hub "¡Espero que podamos jugar otra vez!"
            python:
                ep_rps.moni_wins = 0
                ep_rps.player_wins = 0
        else:
            m 1sua "¡Vaya, empate!"
            m 1tua "¡Debe ser porque estamos muy sincronizados!"
            m 1hub "Jejeje~"
            m 3hua "Pero tenemos que romper el empate tarde o temprano, [player]."
            m 3hub "Ya veremos quién gana la próxima vez, ¡buena suerte!"
            $ persistent.psr_result_game[2] = True

    #Monika wins
    elif ep_rps.moni_wins > ep_rps.player_wins:
        m 3eub "Esta vez gané, [player]~"
        m 3hub "Diste una buena pelea."
        m 3eub "Supongo que tuve suerte."
        m 3eubsa "Pero no te preocupes, lo que más me importa es que ambos nos divirtamos."
        m 1hub "Sé que me ganarás la próxima vez, ¡creo en ti!"
        $ persistent.psr_result_game[1] = True

    #Player wins
    elif ep_rps.moni_wins < ep_rps.player_wins:
        m 1hub "Me ganaste, [player], ¡felicidades!"
        m 1hub "Estoy orgullosa de ti~"
        m 2tub "Pero ten cuidado, la próxima vez intentaré leer tu mente."
        m 2hub "¡Puede que gane!"
        m 2hua "Así que ten cuidado cuando juguemos otra vez."
        m 2hua "Jejeje~"
        $ persistent.psr_result_game[0] = True
        
    python:
        ep_rps.moni_wins = 0
        ep_rps.player_wins = 0
        # Restore chibi dragging state
        persistent.enable_drag_chibika = ep_rps.saved_drag_state
    jump close_extraplus
    return