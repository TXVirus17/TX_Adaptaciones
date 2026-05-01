init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="funfactmental_mental_illnesses",
        ),
        code="FFF"
    )
#TRADUCCION HECHA POR ALKAID
label funfactmental_mental_illnesses:
    m 3euc "¿Sabías que en realidad hay más de 300 discapacidades mentales?"
    m 3eud "¡Es una cantidad increíble, ¿no es así, [player]?"
    m 2euc "Aunque estas son solo las discapacidades documentadas."
    m 3eua "¡Estoy segura de que hay muchas más que ni siquiera están documentadas aún!"
    m 7eub "¡Eso significa que siempre hay más por aprender!"
    # Llamar al final
    call mas_fun_facts_end
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_misdiagnoseshistory",
        ),
        code="FFF"
    )

label mental_misdiagnoseshistory:
    m 3euc "¿Sabías que el autismo solía diagnosticarse como esquizofrenia en 1908?"
    m 3eud "Esto se debe a que antes de que se hiciera investigación y se creara el término oficial de autismo, solo se reconocían las similitudes de la esquizofrenia."
    m 7eud "Obviamente, esto cambió más después de la década de 1940, después de que Grunya Sukhareva comenzara a estudiar más de estos casos e incluso creara la teoría del autismo."
    m 3euc "Aunque su trabajo no se cita en ningún estudio moderno sobre el autismo..."
    m 1eud "Hay mucha historia del autismo aquí... "
    extend 3eub "¡Es realmente interesante también!"
    call mas_fun_facts_end
return


init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_PTSD_Anxietyfunfact",
        ),
        code="FFF"
    )

label mental_PTSD_Anxietyfunfact:
    m 3eua "¿Sabías que el TEPT se considera un trastorno de ansiedad?"
    m 1ruc "Parece bastante obvio cuando lo piensas, así que tal vez sí lo sabías."
    m 7euc "De todos modos, la razón por la que el TEPT se considera un trastorno de ansiedad es debido al miedo constante a que lo que sucedió pueda volver a ocurrir."
    m 1eud "En comparación con un trastorno de ansiedad que tiene el miedo constante a la {i}posibilidad{/i} de que algo suceda alguna vez."
    m 1eua "Siempre hay más en los trastornos de lo que piensas, y todos están conectados de alguna manera."
    call mas_fun_facts_end

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_conformist_trendsFF",
        ),
        code="FFF"
    )

label mental_conformist_trendsFF:
    m 3eua "¿Sabías que a alguien que siempre intenta quedar bien ante los demás se le llama [i]conformista[i/]?"
    m 7eud "Un conformista, en su término básico, significa que una persona se preocupa más por su imagen pública que por lo que cree."
    m 1rusdlb "Es un poco como un ídolo, o incluso una famosa estrella pop."
    m 1euc "Aunque hay formas más graves de conformismo, generalmente no es algo demasiado malo."
    m 3eud "Como, por ejemplo, alguien que tiende a hacer de su objetivo de vida ser querido por todos."
    m 1duc "Es una espiral bastante negativa en la que entrar."
    m 1eua "De todos modos, creo que me estoy desviando del tema aquí."
    call mas_fun_facts_end
