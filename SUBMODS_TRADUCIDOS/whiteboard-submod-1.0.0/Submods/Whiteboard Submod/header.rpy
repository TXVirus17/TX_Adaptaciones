# This file is part of Whiteboard submod by Friends of Monika.(Traducido por TX_Virus)
# Report issues and ask questions at https://github.com/friends-of-monika/mas-whiteboard/issues

init -990 python:
    store.mas_submod_utils.Submod(
        author="Friends of Monika",
        name="Whiteboard Submod",
        description=_("¡Añade una pizarra (virtual) para que puedas dibujar!\n(Traducido por TX_Virus)"),
        version="1.0.0",
        settings_pane="fom_whiteboard_settings_pane"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Whiteboard Submod",
            user_name="friends-of-monika",
            repository_name="mas-whiteboard",
            extraction_depth=2
        )
