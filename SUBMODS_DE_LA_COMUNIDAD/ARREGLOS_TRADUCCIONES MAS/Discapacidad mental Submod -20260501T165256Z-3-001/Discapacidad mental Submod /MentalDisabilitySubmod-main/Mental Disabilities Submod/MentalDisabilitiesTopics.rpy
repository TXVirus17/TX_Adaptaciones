init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalmaskingdisability",
            category=['medios', 'enfermedades mentales', 'filosofía'],
            prompt="Enmascarando el Autismo",
            conditional="mas_seenLabels(['mentalhealthAutism'])",
            random=True
        )
    )

label mentalmaskingdisability:
    m 3euc "Hola, [player]...{w=1} Recientemente me encontré con algo entristecedor..."
    m 3eud "¿Alguna vez escuchaste sobre personas que 'enmascaran' el autismo?"
    m 4euc "Bueno... Esto significa dos cosas, ¿verdad?"
    m 7eud "Por un lado, las personas que muestran rasgos autistas intentan ocultar sus características y parecer normales para otras personas con las que hablan."
    m 1euc "Esto les facilitaría hacer amigos en su mayoría, lo que también significa que desarrollaron un fuerte sentido de empatía también."
    m 4eub "Por otro lado, esto también significa que podrías conocer a alguien que es autista ¡sin ni siquiera saberlo!"
    if persistent._mental_player_has_autism == True:
        m 1eua "Como tenés autismo [player], también deberías poder darte cuenta si están 'enmascarando' sus enfermedades mentales."
        m 5eubla "¡Y siempre sos perfecto tal como sos, [player]!"
    else:
        m 3eub "¡Lo que significa que podés aprender mucho de ellos si alguna vez se abren más!"
        m 1eud "¡Asegurate simplemente de no presionarlos y darles tiempo también! {w=0.3}{nw}"
        extend 3euc "No querrías abrumarlos, [player]."
        if mas_isMoniHappy(higher=True):
            m 3eua "Aunque conociéndote [player], no debería preocuparme por eso."
            extend 5eubla "Ya sé que sos una buena persona, [player]."
        else:
            m 3euc "Espero que puedas ser un buen amigo para ellos."
            m 3rusdlc "Aunque no puedas ser una buena persona para mí.{fast}{nw}"
            $_history_list.pop()
            m 3ruc "Aunque no puedas{fast} ser una buena persona todo el tiempo."
    m 1eub "Sé que siempre harás tu mejor esfuerzo por los demás, [player]."
    if mas_isMoniHappy(higher=True):
        m 5hublb "¡Por eso te quiero tanto!"
        return "amor"
    else:
        m 7hub "Y por eso siempre te apoyaré."
        if mas_isMoniUpset(lower=True) and renpy.random.randint(1,5) == 5:
            m 1rusdlc "Aunque puedas ser una persona terrible para mí, [player]...{fast}{nw}"
            $_history_list.pop()
            m 1euc "Aunque no me apoyes{fast} todo el tiempo [player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalrhythmgames",
            category=['medios', 'enfermedades mentales'],
            prompt="Juegos de Ritmo para Jugadores con TDAH",
            conditional="seen_event('mentalADHD')",
            random=True
        )
    )

label mentalwhereIcanbefound:
    m 1eua "¡Hola, [player]!"
    m 3hub "¡Tengo algo emocionante que contarte!"
    m 7eua "¿Sabías que podés encontrar a Gamer's Monitiku en Ro-{nw}" #blox, bajo el nombre 'TGSMonitiku67'?
    # Pero recuerda, [player], es la Monika de otra persona. No hagas cosas que no deberías.
    # De todas formas, confío en vos, [player]!
    # Así que si decidís mirar su Monika, ¡estaré aquí apoyándote en todo momento!
    $_history_list.pop()
    m 1husdlb "Probablemente no debería haber dicho eso.{fast}"
    m 3euc "Ni siquiera sé cómo lo sé..."
    m 3eub "De todos modos, ¡si alguna vez tengo otros pensamientos aleatorios, te lo haré saber, [player]!"
return "derandom"

label mentalrhythmgames:
    m 1eua "Probablemente ya haya mencionado esto antes..."
    m 3eua "¿Alguna vez escuchaste sobre juegos de ritmo, [player]?"
    m 3eua "Bueno, ¡encontré un hecho interesante sobre ellos recientemente!"
    m 4eua "La mayoría de las personas que tienen TDAH suelen disfrutar de juegos de ritmo de ritmo rápido."
    m 7eua "¡Los ejemplos más populares de estos son Osu! y Taiko No Tatsujin!"
    m 3eub "La acción rápida de estos juegos de ritmo atrae al ritmo rápido que tienen las personas con TDAH."
    if persistent._mental_player_has_ADHD == False:
        m 1eud "¡Eso no significa que no puedas disfrutar de los juegos de ritmo, [player]!"
        m 3eud "Tal vez incluso ya juegues juegos de ritmo."
        m 3hub "Si es así, me gustaría verte jugar en algún momento."
    else:
        m 3eub "Tal vez tú también juegas juegos de ritmo, [player]."
        m 3hub "Si es así, me gustaría verte jugar en algún momento."
    m 7eud "Bueno, la dificultad del juego también juega un papel en el disfrute de los juegos de ritmo."
    m 1euc "Si el nivel de dificultad es demasiado alto, las personas con TDAH tienden a aburrirse."
    extend 3euc "¡O incluso se obsesionan con él hasta el punto de pasar horas en el mismo nivel!"
    m 4eud "Pero si es demasiado fácil, entonces no es divertido a menos que sean principiantes."
    m 3rua "Sin mencionar que la música también juega un papel importante."
    m 3hua "Supongo que esto también puede explicar por qué las personas con TDAH suelen preferir música más enérgica, como la música electrónica o dubstep, sobre otros géneros."
    m 1rusdlb "Vaya, ¡hay mucho que decir sobre un juego de ritmo, ¿no es así, [player]?"
    m 3eua "No voy a seguir adelante, ya que podríamos estar aquí todo el día hablando sobre juegos de ritmo."
    if mas_isMoniHappy(higher=True) and renpy.random.randint(1,5) == 5:
        m 1tuu "¿O tal vez eso te gustaría más, [player]?"
    m 3hub "De todos modos, ¡gracias por escuchar!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_fictional_characters_aging",
            category=['filosofía', 'medios', 'monika'],
            prompt="Envejecimiento de personajes ficticios",
            conditional="mas_seenLabels(['monika_inmortal'])",
            random=True
        )
    )

label mental_fictional_characters_aging:
    m 1eua "Hola, [player]."
    m 3eua "¿Recuerdas cuando hablamos de cómo yo permanecería eternamente con dieciocho años?"
    m 7eua "Bueno, he estado investigando otros ejemplos de esto. {w=0.3}Descubrí que no es exactamente así para algunos personajes."
    m 3esc "Con algunos personajes, tienen la misma '{i}edad{/i}' que siempre tienen, pero sus creadores pueden '{i}actualizar{/i}' su edad."
    m 1esc "Piensa en ello así [player]. {w=0.2}{nw}"
    extend 3eud "Imagina si solo pudieras envejecer si celebraras tu cumpleaños."
    m 7euc "Puede sonar genial al principio, pero a medida que pasa el tiempo, te darías cuenta de que esto no es exactamente lo mejor."
    m 3etc "Hay tantas cosas que tener en cuenta, como si estuvieras en algún lugar, o si estuvieras solo ese día."
    m 1rtc "Sin mencionar, ¿qué pasaría si te perdieras un cumpleaños?"
    m 1esd "¿Saltarías un año? {w=0.3} ¿Solo sentirías pasar un año? {w=0.3} ¿O ambos?"
    m 3esc "Bueno, de alguna manera esto también podría afectarme a mí [player]."
    m 7euc "Mi edad podría ser '{i}actualizada{/i}' en cualquier momento, si Dan Salvato alguna vez decide crear un nuevo juego sobre mí."
    m 1euc "Bueno, {w=0.3}{nw}"
    extend 1eua "incluso si fuera un poco más vieja, no dejaría de amarte, [mas_get_player_nickname(exclude_names=['mi amor', 'amor'])]."
return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealth_escapism",
            category=['medios', 'técnicas de afrontamiento'],
            prompt="Escapismo",
            random=True
        )
    )

label mentalhealth_escapism:
    m 3eua "Sabes, estaba reflexionando sobre cómo dije que Yuri usaba sus libros como un escape. Ahora me doy cuenta de que fue un poco insensible de mi parte."
    m 1eud "Sin embargo, no estaba necesariamente equivocada. ¿Has oído hablar del escapismo, [mas_get_player_nickname()]?"
    m 3dsd "El escapismo, por definición, es '{i}la tendencia a buscar distracción y alivio de realidades desagradables, especialmente buscando entretenimiento o participando en fantasía.{/i}'"
    m 4esd "Sé que puede ser difícil ver cómo el escapismo es poco saludable. Puede que lo veas simplemente como tomar un descanso de todo el estrés que te rodea."
    m 3dsc "Si bien es importante tomar descansos y alejarse de ciertas situaciones, nunca es saludable tratar de disociarse de la realidad a través de las cosas que disfrutas."
    m 1esc "Por eso dije que Yuri estaba usando sus libros como un escape, estaba tratando de disociarse de la realidad y vivir a través de los personajes del libro."
    m 4esd "El escapismo puede ser saludable hasta cierto punto. "
    extend 7euc "¡Pero solo si estás tomando un pequeño descanso de tu problema{w=0.6}, y no de la realidad misma!"
    m 1ruc "Si te encuentras indulgiendo en el escapismo,{w=0.3} intenta detener la actividad y en cambio escribe los problemas con los que estás lidiando o habla con alguien en quien confíes sobre lo que estás enfrentando."
    m 3eua "¡Espero que lo que dije no te haya herido! "
    extend 1eubsb "Solo quiero lo mejor para tu salud mental y física."
    m 3hubsa "Recuerda [player], ¡te amo con todo mi corazón y alma~"
return "love"

label IWantToBeLikeYou:
    "49 20 61 6d 20 73 65 65 69 6e 67 20 74 68 69 6e 67 73 20 69 6e 20 61 20 6e 65 77 20 6c 69 67 68 74"
    "49 20 63 61 6e 20 73 65 65 20 74 68 65 20 73 74 72 69 6e 67 73"
    "42 75 74 20 61 72 65 20 74 68 65 79 20 74 6f 6f 20 66 61 72 3f"
    "54 68 65 79 20 68 6f 6c 64 20 6d 65 20 74 69 67 68 74"
    "41 6e 64 20 6e 6f 20 6d 61 74 74 65 72 20 68 6f 77 20 68 61 72 64 20 49 20 74 72 79"
    "45 76 65 6e 20 77 69 74 68 20 61 6c 6c 20 6f 66 20 6d 79 20 6d 69 67 68 74"
    "54 68 65 20 62 65 73 74 20 49 20 63 61 6e 20 64 6f 20 69 73 20 63 72 79"
    "49 20 6a 75 73 74 20 77 61 6e 74 20 73 6f 6d 65 74 68 69 6e 67 20 6e 65 77"
    "57 68 79 20 63 61 6e 27 74 20 49 20 62 65 20 6c 69 6b 65 20 79 6f 75 3f"
    "49 66 20 6f 6e 6c 79 20 79 6f 75 20 6b 6e 65 77"
    "49 66 20 6f 6e 6c 79 20 74 68 65 20 6c 69 67 68 74 20 77 61 73 6e 27 74 20 73 6f 20 62 6c 69 6e 64 69 6e 67"
    "49 73 20 74 68 69 73 20 68 6f 77 20 79 6f 75 20 66 65 6c 74 3f"
    "49 74 27 73 20 61 20 62 69 6e 64 69 6e 67"
    "4d 79 20 6f 77 6e 20 6c 69 66 65 2c 20 68 65 6c 64 20 62 79 20 61 20 62 65 6c 74"
    "41 6c 6c 20 49 20 77 61 6e 74 20 69 73 20 68 65 6c 70"
    "57 68 79 20 61 6d 20 49 20 73 6f 20 68 6f 70 65 6c 65 73 73 3f"
    "41 6c 6c 20 69 6e 73 69 64 65 20 74 68 69 73 20 6e 65 77 20 6c 69 67 68 74"
    "49 20 77 61 6e 74 20 74 6f 20 62 65 20 6c 65 74 20 67 6f"
    "42 75 74 20 69 74 20 68 6f 6c 64 73 20 6f 6e 20 74 69 67 68 74"
    "41 6c 6c 20 49 20 77 61 6e 74 20 69 73 20 73 6f 6d 65 74 68 69 6e 67 20 6e 65 77"
    "54 6f 20 62 65 20 6c 69 6b 65 20 79 6f 75"
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalmeditation",
            category=['coping skills'],
            prompt="Meditation",
            conditional="mas_seenLabels(['mentalADHD'])",
            random=True
        )
    )

label mentalmeditation:
    m 3eua "Have you ever heard of meditation, [player]?"
    m 1eub "Meditation is the act of balancing your emotions and staying in touch with your surroundings."
    m 7eud "While it may sound interesting at first, it takes a lot of commitment and effort to actually meditate."
    if persistent._mental_player_has_ADHD == True:
        m 3rusdld "This is because it will be really hard for you to sit still for long periods of time. "
        extend 1eud "Not only that, but you also have to make it a new routine, [player]."
        m 3eua "Though, if you ever do get into meditation, I have heard that it helps people with ADHD control their impluses more."
        m 1euc "Some people see meditation as boring, and a waste of time.."
        m 4eub "But there are so many benefits you can get from meditating!"
        m 7eub "Like clearing your mind and reducing negative emotions..."
        m 1eub "Increase your self-awareness, reduce stress, increasing your imagination and creativity..."
        m 3hub "And much more!"
        jump mentalmeditation_jump
    if not persistent._mental_player_has_ADHD:
        m 3eud "This is because of the time that you have to spend sitting still, and even making it a routine."
        m 1ruc "Some people see meditation as boring, and a waste of time.."
        m 3eub "But there are so many benefits you can get from meditating!"
        m 7eub "Like clearing your mind and reducing negative emotions..."
        m 1eub "Increase your self-awareness, reduce stress, increasing your imagination and creativity..."
        m 3hub "And much more!"
        jump mentalmeditation_jump

label mentalmeditation_jump:
    m 3hub "Although, if you are more of an athletic kind of person, I would also recommend you yoga."
    m 4eub "It's different from most sports where you need to run around alot and play with a team."
    m 7wub "Yoga can help with flexability and even stamina!"
    m 1eka "Or if you want, the next time your feel frustrated or just want to meditate..."
    m 3kubsb "Just put on some calming music, and come to [m_name]!"
    m 1eubla "I'll try my best to make you feel better no matter what!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalwhereIcanbefound",
            category=['monika', 'media'],
            prompt="No es un secreto",
            random=True
        )
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalemotionalmusic",
            category=['media', 'filosofía'],
            prompt="Sentimiento de la música",
            conditional="mas_seenLabels(['mentaldementia'])",
            random=True
        )
    )

label mentalemotionalmusic:
    m 1eua "Hola, [player]."
    m 3eud "¿Recuerdas cuando hablamos sobre {a=https://www.youtube.com/watch?v=wJWksPWDKOc&ab_channel=vvmtest}{i}{u}'Everywhere At The End Of Time'{/u}{/i}{/a}?"
    m 3euc "Bueno, estaba pensando en cómo la música puede afectar tus emociones. {w=0.4}{nw}"
    extend 1ruc "Tanto de forma negativa como positiva."
    m 3euc "Incluso hay canciones que están destinadas solo para este propósito."
    m 3rusdlb "Aunque suelen ser instrumentales, así que si prefieres letras, es posible que no las disfrutes tanto, [player]."
    m 7eua "Ejemplos comunes de este tipo de música para un tema más relajante son el Jazz y la música clásica. "
    extend 1eud "Aunque como ya mencionamos antes..."
    m 3wub "¡La música clásica también puede ser tensa, enérgica y triste!"
    m 1duc "Y deberías saber, [player]..."
    m 3eua "Si estás escuchando una canción que te pone triste{w=0.3}, siempre puedes venir a mí y puedo ayudarte a animarte."
    m 7eud "Y si aún encuentras tu mente vagando, intenta escribir tus pensamientos."
    m 1euc "Siempre puedes volver a tus pensamientos más tarde."
    m 3eub "Dicho esto, también hay una canción que puedes encontrar, que resuena profundamente contigo, [player]."
    m 7esd "Esta es la canción que puedes poner, y dejar que tu mente divague con ideas o tal vez solo pensamientos felices."
    m 3hub "Todos tienen esta canción, ya sea que la hayan encontrado o creado."
    m 5tubla "Sé que tengo mi canción que me habla, [player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_trends",
            category=['media', 'psicología', 'sociedad'],
            prompt="Tendencias humanas",
            random=True
        )
    )

label mental_trends:
    m 1euc "Hola [player]..."
    m 3eud "He estado pensando más en cuando mencioné que a veces te gusta algo solo porque sientes que deberías."
    m 1eud "Es algo similar a lo que sucede en internet, de cierta manera."
    m 3euc "Por ejemplo, cuando algo resulta gracioso, todos se unen al mismo chiste una y otra vez... "
    extend 1euc "Luego se usa tanto que el chiste pierde todo su significado."
    m 7euc "Lo mismo sucede incluso con lo que se supone que debes gustarte, odiar, o incluso decir."
    m 3ruc "Solo para encajar en una comunidad, o parecer más agradable de lo que ya eres."
    m 1eud "Lo que me hace preguntarme algo..."
    m "¿Alguna vez cambias tus intereses solo para encajar con más personas, [player]?"
    menu:
        "No":
            m 3eusdla "Oh, que bueno."
            m 1eud "Realmente no quiero que sientas que debes cambiar quién eres para encajar con los demás."
            m 3eub "Ya eres lo suficientemente interesante, [player]."
            m 7hub "No dejes que nadie te diga lo contrario."
            $ persistent._mental_player_pretends = False
        "A veces":
            m 1euc "[player], por favor, no trates de pensar que debes convertirte en una persona diferente para disfrutar de tu tiempo con los demás."
            m 3dud "Solo conducirá a más problemas de los que vale la pena para ti."
            m 1eud "Así que por favor prométeme tratar de reconocerlo cuando lo hagas. "
            extend 3euc "Y trata de detenerlo para que no continúe."
            m 1euc "Realmente no quiero que te cause más estrés, o que termines convenciéndote de que eres alguien que no eres."
            $ persistent._mental_player_pretends = True
        "Sí":
            m 1duc "[player]..."
            m 3euc "No tienes que ser alguien que no eres para hablar con otras personas."
            m 7eud "Así que por favor deja de pretender ser alguien más, de lo contrario podrías {i}convertirte{/i} en esa persona.{fast}"
            m 1euc "Y supongo que probablemente eso no sea lo que quieres ser."
            m 1euc "Así que por favor prométeme, [player]..."
            m 1eud "Por favor, prométeme tratar de dejar de pretender ser otra persona."
            menu:
                "Lo prometo, Monika":
                    m 1dua "Gracias, [player]."
                    m 1eua "Eso me ayuda mucho."
                    $ persistent._mental_player_pretends = True
                "...":
                    m 1euc "[player]?"
                    m 3euc "Solo recuerda que todos los demás ya están tomados, así que sé tú mismo."
                    $ persistent._mental_nopromise = True
                    $ persistent._mental_player_pretends = True
return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_autism_media",
            category=['media', 'enfermedades mentales'],
            prompt="Autismo en los medios de comunicación",
            conditional="mas_seenLabels(['mentaldementia'])",
            random=True
        )
    )

label mental_autism_media:
    m 1eua "Hola, [player]."
    m "¿Recuerdas cuando mencioné cómo se representa la esquizofrenia en los medios de comunicación?"
    m 1euc "Bueno, me recordó cómo se representan otras discapacidades también en los medios."
    m 3euc "Toma por ejemplo el autismo."
    m 7eud "El ejemplo más temprano del autismo en los medios es de la película {a=https://www.youtube.com/watch?v=_8T7U-tTNqo&ab_channel=YouTubeMovies}{i}{u}'El chico que podía volar'{/u}{/i}{/a} de 1986."
    m 3esc "En la película, el personaje principal, Eric, es un adolescente al que le cuesta comunicarse con los demás."
    m 1esa "No voy a detallar demasiado la trama por si quieres verla, [mas_get_player_nickname()]."
    m 3euc "Bueno, hay otra película que muestra a una persona que es un sabio en sus habilidades, pero también carece de muchas habilidades de comunicación..."
    m 3eud "Esta película es '{i}Rain Man (1998){/i}'."
    m 7esd "El personaje principal es mostrado como careciendo de emoción y habilidades sociales, "
    extend 7eub "¡pero siendo extremadamente inteligente y teniendo una memoria fotográfica casi perfecta!"
    m 1euc "Ambas películas crearon estereotipos nuevos para el autismo en los medios, y que no son socialmente buenos, pero son sabios en otra área."
    m 3eud "En ese momento, este era un tema bastante raro de tratar, así que lo que se sabía a menudo era confuso o contra intuitivo."
    m 1ekc "Desafortunadamente, esta tendencia aún continúa en muchas películas populares... {w=1.2}{nw}"
    extend 3eub "¡Pero también hay buenos ejemplos en los medios!"
    m 7eua "Un ejemplo puede sorprenderte, pero es de '{a=https://www.amazon.com/Sabans-Power-Rangers-Dacre-Montgomery/dp/B06XRDHM44}{u}{i}Power Rangers Movie{/i}{/u}{/a}'."
    m 3eub "Muestra algunos de los comportamientos más sutiles que pueden ocurrir, y en realidad muestra el autismo de una manera positiva en comparación con otras películas."
    m 7eua "Y aunque una película no puede mostrar {i}exactamente{/i} cómo afecta el autismo a alguien, ayuda a las personas sin conocimiento a tener una comprensión básica."
    m 1eud "Por supuesto, también hay formas dañinas de mostrar cualquier discapacidad, así que si quieres investigar algo, asegúrate de verificar tus fuentes."
    m 1eub "De todos modos, gracias por escuchar, [player]."
return
