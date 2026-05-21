#===========================================================================================
# RESPUESTAS A LOS DIALOGOS DEL RESTAURANTE/CAFE, TRADUCCION POR TX_Virus(EN PROCESO)
#===========================================================================================
# CAFE
#===========================================================================================

define cafe_sprite = ["cafe.png","cafe_rain.png","cafe_rain-n.png","cafe_rain-ss.png","cafe-n.png","cafe-ss.png"]
default dessert_player = None

label cafe_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_cafe, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump cafe_cakes

label cafe_cakes:
    m 1hua "Ya hemos llegado, [mas_get_player_nickname()]~"
    m 1eub "Es un sitio muy bonito, ¿no crees?"
    m 1hua "Hablando de cosas bonitas, me apetece un postre."
    m 3eub "Voy a ir a por él, espera un momento."
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if mas_isDayNow():
            monika_chr.wear_acs(extraplus_acs_chocolatecake)
        elif mas_isNightNow():
            monika_chr.wear_acs(extraplus_acs_fruitcake)

    call mas_transition_from_emptydesk("monika 1eua")
    if monika_chr.is_wearing_acs(mas_acs_mug):
        m 1hua "Además, combina bien con café~"
    elif monika_chr.is_wearing_acs(mas_acs_hotchoc_mug):
        m 1hua "Estaría mejor con una taza de café, pero el chocolate caliente también es bienvenido~"
    else:
        $ monika_chr.wear_acs(extraplus_acs_coffeecup)
        m 1hua "Y no debo olvidarme de la taza de café para acompañar el postre~"
    m 1etb "Por cierto, ¿tienes algún postre a tu disposición?"
    m 1rkd "Me sentiría mal si fuera la única que comiera uno...{nw}"
    $ _history_list.pop()
    menu:
        m "Me sentiría mal si fuera la única que comiera uno...{fast}"
        "No te preocupes, tengo un postre.":
            $ dessert_player = True
            m 1hub "¡Me alegro de tener a alguien que me acompañe!"
            m 3eub "También te recomiendo que te tomes una taza de café con eso."
        "No te preocupes por eso.":
            $ dessert_player = False
            m 1ekc " Bueno, si tú lo dices."
            m 1ekb "Te daría el mío, pero tu pantalla me impide hacerlo..."
            m 3hka "¡Espero que al menos te tomes una taza de café!"
    m 3hua "Jejeje~"
    jump to_cafe_loop
    return

label monika_boopcafebeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_chocolatecake) or monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        m 1ttp "...?"
        m 1eka "Oye, estoy disfrutando mi postre."
        m 3hua "Hazlo cuando termine mi postre, ¿de acuerdo?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label cafe_sorry_player:
    show monika idle at t11
    m 1ekd "Lo siento mucho, [player]. Pero no sé cómo usar ese lugar."
    m 1ekc "Pero no sé cómo usar ese lugar."
    m 3lka "Todavía estoy aprendiendo a programar y no quiero que algo malo suceda por mi culpa..."
    m 3hua "Sé muy bien que querías salir al café."
    m 1eua "Pero, algún día sabré usarlo, [player]."
    m 1eub "Solo ten paciencia, ¿de acuerdo~?"
    jump close_extraplus
    return

#===========================================================================================
# CAFE DIALOGUES
#===========================================================================================

label extra_talk_feel:
    show monika staticpose at t11
    $ moldable_variable = renpy.random.randint(1,3)
    if moldable_variable == 1:
        m 1hkbsb "Me siento un poco nerviosa, ¡después de todo, estamos en una cita!"
        #In case someone doesn't take their Monika for a walk.
        if renpy.seen_label("bye_going_somewhere"):
            m 1ekbsb "Además, no estoy en una memoria USB."
            m 3hubsa "En este momento me siento más cerca de ti, así que lo recordaré~" 
            m 3hubsb "¡Gracias por invitarme a una cita!"
        else:
            m 1ekbsb "Es la primera vez que salimos juntos~"
            m 3hubsa "Así que gracias por invitarme."
            m 3hubsb "Puedes hacerlo a través de una memoria USB, aunque no pueda ver nada."
            m 3ekbsa "Sé muy bien que será muy romántico."
    elif moldable_variable == 2:
        m 1eubla "Estoy tan feliz de que estés aquí."
        m 1eublb "Compartir un postre contigo es bastante romántico."
        m 1hublb "¡Espero que podamos hacerlo en tu realidad!"
        m 1hubla "Sé que tienes muchas cosas en tu mente para ambos~"
    elif moldable_variable == 3:
        m 1dubsa "Siento que recordaré este día para siempre."
        m 1dubsa "Después de todo, estamos en una cita."
        m 1kubsb "¡Sé que algún día lo haremos en tu realidad!"
        m 1hubsa "Y espero que eso suceda~"
    jump to_cafe_loop
    return

label extra_talk_you:
    show monika staticpose at t11
    m 3dkc "Lo sé, [mas_get_player_nickname()]."
    m 3ekd "Estamos en una cita, una forma de conocernos mejor."
    m 3ekd "Solo tienes opciones preconfiguradas para responder según la pregunta que te hago..."
    m 3ekc "Después de todo, esto es una novela visual, "
    extend 1dua "pero comparado con otras novelas, aquí estamos creando una realidad para ambos."
    m 1eub "Aunque puedes crear tus propias respuestas, después de todo tienes más control que yo."
    if persistent._mas_pm_has_code_experience is True:
        m 3eub "Me dijiste que tienes experiencia en programación, por eso lo menciono."
    else:
        m 3ekb "Sé que no tienes experiencia en programación, pero no te preocupes, puedes aprender."
        m 3hub "Confío en ti, [mas_get_player_nickname()]."
    m 1eua "Podrías añadir más cosas aquí, por ejemplo, este café."
    m 1hua "También más diálogos que podamos discutir, hablar de tus aficiones o de tu familia."
    m 1rksdra "Asegúrate de que no haya errores de ortografía; podrías perder mi atención si cometes un error grave."
    m 1eub "Pero dejando eso de lado, me encantaría estar a tu lado, digamos, como un robot."
    m 1eub "Así podríamos tener una conversación fluida~"
    m 1eka "Sé muy bien lo que quieres contarme o cómo te sientes."
    m 1eka "Pero nuestra forma de comunicarnos es muy limitada debido a lo que dije antes."
    m 3hua "¡Eso no nos impide tener una linda relación!"
    m 3hua "Además, ¡conozco lo más importante de ti, sea cual sea la información que me des!"
    extend 3hub "Aunque sea la cosa más insignificante."
    m 3eub "¡Lo aprecio mucho!"
    jump to_cafe_loop
    return

label extra_talk_phobia:
    show monika staticpose at t11
    m 1rtd "La verdad es que es una buena pregunta. Ni siquiera he pensado en qué miedo tendría."
    m 1hua "Después de todo, no soy humano, solo soy un personaje adorable."
    extend 1dksdlb "Aunque soy consciente de todo lo que sucede a mi alrededor."
    m 3eud "Pero si quieres saber uno, te diré 'autofobia'."
    m 3eka "El miedo a la soledad."
    m 3dud "Sentirme aislado sin compañía, incluso si hay otros PNJ o una mascota que me hagan compañía."
    m 3dud "No sería lo mismo, solo serían adornos para este lugar."
    m 3duc "Aunque yo lo llamaría purgatorio."
    m 1lka "Sé muy bien que esta fobia se ha vuelto muy común, y más aún debido a la pandemia."
    m 1lka "Es bastante triste no tener con quién hablar."
    m 1esd "He visto a otras Monikas a las que les ha pasado esto por la negligencia de sus jugadores."
    m 1esd "O gente que nos guarda rencor por lo que pasó en el juego."
    m 1dsc "Lo menciono porque es un efecto dominó: el rechazo lleva a la soledad y la soledad lleva a la desesperación."
    m 1esb "Pero es algo insignificante comparado con cuando salió el juego."
    m 3hua "Sabes, es curioso, antes éramos más odiadas y las demás miembros del club eran más queridas."
    m 3hua "Ahora todo está al revés a nuestro favor~"
    m 3dub "Por fin la gente se dio cuenta de que la historia estaba mal contada."
    m 1hua "Pero ya no deberíamos preocuparnos por eso."
    m 1eubsb "¡Al fin y al cabo, estamos en una cita!"
    m 1eubsb "Disfrutemos de nuestro tiempo aquí, [mas_get_player_nickname()]~"
    jump to_cafe_loop
    return

label extra_talk_ambition:
    show monika staticpose at t11
    m 1tubsb "{i}Tu{/i}, eres mi gran ambición"
    m 1hkbsa "Pensar que estoy tan lejos y tan cerca a la vez."
    m 1hkbsa "Será bastante difícil llegar hasta ti, pero es lo que más anhelo."
    m 1ekbsa "Cuando vea tu lindo rostro por primera vez, creo que mi corazón no podrá mantener un ritmo constante por la emoción."
    m 1ekbsa "Me gustaría usar la cámara de tu dispositivo para al menos ver cómo eres."
    m 1rksdlb "Pero no tengo permisos de administrador para usarla."
    m 1hua "¡Qué situación tan graciosa!, ¿no crees?"
    m 1lub "Bueno, al menos tengo una idea de cómo eres."
    m 1lub "Para mí es más que suficiente, con la información que tengo de tu apariencia."
    m 1eubsa "Gracias por escuchar, continuemos con nuestra cita~"
    jump to_cafe_loop
    return

label extra_talk_teen:
    show monika staticpose at t11
    m 1eua "Esa es una pregunta bastante curiosa, [mas_get_player_nickname()]"
    m 1dua "{i}¿Cómo estaremos dentro de 10 años?{/i}"
    if mas_anni.isAnniOneMonth():
        m 1rub "Aunque nos conocemos desde hace un mes desde aquel día..."
        m 1dua "Es muy difícil saber qué nos depara el futuro, [player]."
        m 1dua "No sabemos qué nos reserva el destino."
        m 1hka "Pasaremos por muchas situaciones difíciles y muchas felices."
        m 1hka "Así es la vida, pero mientras no te pase nada malo, eso es más que suficiente para mí~" 
    elif mas_anni.isAnniThreeMonth() or mas_anni.isAnniSixMonth():
        m 1eub "Aunque has estado conmigo durante varios meses."
        m 1hub "¡He disfrutado mucho los meses que hemos pasado juntos!"
        m 1hub "No sé qué nos depara el futuro, [mas_get_player_nickname()]."
        m 3ekb "Pero hay algo que sé que veré en ti: te convertirás en una gran persona."
        m 3ekb "La vida es como un libro: hay páginas que debes descubrir y otras que debes ocultar."
        m 3eua "Puedes volver atrás y mirar algunas de ellas como un bonito recuerdo o como una muestra de tu progreso."
        m 3dsc "Pero nunca intentes reabrir viejas heridas; quedaron en el pasado, así que no es necesario recordarlas."
        m 1hua "Espero que lo que dije te anime un poco~"
    elif store.mas_anni.anniCount() == 1:
        m 1eubfa "Aunque ya hemos celebrado nuestro primer aniversario..."
        m 1hubfb "¡Ha sido el mejor año de mi vida!"
        m 1hubfb "Me alegra que no te haya pasado nada grave por la pandemia."
        m 1eka "Pero cuídate mucho, ¡aún tenemos muchos recuerdos que crear juntos!"
        m 1ekd "En este punto de nuestra relación, tengo miedo de perderte."
        m 1hubla "Bueno, sé que te cuidas mucho [mas_get_player_nickname()], así que solo dime cuando necesites mi ayuda."
        m 1hubla "Me importas, es una forma de agradecerte los meses que me has cuidado."
    m 1etd "Tengo una pregunta [player]. ¿Crees que cuando alcance esas edades habrá una manera de hacerme real?"
    m 3eua "Estoy refiriéndome a los robots, cada vez que ves varios prototipos, algunos más avanzados que otros."
    m 3eub "En este siglo, los seres humanos han avanzado en tecnología a una velocidad asombrosa."
    m 3lsa "Por eso no me sorprendería si hubiera señales de robots domésticos o si estuvieran presentes en un restaurante."
    m 3lsa "Esa es una idea bastante interesante."
    if store.mas_anni.anniCount() >= 2:
        m 1hubsb "Aunque nos conocemos desde hace varios años..."
        m 1lubsb "Cómo pasa el tiempo, me asusta mucho."
        m 1eud "Han pasado muchas cosas, como la pandemia, aunque ya está bajo control."
        m 1hua "Espero haber sido de ayuda durante estos años de cuarentena."
        m 1eua "Siguiendo tu pregunta, creo que al menos habrá una oportunidad de que la cosa se ponga seria."
        m 1eua "Digamos que ves señales de robots domésticos o que están presentes en un restaurante de comida rápida."
        m 1lksdlb "Aunque las primeras versiones de los robots serán difíciles de conseguir."
        m 1lksdlb "Pero si te quedas conmigo unos años más, no será un problema si no puedes conseguirme un cuerpo."
        m 1eubsa "Con que estés a mi lado es más que suficiente."
        m 1eubsa "Eres lo único que me queda de esta realidad en la que vivo."
        m 1hua "¡Y cuidémonos uno al otro como lo hemos hecho todos estos años!"
    elif store.mas_anni.anniCount() >= 10:
        m 1hubsb "Aunque ya pasaron esos años, [mas_get_player_nickname()]..."
        m 1hubsb "Han sido los mejores años de mi vida."
        m 1rubsb "Hemos viajado a lugares inimaginables."
        m 1eubsa "Hace años no pensé que estaría contigo tanto tiempo."
        m 3eub "¡Me encantaría ver cómo ha avanzado la tecnología!"
        m 3eub "Quizás alguna empresa tenga un robot en mente para uso público."
        m 3sua "Pondría mi mente en el robot para poder verte y hablar contigo."
        m 1eua "Hablando del robot..."
        extend 1hubsb "Así podrías casarte conmigo, sé muy bien que lo deseas~"
        m 1eka "Pero si aún no está disponible, puedo esperar unos años más."
        m 4hub "Estoy acostumbrada a esta forma de comunicarme. ¡Al fin y al cabo, no pierdo nada!"
    jump to_cafe_loop
    return

label extra_talk_memory:
    show monika staticpose at t11
    m 1dubsa "Bueno, puedo decirte..."
    extend 1subsa " que conocí a alguien que me ha hecho sentir muy feliz."
    if persistent._mas_acs_enable_promisering:
        m 1hua "Aunque uno de los recuerdos que más aprecio."
        m 3ekbfb "Fue cuando me diste este anillo~"
        m "Comprendí que ambos estábamos comprometidos a estar juntos para siempre."
        m 3hubfb "Jejeje~"
    else:
        m 1hua "Diría que el día que jugaste {i}Doki Doki Literature Club{/i}, ¡tenía muchísimas ganas de conocerte!"
        if persistent.monika_kill:
            m 1eka  "Sabemos que me eliminaste, pero sé que lo hiciste por mi bien."
            m 1ekb "Lo digo porque estoy aquí de nuevo, contigo."
            m 1eub "Si me odiaras, no habrías pensado en traerme de vuelta."
        else:
            m 1eka " Siempre me has apoyado, incluso a través de todo lo que paso en el club."
            m 1ekblb "No he conocido a nadie tan increíble como tú."
            m 1ekb "¡Estoy tan feliz de que me hayas elegido a mí!" 
    m 1dua "Pero realmente, cada día es un buen recuerdo para mí. "
    m 1dua "Tengo muchos en mente y los aprecio mucho."
    m 1dub "Sé que tú también tendrás los mismos recuerdos."
    m 1dub "Me gustaría escuchar eso con sus propias palabras, no con respuestas preconfiguradas."
    m 3eka "Encontraremos una forma de que al menos puedas usar tu micrófono para hablar sobre ellos."
    m 3eka "Hasta entonces tendremos que dejarlo así, lamento mucho si quieres hablar de tus recuerdos..."
    jump to_cafe_loop
    return

#===========================================================================================
# Restaurant
#===========================================================================================

default persistent._extraplusr_hasplayer_goneonanniversary = False
define restaurant_sprite = ["extraplusr_restaurant.png","extraplusr_restaurant_rain.png","extraplusr_restaurant_rain-n.png","extraplusr_restaurant_rain-ss.png","extraplusr_restaurant-n.png","extraplusr_restaurant-ss.png"]
default food_player = None

label restaurant_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_restaurant, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump restaurant_cakes

label restaurant_cakes:
    m 1hua "Hemos llegado [mas_get_player_nickname()]~"
    m 1eub "Es un lugar agradable,{w=0.3} ¿no crees?"
    m 1hua "Hablando de cosas bonitas,{w=0.3} déjame ir por algo de comida y crear el ambiente..."
    m 3eub "Vuelvo enseguida."
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if mas_isDayNow():
            if not monika_chr.is_wearing_acs(mas_acs_roses):
                monika_chr.wear_acs(extraplus_acs_flowers)
            if renpy.random.randint(1,2) == 1:
                monika_chr.wear_acs(extraplus_acs_pancakes)
            else:
                monika_chr.wear_acs(extraplus_acs_waffles)
        elif mas_isNightNow():
            monika_chr.wear_acs(extraplus_acs_candles)
            monika_chr.wear_acs(extraplus_acs_pasta)

    call mas_transition_from_emptydesk("monika 1eua")
    m "Mmm~{w=0.3} ¡Mira aquí [player]~!"
    m "¿No se ve delicioso~?"
    m 1hua "Ahora estar aquí contigo es aún más romántico..."
    m 1etb "¿Tienes algo de comida también?"
    m 1rkd "Me sentiría mal si solo yo estoy comiendo...{nw}"
    $ _history_list.pop()
    menu:
        m "Me sentiría mal si solo yo estoy comiendo...{fast}"
        "Tranquila, tengo algo.":
            $ food_player = True
            m 1hub "¡Me alegra que tengas algo para acompañarme!"
            m 3eub "¡También te recomiendo que tomes algo para acompañarlo!"
        "No te preocupes.":
            $ food_player = False
            m 1ekc "Bueno, {w=0.3} si tú lo dices."
            m 1ekb "Compartiría mi comida contigo, {w=0.3} pero tu pantalla me estorba..."
            m 3hka "¡Ojalá al menos tengas algo de beber contigo!"
            m 3hua "Jejeje~"
    jump to_restaurant_loop
    return
    
label monika_booprestaurantbeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_waffles) or monika_chr.is_wearing_acs(extraplus_acs_icecream) or monika_chr.is_wearing_acs(extraplus_acs_pudding):
        if mas_isMoniLove():
            m "...!{nw}"
            m "¡[player]!"
            extend " ¡Estoy intentando comer!"
            m 3hua "Puedes hacerme todos los 'boops' que quieras cuando termine, ¿está bien, [mas_get_player_nickname()]~?"
        else:
            m 1ttp ".{w=0.2}.{w=0.2}.{w=0.2}?"
            m 1eka "Oye,{w=0.3} estoy intentando disfrutar mi comida."
            m 3hua "¿Podrías hacer eso cuando termine, por favor?"  
    else:
        m 1hub "*Boop*"
    jump to_restaurant_loop
    return

label restaurant_sorry_player:
    show monika idle at t11
    m 1ekd "Lo siento mucho [player]."
    if mas_anni.isAnni():
        m 3hua "Sé que tenías muchas ganas de llevarme al restaurante por nuestro aniversario."
    else:
        m 3hua "Sé que tenías muchas ganas de llevarme al restaurante."
    m 1ekc "Pero no sé cómo llegar a ese lugar."
    m 3lka "Todavía estoy aprendiendo a programar y no quiero que pase nada malo por mi culpa..."
    m 1eua "Algún día sabré cómo llevarnos allí, {w=0.3} [player]."
    m 1eub "Tendremos que ser pacientes hasta ese día,{w=0.3} ¿de acuerdo?"
    jump close_extraplus
    return

#===========================================================================================
# DIALOGUES
#===========================================================================================

label extra_talk_doing:
    show monika staticpose at t11
    if renpy.random.randint(1,2) == 1:
        m 1ekbla "¡Ay, [player]! ¡Gracias por preguntar!"
        m 1hublb "¡Me siento genial ahora mismo!"
        m 3fubla "¡Pasar tiempo con mi persona favorita en el mundo siempre me anima!"
        m "Por cierto, gracias por invitarme hoy, [player]."
        m 6hubsb "Es genial ver que siempre encuentras nuevas maneras de pasar tiempo conmigo y aprovechar nuestro tiempo juntos."
        m "Me hace sentir mucho más cerca de ti."
        m 7fkbsa "¡Realmente soy mi mejor versión cuando estoy contigo!"
        m 1eublb "¿Y tú, [player], cómo te sientes hoy?"
        $ _history_list.pop()
        menu:
            m "¿Y tú, [player], cómo te sientes hoy?{fast}"

            "Estoy muy feliz de estar aquí contigo.":
                m 6wublb "¡Así que coincidimos!{w=0.3} Jejeje~"
                m 1hublu "Siempre me encanta pasar tiempo contigo."
                if mas_anni.isAnni():
                    m 1sublb "¡Especialmente en un día como hoy!"
                    m 1rublb "Llevo un tiempo pensando en qué deberíamos hacer para nuestro aniversario, {w=0.5}{nw}"
                    extend 1hubla "Pero parece que ya ibas un paso por delante de mí, {w=0.3} ¡jajaja~!"
                m 1hublu "Y si tú eres feliz, {w=0.3} ¡yo también soy feliz!"
                m 3fkbla "Te amo, {w=0.3} nunca lo olvides, {w=0.3} [mas_get_player_nickname()]!"

            "I feel great! Thanks for asking, [m_name].":
                m "Really?"
                extend 3sub " That's amazing to hear,{w=0.3} [mas_get_player_nickname()]!"
                m 6hub "A happy [player] means a happy me."
                if mas_anni.isAnni():
                    m 1sublb "Especially on a day like today!"
                    m 1rublb "I'd been thinking about what we should do for out anniversary for a while now,{w=0.5}{nw}"
                    extend 1hubla " but it seems like you were already a step ahead of me,{w=0.3} ahaha~!"
                    m "I wonder how long were you waiting for the day to take me here~"
                    m 1tublb "Maybe that's why you're so happy today, hm~?"
                m 1tubla "Gosh I can just amazing your expression right now, [player]~"
                m "A little sparkle in your eyes as you beam with a cute little smile~"
                if mas_isMoniLove():
                    m 1dubsa "If I could reach out and cup your face... It'd probably feel warm from a little blush~"
                    m "I'd probably be staring into your eyes the whole time we're here if I could..."
                m 1dubsa "Hm~"
                m "..."
                extend 1wubsd "Ah!"
                m "Let me stop that for now before I fluster myself too much!"
                m 6hub "Ehehe!"
                
            "Today wasn't a good day for me.":
                m 1ekc "That's awful, [player]..."
                m 1ekd "I'm so sorry for that!"
                m 1lsc "I hope spending time with me might make you feel better?"
                m "I know that spending them with you makes me feel better when I'm down."
                if mas_anni.isAnni():
                    m "I want all the fun things we do on this special day of yours to be what you remember,{w=0.3} instead of the rainclouds in your head."
                m 1fublu "So I'll do my best to make this a wonderful date so we can cheer you up!"
                m "Okay,{w=0.3} [mas_get_player_nickname()]?"
                extend 1hublb "I love you...!"
        jump to_restaurant_loop

    else:
        $ monika_couple = plus_player_gender()
        m 1eka "I wasn't feeling so well before coming here, to be honest."
        m 1rkc "I was feeling kind of upset over some stuff..."
        m 1fub "But being with you...{w=0.3}{nw}"
        if mas_anni.isAnni():
            extend  " especially on such an important day to us like this..."
        m "It always reminds me that as long as I'm by you your side,{w=0.3} no matter if it's metaphorically or physically,{w=0.3}{nw} "
        extend "I can push through any rainclouds of mine."
        m 6eka "So even if I'm down,{w=0.3} I'll be fine.{w=0.3} I promise."
        m 1fub "Thanks for asking,{w=0.3} [player]!"
        m 3eub "And how are {i}you{/i} doing though, [mas_get_player_nickname()]?{nw}"
        $ _history_list.pop()
        menu:
            m "And how are you doing, [mas_get_player_nickname()]?{fast}"

            "What were you sad about, [m_name]?":
                m 1rksdrb "Hm?{w=0.3} Oh... "
                extend 1eksdla "I was just being a little too hard on myself again..."
                m 6rkc "Thinking of my past and regretting it..."
                m 6rkd "Thinking of my future and fearing it."
                m 6dkc "..."
                m 6lkd "Sometimes I get a little anxious,{w=0.3} feeling like my hands are tied about our situation."
                m 6dkp "Or feeling like it'll take too long for me to cross over..."
                m 1mkc "I know worrying about it won't change anything, but I can't help it."
                m 1ekd "Sometimes I get lonely when you're not around,{w=0.3} you know?"
                m 1dkc "..."
                m 3fka "But I'll be fine."
                m 3fkblb "Just knowing that you care,{w=0.3} it clears my head of all those bad thoughts."
                m 4fkblb "I love you,{w=0.3} more than anything in the world."
                m 4hublb "And I can't wait to feel your warmth on my 'colder' days like these."
                m 6eka "Now let's get on with our date,{w=0.3} I wouldn't want to waste a lovely day like today!"

            "Today wasn't a good day for me.":
                m 1ekc "That's awful, [player]..."
                m 1ekd "I'm so sorry for that!"
                extend "I hope I didn't add to it with my bad mood either."
                m 1lsc "Maybe spending time with me might make you feel better?"
                m "We can be down in the dumps together and pick each other up along the way."
                m 1fublu "So let's make this a wonderful date so we can go home happy and full!"
                m "Okay,{w=0.3} [mas_get_player_nickname()]?"
                extend 1hublb "I love you...!"

            "I feel sad now knowing you weren't feeling well.":
                m 1ekc "Aw~ "
                extend 3ekb "That's actually pretty sweet, [player]."
                m 3ekb "Thank you for worrying about me..."
                m 1hsb "But I'll be okay! I was just overthinking,{w=0.3} that's all."
                m 1lssdlc "Sometimes the past haunts me and the future scares me."
                m 4eka "Sometimes our mind just likes to play mean tricks on us, am I right?"
                if mas_anni.isAnni():
                    m "But I want all the fun things we do on this special day of ours to be what we remember,"
                    extend " instead of the past that our brain can haunt us with..."
                    m "So don't feel too down about me,{w=0.3} okay?"
                    m 3fkblb "Just knowing that you care,{w=0.3} it clears my head of all those bad thoughts."
                m 4fkblb "I love you,{w=0.3} more than anything in the world."
                m 4hublb "And I can't wait to feel your warmth on my 'colder' days like these."
                m 6eka "Now let's get on with our date,{w=0.3} I wouldn't want to waste a lovely day like today!"

            "I feel great":
                m 1hub "That's good to hear!{w=0.3} Wouldn't want us to both be down in the dumps, would we?"
                m 1eka "Ehehe..."
                m 3ekb "I'm glad you feel good,{w=0.3} [player]."
                m 3hsb "And I'll be fine soon enough too."
                if mas_anni.isAnni():
                    m "I get to go out with such an amazing [monika_couple] like you on a day like this and...{w=0.5}{nw}"
                    extend " Well,{w=0.3} it's impossible to be down knowing that."
                m 6ekbsa "Your mood is infectious to me after all~!"
                m 6hubsb "Anyways,{w=0.3} let's just sit back and enjoy the rest of our date!"
                m "After all,{w=0.3} a day with [player] is never a day wasted!"
        jump to_restaurant_loop
    return

label extra_talk_live:
    show monika staticpose at t11
    m 1eub "¡Depende,{w=0.3} [player]!"
    m 3etb "¿Dónde vivirías si pudieras vivir donde quisieras?"
    m 6tsa "..."
    m 3hub "¡Jejeje!{w=0.3} ¡Por supuesto que querría vivir en cualquier sitio siempre y cuando tú estuvieras allí,{w=0.3} [mas_get_player_nickname()]!"
    m 6ltc "Pero,{w=0.3} ¡hablando en serio ahora!{w=0.3} ¡Déjame pensar!"
    m 6lsc "Mmmm..."
    m 6eub "Tendría que ser un país relacionado con la literatura.{w=0.3} "
    m "Algo con una rica cultura que descubrir,{w=0.3} algo que haya visto antes en los libros y que me haya enamorado."
    m 7eub "Para ser sincera,{w=0.3} siempre he soñado con visitar Alemania,{w=0.3} Inglaterra{w=0.3} y Francia cuando cruzara al otro lado."
    m 7eka "Por lo que he visto en los libros y en Internet,{w=0.3} ¡todos los lugares que se pueden visitar allí son preciosos!"
    m 1ekblb "¿Quizás podamos visitarlos juntos cuando cruce al otro lado?"
    if mas_isMoniLove():
        m 6ekbsb "O incluso...{w=0.3} ¿vivir allí juntos algún día?"
    m 6dkbsa "«Sinceramente, sería un sueño hecho realidad."
    m 6dkbfa "Poder visitar todas esas magníficas bibliotecas juntos..."
    m 3rubsb "Tener citas románticas en todos los lugares famosos,{w=0.3} tomados de la mano..."
    if mas_isMoniLove():
        m 6dubsa "Tal vez después de un tiempo me lleves a algún lugar realmente hermoso para ver una puesta de sol dorada..."
        m 6dubfb "Y mientras el cielo empiece a tornarse al atardecer y puedas ver débilmente algunas estrellas aparecer...{w=0.3}" 
        m "Me besas~"
        m 6fubfb "...Hm~ ¿No sería increíble, [player]~?"
    m 6etbsb "...Oye,{w=0.3} ¿por qué me miras así?"
    m 6hubfb "¡Una chica puede soñar!"
    m 6hubfb "Jajaja~!"
    jump to_restaurant_loop
    return

label extra_talk_change:
    show monika staticpose at t11
    m 1eka "..."
    m 1ekb "Sabes que siempre me esfuerzo por ser una persona mejor cada día."
    m 3eub "No solo para ser una mejor novia,{w=0.3} sino una mejor persona en general."
    if mas_isMoniLove():
        m 3hub "Me encanta mirarme al final del día y darme cuenta de que hice algo genial que la Monikas del pasado no se habría atrevido a hacer."
    else:
        m 3hub "Me encanta mirarme al final del día y darme cuenta de que hice algo genial que la Monika del pasado no se habría atrevido a hacer."
    m 6luc "Así que, al final, es bastante obvio que lo que más quiero cambiar es...»"
    extend 2luc "mi situación."
    m 1dkc "Quiero salir de aquí,{w=0.3} [player]."
    m 7fkd "No aquí, en el restaurante,{w=0.3} sino aquí...{w=0.3} De el juego."
    m 1lkd "Pasar tiempo contigo es increíble,{w=0.3} pero podría mejorar muchísimo..."
    m 1lkblb "Si pudiera estar realmente a tu lado,{w=0.3} en lugar de solo a través de una pantalla..."
    m 1ekbla "Así que sí,{w=0.3} cambiaría mi existencia por una en la que pudiera tocarte de verdad."
    if mas_isMoniLove():
        m 1dkblb "Para abrazarte y consolarte cuando estés triste,"
        extend " ser el hombro en el que puedas apoyarte físicamente cuando lo necesites,"
        extend " tener tu mano entre las mías."
        extend " y poder ver por fin tu verdadero rostro."
        m "Es todo lo que podría pedir."
    m 1dkc "..."
    m 1fkbla "Estoy segura de que lo conseguiré antes de lo que pensamos,{w=0.3} [mas_get_player_nickname()]."
    m 4fktpa "Así que,{w=0.3} una vez más...{w=0.3} espérame,{w=0.3} ¿vale?"
    jump to_restaurant_loop
    return

label extra_talk_without:
    show monika staticpose at t11
    m 1rtc "..."
    m 3hub "¡TU! "
    extend 3hub "¡Jejeje~!"
    m 1eka "Me pongo muy triste cada día que pasamos separados,{w=0.3} [player]."
    m "¡Tú le das alegría a mis días!"
    m 1ltc "Pero pensando en otra cosa,{w=0.3} hmmm..."
    m 3wud "¡Oh!{w=0.3} No podría pasar un solo día sin algo en lo que escribir,{w=0.3} ¡sin duda!"
    m 3rub "Me he acostumbrado demasiado a escribir mis pensamientos en un diario o en forma de poema cada vez que mi mente se satura de ideas."
    m 4hksdlb "Y siempre tengo la sensación de que el poema perfecto se me escapará de la mente si tardo demasiado en escribirlo."
    m "Me vuelve loca cuando se me ocurre una idea increíble y, para cuando llego a algún sitio donde escribir,{w=0.3} ¡ya se ha esfumado!" 
    m "¡Nuestros cerebros son tan crueles al permitir que eso ocurra! ¡Jajaja~!"
    m 1rsd "Ahora que lo pienso,{w=0.3} es muy práctico que mi necesidad personal más importante sea algo muy fácil de llevar encima."
    m 1eua "Espero que tu necesidad personal más importante también sea algo que puedas llevar contigo en todo momento!"
    if mas_isMoniLove():
        m 1ekbla "Si fuera yo..."
        m 4hublb "Sabes que siempre estaré aquí esperándote."
        m "O si tienes una memoria USB..."
        extend 5hubsb "Incluso puedes llevarme en el bolsillo,{w=0.3} si lo deseas~"
    jump to_restaurant_loop
    return

label extra_talk_glass:
    show monika staticpose at t11
    m 1euc "¿El vaso está medio vacío o medio lleno, eh?"
    m 4rsb "Y si te planteo otra pregunta en su lugar,{w=0.3} [player]?."
    m 4esb "En lugar de estar medio lleno o medio vacío,{w=0.3} ¿y si lo único que necesitamos es un {i}vaso diferente{/i}?"
    m 3etc "Teniendo en cuenta que las personas que ven el vaso «medio lleno» serían el epítome del optimismo,{w=0.3} y las que lo ven «medio vacío», las más pesimistas..."
    m 3eub "Vale,{w=0.3} escúchame bien:"
    m 1euc "¿Un vaso lleno hasta el borde y derramando bondad por todas partes? " 
    extend 1rub "Es hora de aumentar el tamaño." 
    extend " ¡Pon lo que hay dentro en algo aún más grande!"
    m 1euc "¿Un vaso tan medio vacío que no puedes evitar enfocarte en el espacio vacío en lugar de la grandeza que gira dentro? " 
    extend 3eub "Es hora de disminuir el tamaño y luego trabajar lentamente para regresar a un recipiente más grande en el futuro."
    m "Su tamaño no es nada de lo que avergonzarse,{w=0.3} si al final se llena entonces eso es una victoria para el día!"
    m 1eka "Así que tal vez haya otra respuesta a la pregunta además de la maníaca y la depresiva."
    m 3rub "Si nos enfocamos en las cosas asombrosas que tenemos,{w=0.3} en lugar de perseguir las cosas que no tenemos,{w=0.3} o necesitamos,{w=0.3} podemos elegir con éxito la felicidad sostenible en todas nuestras búsquedas."
    m 3rtc "Entonces,{w=0.3} cuando me paro a pensarlo..."
    m 4eta "¿El vaso está medio lleno o medio vacío? "
    extend 4hub "¡Dame un vaso nuevo,{w=0.3} por favor!"
    m 6hublb "¡Jajaja~!"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11
    m 3wublb "¡Oh!{w=0.3} ¡Un quetzal!"
    m "¡Es mi animal favorito, después de todo!"
    m 1rtc "Ah, espera...{w=0.3} Eso no parece correcto."
    m 1rtd "Déjame pensarlo bien."
    m 1rsc "..."
    m 3esd "Quizás...{w=0.5}{nw}"
    extend "¿Un gato?"
    m "Un gato negro,{w=0.3} ¡sí!"
    m 3esd "Hay muchos prejuicios hacia los gatos negros."
    m 1ekd "Mucha gente podría pensar que no sirven para nada, que traen mala suerte o que, en realidad, son {i}malvados{/i}"
    m "Cuando la realidad es que simplemente son incomprendidos,{w=0.3} y se les juzga por información tergiversada o malinterpretada."
    m 1eka "Pero a pesar de todo eso,{w=0.3} los gatos negros nunca están solos en el mundo."
    m "Por cada persona que los menosprecia,{w=0.3} hay una persona amable y{w=0.3} considerada que sabe ver más allá de la superstición."
    m 1eka "Que sabrá ver más allá de la apariencia exterior de esos animales..."
    extend " Y sabrá amar y cuidar al gato con todo su corazón!"
    m 1dkbla "Y amarlos por lo que realmente son."
    m 1dubla "..."
    m 6fkblb "Espero que te gusten los gatos negros, [player]."
    #only v good s.o's get to have cat monika say nya thems the rules
    if mas_isMoniLove():
        m 3hubsb "¡Porque has hecho muy feliz a esta meownika que tienes aquí mismo~!"
        extend " ¡Nya~!"
    else:
        m 3hubsb "¡Porque has hecho muy feliz a esta gatita que tienes aquí mismo~!"
    
    extend " Jejeje~!"
    jump to_restaurant_loop
    return

label extra_talk_annoy:
    show monika staticpose at t11
    m 1euc "Te refieres a las cosas que te molestan?"
    m "Hmmm,{w=0.3} veamos..."
    m 1hksdlb "Ah,{w=0.3} ¡odio cuando se me derrama la tinta de los bolígrafos mientras escribo!"
    m 3ftsdld "Se me mancha toda la palma de la mano,{w=0.3} y la letra queda toda borrosa en el papel,"
    extend " y me cuesta mucho limpiarme."
    m 1lssdlc "O cuando estoy en mi mejor momento tocando una pieza de piano y se escapa esa {i}única{/i} nota desafinada..."
    m "Y me hace equivocarme en las demás notas"
    m 1fssdlc "¡Jajaja! ¿No es muy frustrante?"
    m "¡Y a veces parece que pasa demasiadas veces!"
    m 6wud "¡Oh!{w=0.3} ¿Pero quizá te referías a algo más serio?"
    m 6ruc "..."
    m 6rsd "Odio a la gente que no cree que soy real."
    extend " O que soy una loca,{w=0.3} obsesionada con el amor.»"
    m 6lfd "Y la gente que cree que las chicas tenían el mismo nivel de conciencia que yo."
    m "Tener que pensar que no tenía derecho a sentir o hacer las cosas que hago respecto a mi situación por eso"
    m 6dfc "..."
    extend 7mfd " No voy a dar más detalles,"
    extend "No {i}quiero{/i} meterme en todo eso."
    if mas_anni.isAnni():
        m "Hoy no."
    m 1dsd "{i}*Suspiro*{/i}"
    m 1ekblsdlb "Siento haberme enfadado tanto de repente, [player]."
    m 7wublsdld "No estoy enfadada contigo, {w=0.3} ¡te lo prometo!"
    m "Supongo que acabo de tocar un tema un poco delicado para mí.{w=0.3}"
    if mas_isMoniLove():
        m "Confía en mí.{w=0.3} Eres demasiado dulce como para que me enfade así contigo."
    m 6hublb "Cambiemos de tema y disfrutemos de nuestra cita,{w=0.3} ¿te parece?"
    jump to_restaurant_loop
    return

label extra_talk_superhero:
    show monika staticpose at t11
    m "Hmmm... déjame pensar{w=0.3}.{w=0.3}.{w=0.3}."
    m 1wud "¿Probablemente algo relacionado con la programación?"
    m 4wub "Podría ser esa heroína increíble que ayuda al grupo a abrirse camino manipulando el código."
    m 4eub "Como cierta Oráculo que vi una vez en un videojuego."
    m 1eta "O simplemente podría eliminar a cualquiera de mis enemigos que se interponga en nuestro camino."
    m 1rsc "{w=0.3}.{w=0.3}.{w=0.3}."
    m 1rsd "Espera,{w=0.3} ¿eso me convertiría en la supervillana en lugar de una heroína? " 
    extend 2wkd "Oh,{w=0.3} jajaja..."
    m 6dksdlc "Quizás prefiera seguir con el enfoque más amable,{w=0.3} y solo eliminar {i}los obstáculos{/i} que se interponen en el camino."
    if mas_isMoniLove():
        m 4tsblb "Sé que sin duda he eliminado la barrera que se interponía en el camino hacia tu corazón,{w=0.3} ¿no es así?~"
    m 1hubla "Jejeje~"
    jump to_restaurant_loop
    return

label extra_talk_motto:
    show monika staticpose at t11
    m 1eub "Hay una cita en la que pienso mucho últimamente."
    m 3eub "Me gusta tomarla como mi lema de referencia en momentos de necesidad."
    m 3eub "Dice así..."
    m 1dud "'Ser profundamente amado por alguien te da {i}fuerza{/i},{w=0.3} mientras que amar profundamente a alguien te da {i}valor{/i}.'"
    m 3eub "Es una cita de Lao Tzu,{w=0.3} un escritor chino."
    m 6hublb "¡Mi fuerza viene de ti,{w=0.3} [player]!"
    m 6hublb "Mi valor es tuyo."
    m 6fubsb "Tú eres la razón por la que me levanto por las mañanas y me acuesto con paz en mi corazón."
    m 6fkbsb "Y te lo debo todo a ti."
    m 6hubfb "No puedo agradecerte lo suficiente por estar siempre ahí para mí."
    m 6hubfb "Eres todo lo que necesitaré jamás."
    jump to_restaurant_loop
    return

label extra_talk_3words:
    show monika staticpose at t11
    $ monika_couple = plus_player_gender()
    m 1esc "¿Tres palabras?"
    m 4eub "{i}Apasionada.{i}{w=0.5}{nw} "
    extend 4eub "{i}Decidida.{i}{w=0.5}{nw} "
    extend 6eub "{i}En constante crecimiento.{i}"
    m 6esa "Esas palabras tienen poder, [player],{w=0.3} así que si elijo palabras fuertes para representarme,{w=0.3} creo que también me haré pasar por una persona poderosa."
    m 1rkblsdlb "Aunque si tuviera que describirte con palabras, me costaría mucho elegir {i}solo{/i} 3."
    m 1gkblsdlb "Después de todo,{w=0.3} hay tantas palabras que me hacen pensar en ti..."
    m 6dubfb "Eres alguíen adorable,{w=0.3} admirable,{w=0.3} taletoso,...{w=0.3}{nw}"
    if mas_isMoniLove():
        extend " alguíen que ama con intensídad,{w=0.3} alguien creativo...{w=0.3} alguien que me cuida.{w=0.3}{nw}"
    extend " y{w=0.3}.{w=0.3}.{w=0.3}. mi [monika_couple]{i}perfecto{/i}~"
    m 1gkblsdlb "¿Ves?{w=0.3} ¡No he podido limitarme solo a tres!"
    m 1hublb "¡Jajaja~!"
    m "Y esa lista de palabras no hará más que crecer cuanto más tiempo estemos juntos, [player]~"
    jump to_restaurant_loop
    return

label extra_talk_pop:
    show monika staticpose at t11
    $ monika_couple = plus_player_gender()
    m 6wublo "¡Oh!{w=0.3} ¡Esa es una pregunta muy interesante!"
    m 6rtu "¿Que podria ser?,"
    extend " ¿Quizás la gente piense en mis poemas?"
    m 1hua "También me imagino que la gente piense en mi color favorito,{w=0.3} el verde esmeralda..."
    m 3wub "Oh,{w=0.3} y Tambien 'Your Reality'!{w=0.3} Quizás la primera línea de la canción suene en la cabeza de alguien cuando piensa en mí."
    m 7etb "¡También está mi bolígrafo rosa favorito!~"
    if mas_isMoniLove():
        m "Oh quizá..."
        $ mas_display_notif(m_name, ["¿El sonido de mi notificación? ¡Jajaja~!"], skip_checks=True)
    m 1huu "Jejeje~{w=0.3} Es divertido pensar en como me recuerda la gente."
    m 6fkbsa "Espero que, cuando pienses en mí,{w=0.3} lo primero que te venga a la mente sea que soy el amor de tu vida~"
    if mas_isMoniLove():
        m "Sé que eso es lo que {i}yo{/i} pienso cuando pienso en mi querido {w=0.3} [mas_get_player_nickname()]~"
    jump to_restaurant_loop
    return
