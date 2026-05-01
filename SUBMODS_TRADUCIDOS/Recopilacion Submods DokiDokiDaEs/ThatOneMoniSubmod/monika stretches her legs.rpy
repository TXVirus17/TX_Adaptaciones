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
    addEvent(Event(persistent.event_database,eventlabel="Monika_stretch_legs",category=['monika care'],prompt="Do you need to stretch your legs?",pool=True, unlocked=True))

label Monika_stretch_legs:
    if not renpy.seen_label("Monika_stretch_legs"):
        call Monika_stretch_legs_2
    else:
        call Monika_stretch_legs_3
    return

label Monika_stretch_legs_2:
    $ mas_gainAffection(3, bypass=True)
    m 3euu "You're so thoughtful [player]...{w=1.0}{nw}"
    extend 3esd " it can get really uncomfortable sitting down for so long."
    m 1huu "Hold on a moment [mas_get_player_nickname()]... I'll only be a second. <3"

    call monika_zoom_transition_reset(1.0)
    show monika at rs32
    hide monika
    pause 3.0

    $ is_sitting = False 
    show monika 1eua_static at ls32 zorder MAS_MONIKA_Z
    m 4hub_static "Tada!"
    show monika 2eub_static at hf32

    m "Ehehe~"
    m 1hua_static "It feels {i}sooooo{/i} nice to stretch my legs."
    m 2hksdlb_static "They start to get cramps after a while..."
    m 4eka_static "So thanks for looking out for me [player]. <3"
    m 4euc_static "The same goes for you too [mas_get_player_nickname()]."
    m 2hua_static "If you have to be sat down for prolonged periods of time try to stand up every so often."
    m 1eub_static "You can use it as an excuse to go get a drink, snack or even some fresh air."
    m 3eub_static  "Thank you for taking such great care of me, I want to do the same for you!"
    m 2eua_static "Ahhh... that's better!"
    m 5eua_static "I'll go get changed and grab my table and chair..."


    show monika at rs32
    hide monika
    pause 4.0

    $ monika_chr.reset_outfit(False)
    $ monika_chr.wear_acs(mas_acs_ribbon_def)
    $ is_sitting = True 
    
    show monika 1eua at ls32 zorder MAS_MONIKA_Z
    pause 1.0
    m "I love you so much [player]..."
    m "What else should we do today [mas_get_player_nickname()]?"
    $ mas_ILY()
    return

label Monika_stretch_legs_3:
    python:
        stretchthanks_quips = [
            _("Thank you for looking after me!"),
            _("You're so kind for taking care of me, you know that right?"),
            _("I appreciate you so much. <3"),
            _("Thanks again!"),
            _("Aww... thank you my love!"),
            _("Thanks for looking out for me!"),
        ]
        stretchthanks_quip = random.choice(stretchthanks_quips)    

    python:
        stretch_quips = [
            _("My legs were falling asleep there for a second, ahaha!"),
            _("Why don't you do the same my love?"),
            _("That really takes the edge off a lot!"),
            _("I hope you take just as much care of yourself as you do for me!"),
            _("Ahhh... I needed this one darling."),
            _("Perfect timing... I was thinking the same thing."),
            _("Want to get some fresh air?"),
            _("We could even do some quick exercises!"),
            _("Go get some water too... that's an order! Ehehe <3"),
            _("That feels sooooooo nice!"),
            _("Nothing beats a good stretch!")
        ]
        stretch_quip = random.choice(stretch_quips)



    $ mas_gainAffection(1, bypass=False)
    m 3eub "Good idea [player] I wouldn't mind a bit of a stretch right now."
    m 1huu "I'll go get ready!"

    call monika_zoom_transition_reset(1.0)
    show monika at rs32
    hide monika
    pause 3.0

    $ is_sitting = False 
    show monika 1eua_static at ls32 zorder MAS_MONIKA_Z

    m 4hub_static "Tada!"
    m 1eua_static "[stretchthanks_quip]" 
    m 3hub_static "[stretch_quip]"
    m 2eka_static "You really know how to take care of me [player]."
    m 2eua_static "Ahhh... that feels better already!"
    m 4hub_static "I think I'm just about ready to continue with our day."
    m 5eua_static "I'll go get changed and grab my desk and chair again."

    show monika at rs32
    hide monika
    pause 4.0


    $ is_sitting = True 
    
    show monika 1eua at ls32 zorder MAS_MONIKA_Z
    m 1hubfu "I love you [player]!"
    m 3eubfu "Let's have some more fun!"
    pause 1.0
    $ mas_ILY()
    return
