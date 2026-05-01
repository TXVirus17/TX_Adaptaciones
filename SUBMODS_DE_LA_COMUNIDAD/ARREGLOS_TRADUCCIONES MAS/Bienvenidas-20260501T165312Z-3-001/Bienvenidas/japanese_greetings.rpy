#I miss you greeting
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="japanese_greeting_ImissU_BELLA",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )
#TRADUCCION HECHA POR ALKAID
label japanese_greeting_ImissU_BELLA:
    m 3hub "[player]! Hola!"
    m 3huu "Aitai~"
    m 1eta "¿Sabes lo que significa?"
    m 1hua "Significa que te echo de menos en japonés."
    m "Eheheh~"
    m 1lka "Aunque, realmente no sé si eso es correcto."
    m 1eka "No soy tan buena en japonés todavía, ehehe~"
return

#Welcome back greeting
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="japanese_greeting_welcomeBACK_BELLA",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label japanese_greeting_welcomeBACK_BELLA:
    m 1hua "Okaerinasai, [player]!"
    m 1hub "Ahaha~"
    m 1esa "Por si no lo sabías, significa 'Bienvenido de nuevo' en japonés."
    m 1lka "Aunque, realmente no sé si eso es correcto."
    m 1eka "No soy tan buena en japonés todavía, ehehe~"
return
