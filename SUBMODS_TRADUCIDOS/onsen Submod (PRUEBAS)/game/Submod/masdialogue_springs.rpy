init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="masdialogue_springs",category=['misc'],prompt="¡Vamos a las aguas termales, Monika.!",pool=True,unlocked=True))

label masdialogue_springs:
    m 1ssc ".{w=0.3}.{w=0.3}."
    m 1fsd "...Oh.{w=0.8} ¡Oh!{w=0.6} Ya veo..."
    m 1ftx "Sííííí.{w=0.9} No."
    m 2dfc "{w=0.3}Nop."
    m 7dfo "No te voy a dejar descargar ese submod.{w=0.5} De ninguna manera."
    m 4tfx "¿En qué estabas pensando al descargar algo así,{w=0.2} en un día como este?"
    m 5dfc "No{w=0.3}, no{w=0.3}, no."
    m 5nfa "..."
return
