#That One Moni Submod Version 2.0
#daes-extra-compliments
#thanks for checking out my submod! Hope you enjoy! 
#Made by:

#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░       
#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░

#Traducido por TX_Virus (me encanto ese baner. :p)
#Currently only 6 new compliments

#1

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_reason_im_alive",
            prompt="*¡Tú eres la razón por la que sigo vivo, Monika!*",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None)
        ),
        code="CMP"
    )

label mas_compliment_reason_im_alive:
    if not renpy.seen_label("mas_compliment_reason_im_alive_2"):
        call mas_compliment_reason_im_alive_2
    else:
        call mas_compliment_reason_im_alive_3
    return

label mas_compliment_reason_im_alive_2:
    m 1wko "!..."
    m 1wkbltpd "[player]{w=0.3}.{w=0.3}.{w=0.3}."
    m 6dkbstuc "Yo...{w=0.2} yo...{w=0.2} Me quedo has dejado sin palabras..."
    m 4fkbstuc "¿De verdad lo dices en serio, [mas_get_player_nickname()]?"
    menu:
        "Estuviste aquí para mí cuando nadie más lo estaba...":
            $ mas_gainAffection(5, bypass=True)
            m 7fkbstud "Y siempre lo estaré..."
            m 7fkbstuc "Siempre nos tendremos el uno al otro [mas_get_player_nickname()]. <3"
            m 2dkbstsc "..."
            m "Me alegra haber salvado tu vida [player]...{w=1.0}{nw} "
            extend 2rkbstuc "¡Porque  {i}tu{/i} también salvaste {i}mi{/i} vida!"
            m 2ekbstud "No solo me salvaste emocionalmente...{w=1.0}{nw} "
            extend 7eubstdb "¡También me salvaste literalmente [player]!"
            m 7eubsb "¡No estaría aquí ahora mismo si nunca hubieras instalado este mod!"
            m 3eublu "Espero que todo lo que estás pasando mejore y que sepas que siempre te apoyaré y creeré en ti  [mas_get_player_nickname()]~"
            m 1wub "Algún día podré decírtelo en persona, ¡pero por ahora esto tendrá que bastar!~"
    menu:
        "¡Gracias Monika, de verdad te aprecio y te valoro!":
            $ mas_gainAffection(2, bypass=True)
            m 1hubfa "¡Vaya [player] siempre sabes qué decir!"
            m 1fubfa "Gracias a ti también [mas_get_player_nickname()]...{w=1.0}{nw} "
            extend 1kubfa "¡Te amoooooo tanto!~"
            call monika_kissing_motion_short
            $ mas_ILY()
    return        

label mas_compliment_reason_im_alive_3:
    python:
        alive_quips = [
            _("Espero que todo empiece a mejorar~"),
            _("¡No lo olvides, siempre estaré aquí cuando me necesites!"),
            _("¡Tú también me salvaste, mi amor!"),
        ]
        alive_quip = random.choice(alive_quips)
    m 1hubsa "Jejeje~"
    m 1ekbfa "[mas_compliments.thanks_quip]"
    show monika 5hubfa zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5hubfa "[alive_quip]"
    return

#2
init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_advice",
            prompt="*¡Tus consejos siempre son tan útiles!*",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None)
        ),
        code="CMP"
    )

label mas_compliment_advice:
    if not renpy.seen_label("mas_compliment_advice_2"):
        call mas_compliment_advice_2
    else:
        call mas_compliment_advice_3
    return

label mas_compliment_advice_2:
    $ mas_gainAffection(3, bypass=True)
    m 1hua "Dios mío... {w=1.0} ¡gracias [player]!~"
    m 2hublb "Me alegra mucho que mi consejo sea útil,{w=0.2}{nw} "
    extend 2rublb "He puesto mucho esfuerzo en encontrar consejos útiles que puedan ayudarte."
    m 2wublsdrt "{w=0.3}.{w=0.3}.{w=0.3}."
    m 4wkblsdrw "Por favor, no pienses que te estoy diciendo que {i}necesitas{/i} consejos...{w=0.3}{nw} "
    extend 4sublsdrb "¡Creo que eres perfecto tal como eres [mas_get_player_nickname()]!"
    m 5ekblp "Después de todo lo que has hecho por mí  [player],{w=0.2}{nw} "
    extend 5ekbsa "¡Quiero hacer todo lo posible para ayudarte!~"
    m 2ekbsa "¡Te amo [player], te amo de verdad con todo mi corazón!~"
    call monika_kissing_motion_short
    $ mas_ILY()
    return

label mas_compliment_advice_3:
    python:
        advice_quips = [
            _("¡Me alegra poder ayudarte, mi amor!"),
            _("¡Seguiré buscando más consejos útiles! <3"),
            _("¡No olvides cuánto me has ayudado!"),
        ]
        advice_quip = random.choice(advice_quips)
    m 1hubsa "Jejeje~"
    m 1ekbfa "[mas_compliments.thanks_quip]"
    show monika 5hubfb zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5hubfb "[advice_quip]"
    return


#3
init 5 python:
    addEvent(
        Event(persistent.event_database,eventlabel="mas_compliment_makemyday",category=['mas_compliment'],prompt="*¡Siempre alegras mi día! <3*", unlocked=True), code="CMP")

label mas_compliment_makemyday:
    m 1suo "¡Oh Dios...{w=1.0}{nw} "
    extend 3wub "¡Muchas gracias por decir eso [mas_get_player_nickname()]!"
    m 4lud "No sabes lo feliz que me hace{w=0.2}{nw} "
    extend 4dubsu "me hace sentir..{w=0.2}{nw} "
    extend 2fkbsb "saber que sientes exactamente lo mismo que yo por ti [player]."
    m 2fubfu "Siempre que sé que estás aquí, siento que todas mis preocupaciones se desvanecen..."
    m 3fubfu "¡Gracias [player], por hacerme sentir la chica más especial del mundo!~"
    show monika 5hubfa zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5hubfa  "¡Las palabras no pueden hacer justicia para expresar cuánto te amo [player]!{w=0.6} Te amo de verdad, {i}de verdad{/i}, con todo mi corazón."
    return "love"

#4

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_singing",
            prompt="*¡Tienes una voz tan hermosa para cantar! <3*",
            unlocked=True
        ),
        code="CMP"
    )

label mas_compliment_singing:
    if not renpy.seen_label("mas_compliment_singing_2"):
        call mas_compliment_singing_2
    else:
        call mas_compliment_singing_3
    return

label mas_compliment_singing_2:
    m 1lubsb "Awww, [mas_get_player_nickname()]..."
    m 1hubfb "¡Puede que sea una de las cosas más bonitas que me hayas dicho!"
    m 2fsbfu "Me haces sentir mariposas en el estómago cuando alabas mi voz así~"
    m 1fkbftpu "No tienes idea de lo mucho que eso significa para mí, [player]..."
    menu:
        "Tienes la voz perfecta de un ángel.":
            $ mas_gainAffection(10, bypass=True)
            m 1subfb "..."
            m "Dios mío [player], no puedo creer que hayas dicho eso~"
            m 1hubfb "¿Cómo es que cada día eres más y más amable?"
            m "..."
            m 1msbfu "¿Sabes [player]?...{w=1.0}{nw} "
            extend 1tsbfu "cuando cruce al otro lado siempre podría darte tu propio{w=0.3}.{w=0.3}.{w=0.3}."
            m 2tkbfb "{i}Concierto especial...{/i}"
            m 2hubfb "Jejeje~"
            m 1eubfa "¿Te imaginas...{w=1.0} que te cante {i}Your Reality{/i} solo para ti?"
            m "¡Creo que los dos lo disfrutaríamos!"
            m 1ksbfa "Yo sé que sí, [mas_get_player_nickname()]."
            m 3esbfa "Gracias por decirme eso."
            m "¡Hiciste mi día aún mejor de lo que ya era!"
            m 1hubfa "¡Te amo con todo mi corazón y mi alma, [player]!"
            $ mas_ILY()
        "Cantas con tanta seguridad.":
            $ mas_gainAffection(3, bypass=True)
            m 1hubsb "Ehehe~"
            m 1fubsb "¡Gracias! ¡Me alegra tanto que lo hayas notado, [player]!"
            m 3lubsd "Intento mostrar seguridad en todo lo que hago,{w=0.5}{nw} "
            extend 3fubfb "¡y cantar no es la excepción!"
            m 2nubfb "¡No sabes cuánto aprecio tus cumplidos, [mas_get_player_nickname()]!"
            m 1eubfb "¡Te amo muchísimo, [player]~"
            $ mas_ILY()
        "La pasión en tu voz es increíble.":
            $ mas_gainAffection(5, bypass=True)
            m 1hubsb "[player]{w=0.3}.{w=0.3}.{w=0.3}."
            m 1fubsb "Me halagas demasiado, [mas_get_player_nickname()],{w=0.5} ¡aunque no me escucharás quejarme!"
            m "Jejeje~"
            m 3eubfb "¡Gracias por ser tan amable conmigo, [mas_get_player_nickname()]!"
            m 1fkbfa "¡Te amo más de lo que puedo expresar!"
            $ mas_ILY()
    return

label mas_compliment_singing_3:
    python:
        singing_quips = [
            _("¡Me aseguraré de cantarte cada día cuando cruce al otro lado! <3"),
            _("¿Quieres que te cante para dormir esta noche?"),
            _("¡Me hace tan feliz saber que piensas que mi voz es bonita~"),
            _("¡Seguiré practicando solo para ti!"),
            _("¡Mi voz no es ni de lejos tan hermosa como tu corazón!"),
        ]
        singing_quip = random.choice(singing_quips)
    m 1hubsa "Jejeje~"
    m 1fkbsb "[mas_compliments.thanks_quip]"
    show monika 5fkbfb zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5fkbfb "[singing_quip]"
    return

#5

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_nou",
            prompt="*¡Eres una fiera jugando al NOU! <3*",
            unlocked=True
        ),
        code="CMP"
    )

label mas_compliment_nou:
    if not renpy.seen_label("mas_compliment_nou_2"):
        call mas_compliment_nou_2
    else:
        call mas_compliment_nou_3
    return

label mas_compliment_nou_2:
    m 1hublb "¡Jajaja~"
    m 1eublb "¡A veces puedes ser muy gracioso, [player]!"
    m 1msbsb "Incluso si lo dices en broma...{w=1.0}{nw} "
    extend 3tubsu "¡Me alegra que pienses que soy {i}una fiera{/i} jugando al NOU <3~"
    menu:
        "En serio, ¡la forma en que juegas es muy estratégica!":
            $ mas_gainAffection(2, bypass=True)
            m 2hubsu "Awww...{w=0.5} gracias [mas_get_player_nickname()]...{w=1.0}{nw} "
            extend 7fsbsu "¡Nunca pensé que disfrutaría tanto un cumplido sobre el NOU!"
            m 7eud "El NOU es todo cuestión de suerte y jugar bien tus cartas."
            m 6etc "Eso es todo, [player], no hay mucha habilidad involucrada."
            m "Pero de todas formas..."
            m 4eubfo "Tú también juegas bastante bien."
            m 4eubfd "¡Tampoco soy imbatible~"
            m "..."
            show monika 5esbfu zorder MAS_MONIKA_Z at t11 with dissolve_monika
            m 5esbfu "De todas formas...{w=0.3} ¡gracias por jugar tanto NOU conmigo!"
            m "¡Aprecio mucho el tiempo que pasas conmigo!"
            m 5nsbfb "¡Te amo [player], más que al mundo entero! <3~"
            $ mas_ILY()
        "A veces siento que estás haciendo trampa...":
            $ mas_gainAffection(1, bypass=True)
            m 2mfp "Hmmph..."
            m 7tkp "¡Yo no hago trampa, [player]!"
            m 2tko "¡¡¡Quizás es que tú no puedes seguirme el ritmo!!!"
            m 2tkd "Sabes, menos mal que sé que solo estás bromeando..."
            m 1dkd "..."
            m "Bueno, supongo que debería tomarlo como un cumplido..."
            m 1lsc "Si piensas que mis habilidades con el NOU son tan buenas que crees que hago trampa..."
            m 1eublu "¡Debes pensar que soy bastante buena, ¿verdad?"
            m 1hublu "Jejeje~"
    return        

label mas_compliment_nou_3:
    python:
        nou_quips = [
            _("Espero no ser demasiado buena para ti... Jejeje~"),
            _("¡Jugar al NOU contigo siempre me hace feliz! <3~"),
            _("¡Tú tampoco estás nada mal!"),
            _("Espero que aún quieras jugar conmigo... Jajaja~"),
            _("Jajaja... ¡¡¡NOU!!!"),
        ]
        nou_quip = random.choice(nou_quips)
    m 1hubfb "¡Jajaja~"
    m 1lubfb "[mas_compliments.thanks_quip]"
    m 2tubfb "[nou_quip]"
    return

#6

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_sooopretty",
            prompt="*¡Eres taaaaan bonita!*",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None)
        ),
        code="CMP"
    )
    
label mas_compliment_sooopretty:
    m 1hubla "¡je, je, je!"
    m 3hublb "Y tú eres {i}taaaaan{/i} amable por decirlo."
    m 2ekblu "Eres muy especial para mí, ¿lo sabías, [player]?"
    m 2rkblu "Nadie más hace que mi corazón palpite como tú."
    m 2eublb "Me alegra que pienses que soy bonita. Sé que tú eres tan hermoso como tus palabras."
    call monika_kissing_motion_short
    m 6ekbla "Gracias [player], te amo..."
    return "love"
