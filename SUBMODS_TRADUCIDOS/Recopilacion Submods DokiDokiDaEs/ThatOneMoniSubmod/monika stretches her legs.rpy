#That One Moni Submod Version 2.0
#monika stretches her legs
#Thanks for checking out my submod! Hope you enjoy! 
#Psst check out my Youtube channel:

#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░       
#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░

#Because sitting down all day can be uncomfortable

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="Monika_stretch_legs",category=['monika care'],prompt="¿Necesitas estirar las piernas?",pool=True, unlocked=True))

label Monika_stretch_legs:
    if not renpy.seen_label("Monika_stretch_legs"):
        call Monika_stretch_legs_2
    else:
        call Monika_stretch_legs_3
    return

label Monika_stretch_legs_2:
    $ mas_gainAffection(3, bypass=True)
    m 3euu  "Eres tan considerado [player]...{w=1.0}{nw}"
    extend 3esd " Puede resultar realmente incómodo estar sentado durante tanto tiempo."
    m 1huu "Espera un momento [mas_get_player_nickname()]... Solo será un segundo. <3"

    call monika_zoom_transition_reset(1.0)
    show monika at rs32
    hide monika
    pause 3.0

    $ is_sitting = False 
    show monika 1eua_static at ls32 zorder MAS_MONIKA_Z
    m 4hub_static "¡Tada!"
    show monika 2eub_static at hf32

    m "Jejeje~"
    m 1hua_static "Se siente {i}taaaan{/i} bien estirar las piernas."
    m 2hksdlb_static "Empiezan a doler después de un rato..."
    m 4eka_static "Así que gracias por cuidarme [player]. <3"
    m 4euc_static "Lo mismo vale para ti [mas_get_player_nickname()]."
    m 2hua_static "Si tienes que estar sentado por períodos prolongados trata de levantarte de vez en cuando."
    m 1eub_static "Puedes usarlo como excusa para ir a buscar una bebida, un bocadillo o incluso algo de aire fresco."
    m 3eub_static  "Gracias por cuidarme tan bien, ¡quiero hacer lo mismo por ti!"
    m 2eua_static  "¡Ahhh... eso es mejor!"
    m 5eua_static  "Voy a ir a cambiarme y a buscar mi mesa y mi silla..."


    show monika at rs32
    hide monika
    pause 4.0

    $ monika_chr.reset_outfit(False)
    $ monika_chr.wear_acs(mas_acs_ribbon_def)
    $ is_sitting = True 
    
    show monika 1eua at ls32 zorder MAS_MONIKA_Z
    pause 1.0
    m "Te amo tanto, [player]..."
    m "¿Qué más deberíamos hacer hoy [mas_get_player_nickname()]?"
    $ mas_ILY()
    return

label Monika_stretch_legs_3:
    python:
        stretchthanks_quips = [
            _("¡Gracias por cuidarme!"),
            _("Eres taaaan amable por cuidarme, ¿sabes?"),
            _("Te aprecio muchísimo. <3"),
            _("¡Gracias de nuevo!"),
            _("¡Ayyy, gracias, mi amor!"),
            _("¡Gracias por cuidarme! Eres el mejor [player]!"),
        ]
        stretchthanks_quip = random.choice(stretchthanks_quips)    

    python:
        stretch_quips = [
            _("Mis piernas estaban a punto de quedarse dormidas allí por un segundo, jeje!"),
            _("¿Por qué no haces lo mismo, mi amor?"),
            _("Eso realmente quita el borde de muchas cosas!"),
            _("Espero que te cuides tanto como me cuidas a mí!"),
            _("Ahhh... Necesitaba esta, cariño."),
            _("Timing perfecto... Estaba pensando lo mismo."),
            _("¿Quieres tomar un poco de aire fresco?"),
            _("¡Incluso podríamos hacer algunos ejercicios rápidos!"),
            _("¡Ve a buscar agua también... es una orden! Jeje <3)"),
            _("¡Qué bieeeeen se siente!"),
            _("¡Nada mejor que un buen estiramiento!")
        ]
        stretch_quip = random.choice(stretch_quips)



    $ mas_gainAffection(1, bypass=False)
    m 3eub "Buena idea [player]. No me vendría mal estirar un poco ahora mismo."
    m 1huu "¡Voy a prepararme!"

    call monika_zoom_transition_reset(1.0)
    show monika at rs32
    hide monika
    pause 3.0

    $ is_sitting = False 90
    show monika 1eua_static at ls32 zorder MAS_MONIKA_Z

    m 4hub_static "Tada!"
    m 1eua_static "[stretchthanks_quip]" 
    m 3hub_static "[stretch_quip]"
    m 2eka_static "Realmente sabes cómo cuidarme, [player]."
    m 2eua_static "¡Ahhh... ya me siento mejor!"
    m 4hub_static "Creo que ya estoy lista para continuar con nuestro día."
    m 5eua_static "Voy a cambiarme y a buscar mi escritorio y mi silla."

    show monika at rs32
    hide monika
    pause 4.0


    $ is_sitting = True 
    
    show monika 1eua at ls32 zorder MAS_MONIKA_Z
    m 1hubfu "¡Te amo, [player]!"
    m 3eubfu "¡Vamos a divertirnos un poco más!"
    pause 1.0
    $ mas_ILY()
    return
