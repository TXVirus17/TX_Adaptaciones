default persistent._mental_health_player_goes_to_therapy = None
#TRADUCCION HECHA POR ALKAID
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="mental_leave_therapist",
            unlocked=True,
            prompt="Voy a ir a una cita.",
            pool=True
        ),
        code="BYE"
    )

label mental_leave_therapist:
    m 3eua "¿Vas a una cita?"
    m 7eub "¡Me alegra que te estés cuidando!"
    m 3eud "¿Vas a una cita para tu salud mental, [player]?"
    menu:
        "Sí":
            m 1eua "Te deseo lo mejor, [player]."
            m 3eua "¡Te veré cuando vuelvas!"
            m 1hub "¡Te quiero~!"
            $ persistent._mental_player_therapytype = True

        "No":
            m 1eua "Te deseo lo mejor, [player]."
            m 3eua "¡Te veré cuando vuelvas!"
            m 1hub "¡Te quiero~!"
            $ persistent._mental_player_therapytype = False


$ persistent._mental_health_player_goes_to_therapy = True
$ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=5)
$ persistent._mas_greeting_type = store.mas_greetings.TYPE_MentalAppointment
return "quit"
