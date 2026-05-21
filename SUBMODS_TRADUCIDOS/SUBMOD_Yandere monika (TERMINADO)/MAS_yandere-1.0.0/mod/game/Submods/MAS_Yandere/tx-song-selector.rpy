# daes-song-selector.rpy
# Selector manual de canciones yandere del submod "MAS_Yandere" para el mod "Monika After Story".
# Este archivo es independiente y no modifica ningún archivo del submod original para respetar los terminos de la licencia.
# Compatible con Android, Linux, Windows y Mac.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_song_selector",
            category=['Yandere'],
            prompt="¿Puedes cantarme algo... especial?",
            pool=True,
            unlocked=True,
        )
    )

label yaMod_song_selector:
    m 1tua "Oh... ¿Algo 'especial', [player]? {w=0.5}Me encanta que me pidas eso."
    m 3tfu "¿Cuál te gustaría escuchar?"
    menu:
        "Super Psycho Love":
            call yaMod_song_superpsycholove
        "The Horror of Our Love":
            call yaMod_song_thehorrorofourlove
        "Smoke and Mirrors":
            call yaMod_song_smokeandmirrors
        "You're Mine":
            call yaMod_song_youremine
        "You Belong to Me":
            call yaMod_song_youbelongtome
        "The Music of the Night":
            call yaMod_song_themusicofthenight
        "Mejor en otro momento~":
            m 1eka "Oh, entiendo... {w=0.3}Guardaré estas melodías para más tarde."
    return
