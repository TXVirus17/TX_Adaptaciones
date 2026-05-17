#creds to u/geneTechnician for these ones, thank you for allowing me to host them on github!

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["ltable_acs"] = {
        "_ev": "gt_ltable_acs_select",
        "_min-items": 1,
        "change": "¿Puedes poner algo más en el lado izquierdo de tu escritorio?",
        "wear": "¿Puedes poner algo en el lado izquierdo de tu escritorio?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_ltable_acs_select",
            category=["Escritorio"],
            prompt=store.mas_selspr.get_prompt("ltable_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_ltable_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="ltable_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("¿Qué quieres que ponga en el lado izquierdo del escritorio?")
        sel_map = {}

    m 1eua "¡Claro, [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Ah, está bien"
return


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["rtable_acs"] = {
        "_ev": "gt_rtable_acs_select",
        "_min-items": 1,
        "change": "¿Puedes poner algo más en el lado derecho de tu escritorio?",
        "wear": "¿Puedes poner algo en el lado derecho de tu escritorio?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_rtable_acs_select",
            category=["Escritorio"],
            prompt=store.mas_selspr.get_prompt("rtable_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_rtable_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="rtable_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("¿Qué quieres que ponga en el lado derecho del escritorio?")
        sel_map = {}

    m 1eua "¡Claro, [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Ah, está bien"
return


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["flowers_acs"] = {
        "_ev": "gt_flowers_acs_select",
        "_min-items": 1,
        "change": "¿Puedes poner un conjunto diferente de flores?",
        "wear": "¿Puedes poner algunas flores en tu escritorio?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_flowers_acs_select",
            category=["Escritorio"],
            prompt=store.mas_selspr.get_prompt("flowers_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_flowers_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="flowers_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("¿Qué flores te gustaría que pusiera en el escritorio?")
        sel_map = {}

    m 1eua "¡Claro, [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Ah, está bien"
return