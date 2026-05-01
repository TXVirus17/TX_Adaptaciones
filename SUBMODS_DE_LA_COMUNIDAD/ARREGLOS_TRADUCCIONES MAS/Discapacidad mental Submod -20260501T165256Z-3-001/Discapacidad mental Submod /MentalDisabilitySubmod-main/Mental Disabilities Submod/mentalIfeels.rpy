init 5 python:
    addEvent(Event(persistent._mas_mood_database,eventlabel="mentalhealth_isolated",prompt="...Como si no perteneciera a ningún lugar...",category=[store.mas_moods.TYPE_BAD],unlocked=True),code="MOO")
#TRADUCCION HECHA POR ALKAID
label mentalhealth_isolated:
    m 1ekc "Lamento que te sientas así."
    m 1dkd "Imagino que debe ser bastante desalentador nunca sentirte que encajas."
    if persistent._mas_pm_has_friends:
            if persistent._mas_pm_few_friends:
                m 1eud "Pero ¿tenés algunos amigos cercanos, no, [player]?"
                m 3eub "Deberías verlo como encontrar tu lugar para brillar y ser vos mismo."
                m 7euc "Y si ese no es el caso...{w=0.4} Deberías decirles cómo te sentís realmente."
                jump MentalIsolatedFriends

            else:
                m 1eud "¿Tenés algunos amigos con quienes puedas hablar, no, [player]?"
                m 3eub "Eso solo muestra que tenés tu propio lugar para brillar y ser vos mismo."
                m 7euc "Pero, si ese no es el caso con tus amigos...{w=0.4} Deberías decirles cómo te sentís realmente."
                jump MentalIsolatedFriends


    else:
        m 3ekc "Todavía no tenés a nadie con quien puedas hablar, ¿verdad, [player]?"
        m 1dkc "Yo-{w=0.4} Realmente desearía poder hacer más por vos."
        # Agregar diálogo que mencione si el jugador tiene una discapacidad, y Monika espera que eso no esté jugando un papel
        m 2dtc "Pero por ahora, [player]...{w=1.1}{nw}"
        extend 1etc "Lo único que podés hacer es seguir intentando."
        m 3ekc "Buscar lugares donde encajar puede ser bastante difícil, especialmente si sos vocal sobre tus opiniones..."
        m 7etd "Tal vez podrías intentar buscar lugares para hablar con otros en línea."
        m 1ekb "¡Y quizás incluso puedas encontrar algunos amigos en internet también!"
        m 1ftc  "Solo seguí intentando por mí, [player]."
        m 1dkc "Rendirse no arreglará nada."
        m "...{w=3.0}{nw}"
        m 1etc "De todos modos, [player]...{w=0.6}{nw}"
        m 1eka "Haré todo lo posible para asegurarme de que te sientas como en casa aquí."
        m 7dta "Es lo menos que puedo hacer por vos, [player]."
return


label MentalIsolatedFriends:
    m 1etd "Estoy bastante segura de que tus amigos entenderán cómo te sentís."
    m 2dkc "Mantenerse callado sobre cómo te sentís solo conducirá a más problemas..."
    if persistent._mas_pm_cares_about_dokis:
        m 2ekd "Lo último que quieres es terminar sintiéndote como Sayori."
    m 3ekd "Meterse en esa espiral descendente es realmente malo."
    m 1eksdlc "Solo causa más daño, [player]."
    m 3fkc "Ya sea que te sientas odiado o no, pertenecés a algún lado, [player]."
    m 1etc "Puede que no lo sepas ahora...{w=0.2} Pero {i}sí{/i} pertenecés a algún lugar."
    m 1rtsdlc "Te llevará un tiempo descubrir dónde..."
    m 1eka "Pero mientras tanto, haré todo lo que pueda para ayudarte a sentirte como en casa, [player]."
return
