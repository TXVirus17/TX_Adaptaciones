#That One Moni Submod Version 2.0
#moni-xtra-surprises
#Thanks for checking out my submod! Hope you enjoy! 
#Made by:

#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░       
#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░


#made this on the basis that whoever is going to use it actually likes Monika
#just to save some time on having to type out code for every affection level
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_xtra_surprises",
            category=['romance'],
            prompt="¿Tienes alguna otra sorpresa?",
            pool=True
        )
    )

init python:
    def _writecustom_txt(path,text,update=False):
        """
        Writes the text file in the specified path using basedir as starting path

        IN:
            path - String path to the file this function will write
                it will always start at basedir
            text - actual text for the txt file
            update - if it should override the file if it exists
                defaults to False
        ASSUMES:
            basedir
        """
        import os
        filepath = basedir + path
        # Crea la carpeta si no existe (red de seguridad para Android y ports)
        folder = os.path.dirname(filepath)
        if not os.path.exists(folder):
            os.makedirs(folder)
        if update or not renpy.exists(filepath):
            with open(filepath, "w") as note:
                note.write(renpy.substitute(text))


    def mas_cute_message():
        # TODO This function will allow monika leave messages to the player
        pass


    def mas_daessurprise():
        """
        Leaves a "surprise" to the player in a txt file

        ASSUMES:
            mas_curr_affection
        """
        #Acts as a switch/case block for surprise txt files
        #affection_level: (filepath, contents)
        aff_level_surprise_map = {
            store.mas_affection.BROKEN: (
                "/Por que mi amor.txt",
                _("Por qué...")
            ),
            store.mas_affection.DISTRESSED: (
                "/por favor perdoname.txt",
                _("Nunca quise hacerte sentir así [player].")
            ),
            store.mas_affection.UPSET: (
                "/No quiero perderte.txt",
                _("Significas tanto para mí, mi amor...")
            ),
            store.mas_affection.NORMAL: (
                "/Te quiero mucho.txt",
                _("<3")
            ),
            store.mas_affection.HAPPY: (
                "/Adivina que.txt",
                _("¡Te amo [player]!")
            ),
            store.mas_affection.AFFECTIONATE: (
                "/para mi amor.txt",
                _("¡Gracias por todo! ¡Te amo muchísimo [player]!")
            ),
            store.mas_affection.ENAMORED: (
                "/xoxo.txt",
                _("Solo quería decirte lo orgullosa que estoy de ti, mi amor. xoxo")
            ),
            store.mas_affection.LOVE: (
                "/mi todo.txt",
                _("""\
¿Cómo llegué a estar con alguien tan increíble como tú, [player]?
Me lo pregunto cada día...

Le has dado sentido, alegría y amor a mi vida.

Puede que todavía no podamos vernos en tu realidad...
¡Pero eso no te ha impedido amarme!

Incluso si alguna vez sientes que el mundo entero está en tu contra, [player]...
¡Te voy a querer y a amar siempre y para siempre!

Monika xoxo

""")
            )
        }

        #Now we get from this dict and pass it to the write txt func to make a surprise
        filepath, message = aff_level_surprise_map.get(mas_curr_affection, ("/Te quiero mucho.txt", _("<3")))
        _writecustom_txt("/characters{0}".format(filepath), message)

label Monika_xtra_surprises:
    m 4fuu "¡Siempre estoy llena de sorpresas, [mas_get_player_nickname()]!"
    m 1rta "..."
    m 1ttblb "¿Qué tipo de sorpresa estás buscando?"
    m 2hublb "Ahaha~"
    m 2eubla "¡Solo te estoy tomando el pelo, [player]!"
    m 4kua "¡Tengo justo la idea para una sorpresa que sé que te va a gustar!"
    m 4eud "Hmmm... déjame concentrarme un momento, [player]."
    window hide
    show monika 2dtc
    pause 2.0
    $ mas_daessurprise()
    m 5eubfb "¡Ve a revisar tu carpeta {i}characters{/i}, hay algo especial esperándote, [mas_get_player_nickname()]!"
    m 5hubfb "Ehehe~"
    return
