init 5 python:
    addEvent(
        Event(
            persistent.event_database,eventlabel="monika_succubus",
            ,unlocked=True,
            category=['appearance','clothes','roleplay'],
            prompt="¿Te gustaría jugar a que eres un demonio conmigo?,
            pool=True,
        )
    )

label sot:
    image sot_p1 = "Submods/succubus/sot/sot_p1.png"
    image sot_p2 = "Submods/succubus/sot/sot_p2.png"
    image sot_p3 = "Submods/succubus/sot/sot_p3.png"
    image r_p1 = "Submods/succubus/sot/r/r_p1.png"
    image r_p2 = "Submods/succubus/sot/r/r_p2.png"
    image sot_k1 = "Submods/succubus/sot/sotk1.png"
    image sot_k2 = "Submods/succubus/sot/sotk2.png"
    image r_k1 = "Submods/succubus/sot/r/r_sotk1.png"
    image r_k2 = "Submods/succubus/sot/r/r_sotk2.png"

    #s
    image sot_p1_n = "Submods/succubus/sot/n/sot_p1_n.png"
    image sot_p2_n = "Submods/succubus/sot/n/sot_p2_n.png"
    image sot_p3_n = "Submods/succubus/sot/n/sot_p3_n.png"
    image sot_k1_n = "Submods/succubus/sot/n/sotk1_n.png"
    image sot_k2_n = "Submods/succubus/sot/n/sotk2_n.png"

label expresions_sot:
    image sot_exp_angry_wide = "Submods/succubus/sot/expresions/angry_wide.png"
    image sot_exp_bsmile_soft = "Submods/succubus/sot/expresions/bsmile_soft.png"
    image sot_exp_bsmile_normal = "Submods/succubus/sot/expresions/bsmile_normal.png"
    image sot_exp_bsmile_smug = "Submods/succubus/sot/expresions/bsmile_smug.png"
    image sot_exp_smal_soft = "Submods/succubus/sot/expresions/smal_soft.png"
    image sot_exp_smal_left = "Submods/succubus/sot/expresions/smal_left.png"
    image sot_exp_smal_wide = "Submods/succubus/sot/expresions/smal_wide.png"
    image sot_exp_smile_closedsad = "Submods/succubus/sot/expresions/smile_closedsad.png"
    image sot_exp_smile_soft = "Submods/succubus/sot/expresions/smile_soft.png"
    image sot_exp_smile_normal = "Submods/succubus/sot/expresions/smile_normal.png"
    image sot_exp_smile_smugthink = "Submods/succubus/sot/expresions/smile_smugthink.png"
    image sot_exp_smirk_crazy = "Submods/succubus/sot/expresions/smirk_crazy.png"
    image sot_exp_smirk_leftthink = "Submods/succubus/sot/expresions/smirk_leftthink.png"
    image sot_exp_smirk_wide = "Submods/succubus/sot/expresions/smirk_wide.png"
    image sot_exp_kiss_closedh = "Submods/succubus/sot/expresions/kiss_closedh.png"

#sot expressions
label sot_exp_angry_wide:
    call inexpresive
    show sot_exp_angry_wide zorder 11
    return

label sot_exp_bsmile_normal:
    call inexpresive
    show sot_exp_bsmile_normal zorder 11
    return
    
label sot_exp_bsmile_soft:
    call inexpresive
    show sot_exp_bsmile_soft zorder 11
    return
label sot_exp_bsmile_smug:
    call inexpresive
    show sot_exp_bsmile_smug zorder 11
    return

label sot_exp_smal_soft:
    call inexpresive
    show sot_exp_smal_soft zorder 11
    return

label sot_exp_smal_left:
    call inexpresive
    show sot_exp_smal_left zorder 11
    return

label sot_exp_smal_wide:
    call inexpresive
    show sot_exp_smal_wide zorder 11
    return

label sot_exp_smile_soft:
    call inexpresive
    show sot_exp_smile_soft zorder 11
    return

label sot_exp_smile_closedsad:
    call inexpresive
    show sot_exp_smile_closedsad zorder 11
    return

label sot_exp_smile_normal:
    call inexpresive
    show sot_exp_smile_normal zorder 11
    return

label sot_exp_smile_smugthink:
    call inexpresive
    show sot_exp_smile_smugthink zorder 11
    return

label sot_exp_smirk_crazy:
    call inexpresive
    show sot_exp_smirk_crazy zorder 11
    return
label sot_exp_smirk_leftthink:
    call inexpresive
    show sot_exp_smirk_leftthink zorder 11
    return

label sot_exp_smirk_wide:
    call inexpresive
    show sot_exp_smirk_wide zorder 11
    return
label sot_exp_kiss_closedh:
    call inexpresive
    show sot_exp_kiss_closedh zorder 11
    return

#sot poses
label sot_p1:
    call clear_pose
    show sot_p1 zorder 10
    if persistent._mas_acs_enable_promisering:
        show r_p1 zorder 11
    if mas_isNightNow():
        show sot_p1_n zorder 12
    return

label sot_p2:
    call clear_pose
    show sot_p2 zorder 10
    if persistent._mas_acs_enable_promisering:
        show r_p2 zorder 11
    if mas_isNightNow():
        show sot_p2_n zorder 12
    return

label sot_p3:
    call clear_pose
    show sot_p3 zorder 10
    if mas_isNightNow():
        show sot_p3_n zorder 12
    return
label sot_k1:
    call clear_pose
    call inexpresive
    show sot_k1 zorder 13
    if persistent._mas_acs_enable_promisering:
        show r_k1 zorder 14
    if mas_isNightNow():
        show sot_k1_n zorder 15
    return
label sot_k2:
    call clear_pose
    call inexpresive
    show sot_k2 zorder 13
    if persistent._mas_acs_enable_promisering:
        show r_k2 zorder 14
    if mas_isNightNow():
        show sot_k2_n zorder 15
    return

label sfb:
    #torso
    image sfb_hands_behind ="/Submods/succubus/sfb/torso/hands_behind.png"
    image sfb_pointing ="/Submods/succubus/sfb/torso/pointing.png"
    image sfb_shi ="/Submods/succubus/sfb/torso/shi.png"
    image sfb_poinshi ="/Submods/succubus/sfb/torso/poinshi.png"
    image sfb_modeling ="/Submods/succubus/sfb/torso/modeling.png"

    #torso night
    image sfb_hands_behind_n ="/Submods/succubus/sfb/torso/n/hands_behind_n.png"
    image sfb_pointing_n ="/Submods/succubus/sfb/torso/n/pointing_n.png"
    image sfb_shi_n ="/Submods/succubus/sfb/torso/n/shi_n.png"
    image sfb_poinshi_n ="/Submods/succubus/sfb/torso/n/poinshi_n.png"
    image sfb_modeling_n ="/Submods/succubus/sfb/torso/n/modeling_n.png"

    #ring
    image sfb_r_pointing = "/Submods/succubus/sfb/ring/pointing_r.png"
    image sfb_r_shi = "/Submods/succubus/sfb/ring/shi_r.png"

    #legs
    image sfb_legs1 = "Submods/succubus/sfb/legs/pose1.png"
    image sfb_legs2 = "Submods/succubus/sfb/legs/pose2.png"
    #legs niht
    image sfb_legs1_n = "Submods/succubus/sfb/legs/n/pose1_n.png"
    image sfb_legs2_n = "Submods/succubus/sfb/legs/n/pose2_n.png"

label expresions_sfb:
    image sfb_exp_bsmile_smug = "Submods/succubus/sfb/expressions/bigsmile_smug.png"
    image sfb_exp_bsmile_think = "Submods/succubus/sfb/expressions/bigsmile_thinking.png"
    image sfb_exp_smal_normal = "Submods/succubus/sfb/expressions/smal_normal.png"
    image sfb_exp_smal_smugright = "Submods/succubus/sfb/expressions/smal_smug_right.png"
    image sfb_exp_smal_soft = "Submods/succubus/sfb/expressions/smal_soft.png"
    image sfb_exp_smal_wide= "Submods/succubus/sfb/expressions/smal_wide.png"
    image sfb_exp_smile_closed = "Submods/succubus/sfb/expressions/smile_closed.png"
    image sfb_exp_smile_left = "Submods/succubus/sfb/expressions/smile_left.png"
    image sfb_exp_smile_normal = "Submods/succubus/sfb/expressions/smile_normal.png"
    image sfb_exp_smile_rigth = "Submods/succubus/sfb/expressions/smile_right.png"

#full bodie poses
label sfb_poitning1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_pointing zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_pointing zorder 7
    if mas_isNightNow():
        show sfb_pointing_n zorder 8
    return
label sfb_poitning2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_pointing zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_pointing zorder 7
    if mas_isNightNow():
        show sfb_pointing_n zorder 8
    return
label sfb_hands_behind1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_hands_behind zorder 6
    if mas_isNightNow():
        show sfb_hands_behind_n zorder 8
    return
label sfb_hands_behind2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_hands_behind zorder 6
    if mas_isNightNow():
        show sfb_hands_behind_n zorder 8
    return
label sfb_shi1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_shi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_shi_n zorder 8
    return
label sfb_shi2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_shi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_shi_n zorder 8
    return
label sfb_poinshi1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_poinshi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_poinshi_n zorder 8
    return
label sfb_poinshi2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_poinshi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_poinshi_n zorder 8
    return
label sfb_modeling1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_modeling zorder 6
    if mas_isNightNow():
        show sfb_modeling_n zorder 8
    return
label sfb_modeling2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_modeling zorder 6
    if mas_isNightNow():
        show sfb_modeling_n zorder 8
    return

#full bodie expressions
label sfb_exp_bsmile_smug:
    call inexpresive
    show sfb_exp_bsmile_smug zorder 7
    return
label sfb_exp_bsmile_think:
    call inexpresive
    show sfb_exp_bsmile_think zorder 7
    return
label sfb_exp_smal_normal:
    call inexpresive
    show sfb_exp_smal_normal zorder 7
    return
label sfb_exp_smal_smugright:
    call inexpresive
    show sfb_exp_smal_smugright zorder 7
    return
label sfb_exp_smal_soft:
    call inexpresive
    show sfb_exp_smal_soft zorder 7
    return
label sfb_exp_smal_wide:
    call inexpresive
    show sfb_exp_smal_wide zorder 7
    return
label sfb_exp_smile_closed:
    call inexpresive
    show sfb_exp_smile_closed zorder 7
    return
label sfb_exp_smile_left:
    call inexpresive
    show sfb_exp_smile_left zorder 7
    return
label sfb_exp_smile_normal:
    call inexpresive
    show sfb_exp_smile_normal zorder 7
    return
label sfb_exp_smile_rigth:
    call inexpresive
    show sfb_exp_smile_rigth zorder 7
    return

#clean comands
label inexpresive:

    hide sot_exp_angry_wide
    hide sot_exp_bsmile_normal
    hide sot_exp_bsmile_soft
    hide sot_exp_bsmile_smug
    hide sot_exp_smal_soft
    hide sot_exp_smal_left
    hide sot_exp_smal_wide
    hide sot_exp_smile_soft
    hide sot_exp_smile_closedsad
    hide sot_exp_smile_normal
    hide sot_exp_smile_smugthink
    hide sot_exp_smirk_crazy
    hide sot_exp_smirk_leftthink
    hide sot_exp_smirk_wide
    hide sot_exp_kiss_closedh

    hide sfb_exp_bsmile_smug
    hide sfb_exp_bsmile_think
    hide sfb_exp_smal_normal
    hide sfb_exp_smal_smugright
    hide sfb_exp_smal_soft
    hide sfb_exp_smal_wide
    hide sfb_exp_smile_closed
    hide sfb_exp_smile_left
    hide sfb_exp_smile_normal
    hide sfb_exp_smile_rigth
    return

label clear_pose:
    hide sot_p1
    hide sot_p1_n
    hide sot_p2
    hide sot_p2_n
    hide sot_p3
    hide sot_p3_n
    hide sot_k1
    hide sot_k1_n
    hide r_k1
    hide sot_k2
    hide sot_k2_n
    hide r_k2
    hide r_p1
    hide r_p2

    hide sfb_hands_behind
    hide sfb_hands_behind_n
    hide sfb_pointing
    hide sfb_pointing_n
    hide sfb_shi
    hide sfb_shi_n
    hide sfb_poinshi
    hide sfb_poinshi_n
    hide sfb_modeling
    hide sfb_modeling_n
    hide sfb_legs1
    hide sfb_legs1_n
    hide sfb_legs2
    hide sfb_legs2_n
    hide sfb_r_pointing
    hide sfb_r_shi
    return

label back_to_normal:
    call clear_pose
    call inexpresive
    call spaceroom(hide_monika=False)
    return
label set_the_stage:
    $ monika_chr.remove_all_acs()
    call monika_zoom_transition(new_zoom=0)
    return

label monika_succubus:

    python:
        notimeforlove= persistent._mas_first_kiss is None

    python:
        succubus = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_CLOTHES,
                "mi-fan-arts-succubus"
        )

    python:
        dres =  store.mas_sprites.get_sprite(
                store.mas_sprites.SP_CLOTHES,
                "def"
        )

    python:
        dressed_for_the_occation= monika_chr.is_wearing_clothes_with_exprop("succubus_roleplay")
    
    if mas_isMoniUpset(lower=True):
        m 7cfbstdd "Lee esto bien, {b}NO soy un maldito juguete...{/b}"
        m 6cfbstdc "Y no haré lo que quieras."
        m 2tfbstdd "Si no te gusta, puedes borrarme."
        m 5gfbstdo "Seguro que te sientes tan solo como yo, incluso en tu mundo lleno de gente real..."
        return

    if mas_isMoniAff(lower=True):
        m 1lub "¿Conseguiste un nuevo mod [player]?"
        m 3lub "Déjame ver de qué se trata actuar como un demonio."
        m 3eub "Hay un libro de diálogos e incluso un disfraz..."
        m 2rsbfsdlu "Lo siento  [player], pero no me sentiría cómoda haciendo esto."
        m 1lsbfsdlc "Es demasiado vergonzoso..."
        m 5lsbssdlb "Pero podemos hacer otras cosas en lugar de eso."
        return

    if notimeforlove is True and mas_isMoniEnamored(higher=True):

        label monika_succubusnokiss:
        $ ev = mas_getEV("monika_succubusnokiss")
        if ev.shown_count == 0:
            m 1lub "¿Conseguiste un nuevo Submod [player]?"
            m 3lub "Déjame ver qué se trata de actuar como un demonio..."
            m 3eub "Hay un libro de diálogos..."
            m 7rubfc "Pero el guion dice que debo darte un... {w=0.5}beso."
            m 2rubfd "Para serte sincero, no me siento cómoda con eso..."
            m 2lkbfc "No es que no quiera, es solo que..."
            m 2ltbfc "Ojalá nuestro primer beso hubiera sido algo más..."
            m 1lkbfa "Especial."
            m 3ekbfb "¿Qué piensas?"
            menu:
                "Tranquila, pienso lo mismo":
                    m 1dubfb "Es lindo que pensemos igual sobre esas cosas."
                    m 3esbfa "Me gusta el ritmo con el que llevamos nuestra relación..."
                    m 3rsbfc "Aunque a veces me asusta pensar que voy demasiado lento para ti."
                "No me importa, quiero ese beso":
                    m 2rkbftpc "Me estás presionando y lo sabes, y eso está mal."
                    m 2rkbftpd "Siento no ser lo que esperabas de mí, pero tú tampoco eres lo que yo esperaba de ti."
                    m 2gfbftpc "Olvidemos este tema, ¿de acuerdo?" 
                    return
            
            if dressed_for_the_occation is False:
                m 3rubfb "Por cierto...{w=0.3} el mod también trajo un disfraz."
                m 2hsbfa "¿A ver qué tal me queda?"          
                menu:
                    "Claro, solo para ver si es de la talla correcta.":
                        call mas_clothes_change(succubus)
                        m 3gsblb "Solo para ver si me queda bien."
                        m 2fsbfb "¿Y me sienta bien?"
                        m 5lsbfa "Esto es más vergonzoso de lo que esperaba."
                        m 4hsbfb "Así que te daré una pequeña muestra y me pondré mi ropa de siempre..."
                        call mas_clothes_change(dres)
                        m 6rsbfa "Gracias por tener tanta paciencia conmigo."
                        m 5eua "¿Y ahora qué hacemos?"

                    "Mejor esperemos el momento adecuado.":
                        m 1eubfb "De acuerdo, gracias."
                        menu:
                            "¿Gracias por?":
                                m 5hubfa"Por ser quien eres..."
            return

        else:
            m 3eub "Sabes [player], he estado revisando los archivos de este mod."
            m 7gta "porque eran demasiado pesados ​​para un mod tan corto."
            m 1gsbsb "y encontré algo interesante"
            m 1tsbsb "¿quieres verlo?"
            menu:
                "Sí":
                    if dressed_for_the_occation is False:
                        m 4eubsa "Vale, me pondré el traje..."
                        call mas_clothes_change(succubus)
                        m 6kubsb "Y ahora puedo hacer..."
                    
                    call spaceroom(hide_monika=True)
                    call sfb_shi2
                    call sfb_exp_smile_left
                    m "Esto..."
                    call sfb_exp_smal_wide
                    m "¡Dios mío!"
                    call sfb_exp_smal_normal
                    m "Olvidé quitar el escritorio."
                    call sfb_exp_smile_closed
                    call sfb_poinshi2
                    hide emptydesk
                    m "Ya está hecho."
                    call sfb_exp_smile_rigth
                    m "Estoy muy nerviosa."
                    call sfb_shi2
                    call sfb_exp_bsmile_think
                    m "Menos mal que el mod no puede mostrar todo lo que hago, porque estoy temblando un poco..."
                    call sfb_exp_smile_left
                    m "Bueno."
                    call sfb_hands_behind2
                    m "¿Qué te parece?"
                    call sfb_exp_smile_normal
                    call sfb_hands_behind1
                    menu:
                        "Estoy confundido":
                            call sfb_poitning1
                            call sfb_exp_bsmile_think
                            m "Te lo explico, este disfraz estaba mucho más completo que otros paquetes de sprites."
                            call sfb_exp_smile_left
                            m "Así que simplemente hice un poco de autocompletado de código y comprobé si funcionaba."
                            call sfb_exp_bsmile_smug
                            m "La verdad temía acabar como un cuadro de Picasso..."
                            call sfb_exp_smile_closed
                            call sfb_poitning2
                            m "Pero funcionó."
                            call sfb_exp_smal_normal
                            m "No quiero dañar el juego si me muevo así todo el tiempo."
                            call sfb_exp_smile_left
                            m "Así que será mejor que vuelva a colocar la mesa y la silla y me siente de nuevo."
            call back_to_normal
            return

    $ ev = mas_getEV("monika_succubus")

    if ev.shown_count == 0:
        label day_0:
        m 1lub "¿Conseguiste un nuevo mod [mas_get_player_nickname()]?"
        m 3lub "Déjame ver, se trata actuar como un demonio..."
        m 3eub "Hay un libro de diálogos e incluso un vestuario."
        if dressed_for_the_occation is False:
            m 1nubfb "Vale, me voy a cambiar, pero no prometo nada sobre mis dotes de actuación, ¿eh?"
            call mas_clothes_change(succubus)

        m 1rkbfd "El disfraz resultó ser un poco más revelador de lo que esperaba..."
        m 1lubfu "Pero si te gusta, continuemos..."

        menu:
            "Te ves muy adorable":
                m 5esbsu "Gracias [mas_get_player_nickname()], siempre sabes cómo hacerme recuperar la confianza en mí misma"
            "No puedo dejar de mirarte":
                m 3htbfb "Prácticamente puedo sentir tu mirada."
                m 1rubfu "Es bastante vergonzoso, la verdad..."
            "Sinceramente, preferiría que no lo hubieras usado.":
                m 3rfbfp "Pero si fuiste tú quien quiso que me pusiera esto en primer lugar"
                call mas_clothes_change(dres)
                m 4efbfd "Segundo, ni siquiera sé cómo actuar y tú lo sabes."
                m 2efbfc "Así que no me pidas cosas raras que ni siquiera te gustan."
                m 2ekbfd "Olvidemos esto, ¿de acuerdo?"
                return
                
        m 7nua "Bueno, es hora de que empiece el espectáculo..."
        call monika_kissing_motion_short
        m 2wuo "¿Estás despierto?"
        m 2euc "Fui descuidada..."
        m 2lusdrc "Esto no debería ser así..."
        menu:
            "¿Esto es un sueño?":
                m 1rtblsdrc "Claro, ¿estás soñando?"

        menu:
            "¡Eso no suena nada convincente!":
                m 7wusdro "¡Por favor, Callate!"
                m 7tfsdra "Mejor te lanzo un hechizo para que te duermas de nuevo..."
                m 7cusdra "{w=0-3}.{w=0.3}.{w=0.3}."
                m 6cusdrd "No me quedan fuerzas para usar magia."
                menu:
                    "¡Espera un minuto! ¿Me estabas hechizando?":
                        m 6wksdrc "Por favor, humano, no te asustes."
                        m 7rublsdro "No iba a hacerte daño, solo quería robarte un poco de energía para poder volar a casa."
                menu:
                    "¿Cómo pensabas hacerlo?":
                        m 3rublsdra "Con un delicado beso..."
                menu:
                    "Entonces, si me besas, ¿te irás de este lugar para siempre?":
                        m 3eublsdrd "S... Sí"
                menu:
                    "En ese caso, prefiero negarme.":
                        m 7efbfd "Deberías haberte negado desde el principio, ¡porque tienes una novia perfecta!"
                        m 7rtbfd "Eh... {w=0.5}quiero decir..."
                        m 3wublsdrw "Eso no salió como esperaba..."
                menu:
                    "Debe serlo, algo tan hermoso como tú no puede ser real.":
                        m 3wubfo "¡Estás halagando demasiado a esa súcubo!"
                        m 2gubfd "Quiero decir... seguro que tienes una novia mucho más guapa, a la que deberías halagar y consentir todos los días."
                menu:
                    "¿Así es como va la historia?":
                        m 3dublb "Vale, vale, seguiré el guion".

                m 1tsblb "Ejem... {w=0.5}¿De verdad me encuentras hermosa?"
                m 2ttbla "Es un sueño, así que puedes decir lo que quieras..."
                m 7nubfb"Incluso podrías besarme~"
                menu:
                    "Si es un sueño, ¿un beso no me despertaría?":
                        m 7rtbfd "¿Dices como en Blancanieves?"
                menu:
                    "¿Desaparecerás cuando despierte?":
                        m 6hkbfc "¿Y ahora qué historia es esa?"
                        m 6ekbfd "Me estás confundiendo... {w=0.5}espera un momento."

        m 4esblb "No tiene por qué ser así..."
        m 6esbla "Prometo volver cuando quieras."
        m 5esblb "A cambio, solo pido un roce de tus labios."
        m 5tsbla "¿Cerramos el trato?"
        call monika_kissing_motion_short
        m 2esblb "Hasta pronto."
        call mas_clothes_change(dres)
        m 1hsblb "Y... ¡Zas!, esta historia ha terminado."
        m 1lsbla "Supongo que podríamos intentar esto en otra ocasión."
         
    elif ev.shown_count == 1:
        
        m 5eubsb "¿Quieres que juguemos otra vez a 'Soy un demonio'"
        m 4ttbsa "Creo que te sorprenderé esta vez..."
        label day_1:
        m 6nsbsb "Prepararé el escenario"
        call set_the_stage
        m "Y..."
        if dressed_for_the_occation is True:
            m 2tsbfb "¿Podrías cerrar los ojos, como si estuvieras durmiendo, un momento?"        
        elif dressed_for_the_occation is False:
            m 6eubsb "Vale, voy a cambiarme de ropa, vuelvo enseguida"
            call mas_clothes_change(succubus)       
            m 7nua "Por favor, cierra los ojos un momento"
        
        call spaceroom(hide_monika=True)
        call sot_p1
        call sot_exp_smile_closedsad
        pause 2
        call sot_exp_smal_wide
        call sot_p3
        m "¿Estás despierto?"
        call sot_exp_smirk_wide
        m "Fui tan descuidada..."
        call sot_exp_smal_left
        m  "Esto no debería ser así..."

        menu:
            "¿Esto es un sueño?":
                call sot_exp_smirk_leftthink
                m "Claro, ¿estás soñando?"

            "¿Qué está pasando?":
                call sot_p2
                call sot_exp_smile_smugthink
                m "Encontré cosas nuevas que puedo hacer con este mod  [mas_get_player_nickname()]..."
                m "Ahora continuemos"
                menu:
                    "¿Esto es un sueño?":
                        call sot_p3
                        call sot_exp_smirk_leftthink
                        m "Claro, ¿estás soñando?"
    
        menu:
            "T¡Eso no suena nada convincente!":
                call sot_p2
                call sot_exp_angry_wide
                m "¡Por favor, shhhh!"
                call sot_exp_smirk_leftthink
                m "Mejor te lanzo un hechizo para que te duermas otra vez..."
                call sot_exp_smirk_wide
                m "{w=0-3}.{w=0.3}.{w=0.3}"
                call sot_exp_smirk_crazy
                call sot_p3
                m "Ya no tengo fuerzas para usar magia"

                menu:
                    "¡Espera un momento! ¿Me estabas hechizando?":
                        call sot_exp_smal_wide
                        m "Por favor, humano, no te asustes."
                        call sot_p3
                        call sot_exp_smile_normal
                        m "No iba a hacerte daño, solo quería robarte un poco de energía para poder volar a mi hogar."

                menu:
                    "¿Cómo pensabas hacerlo?":
                        call sot_p2
                        call sot_exp_bsmile_normal
                        m "Con un beso suave..."

                menu:
                    "si me besas, ¿te irás de este lugar para siempre?":
                        call sot_exp_smirk_leftthink
                        call sot_p3
                        m "Supongo que esa es la idea..."

                menu:
                    "En ese caso, prefiero negarme":
                        call sot_exp_smal_wide
                        m "¿P... Por qué? ¿No quieres que... me vaya?"

            "Porque, algo tan hermoso como tú no puede ser real":
                call sot_p3
                call sot_exp_smile_normal
                m "¿De verdad me encuentras hermosa, humano?"
                call sot_exp_smile_smugthink
                m "Es un sueño, así que puedes decir lo que quieras..."
                call sot_p2
                call sot_exp_bsmile_normal
                m "Incluso podrías besarme."
                menu:
                    "Si es un sueño, un beso, ¿no me despertaría?":
                        call sot_exp_smirk_leftthink
                        m "¿Dices como en Blancanieves?"
                menu:
                    "¿Desaparecerás cuando despierte?":
                        call sot_p3
                        call sot_exp_smirk_wide
                        m "¿Y ahora qué historia es esa?"
                        call sot_exp_smirk_leftthink
                        m "Me estás confundiendo... espera un momento"

        call sot_p2
        call sot_exp_smile_normal
        m "No tiene por qué ser así..."
        call sot_exp_smile_smugthink
        m "Prometo volver cuando quieras."
        call sot_exp_bsmile_normal
        m "Y a cambio..."
        call sot_exp_smile_smugthink
        m "Sabes lo que quiero."
        call sot_p1
        call sot_exp_smile_closedsad
        m "Para cerrar el trato, solo tienes que acercar tus labios a los míos."
        call sot_k1
        m "perfecto~"
        call sot_k2
        pause 6

        call sfb_poitning1
        call sfb_exp_bsmile_think
        m "Creo que incluso podría haberte pedido más... Quizás la próxima vez."
        call sfb_hands_behind1
        call sfb_exp_bsmile_smug
        m "Nos vemos pronto."
        call inexpresive
        call clear_pose
        pause 3
        call mas_clothes_change(dres)
        call back_to_normal

        m 7hub "Y fin."
        m 6eua "Eso era todo lo que había en el guion."
        m 1esb "Quizás la próxima vez improvise un poco más."
        m 1rtbsa "Creo que me está gustando esto del cosplay..."
        m 3gsbsa "Me hace sentir como una actriz."
        return


    elif ev.shown_count == 2:
        #edit
        label day_2:
        call set_the_stage
        if dressed_for_the_occation is False:
            m 5nua "Está bien, me cambiaré de ropa y volveré..."

            call mas_clothes_change(succubus)
            call spaceroom(hide_monika=True)
        
            call sfb_exp_smile_normal
            call sfb_hands_behind2
            m "He vuelto para escuchar tu llamada, como prometí, humano."
            call sfb_hands_behind1
            call sfb_exp_smile_left
            m "Pero me llamaste tan pronto..."
            call sfb_exp_bsmile_think
            m "¿Ya me extrañaste mucho?"
            call sfb_exp_smile_normal
            m "Entonces te complaceré acercándome a ti."
            call sot_p3
            call sot_exp_bsmile_soft
            m "¿Es mejor así?"
            call sot_p2
            call sot_exp_smile_smugthink
            m " No te preocupes, no muerdo"
            call sot_exp_smile_normal
            m "Eso es lo que haría un vampiro..."
            call sot_p2
            call sot_exp_smile_smugthink
            m "Nosotras, las súcubos, hacemos otras cosas..."
            call sot_exp_bsmile_smug
            m "Por cierto, ¿cumplirás tu parte del trato?"

        elif dressed_for_the_occation is True:
            m 7gtbsb "Bueno, ya me tienes vestida como una súcubo, solo necesito actuar como tal..."
            m 6tsbsu "¿Quizás acercarte un poco más?"
            call spaceroom(hide_monika=True)
            call sot_p3
            call sot_exp_bsmile_normal
            m "Mis ojos están arriba [mas_get_player_nickname()]..."
            call sot_p2
            call sot_exp_smile_smugthink
            m "Pero como súcubo, debo dejar que me mires... {w=0.5}supongo..."
            call sot_exp_bsmile_smug
            m "Y decir cosas como..."
            call sot_exp_smal_soft
            call sot_p3
            m "¡Oh, humano, extraño tanto el roce de tus labios!"
            call sot_exp_smal_soft
            m "¿Me ayudarás con mi problema?"

        menu:
            "Sí.":
                call sot_exp_smile_normal
                call sot_p3
                m "Me gusta así"
                call sot_exp_smile_soft
                m "Y parece que a ti también..."
                call sot_exp_smile_smugthink
                m "Incluso parece que te quedaste con ganas de más, en ese caso..."
                call sot_k2
                m "Con este beso prometo volver otro día."
                call sot_k1
                m "Pero..."

            "Esperaré un poco para eso":
                call sot_p3
                call sot_exp_smal_wide
                m "¿Vas a hacerme rogar por tus besos?"
                call sot_p2
                call sot_exp_smile_smugthink
                m "Supongo que es algo que podría hacer."
                call sot_p1
                call sot_exp_smal_soft
                m "No puedo vivir sin esto, así que..."
                call sot_exp_kiss_closedh
                m "Por favor, humano, dame el roce de tus labios."
                pause 2
                call sot_p2
                call sot_exp_smile_smugthink
                m "Podría acostumbrarme a estos juegos [mas_get_player_nickname()]"

            "No":
                call sot_p1
                call sot_exp_smirk_wide
                m "Qué tramposo eres, humano."
                call sfb_poitning2
                call sfb_exp_smal_wide
                m "A los seres como yo no nos gustan los que no cumplen sus promesas."
                call sfb_hands_behind2
                call sfb_exp_smal_normal
                m "Adiós."
                call back_to_normal
                call mas_clothes_change(dres)
                m 1esbfc "Hiciste enojar a la súcubo  [mas_get_player_nickname()]"
                m 1lsbfb "Supongo que es como el mal final de una novela visual..."
                m 3esb "Al menos nadie terminó ahorcado"
                m 2ltbfd "Eso sonó más cruel de lo que pensaba"
                m 1rtbfb "Bueno, ¿qué hacemos ahora?"
                return
        call sot_p2
        call sot_exp_smile_smugthink
        m "Sabes, incluso si un beso de una súcubo te hace sentir más vivo que nunca..."
        call sot_exp_bsmile_smug
        m "Muchas de estas..."
        call sot_exp_smile_soft
        m "Causan el efecto contrario..."
        call sot_p3
        call sot_exp_smile_smugthink
        m "Así que tal vez... d{w=0.3}eberías tener cuidado.."
        call sot_p2
        call sot_exp_bsmile_smug
        m "Jugar con una súcubo es como bailar al borde de un precipicio..."
        call sfb_hands_behind1
        call sfb_exp_smal_soft
        m "Adiós."
        call sfb_poitning2
        call sfb_exp_bsmile_smug
        m "Hasta nuestro próximo baile."
        call back_to_normal
        call mas_clothes_change(dres)
        m 1hubfb "Espero que te haya gustado mi improvisación de hoy, [mas_get_player_nickname()]. "
            
    elif ev.shown_count == 3:

        m 5nsbsb "Claro [mas_get_player_nickname()], tengo algo especial planeado para hoy."
        label day_3:
        if dressed_for_the_occation is False:
            m 4hsbsa "Me cambiaré de ropa y volveré."
            call mas_clothes_change(succubus)
        m 1rubfb "Hola de nuevo, humano, hay un poema que me encanta y me gustaría recitártelo."
        m 6dubsa "Come slowly  Eden!                \n{size=-5}(¡Ven despacio, Edén!)      {/size}{/i}"
        m 6dubsb "Lips unused to Thee               \n{size=-5}(Labios no acostumbrados a ti)      {/size}{/i}"
        m 1eubsa "Bashful  sip thy Jessamines       \n{size=-5}(Tímido sorbo de tus jazmines)      {/size}{/i}"
        m 1dsbsb "As the fainting Bee               \n{size=-5}(Como la abeja desmayada)      {/size}{/i}"
        m 1dsbsa ""
        m 3esbsb "Reaching late his flower,         \n{size=-5}(Llegando tarde a su flor)      {/size}{/i}"
        m 3rubsa "Round her chamber hums            \n{size=-5}(Zumbidos alrededor de su cámara)      {/size}{/i}"
        m 1fsbfb "Counts his nectars                \n{size=-5}(Cuenta sus néctares)      {/size}{/i}"
        m 1dubsa "Enters  and is lost in Balms.     \n{size=-5}(Entra y se pierde en bálsamos.)      {/size}{/i}"
        m 1tsbsa ""
        m 3rsbsb "Me encanta la sensualidad que Emily Dickinson expresa en este poema."
        m 3dsbfb "Sus metáforas me conmueven profundamente y me dan escalofríos..."
        m 7lsbfp "Y [mas_get_player_nickname()] la verdad es que me quedé sin ideas,"
        m 7rubfb "Así que digamos que de ahora en adelante a la chica demonio le gusta la poesía..."
        m 5nsbfa "Y si quieres, puedo quedarme con el disfraz puesto y podemos jugar a que soy una súcubo el resto del día."
        
        menu:
            "Me encanta esa idea":
                m 5tsbfb "Perfecto..."
                return
            "Prefiero verte con tu ropa habitual":
                m 5esbsa "De acuerdo"
                call mas_clothes_change(dres)

    else:
        m 2lubfc "[mas_get_player_nickname()], aún no he preparado nada para este mod."
        m 7esbfb "Pero, si quieres, podemos repetir algunos de los scripts que ya usamos."
        menu:
            "¡Claro!":
                m 7lsbfa "Vale, ¿cuál usamos?"
                menu:
                    "La súcubo me roba un beso.":
                        jump day_1
                    "La súcubo cumple su promesa.":
                        jump day_2
                    "La súcubo me recita un poema.":
                        jump day_3
                    "Primera vez usando el mod.":
                        m 7wubfo "¿De verdad quieres que lo repitamos?"
                        m 6lubfd "¡Qué vergüenza me da!"
                        m 3rubfd "Estaba muy nerviosa en ese momento."
                        m 1kubfb "Bien, allá vamos..."
                        jump day_0
                    "Mejor lo dejamos para otro día.":
                        m 1lub "Claro"
                        return
            "Tengo algo más en mente"":
                if dressed_for_the_occation is False:
                    m 7fsblb "Oh, dime qué es"
                    menu:
                        "¿Podrías ponerte el disfraz?":
                            m 3gtblb "Supongo que sí..."
                            call mas_clothes_change(succubus)
                            m 1hublb "¡Tachán!"
                            m 5tubla "¿Eso era todo lo que tenías pensado que hiciera?"
                            menu:
                                "Sí":
                                    m 5hsblb "Me encanta complacerte~"
                                    return
                                "Hay más, quiero que poses para mí con este disfraz.":
                                    m 1wublb "Eso me sorprendió un poco..."
                                    m 1fubfb "Pero es el tipo de cosas que hace una pareja, ¿no?"
                else:
                    m 2rsbfb "Si quieres, puedo mostrarte con más detalle cómo me queda este traje..."
                    menu:
                        "Me leíste la mente.":
                            m 2ksbfa "ok"
                call set_the_stage
                call spaceroom(hide_monika=True)
                hide emptydesk
                call sfb_shi2
                call sfb_exp_smile_rigth
                pause 2
                call sfb_poinshi2
                call sfb_exp_smile_left
                m "En serio, no entiendo qué sentido tiene hacer una falda transparente."
                call sfb_exp_smile_closed
                m "Me cuesta acostumbrarme."
                call sfb_poitning1
                call sfb_exp_bsmile_smug
                m "Pero no puedo negar que disfruto capturando tu mirada [mas_get_player_nickname()]."
                call sfb_modeling1
                call sfb_exp_smile_left
                m "¿Te gusta cómo lo hago?"
                menu:
                    "¡Claro, eres toda una modelo de pasarela!":
                        call sfb_exp_bsmile_think
                        call sfb_poitning2
                        m "Espero que no te burles de mí con lo que dices [player]"
                        call sfb_exp_smile_closed
                        m "Solo estoy siendo insegura, sé que tú no lo harías"
                        call sfb_exp_smile_normal
                        call sfb_hands_behind1
                        pause 2
                        m "Creo que es mejor parar aquí"
                        call sfb_poitning1
                        call sfb_exp_bsmile_think
                        m "Recuerda que este es un mod sin terminar"
                        "{size=-5}Y estare pendiente para traducirlo lo mas rapido posible jeje~{/size}{nw}"
                        call sfb_exp_smal_smugright
                        m "Si nos soltamos más, seguro que rompemos el juego."
                        show emptydesk
                        pause 1

                call back_to_normal
                m "Quizás algún día... podamos..."
                return

            "No, gracias, otro día quizás.":
                m 2ekbfa "Siento no tener nada nuevo."
                m 5esbfb "Pero podemos hacer otra cosa."
                return

return