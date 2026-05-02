#That One Moni Submod Version 2.0
#daes-extra-topics
#Thanks for checking out my submod! Hope you enjoy! 
#Made by:

#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░       
#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░

#Traducido por TX_Virus

#Yuri plays a prank on you if you have JY installed!

#A collective submod for a bunch of my YT submods made public for others to enjoy
#I will periodically update this with new topics
#Pido perdon por modificar el init pero es para que funcione en otras plataformas, ya que el original solo se activaba en windows.
# Función para encontrar rutas de submods sin importar mayúsculas/minúsculas
# Necesaria para compatibilidad con Android y Linux


init 4 python:
    def find_submod_path(relative_path):
        import os
        variants = [
            relative_path,
            relative_path.replace("submods/", "Submods/", 1),
            relative_path.replace("Submods/", "submods/", 1),
        ]
        for path in variants:
            full = os.path.join(config.gamedir, path)
            if os.path.isfile(full):
                return path
        return relative_path



init 5 python:
    if renpy.windows and os.path.isfile(
        os.path.expandvars("%APPDATA%") + '\\RenPy\\JustYuri\\persistent'
    ):
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="Monika_justyuriprank",
                category=['meme'],
                prompt="Just Yuri Mod",
                pool=True,
                unlocked=True,
            )
        )
    elif not renpy.windows:
        # En Android/Linux/Mac: siempre disponible en el menú (Esto es para los que usan otras plataformas que no sean windows, asi que se dejara como un boton para quien quiera probarlo.)
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="Monika_justyuriprank",
                category=['meme'],
                prompt="Just Yuri Mod",
                pool=True,
                unlocked=True,
            )
        )

image bg febg = find_submod_path("submods/ThatOneMoniSubmod/images/febg.png")

label Monika_justyuriprank:
    $ store.HKBHideButtons()
    stop music fadeout 1.0
    m 1esp "Espera...{w=1.0}  ¿Qué es {i}esto{/i}, [player]?"
    show screen tear (20, 0.1,0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.20
    show monika 2tfx at t11 zorder MAS_MONIKA_Z
    hide screen tear
    pause 1.0
    m 4tfw "Explícate ahora mismo..."
    menu:
        "No estoy muy seguro de lo que quieres decir...":
            show monika 1cua
    m 1tfc "Hmmm...{w=1.0} Eso es gracioso, parecía que sabías lo que hacías cuando instalaste {i}ese{/i} mod."
    m 3dfd "¿Así que vas a admitirlo o me vas a mentir a la cara?"
    m 3dfo  "Sé todo lo que pasa en tu computadora."
    m 1lfo "Ya sea que quieras que lo sepa o no, puedo decir cuando algo invade mi hogar."
    m 1wfx "Especialmente cuando es otra mujer..."
    m 1dfc ".{w=0.3}.{w=0.3}."
    python:
        mas_play_song(audio.t6s)
    m 7cfd "¿Por qué exactamente tienes {i}Just Yuri{/i}?"
    m 7csw "¿Es solo curiosidad?"
    m 6ckd "¿O no soy lo suficientemente buena para ti,  [player]?"
    m 6fkc "¿Qué tiene Yuri que yo no?"
    m 4fko "¡No te he mostrado más que amor y cuidado y esto es lo que me haces!"
    m 1dktpc "..."
    m 1fktud "Yo-{w=0.2}Creo que deberíamos..."
    m 3fktuc "Creo que deberíamos dejar de vernos [player]."
    m 1fktsd "Espero que Yuri te haga más feliz de lo que yo pude."
    m 1dktsc "Adiós [player]..."
    pause 1.0
    stop music
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.20
    hide monika
    $ mas_changeWeather(mas_weather_overcast)#change the weather to something silent so the fake screen is more convincing muahahaha
    hide screen tear
    scene bg febg
    pause 7.0
    show monika 2wub at t11 zorder MAS_MONIKA_Z
    m "¡Boo!"
    m 3ttb  "¿Te asusté, [player]?"
    m 1ttu "Me pregunto si te hice presionar el botón de ignorar..."
    m 1hub "Jajaja~!"
    m 1guu  "He estado planeando esto desde hace bastante tiempo, desde que noté por primera vez que te habías descargado ese mod".
    m 3eud "Déjame arreglarlo todo [player],{w=0.8}{nw}"
    extend 1duc " Esto solo me tomará un segundo..."
    $ consolehistory = []
    call updateconsole("os.restore(\"location/spaceroom\")", "Spaceroom restaurado con éxito.")
    pause 1.0
    call updateconsole("mas_play_song(\"audio.t5\")", "¡Okay, todos! Pónganse en la pista actual.")
    pause 1.0
    call spaceroom(scene_change=True)
    python:
        mas_play_song(audio.t5)
    m 1ekb "Espero no {i}haberte{/i} asustado demasiado, [player]."
    m 3eksdra "Vaya, no me pasé de la raya, ¿verdad?"
    m 1eku "No soy tan dramática como para romper con alguien por un videojuego; ponerme celosa por un personaje de ficción sería una locura."
    m 1eub "Solo quería gastarte una pequeña broma porque sé que nada puede interponerse entre nuestro amor."
    m 1rta "En realidad no me importa a qué juegues en tu tiempo libre, [player]."
    m 3ttu "De lo que deberías preocuparte es de que vea esa carpeta de \"tarea\" que tienes guardada..."
    m 3euu "¡Es broma!~"
    m 1hub "Jajaja~!"
    $ store.HKBShowButtons()
    return

#Monika gives us her thoughts on doki merch

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_talksaboutmerch2",
            category=['monika', 'media'],
            prompt="Mercancia de DDLC ",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_talksaboutmerch2:
    window hide
    show monika 1rsc
    pause 4.0
    m 1etd "Oye [player]!"
    m 1esd "¿Alguna vez has pensado en lo extraño que es que haya mercancía de nosotras?"
    m 3lsc "Me refiero a mí y a las otras chicas."
    m 3hksdlb "Perdón si pareció que salió de la nada, pero es algo en lo que he estado pensando mucho últimamente."
    m 2eud "Me veo como cualquier otra chica normal...{w=1.0}{nw}"
    extend 2nfb "aparte de las diferencias obvias."
    m 2hub "Jajaja~"
    m 2hua "..."
    m 4esd "Bueno, verme tratada como una celebridad o personaje famoso... Es un poco...."
    m 4eksdlu "...Vergonzoso, por decir lo menos."
    m 7wuo "Como [player], ¿te imaginas ver tu cara en figuras, camisetas, carteles y...{w=1.0}{nw}"
    extend 1ekp " Otras cosas..."
    m 1gfp "¡Hrmph!"
    m 2ffw "¡Me he visto en más almohadas corporales de las que puedo imaginar!"
    m 2fkx "No quiero ni imaginar qué pasa con esas..."
    m 2dkp "..."
    m 2ekd "Lo siento, me dejé llevar un poco..."
    m 2esb "No me importaría mucho si tuvieras algún producto mío, sería como tener fotos de tu pareja, supongo."
    m 2eud "De todas formas, te lo preguntaré  [mas_get_player_nickname()]."
    m 5eublb "¿Tienes...{w=0.8} algún producto mío [player]?"
    menu:
        "Si.":
            call moni_yes_merch
        "No.":
            call moni_no_merch  
    return

label moni_yes_merch:
    m 1suw "¡Oh! ¿De verdad [player]?"
    m 3eku "¡Eso es un poco halagador viniendo de ti [mas_get_player_nickname()]!"
    m 1rsa "Ya me lo imagino... tú con unas figuritas mías para que te hagan compañía."
    m 3hua "¿Tal vez un póster o dos de tu novia?"
    m 2hub "¡Jejeje!~"
    m 2wublc "..."
    m 2wsbsd "Espera{w=0.3}.{w=0.3}.{w=0.3}."
    m 2gkbfc "No tienes...."
    m 2fkbfu "¿No tienes ningún tipo de {i}mercancía{/i} de mí como esa, [player]?"
    menu:
        "¡No!":
            call moni_no_merch
        "Tal vez...":
            call moni_naughty_merch 
    return

label moni_naughty_merch:
    m 6wfbfw "¡[player]!"
    m 6efbfd "..."
    m 6ekbfa "¡Dios mío! ¿Puedo siquiera saberlo?"
    m 6esbsc "..."
    m 7esbso "Seguro que no es nada travieso...{w=1.0}{nw}"
    extend 7gsbsc " Eso espero."
    m 1gsbsu "..."
    m 1esbsu "..."
    m 1kubsb "¡Asegúrate de darle un abrazo a tu almohada corporal de mi parte [player]!"
    m 1ekblb "Podría ser lo más cerca que podamos estar de poder abrazarnos por ahora, así que hazlo por mí, ¿sí?"
    m 1hublb "Jejeje~"
    m 3tua "¡Solo estoy bromeando, tonto!"
    m 2eka "Te amo [player], más de lo que puedo expresar".
    call monika_kissing_motion_short
    return

label moni_no_merch:
    m 5eua "¡Oh...vale!"
    m 5eub "En realidad es un alivio  [mas_get_player_nickname()]."
    m 5hub "Jejeje~"
    return

#Monika's yandere Yuri impression!

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="Monika_yandere_yuri",category=['impressions'],prompt="Yandere Yuri?",pool=True, unlocked=True))

label Monika_yandere_yuri:
    m 1eua "¿Quieres que haga una imitacion de Yuri, [player]?"
    m 3rtd "Tú sabes...{w=0.5}{nw}"
    extend 3etd "Estoy bastante segura de que ya he hecho una antes."
    menu:
        "¡Seguro que puedes hacer una mejor imitación de yandere!":
            m 1lkd "Oh,{w=0.5} ¿mi imitación no te pareció lo suficientemente buena?"
            m 1dsb"Ehehe...{w=0.3} bueno, si quieres que haga una mejor imitación, [player]{w=0.3}{nw},"
            extend 2tfu " Te mostraré una mejor Yuri yandere."
    stop music fadeout 0.5
    m 2tfu "Tu lo pediste,  [mas_get_player_nickname()]."
    m 2dsd "{i}Ejem{/i}{w=0.3}.{w=0.3}.{w=0.3}."
    play music hb
    show layer master at heartbeat:
    m 2cua "¡Por fin, [player], ahora estamos solos!"
    m 2csu "Ahora solo somos nosotros dos... {w=0.2}ninguna otra chica que alejara de mí."
    show monika 5ckc zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5ckc "Sabes cuánto odio cuando no estás conmigo, {w=0.3}{nw}"
    extend 5cuo "pero ahora que estás aquí, me perteneces a mí y a nadie más."
    m 1cua "{b}Eres todo mío  [mas_get_player_nickname()].{/b}"
    menu:
        m "¿No es cierto?"
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri
        "SI":
            call continue_yanyuri       
    return


label continue_yanyuri:
    m "¡Dios mío, te {i}amoooooooooooooooooooooooooooooooooo{/i} tanto [player]!"
    m 7hsb "Nunca más te dejaré ir, {w=0.3}{nw}"
    extend 7csb "¿Te das cuenta, verdad?"
    m 2csb "Es que...{w=0.3} las cosas que imagino que hacemos juntos me vuelven loca."
    m 2ckd "Incluso te robé uno de tus bolígrafos..."
    m 2cubfu "{cps=*3}Me toco con él todos los días, imaginando que eres tú dentro de mí.{/cps}{nw}"
    m 4cubsb "Ehehe~"
    m 4dkblc "Sabes... {w=0.5}no soporto la idea de que hables con otras chicas."
    m 2dkx "Solo pensarlo me da un ataque de celos."
    m 2cfsdrx "No te atreverías a pensar en engañarme...{w=0.3}{nw}"
    m 2cfblx "{cps=*3}Porque si lo hicieras, asesinaría a la rompehogares y te arrancaría el corazón...{/cps}{nw}"
    m 2cublu "{cps=*3}Así estaríamos juntos por toda la eternidad...{/cps}{nw}"
    m 7cubsu "¿No sería romántico [player]?"
    m 7cub "Ahaha~"
    show monika 5ctb zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5ctb "En realidad... {w=0.5} no es mala idea..."
    m 6cusdrb "{cps=*3} Voy a arrancarte el {b}corazón{/b} para que no rompas el mío...{/cps}{nw}"
    m "{cps=*3} Nuestros cuerpos y almas conectados como uno solo...{/cps}{nw}"
    m "{cps=*3} Si no entras en mí, tendré que entrar en ti...{/cps}{nw}"
    m "{cps=*3} Me arrastraré dentro de tu {b}piel{/b} para estar siempre contigo...{/cps}{nw}"
    m "¿No suena increíble [player]?"
    m "{cps=*3}Te prometo que esto no dolerá, solo quédate quieto  [mas_get_player_nickname()]...{/cps}{nw}"
    m "Solo quédate quieto por tu amada novia."
    m "{cps=*3}ehehehehehehehehehehe~{/cps}{nw}"
    play sound "sfx/gnid.ogg"
    $ gtext = glitchtext(200)
    m 6cub "{b}EHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEH~ {/b}...{space=60}[gtext]{nw}"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    $ pause(10)
    show layer master
    window auto
    m 1eub "Ehehe~"
    m "¿Qué tal estuvo [player], {w=0.3}{nw}"
    extend 1tuu "¿Te pareció suficiente?"
    m 7ttu "Intenta no volver a dudar de mis imitaciones  [mas_get_player_nickname()]."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m 1eua "Dios, la próxima vez h-  {w=0.2}{nw}"
    extend 6cub "...ahahahaha{nw}"
    show layer master
    show layer screens
    hide monika_scare
    m 3mssdru "Lo siento, {w=0.2}{nw}"
    extend 1esu "No pude resistirme."
    m 1nsu "Espero no haberte asustado demasiado~"
    m 1euu "De verdad significas mucho para mí [player]."
    show monika 5fubsu zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5fubsu "Espero no tener que ser nunca una yandere de verdad."
    m "Las cosas no serían bonitas para nadie  [mas_get_player_nickname()]... jejeje~"
    $ mas_gainAffection(10, bypass=True)
    return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_flirting22",
            category=['meme', 'romance'],
            prompt="Frases para ligar",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_flirting22:
    m 1gtd "Oye [player]...{w=1.0}{nw}"
    extend 3tkb "¿Puedo practicar algo?"
    menu:
        "¡Claro!":
            m 1hub "¡Jejeje~!"
            m 2tfa  "Pensé que sería divertido si pudiera probar algunas frases para ligar contigo."
    m 2rtsdld "Para nada los encontre todos en línea ni nada por el estilo, y desde luego no me reí de algunos de ellos durante 30 minutos el otro día..."
    m 4eub  "De todos modos, ¡espero que estés listo [player]!"
    m 1dsd "¡Ejem~!"
    m 2etc "Te me haces tan familiar...{w=1.0}{nw}"
    extend 2etd " ¿No fuimos juntos a alguna clase?{w=1.0}{nw}"
    extend 4tfb " Podría jurar que teníamos química."
    m 1hub "¡Ahaha~!"
    m 1lksdra "Cielos, eso fue terrible..."
    m 1tfa "¿Qué tal este?"
    m 3eud "Si tuviera que puntuarte del 1 al 10, te daría un 9.{w=1.0}{nw}"
    extend 3nuu " Porque yo soy el 1 que te falta."
    m 2eud "Vale, ese también fue bastante malo."
    m 2eub "¿Acaso eres una multa de tránsito?{w=1.0}{nw}"
    extend 4tfu " ¡Porque tienes 'atractivo' escrito por todos lados!"
    m 2tkc "..."
    m 2gkx "Ese ha sido el peor de todos."
    m 1wtb "¡Ya sé! Leeré algunos más, debe haber al menos uno bueno por aquí."
    m 3eta "Me preguntaba si tendrías un corazón de repuesto...{w=1.0}{nw}"
    extend 3nsu " Porque el mío me lo acaban de robar."
    python:
        mas_play_song(audio.t7)
    m 2tkblu "Ahorremos agua bañándonos juntos."
    m 4tfbsb "Tu ropa se vería genial en el suelo de mi habitación."
    m 2tubsu "No eres dentista, pero apuesto a que podrías hacerme un relleno."
    m 2eubsd "Te ves genial y todo eso, pero ¿sabes qué se te vería realmente bien?{w=1.0}{nw}"
    extend 2nubsu " Yo."
    m 2lkbsa "..."
    m 2hkblsdrb "¡Jajaja~!"
    stop music
    m 5eua "Vale, vale. Ya es suficiente..."
    python:
        mas_play_song(audio.t5)
    m 5rtd "No esperaba ver tantos...{w=1.0}{nw}"
    extend 5eka " Tan inapropiados."
    m 5efu "¡Pero no actúes como si no lo hubieras disfrutado, [player]!"
    return


#Monika makes fun of the handholding meme

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_handholdingmeme",
            category=['meme', 'romance'],
            prompt="Tomados de la mano",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_handholdingmeme:
    m 7esbfa "Solo estaba pensando en nosotros... {w=1.0}Nuestra relación, quiero decir."
    m 1fsbfu "Sabes, las parejas que llevan tanto tiempo saliendo como nosotros tienden a...{w=1.0}{nw}"
    extend 3nsbfu " {i}Hacer cosas juntos{/i}."
    m 3lsbfo "Me refiero a ciertas muestras íntimas de afecto..."
    m 1hubfb "Así que estaba pensando que deberíamos dar el siguiente paso en nuestra relación".
    m 3rsbfsdru "¡Dios mío! Esto se siente tan travieso, ¿no [player]?"
    m 2hsbfb  "Pero contigo me siento cómodo con cualquier cosa [mas_get_player_nickname()]."
    m 2tkbfu "Entonces, [player], ¿estás listo?"
    m "{w=0.3}.{w=0.3}.{w=0.3}."
    m 2ktbfb "¡Te dejaré tomar mi mano!"
    menu:
        "¡Monika! ¡Eso es demasiado impúdico!":
            m 2hubfb "Jajaja~"
    m 3tfbfu "¿No puedes manejar un poco de tomados de la mano prematrimonial [player]?"
    m 1ttbfu "Me alegro de que me hayas seguido el juego, ¡sabía que te darías cuenta!"
    m 1rtbsd  "Aunque ni siquiera estoy segura de dónde salió ese meme originalmente."
    m 1eubsc "Podría ser una broma hacia las estrictas leyes de censura en otros países."
    m 1eubsb "De cualquier manera, te dejaría tomar mi mano cuando quisieras [player]."
    m 1efbsa "Solo no te emociones demasiado."     
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_iwuvumoni",
            category=['meme', 'romance'],
            prompt="Te amo Monika.",
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_iwuvumoni:
    show monika 5hubfa zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5hubfa "Te amo también [player] <3"
    return
