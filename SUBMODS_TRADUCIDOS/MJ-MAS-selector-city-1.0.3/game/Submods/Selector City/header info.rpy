#credit to my-otter-self / your-otter-friend for help with the repo, creds to raVen and (sigh) ATOM_real for original selector code to base all these on

init -990 python in mas_submod_utils:
    Submod(
        author="MayJay",
        name="Selector City",
        description="Una colección de selectores mantenida por u/mayday-mayjay en un área para utilizar el actualizador de submods. Por favor, abre un problema en el repositorio o ve a mi servidor de trabajo de submods si hay algún problema: https://discord.gg/Tx23rczN8N\n{size=5}(Traduccion por TX_Virus){/size}",
        version="1.0.3",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Selector City",
            user_name="mayday-mayjay",
            repository_name="MJ-MAS-selector-city",
            submod_dir="/Submods/Selector City",
            extraction_depth=3,
            redirected_files=(
                "README.md"
            )
        )
