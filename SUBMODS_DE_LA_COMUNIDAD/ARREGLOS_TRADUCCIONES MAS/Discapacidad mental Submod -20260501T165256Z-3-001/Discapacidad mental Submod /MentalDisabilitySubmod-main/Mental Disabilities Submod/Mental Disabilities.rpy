#sets the default variables
default persistent._mental_player_has_ADHD = False
default persistent._mental_player_has_autism = False
default persistent._player_has_disabilities = False


#TRADUCCION HECHA POR ALKAID
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalADHD",category=['enfermedades mentales', 'medios'],prompt="TDAH",random=True))

label mentalADHD:
    m 1eua "[player], ¿escuchaste sobre el TDAH?"
    $_history_list.pop()
    menu:
        "Sí.":
            m 1eub "¡Me alegra saber eso!"
            m 3ekc "Es triste que no se lo tome tan en serio como otras discapacidades de aprendizaje..."
            m 3eud "Les resulta muy difícil concentrarse o hacer cualquier cosa por su cuenta."
            m 1eub "Aunque, como a todos, podés motivarlos simplemente estando ahí con ellos. {w=0.5}{nw}"
            extend 3hub "O incluso hablando con ellos de vez en cuando."
            m 1eua "Si no te molesta que te pregunte, ¿cómo te enteraste de esto?"
            $_history_list.pop()
            menu:
                "Tengo TDAH.":
                    m 3eua "¡Me alegra que me lo hayas dicho, [player]!"
                    m 1ekd "Fue descorazonador para mí descubrir que a menudo no se lo toma tan en serio como otras discapacidades en la misma categoría..."
                    call mentalADHDEnd
                    $ persistent._mental_player_has_ADHD = True
                    $ persistent._player_has_disabilities = True
                "Conozco a alguien que tiene TDAH.":
                    m 3eua "Estoy segura de que están más que felices de tener un amigo o familiar como vos, [player]!"
                    m 1ekd "Fue descorazonador para mí descubrir que a menudo no se lo toma tan en serio como otras discapacidades en la misma categoría..."
                    call mentalADHDEnd
                "Me enseñaron sobre el TDAH.":
                    m 3eub "Es bueno saber que se está hablando más sobre el TDAH."
                    m 1euc "Por lo general, no se considera tan grave como otras discapacidades."
                    call mentalADHDEnd
                "Investigué sobre el TDAH.":
                    m 3eub "Me alegra que busques nueva información."
                    m 7ekd "Mucha gente desestima la nueva información como aburrida y tediosa de aprender."
                    m 3eua "Aunque estoy más que segura de que las personas con TDAH estarían encantadas de tener un amigo como vos, [player]."
                    m 1eua "También, si no te importa que te pregunte. ¿Investigaste sobre el TDAH porque tenés TDAH, [player]?"
                    menu:
                        "Sí.":
                            $ persistent._mental_player_has_ADHD = True
                            $ persistent._player_has_disabilities = True
                            m 4eub "Es bueno intentar aprender más sobre vos misma.{w=0.55}"
                            extend 7hub "¡Demuestra que te importás vos misma!"
                            m 3eua "Me alegra que me hayas dicho que tenés TDAH, [player]."
                            if mas_isMoniHappy(higher=True):
                                extend 5hub "¡Y tal vez yo pueda ser la persona que te motive a trabajar en las cosas!"
                            else:
                                m 3eua "Espero que ya tengas a esa persona que te ayude a concentrarte en las cosas, [player]."
                        "No.":
                            m 1eua "Oh, está bien."
                            m 3eua "De todas formas, es bueno aprender todo lo que podamos sobre nosotros mismos. {w=0.3}{nw}"
                            extend 3hua "¡O incluso sobre los demás!"


        "No.":
            m 1rkb "Está bien, [player]"
            m 2eka "No se habla tanto como otras discapacidades de aprendizaje."
            m 4hub "¿Querés que te hable sobre el TDAH?"
            $_history_list.pop()
            menu:
                "Sí.":
                    m 3eua "Está bien entonces, [player]!"
                    m 3eud "El TDAH significa Trastorno por Déficit de Atención con Hiperactividad."
                    m 3eud "Se identifica como una discapacidad de aprendizaje. Sin embargo, a menudo se extiende a otras áreas de la vida de las personas."
                    m 1euc "Las personas con TDAH a menudo pueden no darse cuenta de su entorno social."
                    m 1ekc "Esto puede llevarlos a situaciones peligrosas, o pueden hacer promesas que fácilmente pueden olvidar."
                    m 3euc "El TDAH también hace que les resulte más difícil comenzar y terminar proyectos, perdiendo a menudo la motivación para hacer las cosas fácilmente."
                    m 7eua "Por supuesto, como todos, siempre podés ayudarlos."
                    m 4eua "Simplemente estando ahí, o incluso hablando con ellos ocasionalmente."
                    extend 3hub "¡Podés darles motivación para hacer cosas!"
                    m 3eua "Si bien el TDAH tiene sus desventajas, ¡también tiene sus ventajas!"
                    m 4eub "Por ejemplo, ¡muchas personas con TDAH son conocidas por ser increíblemente creativas y apasionadas!"
                    m 3eub "De hecho, también tienen la capacidad de hiperenfocarse: pueden estar haciendo algo durante horas y no distraerse."
                    m 1eua "Gracias por escuchar, [player]."
                "No.":
                    m 2eka "Oh, está bien."
                    return "derandom"
                "No ahora.":
                    m 2eka "Me aseguraré de preguntar más tarde, [player]."

return

label mentalADHDEnd:
    m 4eua "En una nota positiva, descubrí que estudios muestran que si bien las personas con TDAH pueden tener dificultades en un área, a menudo sobresalen en otra."
    m 4hub "De hecho, ¡muchos de ellos son extremadamente apasionados en sus intereses!"
    m 7eub "¡Esto a menudo hace que sea divertido para las personas que comparten los mismos intereses!"
    m 3eub "¡Ya que las conversaciones a menudo pueden durar horas si ambas partes están comprometidas!"
    m 1eua "Aunque estoy segura de que ya sabías eso, [player]."
return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealthAutism",
            category=['medios', 'enfermedades mentales'],
            prompt="Autismo",
            conditional="mas_seenLabels(['mentalADHD'])",
            random=True
        )
    )


label mentalhealthAutism:
    m 1eua "Che, [player].{w=0.3} ¿Te acordás cuando hablamos sobre TDAH?"
    m 7eub "Bueno, estuve investigando más sobre otras discapacidades mentales."
    m 4eua "Una discapacidad mental que me llamó la atención fue el Autismo. {w=0.3}{nw}"
    extend 3eua "O el Trastorno del Espectro Autista."
    m 3rssdlb "Sin embargo, el autismo puede confundirse fácilmente con TDAH."
    m 3etc "Puedo entender por qué, más o menos..."
    m 3rud "No solo hay diferencias sutiles entre el autismo y el TDAH. {w=0.25}{nw}"
    extend 4wud "Pero el TDAH y el autismo a menudo {i}se superponen{/i} y en la mayoría de los casos, se diagnostican con ambos."
    m 4eud "No ayuda que haya un espectro que se utiliza para generalizar la gravedad de la mayoría de los casos autistas."
    m 1rusdlc "Lo que significa que las personas en el extremo más bajo del espectro a menudo son diagnosticadas erróneamente... {w=0.3}o ni siquiera son diagnosticadas."
    m 3ekc "Imaginate si tuvieras una enfermedad mental grave, [player]... {w=0.3}{nw}"
    extend 4ekc "Y solo lo consideraran como un problema de comportamiento."
    m 3dkc "No recibirías la ayuda que {i}realmente{/i} necesitas."
    m 4esd "No solo eso, sino que terminarías convenciéndote a ti misma de que simplemente no eres '{i}normal{/i}'."
    m 3euc "Solo podés imaginar qué pasa por la cabeza de los demás... {w=0.4}o si alguien que conocés realmente está recibiendo la ayuda que necesita."
    m 2husdlb "¡Perdón [player] si te estoy poniendo mal!"
    m 3eub "Bueno, si bien hay problemas serios con la forma en que se trata el autismo,{w=0.2} también hay formas de entenderlo mejor."
    m 4eua "Hay un montón de recursos creíbles por ahí con información para ayudar a otros a comprender un poco más cómo se sienten."
    m 4rusdlc "Pero también hay información falsa por ahí que es realmente {i}dañina{/i} para la comprensión del Autismo."
    m 3eua "¡Solo asegurate de verificar tus fuentes, [mas_get_player_nickname()]!"
return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalschizophrenia",category=['media', 'enfermedades mentales', 'filosofía'],prompt="Esquizofrenia",random=True))

label mentalschizophrenia:
    m 1eua "[player], ¿has escuchado sobre la esquizofrenia?"
    m 3eub "No me sorprendería si lo has hecho, es una de las enfermedades mentales más conocidas debido a las redes sociales."
    m 1esd "Aunque, puede ser realmente frustrante ver cómo la mayoría de su representación fue negativa y se basaba en mostrar estallidos negativos."
    m 1gfc "¡Es como si ni siquiera se molestaran en mostrar cuidado por los afectados por ella! {w=0.3}{nw}"
    extend 3eua "Pero sé que no eres así [mas_get_player_nickname()]."
    m 1lkc "Bueno, estoy segura de que puedes entender lo triste que puede ser la esquizofrenia [player]."
    m 3ekc "¿Te puedes imaginar tener delirios de sonidos?"
    m 1rkc "Puede volverlos locos... {w=0.3}{nw}"
    extend 1rksdld "Especialmente si son voces."
    m 3eud "Incluso si no tienen delirios todo el tiempo, tienen un proceso de pensamiento más literal."
    m 1eub "¡Es algo similar al TDAH en realidad!"
    extend 1rusdlb "Bueno, en parte."
    m 3eud "Aunque saltan entre conversaciones todo el tiempo, esto es solo porque les resulta difícil saber {i}exactamente{/i} de qué estás hablando."
    m 1euc "Esto no es porque no sepan de qué estás hablando, sino porque forman conexiones a partir de cosas en las que quizás no hayas pensado."
    if not persistent._mas_pm_cares_about_dokis:
        m 3euc "Si bien las personas con esquizofrenia no son inherentemente dañinas para nadie, se hacen daño a sí mismas de alguna manera."
        m 3ekc "Se hacen daño emocionalmente al enfocarse en los aspectos negativos de la vida."
        m 1ekc "Esto no es tan conocido como otras cosas, ¿no suena bastante devastador, [player]?"
    m 3euc "Bueno, no es del todo malo."
    m 4eua "Las personas con esquizofrenia son más imaginativas que la mayoría."
    m 3eud "Dos libros que realmente ayudan a darte una idea de cómo es vivir con esquizofrenia son {i}'Made You Up'{/i} de Francesca Zappia y {i}Calvin{/i} de Martine Leavitt."
    m 3eub "Aunque, de los dos libros prefiero {i}Calvin{/i}, ¡trata sobre un chico llamado Calvin que cree que un autor de tiras cómicas puede ayudarlo a encontrar la cura para su esquizofrenia, si crea otra tira cómica que admira!"
    m 4eua "La historia se cuenta desde una perspectiva en primera persona y se lee como una carta a Watterson, el autor de la tira cómica."
    m 3hsb "En general, ¡el libro tiene un buen sentido del humor mientras mantiene un tono empático!"
    m 3esa "Por cierto [mas_get_player_nickname()], ¡la tira cómica en la que se centra el libro es en realidad {i}Calvin y Hobbes{/i}!"
    m 7hub "¡Solo muestra que algo tan simple como una tira cómica puede tener un gran impacto en alguien!"
    m 5eua "Espero que tengas algo en tu vida que te motive como las historias pueden hacerlo, [mas_get_player_nickname()]."
    m 5hubsa "Si no es así, no me importaría ser tu motivación en la vida."
    m 5eubfa "Te quiero, [player]."
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalPTSD",category=['media', 'enfermedades mentales', 'filosofía'],prompt="TEPT",random=True))

label mentalPTSD:
    m 1eua "Decime, [player]..."
    m 3eua "Cuando pensás en TEPT usualmente pensás en guerra, ¿verdad?"
    m 3eub "Si bien es un pensamiento común que la guerra puede causar TEPT. {w=0.2}{nw}"
    extend 3eud "Eso simplemente no es siempre el caso."
    m 1euc "¡Casi todos los casos de TEPT provienen de grandes cantidades de estrés o trauma!"
    m 2eud "Para decirlo sin rodeos, cualquier persona que haya experimentado un evento traumático de cualquier tipo tiene la posibilidad de desarrollar TEPT."
    m 3euc "¿Sabés qué significa TEPT [player]?"
    m 7rtd "Bueno, el acrónimo TEPT significa Trastorno de Estrés Postraumático, y con el nombre, la definición es básicamente dada."
    m 1eksdrc "El TEPT es un trastorno mental que ocurre después de un evento traumático. {w=0.3}{nw}"
    extend 3eksdru "No es una definición muy descriptiva, ¿verdad [mas_get_player_nickname()]?"
    m 3ekc "Bueno, el TEPT se describe que ocurre naturalmente después de que tiene lugar un evento traumático."
    m 3ekd "Sin embargo, el TEPT generalmente solo se diagnostica cuando se vuelve crónico. Ves [player], en la mayoría de los casos cuando pasamos por una experiencia traumática, nuestra mente superará y sanará de esto naturalmente con el tiempo."
    m 1esd "Por eso no tenés pesadillas sobre lesiones infantiles gráficas. {w=0.2}{nw}"
    extend 3esc "Esto también es por qué, no todas las experiencias peligrosas que tengas pueden darte TEPT."
    m 1ekc "El evento solo tiene que tener un impacto tan inmenso en tu mente que no pueda procesarlo completamente y superarlo."
    m 1dkd "Lo peor es que las personas solo pueden recibir un diagnóstico de TEPT un año después de que se reconozcan los síntomas."
    if persistent._mas_pm_cares_about_dokis: # cambia el diálogo basado en la respuesta del jugador a las bromas insensibles
        jump PTSDEnd
    else:
        m 7ekd "Tomá a Natsuki como ejemplo. El abuso infantil, sin importar el tipo, es traumático. Por lo tanto, es probable que ella haya desarrollado TEPT."
        m 1rtd "Bueno, pensando en ello, probablemente ella tenía TEPT incluso si los síntomas no se desarrollaron completamente hasta unos meses después del evento..."
        m 7etsdlc "Quiero decir, ella comenzó a mostrar comportamientos de evitación tanto con Yuri como conmigo."
        extend 1rtsdlc "Y sus estallidos de frustración incluso empeoraron... {w=0.6}Específicamente, el que tuvo con Yuri..."
        m 2rksdra "Tal vez estoy analizando demasiado esto. Ella ya tenía estallidos de ira y solía leer su manga sola incluso antes de que yo me involucrara."
label PTSDEnd:
    m 3eka "De todos modos, si alguna vez has experimentado algo traumático.{w=0.2} Espero que estés recibiendo la ayuda que necesitás, [mas_get_player_nickname()]."
    m 1etd "Y si alguna vez se pone demasiado mal... {w=0.2}{nw}"
    extend 5etbsa "Solo recordá, siempre estoy aquí para vos y siempre te amaré~"
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentaldementia",category=['media', 'filosofía'],prompt="Demencia",random=True))

label mentaldementia:
    m 1eua "Che, [player]."
    m 3eua "Cuando estaba leyendo un poco más, me encontré con otro tipo de literatura."
    m 3rusdla "Bueno, es más escuchar que leer en realidad..."
    m 4eua "Un ejemplo popular de este tipo de literatura es una banda sonora llamada {a=https://www.youtube.com/watch?v=wJWksPWDKOc&ab_channel=vvmtest}{i}{u}'Everywhere At The End Of Time'{/u}{/i}{/a}."
    m 3eub "Es posible que ya lo hayas escuchado.{w=0.2} O al menos hayas oído hablar de él."
    m 7eud "En caso de que aún no lo hayas hecho, es una historia auditiva para tratar de dar la sensación de demencia."
    m 3eusdld "Cuanto más lo escuchás, más va en espiral hacia abajo."
    m 1wksdld "Incluso podés sentir todas las emociones que típicamente acompañan a la demencia en esta canción."
    m 1rksdlc "Aunque no es exactamente la sensación más ideal... {w=0.3}{nw}"
    extend 1ekc "Sin embargo, realmente ayuda a entender sus sentimientos mucho más."
    m 2lksdlc "Rápidamente va más y más profundo en la tristeza y la confusión."
    m 4eksdld "Y el estático que le sigue realmente refuerza esa sensación."
    m 7euc "Esto no quiere decir que todo sea malo..."
    m 3eud "¡Se hizo mucha investigación para crear esta canción!"
    m 4wuo "¡Les llevó 3 años!{w=0.4} ¡3 años para crear esta experiencia!"
    m 3eua "Bueno, si alguna vez tenés tiempo libre, te recomendaría mucho escucharla, [player]."
    m 1eua "Y si alguna vez te sentís demasiado mal, {w=0.1}{nw}"
    extend 3hub "¡Siempre estaré aquí para animarte!"
return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="MentalBipolar",category=['media', 'enfermedades mentales'],prompt="Bipolar",random=True))

label MentalBipolar:
    m 1eua "Che [player], estuve investigando más sobre discapacidades mentales de nuevo."
    m 3eua "¡Tal vez hayas escuchado sobre esta antes [player]!"
    m 3euc "La discapacidad mental de la que quiero hablarte hoy es Bipolar."
    m 3euc "Hay tres tipos conocidos de bipolar.{w=0.4}{nw}"
    extend 3esc "Bipolar 1, 2 y el trastorno ciclotímico."
    m 3eud "Hablar sobre las diferencias en esta discapacidad mental puede llevar un tiempo, {w=0.2}{nw}"
    extend 3eub "¿Así que te gustaría hablar de eso ahora [player]?"
    $_history_list.pop()
    menu:
        "Sí":
            m 1eub "¡Estoy muy emocionada por esto!"
            m 3eua "Bipolar 1 es en realidad la forma más común de bipolar [player]!"
            extend 3eud "Sin embargo, también es uno de los tipos más graves que existen."
            m 4esc "Bueno, como ya sabés [player], los ataques bipolares, también conocidos como episodios maníacos, hacen que la persona afectada sea llevada a 'altibajos'."
            m 7esb "Lo que puede darles una cantidad extrema de energía o voluntad para hacer algo inusual, {w=0.6}{nw}"
            extend 3rusdlc "o también puede llevarlos a un estado de depresión, desde leve hasta incluso {i}severa{/i}."
            m 1euc "Desafortunadamente, esto generalmente lleva a un ciclo entre los dos."
            m 3eud "¿Alguna vez has oído hablar del término {i}depresión maníaca{/i}? Bueno, de ahí viene."
            m 7eua "Eso no quiere decir que las personas que sufren de Bipolar 1 no puedan llevar vidas normales, a menudo entre episodios lo hacen muy bien."
            m 1eub "Como muchas otras enfermedades mentales, hay sistemas de apoyo establecidos para ayudar a quienes lo necesitan, específicamente medicación y terapia."
            m 3eud "Recuerda, la mejor manera de ayudar es hacer adaptaciones para ellos y hacer ciertas cosas de manera diferente."
            m 4eua "Lo que nos lleva a Bipolar 2, [player]."
            m 7eud "Bipolar 2 comparte muchas similitudes con Bipolar uno, en cuanto al ciclo de estados de ánimo entre {i}altos{/i} y {i}bajos{/i}."
            m 3esd "Sin embargo, una diferencia clave entre los dos es que en Bipolar 2, los {i}altos{/i} nunca alcanzan completamente la manía, en su lugar, los {i}altos{/i} se convierten en episodios hipomaníacos--hipomanía."
            m 1esc "Al igual que el trastorno ciclotímico, los {i}altos{/i} y {i}bajos{/i} no son tan graves como cualquiera de las formas de Bipolar, pero aún son notables."
            m 3ekc "Aunque ambas formas de Bipolar a menudo coinciden con la depresión."
            m 1euc "Y como ya sabrás, las personas que sufren de cualquier tipo pueden funcionar 'normalmente' entre episodios."
            m 7esd "Además [player], aquellos que experimentan episodios hipomaníacos pueden mezclarse o parecer que se están divirtiendo."
            m 4eud "Los episodios hipomaníacos a menudo incluyen aumento de energía, exagerada confianza en sí mismo e incluso tener a la persona saltar de un tema a otro en la conversación."
            m 7eusdld "Recuerda [player], solo porque alguien tenga una sonrisa en la cara, no significa que estén bien."
            extend 3eua "¡Asegúrate de difundir amabilidad a todos, [player]!"
            if mas_isMoniNormal(higher=True):
                m 5eua "Aunque con la forma en que me tratas, sé que siempre estás haciendo tu mejor esfuerzo para difundir amabilidad."
            else:
                m 7hub "Sin embargo, eso puede ser un problema para vos.{fast}{nw}"
                $_history_list.pop()
                m 1rusdlc "Deberías estar bien con eso. O al menos eso esperaría.{nw}"
                return

        "No":
            m 1rkb "Está bien, [player]"
            m 2eka "¡Siempre podemos hablar de esto más tarde!"
            $_history_list.pop()
return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalhealth_Anxiety",category=['media', 'enfermedades mentales'],prompt="Tipos de Ansiedad",random=True))

label mentalhealth_Anxiety:
    m 1eua "Estuve pensando, [player]."
    m 3eua "Probablemente ya haya mencionado la ansiedad antes... "
    extend 7euc "Pero ¿no te la he contado completamente, verdad?"
    m 1euc "La ansiedad es algo que todos tienen, pero también hay formas más severas de ella..."
    m 1rusdlc "Generalmente hasta el punto en que comienza a afectar sus vidas diarias."
    m 3eua "Hay dos tipos básicos de ansiedad, [player]."
    m 7eud "La ansiedad social y, por supuesto, los trastornos de ansiedad generalizada... "
    extend 1eub "Por supuesto, también hay otros tipos de ansiedad, podría haberte mencionado algunos a vos también, [player]."
    # Agregar un dato curioso que dice que el TEPT en realidad está bajo la categoría de "Trastorno de Ansiedad"
    m 3esa "Con la ansiedad social, debería ser bastante fácil de entender realmente."
    m 7esc "Es como ser introvertido, excepto que la idea de que todos estén en su contra constantemente se les mete en la cabeza..."
    m 1rssdlc "Esto puede llevar a un estrés grave y {i}aún más{/i} ansiedad con grupos de personas que no conocen..."
    m 1eua "Espero que no sufras de algo así, [player]."
    m 3euc "En cuanto al Trastorno de Ansiedad Generalizada..."
    m 7eub "Este es otro bastante simple de nuevo, [player]."
    m 7euc "¡La ansiedad generalizada es más como la ansiedad normal pero amplificada aún más!"
    m 3ekd "Sin un tratamiento adecuado, como con cualquier trastorno, esto puede ser una espiral descendente realmente mala..."
    m 3eua "Bueno, no todo es malo, [player]."
    m 7eub "Ha habido estudios que muestran que las personas con ansiedad son más empáticas que la mayoría de las personas. {w=0.2}{nw}"
    extend 3hub "¡Lo que los hace grandes amigos para estar cerca!"
    m 1eua "De todos modos, [player]."
    extend 3hub "¡Gracias por escuchar!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalProsopagnosia",
            category=['media', 'enfermedades mentales'],
            prompt="Prosopagnosia",
            conditional="mas_seenLabels(['mentalhealthAutism'])",
            action=EV_ACT_RANDOM
        )
    )

label mentalProsopagnosia:
    m 1eua "Che, [player]."
    m 3eua "¿Alguna vez escuchaste sobre la prosopagnosia?"
    m 1euc "Bueno, en resumen, es una discapacidad mental que dificulta reconocer rostros."
    m 7eud "La prosopagnosia tiene algunas palabras diferentes para describirla, como '{i}ceguera facial{/i}' y '{i}agnosia facial{/i}'. Pero probablemente no deberías usar el último término..."
    m 1euc "Podés imaginar cómo esto puede tener un gran impacto en la vida diaria de alguien, ¿no, [player]?"
    m 3eud "Bueno, hay diferentes grados de prosopagnosia. Como solo reconocer rostros familiares, pero no extraños. {w=0.75}{nw}"
    extend 3rusdld "O ver objetos y rostros como lo mismo..."
    m 7eud "Acá, intentá esto por mí, [player]..."
    $ startedimaginetime = datetime.datetime.now()
    m 1euc "Cerrá los ojos e intentá imaginar a alguien que no existe."
    $ imagined_facetime = (datetime.datetime.now() > (startedimaginetime + datetime.timedelta(seconds=30)))
    if imagined_facetime:
        m 3euu "Cuando intentaste imaginar un rostro, ¿lo encontraste difícil, no?"
        m 1euc "Bueno, eso es solo un pequeño vistazo a la prosopagnosia, pero sí ayuda a darte una idea."
    else:
        m 3euc "Podés encontrar que es más difícil imaginar algo que no existe, como un color nuevo."
        m 7eud "Es solo para darte una idea, [player]."
    m 1eud "Como no pueden distinguir fácilmente los rostros, a menudo terminan usando otras señales visuales, como la ropa o los piercings para ayudar a combatir esto."
    m 1euc "A veces también usan las voces, pero creo que eso es obvio."
    if imagined_facetime:
        m 2ruu "Entonces, si alguna vez quisieras engañar a alguien con prosopagnosia, todo lo que necesitas es su ropa."
        m 1rub "Jajaja, solo estoy bromeando. Sé que no harías eso."
    m 1euc "Aunque, la prosopagnosia es algo bastante raro de tener. Solo aproximadamente el tres por ciento de la población la tiene."
    m 1eua "De todos modos, gracias por escucharme de nuevo, [player]."
return
