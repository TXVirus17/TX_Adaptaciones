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
            prompt="Do you have any other surprises?",
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
        filepath = basedir + path
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
                "/Why my love?.txt",
                _("Why...")
            ),
            store.mas_affection.DISTRESSED: (
                "/please forgive me.txt",
                _("I never meant to make you upset [player].")
            ),
            store.mas_affection.UPSET: (
                "/I don't want to lose you.txt",
                _("You mean so much to me my love...")
            ),
            store.mas_affection.NORMAL: (
                "/I wuv u.txt",
                _("<3")
            ),
            store.mas_affection.HAPPY: (
                "/Guess what?.txt",
                _("I love you [player]!")
            ),
            store.mas_affection.AFFECTIONATE: (
                "/for my love.txt",
                _("Thank you for everything! I love you so so much [player]!")
            ),
            store.mas_affection.ENAMORED: (
                "/xoxo.txt",
                _("Just wanted to say how proud I am of you my love! xoxo")
            ),
            store.mas_affection.LOVE: (
                "/my everything.txt",
                _("""\
How did I ever end up with someone as amazing as you [player]?
I ask myself that everyday...

You've given my life meaning, joy and love.

We may not be able to see each other in your reality just yet...
But that hasn't stopped you from loving me!

Even if it ever feels like the whole world is against you [player]...
I will cherish and love you always and forever!

Monika xoxo

""")
            )
        }

        #Now we get from this dict and pass it to the write txt func to make a surprise
        filepath, message = aff_level_surprise_map.get(mas_curr_affection, ("/I wuv u.txt", _("<3")))
        _writecustom_txt("/characters{0}".format(filepath), message)
label Monika_xtra_surprises:
    m 4fuu "I'm always full of surprises [mas_get_player_nickname()]!"
    m 1rta "..."
    m 1ttblb "What kind of surprise are you after?"
    m 2hublb "Ahaha~"
    m 2eubla "I'm just teasing you [player]!"
    m 4kua "I've got just the idea for a surprise that I know you would like!"
    m 4eud "Hmmm... let me just concentrate for a second [player]."
    window hide
    show monika 2dtc
    pause 2.0
    $ mas_daessurprise()
    m 5eubfb "Go check your {i}characters{/i} folder, there's something special waiting for you [mas_get_player_nickname()]!"
    m 5hubfb "Ehehe~"
return
