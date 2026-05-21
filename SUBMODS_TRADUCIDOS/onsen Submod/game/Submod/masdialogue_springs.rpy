init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="masdialogue_springs",category=['misc'],prompt="Let's go to the onsen, Monika!",pool=True,unlocked=True))

label masdialogue_springs:
     m 1ssc ".{w=0.3}.{w=0.3}."
     m 1fsd "...Oh.{w=0.8} Oh!{w=0.6} I see."
     m 1ftx "Yeaaaaaah.{w=0.9} No."
     m 2dfc "{w=0.3}Nope."
     m 7dfo "I'm not letting you download that submod.{w=0.5} No way."
     m 4tfx "What were you thinking{w=0.2}, downloading such a thing on a day like this?"
     m 5dfc "Nuh{w=0.3}, uh{w=0.3}, uh."
     m 5nfa "..."
return
