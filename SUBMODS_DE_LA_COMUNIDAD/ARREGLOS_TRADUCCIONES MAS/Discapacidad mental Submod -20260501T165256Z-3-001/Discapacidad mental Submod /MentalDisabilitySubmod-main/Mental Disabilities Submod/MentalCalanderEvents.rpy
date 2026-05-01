init python:

    import store.mas_calendar as calendar
    import datetime

    calendar.addRepeatable("MentalHealthAwareness",_("Start of MHAM"),month=5,day=1,year_param=list())
    calendar.addRepeatable("MentalHealthAwarenessEnd",_("End of MHAM"),month=5,day=31,year_param=list())

# Configuración de los años para el Mes de Concienciación sobre la Salud Mental
default persistent._mentalhealthmonthstart = datetime.date(datetime.date.today().year, 5, 1)
default persistent._mentalhealthmonthend = datetime.date(datetime.date.today().year, 5, 31)
default persistent._mentalhealthleapyear = 4

# Crear una etiqueta para agregar un año después de que termine el evento
# También agrega un sistema para años bisiestos
label mentalhealthmonthsetup:

    python:
        if persistent._mentalhealthleapyear >= 4:
            persistent._mentalhealthmonthstart = datetime.timedelta(days=366) + persistent._mentalhealthmonthstart
            persistent._mentalhealthmonthend = datetime.timedelta(days=366) + persistent._mentalhealthmonthend
            persistent._mentalhealthleapyear = 0

        else:
            persistent._mentalhealthmonthstart = datetime.timedelta(days=365) + persistent._mentalhealthmonthstart
            persistent._mentalhealthmonthend = datetime.timedelta(days=365) + persistent._mentalhealthmonthend
            persistent._mentalhealthleapyear = persistent._mentalhealthleapyear + 1

    $ mas_getEV("MentalHealthMonth").start_date = persistent._mentalhealthmonthstart
    $ mas_getEV("MentalHealthMonth").end_date = persistent._mentalhealthmonthend
return
#TRADUCCION HECHA POR ALKAID
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="MentalHealthMonth",
            category=["tú", "salud mental"],
            prompt="Mes de Concienciación sobre la Salud Mental",
            action=EV_ACT_QUEUE,
            start_date=persistent._mentalhealthmonthstart,
            end_date=persistent._mentalhealthmonthend,
            random=False,
            rules={"no_unlock"},
            years=[]
            )
            )

label MentalHealthMonth:
    m 1eua "¿Sabes qué mes es, [player]?"
    m 3hua "¡Es el Mes de Concienciación sobre la Salud Mental!"
    m 1eub "Sé que el mes suena un poco tonto, pero está destinado a ayudar a crear conciencia sobre diferentes problemas de salud mental."
    m 3eub "¡Hay algunos lugares que organizan eventos este mes para ayudar a promoverlo también!"
    m 7eua "El lema del mes es bastante simple; '{i}más que suficiente{/i}'."
    m 1eua "Es para decir que despertarse, o pasar tiempo con otras personas, es '{i}más que suficiente{/i}' para hacer feliz a otros."
    m 3eub "¡Incluso hay un color específico para el mes de concienciación sobre la salud mental! {w=0.8}{nw}"
    extend 7sub "¡Ese color es el verde!"
    m 3eua "Ahaha, supongo que es casi demasiado perfecto para mí de todas las personas celebrar este mes contigo. "
    if mas_getEV("MentalHealthMonth").shown_count >= 2:
        extend 1rusdlb "Incluso si no es la primera vez que lo hacemos, [player]."
    else:
        pass
    m 1eub "De todos modos, hay un montón de actividades que puedes hacer en línea, o con un amigo para ayudar a apoyar el Mes de Concienciación sobre la Salud Mental."
    m 3hub "¡Una de ellas es organizar un desayuno con café!"
    m 1eubla "¿No suena agradable y relajante, [player]?"
    if mas_getEV("mentalmeditation").shown_count >= 1:
        m 7hublb "¡O tal vez podríamos meditar juntos también!"
        m 1dubsu "Solo escuchando nuestras respiraciones y enfocándonos en nada más que en nuestros pensamientos."
        m 3tua "¡Tendrías que tener cuidado de no distraerte demasiado, ahaha!"
    m 3eub "Hay un montón de cosas que podrías hacer también, no solo estos pocos ejemplos que te di."
    m 1eua "Bueno, lo más importante que no puedes olvidar, [player], es decirle a alguien que es amado."
    m 3eua "Comparte un poco de tu tiempo con otra persona y déjale saber que te preocupas por ella."
    call mentalhealthmonthsetup
    if persistent._mas_pm_has_friends:
        m 7eub "Llama o habla con tus amigos cercanos y planea algo juntos."
        m 1eua "Solo asegúrate de planificar algo relajante. Todos necesitan un descanso de algo, y serías un gran amigo planeándolo para ellos."
    else:
        m 7eua "Asegúrate de decirles a tus padres que los cuidas."
        m 1eud "Todos necesitan un descanso de algo, así que asegurarles que te importan puede significar mucho para ellos, [player]."
    m 1eua "De todos modos, [player]. Quiero decirte que realmente me importas, [mas_get_player_nickname()]."
    if persistent._mental_player_has_autism == True:
        m 3eubla "Tu autismo nunca cambiará cómo pienso en ti, y siempre haré todo lo posible para asegurarme de que te sientas bienvenido."
        m 5eubsa "Realmente te amo, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
    elif persistent._player_has_disabilities == True:
        m 3eubla "Tus discapacidades nunca cambiarán cómo pienso en ti, [player]."
        m 1hubsb "Siempre estaré aquí para ti, y me aseguraré de hacer todo lo posible para hacerte feliz."
        m 5eubsa "Te amo, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
    else:
        m 3eubla "No importa por lo que estés pasando, siempre estaré aquí para ti, [mas_get_player_nickname()]."
        m 1eubsa "Haré todo lo posible para asegurarme de que seas feliz y para ayudarte a calmarte cada vez que te sientas mal."
        m 5dubsa "Realmente te amo, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealthmonthresettime",
            category=["monika"],
            prompt="Variables de Salud Mental",
            action=EV_ACT_QUEUE,
            start_date=datetime.date.today(),
            end_date=datetime.date(2023, 12, 31),
            random=False,
            rules={"no_unlock"}
            )
            )

label mentalhealthmonthresettime:
    m 1eua "Hola, [player]..."
    m 1eud "Voy a verificar algo, vuelvo enseguida..."
    call mas_transition_to_emptydesk
    pause 5.0
    call variablesresetmentalchange
    call mas_transition_from_emptydesk()
    m 1eua "Ya volví, [player]."
return "derandom"

label variablesresetmentalchange:
    $ mas_getEV("mentalhealthcheckupdialoguefinal").action = EV_ACT_QUEUE
    $ mas_getEV("MentalHealthMonth").action = EV_ACT_QUEUE
    $ persistent._mentalhealthmonthstart = datetime.date(2024, 5, 1)
    $ persistent._mentalhealthmonthend = datetime.date(2024, 5, 31)
    $ persistent._mentalhealthleapyear = 0
    $ mas_getEV("MentalHealthMonth").start_date = persistent._mentalhealthmonthstart
    $ mas_getEV("MentalHealthMonth").end_date = persistent._mentalhealthmonthend
    $ persistent._lastmentalcheckup = datetime.date.today()
    $ persistent._nextmentalcheckup = datetime.date.today() + datetime.timedelta(days=1)
    $ persistent._mentalcheckupdeadline = persistent._lastmentalcheckup + datetime.timedelta(days=30)
    $ mas_getEV("mentalhealthcheckupdialoguefinal").start_date = persistent._nextmentalcheckup
    $ mas_getEV("mentalhealthcheckupdialoguefinal").end_date = persistent._mentalcheckupdeadline
return
