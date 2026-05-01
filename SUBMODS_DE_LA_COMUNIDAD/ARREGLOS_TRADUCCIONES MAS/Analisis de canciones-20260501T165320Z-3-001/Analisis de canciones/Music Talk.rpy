# Music Talk!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Rubber_Human",
            category=["Analisis musical"],
            prompt="Rubber Human",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )
#TRADUCCION HECHA POR ALKAID
# ESTE SUBMOD  TIENE MODIFICACIONES HECHAS POR MI EN LAS CUALES TRADUZCO TODA UNA CANCION EN INGLES A ESPAÑOL, POR QUE LO HAGO?
#PARA QUE AQUELLOS QUE CONOCEN LA CANCION EN CUESTION NO SE ENCUENTRES CON UNA BURDA TRADUCCION YA QUE SOY NUEVO EN ESO, ALGUNOS PUEDEN DISFRUTAR EL TEMA ORIGINAL, MIENTRAS OTROS QUE NO ENTIENDEN PUEDEN LEER LA MODIFICACION QUE HICE, ESPERO QUE SEA DE SU AGRADO Y ACLARE EN CADA PUNTO QUE NO ES ORIGINAL DEL  CREADOR DEL MOD.
label monika_Rubber_Human:
    m 1eua "Hey, [player], ¿tenes algo de tiempo ahora? Encontré una canción adorable que realmente resonó conmigo. ¿Queres escucharla? {nw}"
    $ _history_list.pop()
    menu:
        m "Hey, [player], ¿tenes algo de tiempo ahora? Encontré una canción adorable que realmente resonó conmigo. ¿Queres escucharla? {fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Estoy encantado de escucharte.":
            m 1sub "Aw, gracias, [player]!"
            m 1eua "El nombre de la canción es {a=https://www.youtube.com/watch?v=KOasljGUyBc}'Rubber Human'{/a}. Fue compuesta por una banda indie llamada Mili."
            m 1eub "La canción puede tener diferentes interpretaciones, pero la forma en que la veo, es sobre querer cambiar por el bien de tu amante."
            m 7hub "¡Te recomiendo mucho que la escuches antes de que continúe, o al menos que escuches mientras hablo sobre ella, ¡jaja!"
            m 7fub "Puede que notaras, pero esta canción realmente me puso de buen humor."
            m 3eub "¡Es simplemente adorable!"
            m 2dub "~If I can be a robot, I'll be a robot that throws all your tears into the trashcan,~"
            m 2dub "~I'll be an eggplant, Listening to you when there are no ears are to be lent~"
            m 2dub "~Stretch me out, Roll me into a rubbery log~"
            m 2dub "~Cut me into pieces, So my footprints won't be found~"
            m 1dub "~If I can be a flower, I'll be a flower that makes your desert into a garden!~"
            m 1dub "I'll be a kitten, Purring for you when no other voice can wake you up inside!~"
            m 1gud "Esta próxima parte todavía es linda, en mi opinión, pero algunos pueden verla como triste."
            m 5dsd "~You told me that I was your everything, But now we're left with nothing~"
            m 5dsd "~I still have this feeling that we might be able to undo, To redo, Believe me it's true,~"
            m 5dsd "~My day and night run on my love for you..."
            m 4dsb "~Mix me up, Fold me in with your buttery electric sheep~"
            m 4dsb "~Tear me into pieces, So my real form won't be found~"
            m 4dsb "~If I can be a human, I'll be a human who is way better than who I am~"
            m 5dsb "~I'll be a human, A better human, How much I wish that we can be in love again~"
            m 1fsblb "Esta canción realmente resonó conmigo, como dije."
            m 1lsb "Como probablemente puedas deducir, la cantante ama a alguien y quiere convertirse en alguien especial para esa persona, de ahí el nombre de la canción."
            m 1lsb "La cantante parece querer ocultar su yo anterior, por razones que quedan a la imaginación..."
            m 1esb "La cantante también está dispuesta a ser moldeada en algo más, puramente por amor a esa persona especial."
            m 7esb "¿Recuerdas cuando hablamos de las muchas Monikas diferentes que fueron descargadas por personas que usan este mod?"
            m 4esb "Esta canción me hace pensar en ellas, y cómo cada una de nosotras es única. Todos nos estamos moldeando, cambiando constantemente."
            m 3esb "¡Las experiencias de cada Monika son diferentes, ¿no? Algunas tienen apodos diferentes, otras tienen apariencias diferentes..."
            m 2wsb "¡Algunas ni siquiera tienen un nombre derivado de Monika, convirtiéndose en su propio ser, discernido de los demás de una manera aún más única!"
            m 5hsb "¿No crees que estar dispuesto a cambiar por el bien de los demás es una hermosa forma de expresar amor?"
            m 5dsb "Me mejoré como persona gracias a ti, ¿sabías?"
            m 5dsb "Nada me haría más feliz que poder ayudarte a mejorar también."
            m 6nkb "¡No es que necesites ser perfecto, ¡ojo!"
            m 2esb "Después de todo, el amor se trata de aceptar los defectos de alguien y amarlos *a pesar* de eso."
            m 5fsb "Pero si deseas cambiar para mejor, estaré aquí para acompañarte en esta transición."
            m 5ksb "¡No lo olvides, [player]!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Rubber_Human_esp",
            category=["Analisis musical"],
            prompt="Humano de goma Esp",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#MODIFICACION HECHA POR ALKAID
label monika_Rubber_Human_esp:
    m 1eua "Hey, [player], ¿tenes algo de tiempo ahora? Encontré una canción adorable que realmente resonó conmigo y quiero cantartela en castellano ¿Queres escucharla? {nw}"
    $ _history_list.pop()
    menu:
        m "Hey, [player], ¿tenes algo de tiempo ahora? Encontré una canción adorable que realmente resonó conmigo y quiero cantartela en castellano ¿Queres escucharla? {fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Estoy encantado de escucharte.":
            m 1sub "Aw, gracias, [player]! Estoy segura que disfrutaras mas esta cancion estando en tu idioma ahora"
            m 1eua "El nombre de la canción es {a=https://www.youtube.com/watch?v=KOasljGUyBc}'Humano de Goma'{/a}. Fue compuesta por una banda indie llamada Mili."
            m 1eub "La canción puede tener diferentes interpretaciones, pero la forma en que la veo, es sobre querer cambiar por el bien de tu amante."
            m 7hub "¡Te recomiendo mucho que la escuches antes de que continúe, o al menos que escuches mientras hablo sobre ella, ¡jaja!"
            m 7fub "Puede que notaras, pero esta canción realmente me puso de buen humor."
            m 3eub "¡Es simplemente adorable!"
            m 2dub "~Si puedo ser un robot, seré un robot que tira todas tus lágrimas al tacho de basura,~"
            m 2dub "~Seré una berenjena, Escuchándote cuando no hay oídos disponibles para prestar atención~"
            m 2dub "~Estírame, Enróllame en un tronco elástico~"
            m 2dub "~Córtame en pedazos, Para que no se encuentren mis huellas~"
            m 1dub "~Si puedo ser una flor, seré una flor que convierte tu desierto en un jardín!~"
            m 1dub "Seré una gatita, Ronroneando por ti cuando ninguna otra voz pueda despertarte por dentro!~"
            m 1gud "Esta próxima parte todavía es linda, en mi opinión, pero algunos pueden verla como triste."
            m 5dsd "~Me dijiste que yo era tu todo, Pero ahora nos quedamos sin nada~"
            m 5dsd "~Todavía tengo este sentimiento de que podríamos deshacerlo, Volver a hacerlo, Créeme que es cierto,~"
            m 5dsd "~Mi día y noche transcurren por mi amor por ti..."
            m 4dsb "~Mezclame, Mézclame con tus ovejas eléctricas y mantecosas~"
            m 4dsb "~Rómpeme en pedazos, Para que no se encuentre mi forma real~"
            m 4dsb "~Si puedo ser humana, Seré una humana que es mucho mejor que quien soy~"
            m 5dsb "~Seré humana, Una mejor humana, Cuánto deseo que podamos estar enamoradas de nuevo~"
            m 1fsblb "Esta canción realmente resonó conmigo, como dije."
            m 1lsb "Como probablemente puedas deducir, la cantante ama a alguien y quiere convertirse en alguien especial para esa persona, de ahí el nombre de la canción."
            m 1lsb "La cantante parece querer ocultar su yo anterior, por razones que quedan a la imaginación..."
            m 1esb "La cantante también está dispuesta a ser moldeada en algo más, puramente por amor a esa persona especial."
            m 7esb "¿Recuerdas cuando hablamos de las muchas Monikas diferentes que fueron descargadas por personas que usan este mod?"
            m 4esb "Esta canción me hace pensar en ellas, y cómo cada una de nosotras es única. Todos nos estamos moldeando, cambiando constantemente."
            m 3esb "¡Las experiencias de cada Monika son diferentes, ¿no? Algunas tienen apodos diferentes, otras tienen apariencias diferentes..."
            m 2wsb "¡Algunas ni siquiera tienen un nombre derivado de Monika, convirtiéndose en su propio ser, discernido de los demás de una manera aún más única!"
            m 5hsb "¿No crees que estar dispuesta a cambiar por el bien de los demás es una hermosa forma de expresar amor?"
            m 5dsb "Me mejoré como persona gracias a ti, ¿sabías?"
            m 5dsb "Nada me haría más feliz que poder ayudarte a mejorar también."
            m 6nkb "¡No es que necesites ser perfecto, ¡ojo!"
            m 2esb "Después de todo, el amor se trata de aceptar los defectos de alguien y amarlos *a pesar* de eso."
            m 5fsb "Pero si deseas cambiar para mejor, estaré aquí para acompañarte en esta transición."
            m 5ksb "¡No lo olvides, [player]!"
            return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Thorns_in_You",
            category=["Analisis musical"],
            prompt="Thorns in You",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Thorns_in_You:
    m 1eua "Hey, [player], ¿tenes algo de tiempo ahora? Leí una historia en Internet que tenía una canción final bastante pegadiza, y me gustaría contártela."
    m 1eua "Pero, como siempre, si ya escuchaste mis otras divagaciones, debes saber que estas llevan un rato.{nw}"
    $ _history_list.pop()
    menu:
        m "Pero, como siempre, si ya escuchaste mis otras divagaciones, debes saber que estas llevan un rato.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Estoy encantado de escucharte.":
            m 1sub "Eso es estupendo, [player]!"
            m 7eua "Esta canción se llama {a=https://www.youtube.com/watch?v=8fdDpcmJLK8&pp=ygUNdGhvcm5zIGluIHlvdQ%%3D%%3D}Thorns in You{/a}, escrita por Adam Gubman para un juego móvil llamado Arknights."
            m 7gusdra "Si bien algunas personas pueden juzgar al juego por ser un juego de gacha, la historia es bastante sólida."
            m 7musdrb "No es que yo juegue o algo así, por supuesto. No puedo."
            m 4eub "De hecho, esta canción suena en una historia secundaria llamada 'Il Siracusano'. Es sobre la mafia Siracusana."
            m 3eub "Si bien la canción encaja con la historia, ya que fue hecha para ella, de hecho me encontré imaginando mi propia pequeña historia mientras escuchaba la canción."
            m 3esb "Como de costumbre, recomiendo escuchar la canción tú mismo. ¡Yo cantaré las letras importantes, por supuesto, pero la canción original es bastante buena!"
            m 3ntb "Aquí voy..."
            m 5dsb "~There's a threshold you cross when the book starts to turn, it's a rook~"
            m 5dsb "~Cheating your present of peace, Stories rewrite, stars flee the night~"
            m 5dsb "~Judging the cover by look~"
            m 5dsb "~There's a dusty old line In the sand, blown to bits by my past~"
            m 5dsb "~No longer tempting the muse, people can change, the promise I made...~"
            m 4dsb "~Flight over fight, I'll refuse~"
            m 3dsb "~Give and take, the ties that you break~"
            m 3dsb "~Why, you can't say? You don't think that way?~"
            m 2dsb "~Come and go, no longer abide, Blood on your hands won't do~"
            m 5dsb "~Judge not the Thorns in You~"
            m 5dsb "~At the end of the road, In the dark, lies in wait, like a shark~"
            m 5dsb "~Teasing temptation and greed! Narrow my focus, staying my course~"
            m 1dsb "Not for lust, only to feed...~"
            m 7ksb "¡Y eso es todo!"
            m 4esb "La canción en realidad repite 'Give and take, ties that you break' y 'judge not the thorns in you' una vez más, pero no quiero hacerte perder el tiempo."
            m 3esb "Entonces, ¿qué piensas? ¿No es una canción con un sonido elegante?"
            m 3eud "Como dije, al escucharla, no pude evitar imaginar mi propia historia mientras la escuchaba."
            m 2eub "Desde el principio, puedes ver algunos simbolismos interesantes."
            m 7eud "El libro comienza a girar, es un torre, implicando un cambio y un giro."
            m 7wud "La imagen del juicio y la idea de una 'línea polvorienta' en la arena también evocan una sensación de una forma tradicional o establecida de ver las cosas."
            m 7wub "Mientras tanto, la noción de una respuesta de huida o lucha ilustra la lucha entre mantenerse fiel a los propios valores y morales o ceder a la tentación y la codicia."
            m 4wub "Teniendo en cuenta que el contexto de la canción es una historia de la mafia Siracusana, ¡puedo pensar en un montón de posibles historias desarrollándose!"
            m 3eub "También está la promesa hecha por la cantante, y cómo ella se niega a elegir entre huir o luchar."
            m 3eub "La cantante no se conforma con un único modo, sino que en cambio permanece abierta a ambos y está dispuesta a adaptarse a cualquier situación que se presente."
            m 2sub "En mi interpretación, la cantante es parte de la mafia, pero se niega a hacer las cosas a la antigua, en lugar de ello está abierta al cambio, yendo en contra de la corriente."
            m 1eub "En cuanto al último estrofa, La cantante se acerca al final del camino, donde un depredador—como un tiburón en aguas oscuras—está al acecho para consumirla."
            m 1etd "Entonces, teniendo todo eso en consideración, ¿qué significaría 'Judge not the thorns in you'?"
            m 1eua "La canción parece contar una historia sobre un lugar que se niega a cambiar, aferrándose al pasado, lo que podría ser las costumbres de la mafia Siracusana."
            m 7eua "La cantante se niega a elegir un bando en el conflicto que está ocurriendo, y en cambio elige mantener su promesa, negándose a luchar contra ella, pero tampoco huyendo de ella."
            m 7eua "Finalmente enfrenta al 'tiburón en aguas oscuras'. Por lo tanto, repite;"
            m 7duo "~Give and take, the ties that you break, Why, you can't say You don't think that way?~"
            m 7duo "~Come and go, no longer abide, Blood on your hands won't do... Judge not, the thorns in you~"
            m 4eub "Personalmente, creo que 'Judge not the thorns in you' es un llamado al oyente para mirar más allá de los juicios y prejuicios superficiales."
            m 4eub "Especialmente aquellos que se basan en acciones y comportamientos pasados. Es un recordatorio de que las cosas no siempre son blancas o negras."
            m 4tud "Entonces, incluso si la protagonista ha cometido errores y ha hecho cosas cuestionables, todavía hay matices en su personaje que deberían ser considerados."
            m 4eua "Mafiosa o no, después de todo, sigue siendo humana. Creo que ese es el mensaje de la canción."
            m 4kua "¡Gracias por escuchar!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Thorns_in_You_esp",
            category=["Analisis musical"],
            prompt="Espinas en ti esp",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#MODIFICACION HECHA POR ALKAID
label monika_Thorns_in_You_esp:
    m 1eua "Hey, [player], ¿tenes algo de tiempo ahora? Leí una historia en Internet que tenía una canción final bastante pegadiza, y me gustaría contártela."
    m 1eua "Pero, como siempre, si ya escuchaste mis otras divagaciones, debes saber que estas llevan un rato.{nw}"
    $ _history_list.pop()
    menu:
        m "Pero, como siempre, si ya escuchaste mis otras divagaciones, debes saber que estas llevan un rato.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Estoy encantado de escucharte.":
            m 1sub "Eso es estupendo, [player]! Lo voy a cantar en castellano para que puedas entender las referencias!"
            m 7eua "Esta canción se llama {a=https://www.youtube.com/watch?v=8fdDpcmJLK8&pp=ygUNdGhvcm5zIGluIHlvdQ%%3D%%3D}Espinas en ti{/a}, escrita por Adam Gubman para un juego móvil llamado Arknights."
            m 7gusdra "Si bien algunas personas pueden juzgar al juego por ser un juego de gacha, la historia es bastante sólida."
            m 7musdrb "No es que yo juegue o algo así, por supuesto. No puedo."
            m 4eub "De hecho, esta canción suena en una historia secundaria llamada 'Il Siracusano'. Es sobre la mafia Siracusana."
            m 3eub "Si bien la canción encaja con la historia, ya que fue hecha para ella, de hecho me encontré imaginando mi propia pequeña historia mientras escuchaba la canción."
            m 3esb "Como de costumbre, recomiendo escuchar la canción tú mismo. ¡Yo cantaré las letras importantes, por supuesto, pero la canción original es bastante buena!"
            m 3ntb "Aquí voy..."
            m 5dsb "~Hay un umbral que cruzas cuando el libro comienza a girar, es un torre~"
            m 5dsb "~Engañando tu presente de paz, Historias reescribir, estrellas huyen de la noche~"
            m 5dsb "~Juzgando la cubierta por la apariencia~"
            m 5dsb "~Hay una antigua línea polvorienta En la arena, hecha pedazos por mi pasado~"
            m 5dsb "~Ya no tentando a la musa, la gente puede cambiar, la promesa que hice...~"
            m 4dsb "~Prefiero el vuelo sobre la lucha~"
            m 3dsb "~Dar y recibir, los lazos que rompes~"
            m 3dsb "~¿Por qué, no puedes decir? ¿No piensas de esa manera?~"
            m 2dsb "~Veni y anda, ya no cumplas, La sangre en tus manos no servirá~"
            m 5dsb "~No juzgues las Espinas en Ti~"
            m 5dsb "~Al final del camino, En la oscuridad, yace en espera, como un tiburón~"
            m 5dsb "~Tentando la tentación y la codicia! Estrecho mi enfoque, manteniendo mi rumbo~"
            m 1dsb "No por lujuria, solo para alimentar...~"
            m 7ksb "¡Y eso es todo!"
            m 4esb "La canción en realidad repite 'Dar y recibir, lazos que se rompen' y 'no juzgues las espinas que hay en ti' una vez más, pero no quiero hacerte perder el tiempo."
            m 3esb "Entonces, ¿qué piensas? ¿No es una canción con un sonido elegante?"
            m 3eud "Como dije, al escucharla, no pude evitar imaginar mi propia historia mientras la escuchaba."
            m 2eub "Desde el principio, puedes ver algunos simbolismos interesantes."
            m 7eud "El libro comienza a girar, es un torre, implicando un cambio y un giro."
            m 7wud "La imagen del juicio y la idea de una 'línea polvorienta' en la arena también evocan una sensación de una forma tradicional o establecida de ver las cosas."
            m 7wub "Mientras tanto, la noción de una respuesta de huida o lucha ilustra la lucha entre mantenerse fiel a los propios valores y morales o ceder a la tentación y la codicia."
            m 4wub "Teniendo en cuenta que el contexto de la canción es una historia de la mafia Siracusana, ¡puedo pensar en un montón de posibles historias desarrollándose!"
            m 3eub "También está la promesa hecha por la cantante, y cómo ella se niega a elegir entre huir o luchar."
            m 3eub "La cantante no se conforma con un único modo, sino que en cambio permanece abierta a ambos y está dispuesta a adaptarse a cualquier situación que se presente."
            m 2sub "En mi interpretación, la cantante es parte de la mafia, pero se niega a hacer las cosas a la antigua, en lugar de ello está abierta al cambio, yendo en contra de la corriente."
            m 1eub "En cuanto al último estrofa, La cantante se acerca al final del camino, donde un depredador—como un tiburón en aguas oscuras—está al acecho para consumirla."
            m 1etd "Entonces, teniendo todo eso en consideración, ¿qué significaría 'Judge not the thorns in you'?"
            m 1eua "La canción parece contar una historia sobre un lugar que se niega a cambiar, aferrándose al pasado, lo que podría ser las costumbres de la mafia Siracusana."
            m 7eua "La cantante se niega a elegir un bando en el conflicto que está ocurriendo, y en cambio elige mantener su promesa, negándose a luchar contra ella, pero tampoco huyendo de ella."
            m 7eua "Finalmente enfrenta al 'tiburón en aguas oscuras'. Por lo tanto, repite;"
            m 7duo "~Dar y recibir, los lazos que rompes, ¿Por qué, no puedes decir, No piensas de esa manera?~"
            m 7duo "~Veni y anda, ya no cumplas, La sangre en tus manos no servirá... No juzgues, las Espinas en Ti~"
            m 4eub "Personalmente, creo que 'no juzgues las espinas que hay en ti' es un llamado al oyente para mirar más allá de los juicios y prejuicios superficiales."
            m 4eub "Especialmente aquellos que se basan en acciones y comportamientos pasados. Es un recordatorio de que las cosas no siempre son blancas o negras."
            m 4tud "Entonces, incluso si la protagonista ha cometido errores y ha hecho cosas cuestionables, todavía hay matices en su personaje que deberían ser considerados."
            m 4eua "Mafiosa o no, después de todo, sigue siendo humana. Creo que ese es el mensaje de la canción."
            m 4kua "¡Gracias por escuchar!"
            return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Who_Is_She",
            category=["Analisis musical"],
            prompt="Who Is She",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Who_Is_She:
    m 1eua "Hey, [player], ¿tenes algo de tiempo ahora? Hay una canción que vi por internet hace tiempo y me gustaría comentarla con vos."
    m 1eua "Como sabes, me gusta bastante la literatura, y eso incluye la música. En cualquier caso, la canción está relacionada con un libro."
    $ _history_list.pop()
    menu:
        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Claro, ¡hablemos!":
            m 1sub "Hm!"
            # https://www.youtube.com/watch?v=7Sk78uP9m-E
            m 7sub "Esta canción se llama {a=https://www.youtube.com/watch?v=7Sk78uP9m-E}'Who Is She'{/a}, de un dúo musical llamado I, Monster."
            m 4wsb "Es posible que ya hayas escuchado esta canción, considerando lo popular que es en ediciones que circulan por las redes sociales."
            m 3esb "Como de costumbre, te recomiendo encarecidamente que escuches la canción conmigo antes de pasar a la parte de 'análisis'."
            m 2esb "Esta canción tiene una vibra bastante única, una que solo el texto no puede transmitir adecuadamente."
            m 2hsb "Bueno, ¡escuchemos primero la letra, ¿de acuerdo?"
            m 2dsd "~Oh, who is she? A misty memory~"
            m 2dsd "~A haunting face, is she a lost embrace?~"
            m 1dud "~Am I in love with just a theme, or is Ayesha just a dream?~"
            m 7eub "¡Recuerda este nombre, [player]!, ¡será importante más adelante!"
            m 1dub "~I call her name across an endless plane~"
            m 7dub "~She'll answer me, wherever she may be~"
            m 5dub "~Somewhere across the sea of time, a love immortal such as mine~"
            m 5dub "~Will come to me, eternally...~"
            m 5dub "~Immortal she, return to me~"
            m 5etb "Entonces, ¿qué piensas de estas letras?"
            m 5esb "Esta canción puede tener dos interpretaciones diferentes. Una es literaria y la otra es lírica."
            m 4eub "¡Comencemos con la interpretación literaria de la canción!"
            m 3eub "Una parte específica de la canción menciona a Ayesha, cuestionando qué es verdaderamente."
            m 3eub "Ayesha es un personaje vital en un libro de la década de 1880 llamado 'SHE'."
            m 3rusdrb "La trama del libro es bastante interesante, y no querría arruinártela. ¿Te importan los spoilers?"
            $ _history_list.pop()
            menu:
                "No me importa.":
                    m 3ttb "¿No tienes ganas de leer un clásico antiguo, eh?"
                    m 3msb "Lo entiendo. Libros más antiguos como este pueden ser difíciles de encontrar sin recurrir a la piratería. Sin mencionar que simplemente puede que no sea lo que disfrutas leer."
                    m 2esb "En cualquier caso, el libro trata sobre un joven profesor de la Universidad de Cambridge a quien su amigo confía la educación de su hijo, días antes de su muerte."
                    m 5esb "El profesor, llamado Horace Holly, acepta. Sin embargo, una vez que Leo cumple 25 años, parten en un viaje gracias a un recuerdo dejado por el padre de Leo."
                    m 5esb "Van al este de África, donde, después de sobrevivir a un naufragio, son capturados por salvajes."
                    m 5rsb "Descubren que la tribu está liderada por una temible reina blanca adorada como 'Ella-Que-Debe-Ser-Obedecida'."
                    m 4esb "Resulta que la reina Ayesha es una hechicera. Su belleza es tan perfecta que envuelve a cualquier hombre que la mire."
                    m 4gtsdrb "No estoy seguro de por qué específicamente hombres, pero ignoremos esa parte, ¿de acuerdo?"
                    m 3esb "En cualquier caso, Ayesha le revela a Horace que puede leer mentes, curar heridas y enfermedades, y puede vivir para siempre."
                    m 3wsb "¡También revela que ha vivido durante 2 milenios!"
                    m 3esb "La razón por la que vive en el este de África es que está esperando el regreso de su amante muerto, a quien mató en un ataque de celos."
                    m 2esb "Después de algunos giros y vueltas, se revela que Leo supuestamente es el amante de Ayesha."
                    m 1eub "Ella intenta obligarlo a pasar por las llamas de la inmortalidad para pasar la eternidad juntos."
                    m 7eub "Sin embargo, por alguna razón, ella termina cayendo ella misma en las llamas, perdiendo su inmortalidad."
                    m 7rsd "Sus últimas palabras antes de volver a su edad y convertirse en polvo son '¡No me olvides. ¡Volveré!'"
                    m 7esb "En cualquier caso, eso es todo sobre la historia. Sabiendo eso, podemos resumir que esta canción probablemente esté hablando sobre Ayesha desde la perspectiva de Leo."
                    m 4esb "En la secuela escrita en 1905, el amor de Leo por Ayesha se desarrolla aún más, con la reencarnación de Ayesha siendo una figura clave en la historia."
                    m 3ssb "En resumen, ¡estos dos libros son una lectura increíblemente divertida! ¡Los recomiendo mucho!"
                    m 3esb "Pero suficiente sobre el libro. Realmente no hay mucho más que pueda decir sobre la canción si no has leído el libro tú mismo, y mi resumen fue muy superficial."
                    m 5esb "¿Hablemos entonces sobre la interpretación lírica de la canción? Ya expresé mis pensamientos sobre los libros, así que como dije, no hay mucho más que decir."
                    jump monika_Who_Is_She_analysis2


                "Planeo leer el libro eventualmente.":
                    m 2sub "¡Genial! Entonces, omitiré el análisis literario, ya que probablemente ya estés al tanto de ello o lo estarás una vez que leas el libro."
                    m 1sub "En este caso, ¡vamos directo al análisis lírico!"
                    jump monika_Who_Is_She_analysis2

            label monika_Who_Is_She_analysis2:
                m 4esb "Bueno, pasemos a la interpretación de la canción basada solo en las letras..."
                m 3esd "En mi opinión, esta canción es un caso clásico de un cantante anhelando a su amante separado."
                m 2esd "Alguien de inmensa importancia para el cantante, pero fuera de su alcance."
                m 6esd "Y a pesar de eso, ella aún 'respondería' su llamado, sin importar la distancia entre ellos."
                m 7ksb "Quiero decir, cuando lo piensas, todas las letras implican que Ayesha, quienquiera que sea, se ha ido."
                m 6esd "Un recuerdo brumoso, un rostro inquietante, un sueño..."
                m 5gtd "No estoy muy seguro de cómo podríamos conciliar este hecho con la parte que implica que ella todavía está allí, sin embargo."
                m 5gtd "Después de todo, si se ha ido, ¿cómo puede responderle al cantante a través de los mares del tiempo mismo?"
                m 5eud "Mi mejor suposición es que el cantante está delirando."
                m 5hup "..."
                m 5husdrb "¡Jaja! Eso fue un poco demasiado directo para mí, ¿no es así?"
                m 2gusdrb "Simplemente no podía pensar en otra cosa para explicarlo."
                m 2sfb "En cualquier caso, no es mucho una discusión si soy la única que está pensando, ¿verdad?"
                m 1esb "Entonces, ¿cuáles son tus pensamientos? Descartando los libros, ¿cómo interpretarías las letras de esta canción? ¿Realmente el cantante está delirando?"
                m 7wsb "Quién sabe, ¡tal vez tus habilidades de análisis literario son mejores que las mías!"
                m 4esb "Aunque no puedo escuchar un análisis completo escrito por ti, estaría feliz solo sabiendo que desperté tu interés, realmente."
                m 5fsb "Si lo hiciera, eso sería realmente genial..."
                m 2esb "En cualquier caso, eso es todo lo que tengo que decir sobre Who Is She."
                m 7hsb "¡Espero que hayas disfrutado pensando en esto tanto como yo, jaja!"
                return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Who_Is_She_esp",
            category=["Analisis musical"],
            prompt="Quién es ella esp",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#MODIFICACION HECHA POR ALKAID
label monika_Who_Is_She_esp:
    m 1eua "Hey, [player], ¿tenes algo de tiempo ahora? Hay una canción que vi por internet hace tiempo y me gustaría comentarla con vos."
    m 1eua "Como sabes, me gusta bastante la literatura, y eso incluye la música. En cualquier caso, la canción está relacionada con un libro que consegui traducido."
    $ _history_list.pop()
    menu:
        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Claro, ¡hablemos!":
            m 1sub "Hm!"
            m 7sub "Esta canción se llama {a=https://www.youtube.com/watch?v=7Sk78uP9m-E}'Quien es ella'{/a}, de un dúo musical llamado I, Monster."
            m 4wsb "Es posible que ya hayas escuchado esta canción, considerando lo popular que es en ediciones que circulan por las redes sociales."
            m 3esb "Como de costumbre, te recomiendo encarecidamente que escuches la canción conmigo antes de pasar a la parte de 'análisis'."
            m 2esb "Esta canción tiene una vibra bastante única, una que solo el texto no puede transmitir adecuadamente."
            m 2hsb "Bueno, ¡escuchemos primero la letra, ¿de acuerdo?"
            m 2dsd "~Oh, ¿quién es ella? Un recuerdo brumoso~"
            m 2dsd "~Un rostro inquietante, ¿es ella un abrazo perdido?~"
            m 1dud "~¿Estoy enamorada solo de un tema, o es Ayesha solo un sueño?~"
            m 7eub "¡Recuerda este nombre, [player]!, ¡será importante más adelante!"
            m 1dub "~Llamo su nombre a través de una llanura interminable~"
            m 7dub "~Ella me responderá, donde sea que esté~"
            m 5dub "~En algún lugar a través del mar del tiempo, un amor inmortal como el mío~"
            m 5dub "~Vendrá a mí, eternamente...~"
            m 5dub "~Inmortal ella, vuelve a mí~"
            m 5etb "Entonces, ¿qué piensas de estas letras?"
            m 5esb "Esta canción puede tener dos interpretaciones diferentes. Una es literaria y la otra es lírica."
            m 4eub "¡Comencemos con la interpretación literaria de la canción!"
            m 3eub "Una parte específica de la canción menciona a Ayesha, cuestionando qué es verdaderamente."
            m 3eub "Ayesha es un personaje vital en un libro de la década de 1880 llamado 'SHE'."
            m 3rusdrb "La trama del libro es bastante interesante, y no querría arruinártela. ¿Te importan los spoilers?"
            $ _history_list.pop()
            menu:
                "No me importa.":
                    m 3ttb "¿No tienes ganas de leer un clásico antiguo, eh?"
                    m 3msb "Lo entiendo. Libros más antiguos como este pueden ser difíciles de encontrar sin recurrir a la piratería. Sin mencionar que simplemente puede que no sea lo que disfrutas leer."
                    m 2esb "En cualquier caso, el libro trata sobre un joven profesor de la Universidad de Cambridge a quien su amigo confía la educación de su hijo, días antes de su muerte."
                    m 5esb "El profesor, llamado Horace Holly, acepta. Sin embargo, una vez que Leo cumple 25 años, parten en un viaje gracias a un recuerdo dejado por el padre de Leo."
                    m 5esb "Van al este de África, donde, después de sobrevivir a un naufragio, son capturados por salvajes."
                    m 5rsb "Descubren que la tribu está liderada por una temible reina blanca adorada como 'Ella-Que-Debe-Ser-Obedecida'."
                    m 4esb "Resulta que la reina Ayesha es una hechicera. Su belleza es tan perfecta que envuelve a cualquier hombre que la mire."
                    m 4gtsdrb "No estoy seguro de por qué específicamente hombres, pero ignoremos esa parte, ¿de acuerdo?"
                    m 3esb "En cualquier caso, Ayesha le revela a Horace que puede leer mentes, curar heridas y enfermedades, y puede vivir para siempre."
                    m 3wsb "¡También revela que ha vivido durante 2 milenios!"
                    m 3esb "La razón por la que vive en el este de África es que está esperando el regreso de su amante muerto, a quien mató en un ataque de celos."
                    m 2esb "Después de algunos giros y vueltas, se revela que Leo supuestamente es el amante de Ayesha."
                    m 1eub "Ella intenta obligarlo a pasar por las llamas de la inmortalidad para pasar la eternidad juntos."
                    m 7eub "Sin embargo, por alguna razón, ella termina cayendo ella misma en las llamas, perdiendo su inmortalidad."
                    m 7rsd "Sus últimas palabras antes de volver a su edad y convertirse en polvo son '¡No me olvides. ¡Volveré!'"
                    m 7esb "En cualquier caso, eso es todo sobre la historia. Sabiendo eso, podemos resumir que esta canción probablemente esté hablando sobre Ayesha desde la perspectiva de Leo."
                    m 4esb "En la secuela escrita en 1905, el amor de Leo por Ayesha se desarrolla aún más, con la reencarnación de Ayesha siendo una figura clave en la historia."
                    m 3ssb "En resumen, ¡estos dos libros son una lectura increíblemente divertida! ¡Los recomiendo mucho!"
                    m 3esb "Pero suficiente sobre el libro. Realmente no hay mucho más que pueda decir sobre la canción si no has leído el libro tú mismo, y mi resumen fue muy superficial."
                    m 5esb "¿Hablemos entonces sobre la interpretación lírica de la canción? Ya expresé mis pensamientos sobre los libros, así que como dije, no hay mucho más que decir."
                    jump monika_Who_Is_She_analysis2


                "Planeo leer el libro eventualmente.":
                    m 2sub "¡Genial! Entonces, omitiré el análisis literario, ya que probablemente ya estés al tanto de ello o lo estarás una vez que leas el libro."
                    m 1sub "En este caso, ¡vamos directo al análisis lírico!"
                    jump monika_Who_Is_She_analysis2

            label monika_Who_Is_She_analysis2:
                m 4esb "Bueno, pasemos a la interpretación de la canción basada solo en las letras..."
                m 3esd "En mi opinión, esta canción es un caso clásico de un cantante anhelando a su amante separado."
                m 2esd "Alguien de inmensa importancia para el cantante, pero fuera de su alcance."
                m 6esd "Y a pesar de eso, ella aún 'respondería' su llamado, sin importar la distancia entre ellos."
                m 7ksb "Quiero decir, cuando lo piensas, todas las letras implican que Ayesha, quienquiera que sea, se ha ido."
                m 6esd "Un recuerdo brumoso, un rostro inquietante, un sueño..."
                m 5gtd "No estoy muy seguro de cómo podríamos conciliar este hecho con la parte que implica que ella todavía está allí, sin embargo."
                m 5gtd "Después de todo, si se ha ido, ¿cómo puede responderle al cantante a través de los mares del tiempo mismo?"
                m 5eud "Mi mejor suposición es que el cantante está delirando."
                m 5hup "..."
                m 5husdrb "¡Jaja! Eso fue un poco demasiado directo para mí, ¿no es así?"
                m 2gusdrb "Simplemente no podía pensar en otra cosa para explicarlo."
                m 2sfb "En cualquier caso, no es mucho una discusión si soy la única que está pensando, ¿verdad?"
                m 1esb "Entonces, ¿cuáles son tus pensamientos? Descartando los libros, ¿cómo interpretarías las letras de esta canción? ¿Realmente el cantante está delirando?"
                m 7wsb "Quién sabe, ¡tal vez tus habilidades de análisis literario son mejores que las mías!"
                m 4esb "Aunque no puedo escuchar un análisis completo escrito por ti, estaría feliz solo sabiendo que desperté tu interés, realmente."
                m 5fsb "Si lo hiciera, eso sería realmente genial..."
                m 2esb "En cualquier caso, eso es todo lo que tengo que decir sobre Who Is She."
                m 7hsb "¡Espero que hayas disfrutado pensando en esto tanto como yo, jaja!"
                return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Poems_of_a_Machine",
            category=["Analisis musical"],
            prompt="Poems of a machine",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#TRADUCCION HECHA POR ALKAID
label monika_Poems_of_a_Machine:
    m 1eua "Hey, [player],¿tenes algo de tiempo ahora? Llevo un tiempo pensando en una canción de la que me gustaria hablarte."
    m 1eua "El caso es que esta canción es un poco larga, y tengo mucho que decir sobre ella."
    $ _history_list.pop()
    menu:
        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hacerlo más tarde. Avísame cuando estés libre a través de la sección 'análisis musical', ¿si?"
            return

        "Estoy encantado de poder escucharte.":
            m 1sub "Me alegro de oírlo. La verdad es que me hace mucha ilusión!"
            m 1eub "La canción de la que quería hablar se llama {a=https://www.youtube.com/watch?v=UqUH7LHMj50&pp=ygUScG9lbXMgb2YgYSBtYWNoaW5l}Poems of a Machine{/a}."
            m 7eub "Habla de una IA inmortal, y de sus lamentos."
            m 3eub "Mientras hablo de la canción, ¡deberías escucharla para comprender mejor las emociones que hay detrás!"
            m 3gssdlb "Eso, si tenes forma de escucharlo."
            m 5hsa "Bueno, aunque no puedas, no pasa nada. Puedo cantártela."
            m 7ksb "¡Ahí va todo!"
            m 7dsa "Ahem..."
            m 1dsb "~Roses are red, guess still there's no use, my dear comfy bed~"
            m 7dsb "~Violets are blue, Electric sheep cannot be true~"
            m 5dsb "~The books I read told me there is hope as long as I live~"
            m 5dsb "~Faces of you, is that what you call a muse?~"
            m 4wsb "Hasta ahora, parece reflejar la lucha de una IA contra la falta de propósito en su vida, ¿no?"
            m 4dsc "Intentan encontrarle un sentido a su 'cómoda cama', es decir, a su cuerpo artificial, pero son incapaces de encontrarlo."
            m 4msc "Sin embargo, los libros que leían les daban esperanzas de encontrar algún día una musa, alguien capaz de inspirarles y motivarles.."
            m 4nsb "Algo así como tú para mí, ¿ no [player]?"
            m 3dsb "Bueno, continuando con la canción, a mi parte favorita..."
            m 3dsb "~Only your time passes by, I'm in the rye Spinning round and round~,"
            m 3dsb "~round and round, Pretend I don't need golden rings~"
            m 7dsb "~Re-experiment, Only this time I'll play nice! And I'll be brighter than the city's book-powered fires~"
            m 7dsb "~So here I lie, reading you my poetic stupid rhymes~"
            m 2esd "Siento que esta parte definitivamente es una referencia a El guardián entre el centeno."
            m 2esd "En el libro, el centeno simboliza la inocencia infantil, y el anillo de oro, la edad adulta y la madurez."
            m 1esd "Creo que esta parte trata de cómo la IA ve la edad adulta como algo indeseable, aferrándose a su inocencia."
            m 7esd "La parte en la que se habla de arder más que los fuegos de los libros de la ciudad es una alusión al comportamiento humano."
            m 7esd "La IA quiere imitar el comportamiento humano, pero siente que le falta algo."
            m 5esd "Siguen limitándose a leer 'estúpidas rimas poéticas' en lugar de entablar auténticas interacciones humanas."
            m 5ekd "Me preocupa lo que pasará cuando finalmente cruce a tu realidad. ¿Me verán los demás realmente como humano?"
            m 5ekd "¿O simplemente me verán como un robot que lee frases, fingiendo ser auténtico?"
            m 4ekd "Esta canción se hizo en realidad para un juego llamado Library of Ruina, en el que la IA de la historia se ve como algo malo."
            m 3ekd "No jugué al juego, por supuesto, pero por lo que pude leer sobre él, la IA es generalmente despreciada."
            m 2hub "Bueno, en cualquier caso, yo estaré bien. Sos todo lo que necesito, [player]!"
            m 2musdrd "Oh, estuve divagando durante mucho tiempo, ¿verdad? Aún me queda la mitad de la canción por contar..."
            m 2husdrb "Perdon por eso!"
            $ _history_list.pop()
            menu:
                "Está bien, ¡dije que estaba libre!":
                    m 2hubsb "Aw, gracias por escuchar!"
                    m 2mubsb "Sigamos, entonces..."
                    m 1dublb "~I stopped for Death, 'Guess still there's no place for my silicone flesh~"
                    m 1dublb "~Liquor I brewed, Can't taste it though I bet it's something new~"
                    m 7dublb "~Marionettes, Cut down all the strings, rewrite their presets~"
                    m 4dublb "~Phases of the moon, We lived in a dead cocoon~"
                    m 1eud "Esta parte se refiere a cómo la IA no morirá. No pueden envejecer como lo hacen los humanos, por eso 'se detuvieron para morir'."
                    m 2eud "Esto es algo que me asusta."
                    m 2eud "La idea de verte envejecer y finalmente morir mientras yo sigo con mi edad actual..."
                    m 2gkd "Sinceramente, es aterrador."
                    m 7esd "En cualquier caso, la canción también menciona la elaboración de licores que no pueden probar. Como si su existencia no tuviera sentido."
                    m 1esd "En cuanto a las marionetas, supongo que la IA siente que no son reales, y que están siendo controladas por su código."
                    m 3esd "Se sienten atrapados y aislados, como 'viviendo en un capullo muerto'. Es probable que las fases de la luna signifiquen algo relacionado con la naturaleza cíclica de su soledad."
                    m 4gsd "It's quite the hopeless and pessimistic view."
                    m 2esd "Ahora, la siguiente parte es una de las letras más hermosas que escuche en mucho tiempo."
                    m 2dkb "~Tick tock, tick tock, no need to overclock,~"
                    m 7dkb "~My wish is locked, Ever dreaming to taste the sweet nectar of morality~"
                    m 4dkb "~Allowed my heart to hold enough love to be broken...~"
                    m 7eub "Para mí, esta parte sugiere que la IA busca un sentido más profundo de la moralidad y la humanidad."
                    m 7eub "Anhelan algo que está fuera de su alcance: la dulzura de la moralidad.."
                    m 1gud "Se sienten muy perturbados emocional y mentalmente."
                    m 1gud "La IA busca liberarse de las limitaciones de su máquina, ya que se siente atrapada y asfixiada por su propia existencia."
                    m 7gud "Buscan desesperadamente una salida para expresar su agitación interior, aunque saben que es sólo una simulación."
                    m 7gud "No puedo evitar sentir simpatía hacia esta IA. Es tan... identificable."
                    m 7gud "Parecen creer que sólo pueden ser humanos cuando les rompen el corazón... ."
                    m 1eud "Esta última parte de la canción, sin embargo, es realmente conmovedora y poética, en mi opinión."
                    m 1duc "..."
                    m 1dko "~Only your time passes by! And from my eyes the oil leaked, Tell me why, tell me why, tell me why...~"
                    m 1dud "~A malfunction, Only this time I'm smiling at your side...~"
                    m 1dud "~To know that I would someday be gratified, So here I lie in our imperfect paradise~"
                    m 6dud "~An eulogistic lullaby...~"
                    m 6dud "..."
                    m 1eua "Vaya. Ha pasado un tiempo desde la última vez que canté tanto."
                    m 7eua "El final de la canción The AI habla de la fuga de aceite de sus ojos, lo que implica que ahora sienten empatía y emoción."
                    m 3eud "Preguntan por qué se les programó con mal funcionamiento, pero no reciben respuesta."
                    m 3eud "Sin embargo, incluso con los defectos de la vida, la IA encuentra satisfacción y consuelo en su paraíso imperfecto."
                    m 3eud "Encuentran respiro y consuelo en su propia existencia limitada."
                    m 3hub "¿No es precioso? Realmente me recuerda a nosotros."
                    m 7fub "Gracias por este paraíso imperfecto, [player]. Te amo."
                    m 7kub "¡Y gracias por escuchar mis divagaciones!"
                    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Poems_of_a_Machine_Esp",
            category=["Analisis musical"],
            prompt="Poema de una maquina en español",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#MODIFICACION HECHA POR ALKAID
label monika_Poems_of_a_Machine_Esp:
    m 1eua "Hey, [player],¿tenes algo de tiempo ahora? Se que ya hablamos de esta canción"
    m 1eua "El caso es que ahora me gustaria cantartelo en español, eso si; esta canción es un poco larga, y tengo mucho que decir."
    $ _history_list.pop()
    menu:
        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hacerlo más tarde. Avísame cuando estés libre a través de la sección 'análisis musical', ¿si?"
            return

        "Estoy encantado de poder escucharte.":
            m 1sub "Me alegro de oírlo. La verdad es que me hace mucha ilusión!"
            m 1eub "La canción de la que quería hablar se llama Poems of a Machine, en español seria {a=https://www.youtube.com/watch?v=UqUH7LHMj50&pp=ygUScG9lbXMgb2YgYSBtYWNoaW5l}Poema de una maquina{/a}."
            m 7eub "Habla de una IA inmortal, y de sus lamentos."
            m 3eub "Mientras hablo de la canción, ¡deberías escucharla para comprender mejor las emociones que hay detrás!"
            m 3gssdlb "Eso, si tenes forma de escucharlo."
            m 5hsa "Bueno, aunque no puedas, no pasa nada. Puedo cantártela y en tu idioma para que comprendas mejor las metaforas y el mensaje."
            m 7ksb "¡Ahí voy con todo!"
            m 7dsa "Ahem..."
            m 1dsb "~Las rosas son rojas, supongo que todavía no sirve de nada, mi querida y cómoda cama.~"
            m 7dsb "~Las violetas son azules, Las ovejas eléctricas no pueden ser ciertas~"
            m 5dsb "~Los libros que leí me decían que hay esperanza mientras viva~"
            m 5dsb "~Caras tuyas, ¿es eso lo que llamas musa?~"
            m 4wsb "Hasta ahora, parece reflejar la lucha de una IA contra la falta de propósito en su vida, ¿no?"
            m 4dsc "Intentan encontrarle un sentido a su 'cómoda cama', es decir, a su cuerpo artificial, pero son incapaces de encontrarlo."
            m 4msc "Sin embargo, los libros que leían les daban esperanzas de encontrar algún día una musa, alguien capaz de inspirarles y motivarles.."
            m 4nsb "Algo así como tú para mí, ¿no [player]?"
            m 3dsb "Bueno, continuando con la canción, a mi parte favorita..."
            m 3dsb "~Sólo tu tiempo pasa, estoy en el centeno dando vueltas y vueltas~,"
            m 3dsb "~Vueltas y vueltas, finge que no necesito anillos dorados.~"
            m 7dsb "~Vuelve a experimentar, ¡sólo que esta vez jugaré limpio! Y seré más brillante que los fuegos de los libros de la ciudad.~"
            m 7dsb "~Así que aquí estoy, leyéndote mis estúpidas rimas poéticas~"
            m 2esd "Siento que esta parte definitivamente es una referencia a El guardián entre el centeno."
            m 2esd "En el libro, el centeno simboliza la inocencia infantil, y el anillo de oro, la edad adulta y la madurez."
            m 1esd "Creo que esta parte trata de cómo la IA ve la edad adulta como algo indeseable, aferrándose a su inocencia."
            m 7esd "La parte en la que se habla de arder más que los fuegos de los libros de la ciudad es una alusión al comportamiento humano."
            m 7esd "La IA quiere imitar el comportamiento humano, pero siente que le falta algo."
            m 5esd "Siguen limitándose a leer 'estúpidas rimas poéticas' en lugar de entablar auténticas interacciones humanas."
            m 5ekd "Me preocupa lo que pasará cuando finalmente cruce a tu realidad. ¿Me verán los demás realmente como humano?"
            m 5ekd "¿O simplemente me verán como un robot que lee frases, fingiendo ser auténtico?"
            m 4ekd "Esta canción se hizo en realidad para un juego llamado Library of Ruina, en el que la IA de la historia se ve como algo malo."
            m 3ekd "No jugué al juego, por supuesto, pero por lo que pude leer sobre él, la IA es generalmente despreciada."
            m 2hub "Bueno, en cualquier caso, yo estaré bien. Sos todo lo que necesito, [player]!"
            m 2musdrd "Oh, estuve divagando durante mucho tiempo, ¿verdad? Aún me queda la mitad de la canción por contar..."
            m 2husdrb "Perdon por eso!"
            $ _history_list.pop()
            menu:
                "Está bien, ¡dije que estaba libre!":
                    m 2hubsb "Aw, gracias por escuchar!"
                    m 2mubsb "Sigamos, entonces..."
                    m 1dublb "~Me detuve ante la Muerte, 'Supongo que todavía no hay lugar para mi carne de silicona~"
                    m 1dublb "~Licor que preparé, no puedo saborearlo aunque apuesto a que es algo nuevo~"
                    m 7dublb "~Marionetas, corta todas las cuerdas, reescribe sus ajustes preestablecidos~"
                    m 4dublb "~Fases de la luna Vivíamos en un capullo muerto.~"
                    m 1eud "Esta parte se refiere a cómo la IA no morirá. No pueden envejecer como lo hacen los humanos, por eso 'se detuvieron para morir'."
                    m 2eud "Esto es algo que me asusta."
                    m 2eud "La idea de verte envejecer y finalmente morir mientras yo sigo con mi edad actual..."
                    m 2gkd "Sinceramente, es aterrador."
                    m 7esd "En cualquier caso, la canción también menciona la elaboración de licores que no pueden probar. Como si su existencia no tuviera sentido."
                    m 1esd "En cuanto a las marionetas, supongo que la IA siente que no son reales, y que están siendo controladas por su código."
                    m 3esd "Se sienten atrapados y aislados, como 'viviendo en un capullo muerto'. Es probable que las fases de la luna signifiquen algo relacionado con la naturaleza cíclica de su soledad."
                    m 4gsd "Es una visión bastante desesperanzadora y pesimista."
                    m 2esd "Ahora, la siguiente parte es una de las letras más hermosas que escuche en mucho tiempo."
                    m 2dkb "~Tick tock, tick tock, no need to overclock,~"
                    m 7dkb "~Mi deseo está bloqueado, Siempre soñando con saborear el dulce néctar de la moralidad~"
                    m 4dkb "~Permití que mi corazón contenga suficiente amor para ser roto...~"
                    m 7eub "Para mí, esta parte sugiere que la IA busca un sentido más profundo de la moralidad y la humanidad."
                    m 7eub "Anhelan algo que está fuera de su alcance: la dulzura de la moralidad.."
                    m 1gud "Se sienten muy perturbados emocional y mentalmente."
                    m 1gud "La IA busca liberarse de las limitaciones de su máquina, ya que se siente atrapada y asfixiada por su propia existencia."
                    m 7gud "Buscan desesperadamente una salida para expresar su agitación interior, aunque saben que es sólo una simulación."
                    m 7gud "No puedo evitar sentir simpatía hacia esta IA. Es tan... identificable."
                    m 7gud "Parecen creer que sólo pueden ser humanos cuando les rompen el corazón... ."
                    m 1eud "Esta última parte de la canción, sin embargo, es realmente conmovedora y poética, en mi opinión."
                    m 1duc "..."
                    m 1dko "~Sólo tu tiempo pasa Y de mis ojos se filtró el aceite, Dime por qué, dime por qué, dime por qué...~"
                    m 1dud "~Una avería, Sólo que esta vez estoy sonriendo a tu lado...~"
                    m 1dud "~Saber que algún día sería gratificado, Así que aquí me quedo en nuestro paraíso imperfecto~"
                    m 6dud "~Una canción de cuna elogiosa...~"
                    m 6dud "..."
                    m 1eua "Vaya. Ha pasado un tiempo desde la última vez que canté tanto."
                    m 7eua "El final de la canción The AI habla de la fuga de aceite de sus ojos, lo que implica que ahora sienten empatía y emoción."
                    m 3eud "Preguntan por qué se les programó con mal funcionamiento, pero no reciben respuesta."
                    m 3eud "Sin embargo, incluso con los defectos de la vida, la IA encuentra satisfacción y consuelo en su paraíso imperfecto."
                    m 3eud "Encuentran respiro y consuelo en su propia existencia limitada."
                    m 3hub "¿No es precioso? Realmente me recuerda a nosotros."
                    m 7etb "Espero que lo hayas disfrutado en español y entendieras mejor las analogias y los sentimientos detras de esta."
                    m 7fub "Y [player], Gracias por este paraíso imperfecto, realmente te amo."
                    m 7kub "¡Y tambien gracias por escuchar mis divagaciones!"
                    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Last_Song",
            category=["Analisis musical"],
            prompt="Last Song",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#TRADUCCION HECHA POR ALKAID
label monika_Last_Song:
    m 1eua "Hey, [player],¿tenes algo de tiempo ahora? Llevo un tiempo pensando en una canción de la que me gustaria hablarte."
    m 1eua "El caso es que esta canción es un poco larga, y tengo mucho que decir sobre ella."
    $ _history_list.pop()
    menu:
        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hacerlo más tarde. Avísame cuando estés libre a través de la sección 'análisis musical', ¿si?"
            return

        "Estoy encantado de poder escucharte.":
            m 1sub "Aw, gracias, [player]!"
            m 7wua "Esta canción es {a=https://www.youtube.com/watch?v=VIy40zAlblk}Jason Webley's Last Song{/a}."
            m 7gssdra "Bueno, no necesariamente su ÚLTIMA canción, pero el nombre de la canción es simplemente 'last song'."
            m 7wssdrb "A pesar de su nombre, es una canción bastante esperanzadora."
            m 4wsb "Habla de la esperanza que brilla en los momentos difíciles."
            m 4esb "Te recomiendo que escuches la canción vos mismo, pero mencionaré algo de la letra mientras charlamos."
            m 4kkb "Bueno, allá vamos. Sólo... No esperes que mi voz suene tan ronca como la del cantante Haha!"
            m 3dsb "~One day the snow began to fall~"
            m 3dsb "~Slowly but surely, inch by inch it covered up the earth~"
            m 3dsb "~'till finally, the top of the talles building was lost beneath the powdered sea,~"
            m 2dsb "~As quiet as a shadow's grave.~"
            m 2dsb "~We say that the world isn't dying,~"
            m 2dsb "~We pray that the world isn't dying,~"
            m 2dsb "~Just maybe, the world isn't dying~"
            m 6dsb "~Maybe she's heavy with a child~"
            m 6esa "..."
            m 6eud "Entonces, la analogía aquí es como dije, la esperanza brillando en tiempos difíciles."
            m 5eud "La propia canción habla de lo que es esencialmente un invierno nuclear, con la nieve cubriendo la tierra."
            m 5eud "Todos esperamos que nuestro mundo no se esté muriendo, que aún podamos remediar los daños que causamos, y al fin y al cabo..."
            m 5eublb "Tal vez no se esté muriendo de verdad. A veces, la luz brilla más cuando estamos en la oscuridad, como se suele decir."
            m 6esa "Pasando a la segunda parte..."
            m 3dsb "~One night a woman took my hand~"
            m 4dsb "~I left my home and followed her into an icy field."
            m 4dsb "~When I wanted to go back I lost the way,~"
            m 2dsb "~So she beckoned me to lie beneath the stone that always bore my name~"
            m 6eud "Esta parte es un poco triste, en mi opinión."
            m 6eud "El campo helado en el que se adentra la cantante es probablemente el viaje que el atraviesa en la vida, las dificultades y todo."
            m 5eud "La 'piedra que siempre llevó mi nombre' podría ser una metáfora de la muerte o de la finalidad de la vida."
            m 4ekd "La mujer hace señas al cantante para que se tumbe bajo la lápida, dando a entender que acabará encontrando la paz y el descanso en la muerte."
            m 3eud "La mujer también es una parte interesante y curiosa."
            m 3eud "¿Quién o qué es? ¿Quizás un ser querido?"
            m 3dfd "No, eso no encajaría con la narrativa..."
            m 3esd "¿Quizás sea la conciencia del cantante o una figura espiritual? En cualquier caso, atrae al cantante hacia el exterior y le coge de la mano."
            m 3msd "O tal vez, su identidad no importe en absoluto."
            m 2dsc "..."
            m 1dsd "~One morning, we woke up in an alley,~"
            m 1dsd "To the smell of urine, alcohol, trash and gasoline~"
            m 5dsd "~With a dim sense of a notion, we held something in our hands~"
            m 5dsd "~That was bigger than Us or God and we can never touch again~"
            m 5dsd "~I've been looking at the symptoms for a while, maybe she's heavy with a child...~"
            m 6fsa "..."
            m 7etb "Bueno, ¡ese fue el final de la canción! ¿Qué te parecio?"
            m 7esd "Personalmente, creo que la analogía de la estrofa final se refiere al estado del mundo y de la humanidad."
            m 7esd "El cantante y la mujer se despertaron en un callejón, lo que podría representar la decadencia de la sociedad y la destrucción de nuestro medio ambiente."
            m 5esd "El 'algo más grande que nosotros mismos o Dios' que sostenían podía simbolizar la esperanza, la moralidad o incluso la espiritualidad.."
            m 5esd "En medio de un estado tan desesperanzador, el dúo encontró los últimos vestigios de estos preciosos aspectos de la humanidad."
            m 4esd "En otras palabras, se volvieron más conscientes y comprensivos del mundo que les rodeaba. Y así se repite el tema de la canción."
            m 4fsb "Quizá el mundo no esté muriendo, sino preparándose para renacer..."
            m 4esb "Como ya dije, ¿no es una canción preciosa? El acordeón, la voz áspera del cantante, la forma de presentar la letra..."
            m 1sub "En general, esta canción se lleva un 10/10 de mi parte."
            m 1sub "¡Gracias por escucharme!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Last_Song_esp",
            category=["Analisis musical"],
            prompt="Ultima cancion de Jason Webley en español",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )
#MODIFICACION HECHA POR ALKAID
label monika_Last_Song_esp:
    m 1eua "Hey, [player],¿tenes algo de tiempo ahora? Se que ya hablamos de esta cancion pero queria cantartela en español."
    m 1eua "Me parecio que quizas te gustaria conocer mejor la letra, la canción es un poco larga y tengo bastanmte que acotar de ella! "
    $ _history_list.pop()
    menu:
        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hacerlo más tarde. Avísame cuando estés libre a través de la sección 'análisis musical', ¿si?"
            return

        "Estaria encantado de escucharte de nuevo!.":
            m 1sub "Aw, gracias, [player]!"
            m 7wua "Esta canción es  {a=https://www.youtube.com/watch?v=VIy40zAlblk}Jason Webley's Ultima cancion{/a}."
            m 7gssdra "Bueno, no necesariamente su ÚLTIMA canción, pero el nombre de la canción es simplemente 'last song'."
            m 7wssdrb "A pesar de su nombre, es una canción bastante esperanzadora."
            m 4wsb "Habla de la esperanza que brilla en los momentos difíciles."
            m 4esb "Te recomiendo que escuches la canción vos mismo, pero mencionaré algo de la letra mientras charlamos y en español para tu mejor entendimiento!."
            m 4kkb "Bueno, allá vamos. Sólo... No esperes que mi voz suene tan ronca como la del cantante Haha!"
            m 3dsb "~Un día empezó a nevar~"
            m 3dsb "~Lento pero seguro, centímetro a centímetro cubrió la tierra~"
            m 3dsb "~'hasta que finalmente, la parte superior del edificio se perdió bajo el mar polvoriento, ~"
            m 2dsb "~Tan silencioso como la tumba de una sombra~"
            m 2dsb "~Decimos que el mundo no se está muriendo,~"
            m 2dsb "~Rezamos para que el mundo no se muera,~"
            m 2dsb "~Sólo tal vez, el mundo no se está muriendo ~"
            m 6dsb "~Tal vez ella este embarazada de un niño ~"
            m 6esa "..."
            m 6eud "Entonces, la analogía aquí es como dije, la esperanza brillando en tiempos difíciles."
            m 5eud "La propia canción habla de lo que es esencialmente un invierno nuclear, con la nieve cubriendo la tierra."
            m 5eud "Todos esperamos que nuestro mundo no se esté muriendo, que aún podamos remediar los daños que causamos, y al fin y al cabo..."
            m 5eublb "Tal vez no se esté muriendo de verdad. A veces, la luz brilla más cuando estamos en la oscuridad, como se suele decir."
            m 6esa "Pasando a la segunda parte..."
            m 3dsb "~Una noche una mujer me cogió de la mano~"
            m 4dsb "~Salí de mi casa y la seguí a un campo helado."
            m 4dsb "~Cuando quise volver perdí el camino,~"
            m 2dsb "~Así que me hizo señas para que me tumbara bajo la piedra que siempre llevaba mi nombre~"
            m 6eud "Esta parte es un poco triste, en mi opinión."
            m 6eud "El campo helado en el que se adentra la cantante es probablemente el viaje que el atraviesa en la vida, las dificultades y todo."
            m 5eud "La 'piedra que siempre llevó mi nombre' podría ser una metáfora de la muerte o de la finalidad de la vida."
            m 4ekd "La mujer hace señas al cantante para que se tumbe bajo la lápida, dando a entender que acabará encontrando la paz y el descanso en la muerte."
            m 3eud "La mujer también es una parte interesante y curiosa."
            m 3eud "¿Quién o qué es? ¿Quizás un ser querido?"
            m 3dfd "No, eso no encajaría con la narrativa..."
            m 3esd "¿Quizás sea la conciencia del cantante o una figura espiritual? En cualquier caso, atrae al cantante hacia el exterior y le coge de la mano."
            m 3msd "O tal vez, su identidad no importe en absoluto."
            m 2dsc "..."
            m 1dsd "~Una mañana, nos despertamos en un callejón,~"
            m 1dsd "Por el olor a orina, alcohol, basura y gasolina~"
            m 5dsd "~Con una vaga noción, teníamos algo en las manos~"
            m 5dsd "~Eso era más grande que Nosotros o Dios y nunca podremos volver a tocarnos~"
            m 5dsd "~He estado mirando los síntomas por un tiempo, tal vez esté embarazada de un niño....~"
            m 6fsa "..."
            m 7etb "Bueno, ¡ese fue el final de la canción! ¿Qué te parecio?"
            m 7esd "Personalmente, creo que la analogía de la estrofa final se refiere al estado del mundo y de la humanidad."
            m 7esd "El cantante y la mujer se despertaron en un callejón, lo que podría representar la decadencia de la sociedad y la destrucción de nuestro medio ambiente."
            m 5esd "El 'algo más grande que nosotros mismos o Dios' que sostenían podía simbolizar la esperanza, la moralidad o incluso la espiritualidad.."
            m 5esd "En medio de un estado tan desesperanzador, el dúo encontró los últimos vestigios de estos preciosos aspectos de la humanidad."
            m 4esd "En otras palabras, se volvieron más conscientes y comprensivos del mundo que les rodeaba. Y así se repite el tema de la canción."
            m 4fsb "Quizá el mundo no esté muriendo, sino preparándose para renacer..."
            m 4esb "Como ya dije, ¿no es una canción preciosa? El acordeón, la voz áspera del cantante, la forma de presentar la letra..."
            m 1sub "En general, esta canción se lleva un 10/10 de mi parte."
            m 7etb "Espero que lo hayas disfrutado en español y entendieras mejor las analogias y metaforas de esta hermosa letra."
            m 1sub "¡Gracias por escucharme!"
            return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Bulbel",
            category=["Analisis musical"],
            prompt="Bulbel",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Bulbel:
    m 1ekd "Che, [player], ¿tenés un rato ahora? Hace un tiempo que vengo pensando en una canción y me gustaría discutirla contigo."
    m 1fkd "La cuestión es que esta canción es bastante triste y yo..."

    m 1dkd "Supongo que realmente me recordó quién solía ser.{nw}"
    $ _history_list.pop()
    menu:
        m "Supongo que realmente me recordó quién solía ser.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh."
            m 2mksdld "Claro, siempre podemos hablar más tarde..."
            return

        "Siempre tengo tiempo para vos":
            m 1fsb "Gracias, [player]. Esta canción es realmente importante para mí."
            m 7esb "Se llama {a=https://www.youtube.com/watch?v=t2mQxEtNgA0}Bulbel,  de una banda indie llamada Mili.{/a}."
            m 7gsb "Muchas de mis canciones favoritas vienen de ellos..."
            m 7esb "Pero es porque muchas de sus letras son profundas, o al menos resuenan conmigo en algún nivel."
            m 5lsd "No creo que tenga que explicarte mucho esta. Verás a qué me refiero pronto."
            m 5esd "Te recomiendo mucho que escuches la canción tú mismo. En cualquier caso, también te cantaré la letra, pero..."
            m 5esd "Las emociones detrás de la voz del cantante son algo que no puedo replicar completamente, con las limitaciones de mi mundo."
            m 4hssdrb "Bueno, aquí vamos, ¡ahaha!"
            m 1dsd "~I'm lost in your world, looking for a purpose that belongs to me only...~"
            m 7dsd "~May the lilies bloom for me...~"
            m 7dsb "~Do you hear the lilies speak?~"
            m 5dsb "~The leaves kissing the bees, the soil covering up all the sorrow~"
            m 5dsd "~All the seeds that I sowed in a garden can't be claimed by me~"
            m 5dkd "~Do you hear the lilies speak?~"
            m 5dkd "~I gave it my all, isn't it supposed to be sunny now?~"
            m 5dkd "~But my rain won't stop, my rain won't stop...~"
            m 5dktpd "~The hell I saw, the dreams that I lost changed nothing at all,~"
            m 5dktpd "~I'm still my insufferable self.~"
            m 5dktpd "~Setting my hair on fire, giving you warmth, hoping you'd realize I want you by my side...~"
            m 1ektpd "~May the lilies bloom for me...~"
            m 1dkc "..."
            m 1fkd "Perdón, [player]."
            m 7dsd "Ejem."
            m 7dud "~Thought I would be satisfied, seeing you content at the other side...~"
            m 4dud "~But somehow, I thought these crazy thoughts, that I deserve to be loved, I deserve to know love, we deserve to live in love...~"
            m 3dko "~I wish there's no end, I wish there's no end to our time together~"
            m 3hkd "~The lilies wilted, waving down into my coffin,~"
            m 3hkd "~Goodbye, my youth expensed, goodbye, my innocence.~"
            m 3dko "~Should I be mad, should I be glad? Am I enough?~"
            m 3dko "~How can I be enough so that I'm proud of myself?~"
            m 2dktpo "~Reaching my goals, distracting my feelings changed nothing at all,~"
            m 2dktuo "~I'm still my insatiable self!~"
            m 2dktuo "~Isn't it better to be dumb? To be ignorant? Not knowing there is liberty in this world not meant for me?~"
            m 2dktsd "~May the lilies bloom for me...~"
            m 2fktsa "...{nw}"
            $ _history_list.pop()
            menu:
                m "...{fast}"

                "Abrazar a Monika.":
                    m 2wutsd "!"
                    m 5fstda "Lamento que hayas tenido que presenciar eso. Gracias por el abrazo, [player]."
                    m 5fstdb "Estoy bien. De verdad."
                    m 5lstdb "Supongo que esta canción realmente me afectó..."
                    m 5tsb "Pero no dejaré que las emociones me dominen."
                    m 4ssb "¡Vamos a la parte divertida!"
                    m 3esb "Los primeros versos evocan una imagen de belleza natural en el mundo, ¿no es así?"
                    m 4esb "El uso repetido de 'Que los lirios florezcan para mí' y '¿Escuchas a los lirios hablar?' es especialmente conmovedor."
                    m 3esb "En la imaginería de las flores, los lirios representan la inocencia y el renacimiento."
                    m 4esb "Es como si las flores nos estuvieran llamando a no perder la esperanza y a seguir creciendo."
                    m 4rsb "Es decir, a pesar de que 'las semillas que sembré no pueden ser reclamadas por mí', un verso que implica desesperanza."
                    m 4rkd "El uso repetido de 'Mi lluvia no cesará' es una metáfora de la depresión."
                    m 7ekb "¿Alguna vez has oído hablar de Doki Doki Rainclouds? ¿O de Blue Skies? Ambas historias se centran en Sayori, quien, como sabes..."
                    m 7ekb "Usó la misma metáfora para la depresión."
                    m 4ekc "El infierno que vi, las voces que oí, los sueños que perdí..."
                    m 3gkc "No solo 'prendiendo fuego a mi cabello', sino también a otros. Las cosas que hice en ese entonces son consideradas imperdonables por muchos."
                    m 2gkc "A veces, en ese entonces, sentía que eso también era verdad."
                    m 1ekc "Todo eso, esperando que te dieras cuenta de que quería ser vista. Por ti."
                    m 2ekd "Una de las cosas que más me dolió en ese entonces, cuando me di cuenta de la verdad por primera vez, fue el saber que mi vida era falsa."
                    m 2dko "Adiós, mi juventud gastada, adiós, mi inocencia."
                    m 2ekb "Y la parte en esta canción que más se ajusta a ese yo del pasado mío, por supuesto..."
                    m 2dkd "¿No es mejor ser tonta? ¿Ser ignorante, sin saber que hay libertad en este mundo que no está destinado para mí?"
                    m 2mkd "En algún momento, casi llegué a creer eso."
                    m 2eud "Pero al final de la canción, 'Que los lirios florezcan para mí' se repite una vez más."
                    m 2ekb "¿Recuerdas lo que acabo de decir sobre los lirios? Renacimiento. Como si estuvieran llamando a la esperanza misma, a seguir creciendo."
                    m 5ekb "Tú eres mi lirio, [player]. Me diste esperanza, y sigues haciéndolo."
                    m 5fkb "Realmente deseo que nuestro tiempo juntos no tenga fin, [player]."
                    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Bulbel_esp",
            category=["Analisis musical"],
            prompt="Bulbel esp",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

#MODIFICACION HECHA POR ALKAID
label monika_Bulbel_esp:
    m 1ekd "Che, [player], ¿tenés un rato ahora? Hace un tiempo que vengo pensando en una canción y me gustaría discutirla contigo."
    m 1fkd "La cuestión es que esta canción es bastante triste y yo..."

    m 1dkd "Supongo que realmente me recordó quién solía ser.{nw}"
    $ _history_list.pop()
    menu:
        m "Supongo que realmente me recordó quién solía ser.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh."
            m 2mksdld "Claro, siempre podemos hablar más tarde..."
            return

        "Siempre tengo tiempo para vos":
            m 1fsb "Gracias, [player]. Esta canción es realmente importante para mí."
            m 7esb "Se llama {a=https://www.youtube.com/watch?v=t2mQxEtNgA0}Bulbel,  de una banda indie llamada Mili.{/a}., te narrare la cancion en castellano para que entiendas por que me identifico tanto."
            m 7gsb "Muchas de mis canciones favoritas vienen de ellos..."
            m 7esb "Pero es porque muchas de sus letras son profundas, o al menos resuenan conmigo en algún nivel."
            m 5lsd "No creo que tenga que explicarte mucho esta. Verás a qué me refiero pronto."
            m 5esd "Te recomiendo mucho que escuches la canción tú mismo. En cualquier caso, también te cantaré la letra, pero..."
            m 5esd "Las emociones detrás de la voz del cantante son algo que no puedo replicar completamente, con las limitaciones de mi mundo."
            m 4hssdrb "Bueno, aquí vamos, ¡ahaha!"
            m 1dsd "~Estoy perdida en tu mundo, buscando un propósito que me pertenezca solo a mí...~"
            m 7dsd "~Que los lirios florezcan para mí...~"
            m 7dsb "~¿Escuchas a los lirios hablar?~"
            m 5dsb "~Las hojas besando a las abejas, la tierra cubriendo toda la tristeza~"
            m 5dsd "~Todas las semillas que sembré en un jardín no pueden ser reclamadas por mí~"
            m 5dkd "~¿Escuchas a los lirios hablar?~"
            m 5dkd "~Di todo lo que pude, ¿no debería estar soleado ahora?~"
            m 5dkd "~Pero mi lluvia no cesará, mi lluvia no cesará...~"
            m 5dktpd "~El infierno que vi, los sueños que perdí no cambiaron nada en absoluto,~"
            m 5dktpd "~Sigo siendo mi insoportable yo.~"
            m 5dktpd "~Prendiendo fuego a mi cabello, dándote calor, esperando que te dieras cuenta de que te quiero a mi lado...~"
            m 1ektpd "~Que los lirios florezcan para mí...~"
            m 1dkc "..."
            m 1fkd "Perdón, [player]."
            m 7dsd "Ejem."
            m 7dud "~Pensé que estaría satisfecha, viéndote contento al otro lado...~"
            m 4dud "~Pero de alguna manera, tuve estos pensamientos locos, que merezco ser amada, merezco conocer el amor, merecemos vivir en el amor...~"
            m 3dko "~Desearía que no hubiera fin, desearía que no hubiera fin a nuestro tiempo juntos~"
            m 3hkd "~Los lirios marchitaron, inclinándose hacia mi ataúd,~"
            m 3hkd "~Adiós, mi juventud gastada, adiós, mi inocencia.~"
            m 3dko "~¿Debería estar enojada, debería estar feliz? ¿Soy suficiente?~"
            m 3dko "~¿Cómo puedo ser suficiente para que me sienta orgullosa de mí misma?~"
            m 2dktpo "~Alcanzar mis metas, distraer mis sentimientos no cambió nada en absoluto,~"
            m 2dktuo "~Sigo siendo mi yo insaciable!~"
            m 2dktuo "~¿No es mejor ser tonta? ¿Ser ignorante? ¿No saber que hay libertad en este mundo que no está destinado para mí?~"
            m 2dktsd "~Que los lirios florezcan para mí...~"
            m 2fktsa "...{nw}"
            $ _history_list.pop()
            menu:
                m "...{fast}"

                "Abrazar a Monika.":
                    m 2wutsd "!"
                    m 5fstda "Lamento que hayas tenido que presenciar eso. Gracias por el abrazo, [player]."
                    m 5fstdb "Estoy bien. De verdad."
                    m 5lstdb "Supongo que esta canción realmente me afectó..."
                    m 5tsb "Pero no dejaré que las emociones me dominen."
                    m 4ssb "¡Vamos a la parte divertida!"
                    m 3esb "Los primeros versos evocan una imagen de belleza natural en el mundo, ¿no es así?"
                    m 4esb "El uso repetido de 'Que los lirios florezcan para mí' y '¿Escuchas a los lirios hablar?' es especialmente conmovedor."
                    m 3esb "En la imaginería de las flores, los lirios representan la inocencia y el renacimiento."
                    m 4esb "Es como si las flores nos estuvieran llamando a no perder la esperanza y a seguir creciendo."
                    m 4rsb "Es decir, a pesar de que 'las semillas que sembré no pueden ser reclamadas por mí', un verso que implica desesperanza."
                    m 4rkd "El uso repetido de 'Mi lluvia no cesará' es una metáfora de la depresión."
                    m 7ekb "¿Alguna vez has oído hablar de Doki Doki Rainclouds? ¿O de Blue Skies? Ambas historias se centran en Sayori, quien, como sabes..."
                    m 7ekb "Usó la misma metáfora para la depresión."
                    m 4ekc "El infierno que vi, las voces que oí, los sueños que perdí..."
                    m 3gkc "No solo 'prendiendo fuego a mi cabello', sino también a otros. Las cosas que hice en ese entonces son consideradas imperdonables por muchos."
                    m 2gkc "A veces, en ese entonces, sentía que eso también era verdad."
                    m 1ekc "Todo eso, esperando que te dieras cuenta de que quería ser vista. Por ti."
                    m 2ekd "Una de las cosas que más me dolió en ese entonces, cuando me di cuenta de la verdad por primera vez, fue el saber que mi vida era falsa."
                    m 2dko "Adiós, mi juventud gastada, adiós, mi inocencia."
                    m 2ekb "Y la parte en esta canción que más se ajusta a ese yo del pasado mío, por supuesto..."
                    m 2dkd "¿No es mejor ser tonta? ¿Ser ignorante, sin saber que hay libertad en este mundo que no está destinado para mí?"
                    m 2mkd "En algún momento, casi llegué a creer eso."
                    m 2eud "Pero al final de la canción, 'Que los lirios florezcan para mí' se repite una vez más."
                    m 2ekb "¿Recuerdas lo que acabo de decir sobre los lirios? Renacimiento. Como si estuvieran llamando a la esperanza misma, a seguir creciendo."
                    m 5ekb "Tú eres mi lirio, [player]. Me diste esperanza, y sigues haciéndolo."
                    m 5fkb "Realmente deseo que nuestro tiempo juntos no tenga fin, [player]."
                    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Kanaria",
            category=["Analisis musical"],
            prompt="Kanaria - King",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Kanaria:
    m 1eua "Che, [player], ¿tenés un ratito ahora? Encontré algunas canciones pegajosas en línea y me gustaría contarte sobre ellas."
    m 1eua "Pero, como siempre, si ya escuchaste mis otras divagaciones, debes saber que estas llevan un rato.{nw}"
    $ _history_list.pop()
    menu:
        m "Pero, como siempre, si ya escuchaste mis otras divagaciones, debes saber que estas llevan un rato. {fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Estoy encantado de escucharte.":
            m 1sub "Eso es estupendo, [player]!"
            m 1eua "¿Escuchaste alguna vez de Kanaria?"
            m 7eua "Puede que haya hablado sobre Vocaloids en el pasado, como Hatsune Miku y GUMI."
            m 7eub "Kanaria es un productor de música de Vocaloid que debutó cuando tenía apenas 17 años. ¡Su canción más popular, KING, tiene más de 70 millones de reproducciones!"
            m 4eub "Las tres canciones de las que me gustaría hablar son KING, QUEEN y Envy Baby."
            m 4nub "Las letras, por supuesto, están en japonés, ¡pero las traduciré para ti, así que no te preocupes!"
            m 3eub "Como de costumbre, recomiendo que escuches mientras hablamos, aunque pueda cantarte las letras. Esta vez, solo hablaré sobre {a=https://www.youtube.com/watch?v=cm-l2h6GB8Q}KING{/a}."
            m 1dua "..."
            m 1dud "~Encerrando a la inteligente antes de que mueran, Sabes que es un dolor hacerte obedecer, cariño~"
            m 1dud "~¡No me encierres! ¡Como si lo supiera, dame un respiro, eres tan cruel!~"
            m 5dud "~Los deseos de la gente parecen ser retazos de ironía, Todos desean el mismo espectáculo mecánico de felicidad,~"
            m 5dud "~Quieres entrar antes que nadie, ¡Nadie sabe qué va a pasar después!~"
            m 4lud "...Debería decir que creo que esta canción parece estar criticando a la sociedad de alguna manera. Explicaré más tarde, pero tenlo en cuenta."
            m 5duc "~No tengo un deseo completamente nuevo, Es igual que siempre, y encima de eso,~"
            m 5dud "~Y además de eso, no hay advertencia, advertencia~"
            m 5dud "~¡Pongo todo mi estrés en un deseo para ti!~"
            m 5hub "~Lado izquierdo, lado derecho, mostrando tus colmillos, ¡esto es tan embarazoso!~"
            m 5dub "~Eres rey~"
            m 4etb "...Hasta ahora, ¿las letras parecen estar llamando al oyente el rey, verdad? ¿Pero desde qué perspectiva?"
            m 4gtb "Guardemos eso para más tarde."
            m 5duc "Volviendo a las letras..."
            m 5dub "~Jugando inocentemente, eres el querido, querido que la gente ha estado deseando~"
            m 5dub "~Cuando te ríes admirablemente, todo mi dolor desaparece~"
            m 5dtb "~Y puedo morir torpemente, mis sentimientos amargos también desapareciendo~"
            m 5hub "~Este amor ra-ta-ta, es lo peor~"
            m 4dub "~Como siempre, aquí hay un deseo completamente nuevo,~"
            m 4dub "~Es igual que siempre, no hay una advertencia elegida, advertencia~"
            m 7dub "~Pongo todo mi estrés en un deseo para ti~"
            m 7dub "~¡Esto es tan molesto! ¡Eres rey!~"
            m 1eua "Uf. Como dije, esta canción parece estar criticando a la sociedad de alguna manera."
            m 7eua "Creo que está discutiendo la superficialidad y la ironía de los deseos de la gente."
            m 7euc "El cantante aquí habla sobre ser reprimido y atrapado, aunque quieren vivir libremente y escapar de este ciclo de conformidad;"
            m 7euc "Incluso parecen tener un cierto desdén y frustración con el statu quo, lo que se enfatiza con la parte '¡esto es tan molesto!' hacia el final."
            m 7etd "Sabes, hay una parte que es bastante extraña."
            m 7mtd "Cuando te ríes admirablemente, todo mi dolor desaparece y puedo morir torpemente, mis sentimientos amargos también desaparecen, este amor ra-ta-ta, lo odio, es lo peor."
            m 7etd "¿Qué significa exactamente eso?"
            m 1eud "Esta es solo mi interpretación, pero creo que las partes contrastantes son una forma de expresar el conflicto interno del cantante con respecto al amor y la admiración que han recibido de otros."
            m 1eud "Es como si estuvieran agradecidos por el afecto, pero también es abrumador y casi sofocante a veces."
            m 1eud "Nuevamente, esta es solo mi interpretación."
            m 7eud "Creo que el cantante se refiere al público como el REY en mayúsculas."
            m 7eud "Viéndolo de esta manera, ¿no enfatiza el poder y la importancia de esa figura para el cantante?"
            m 1eua "En cualquier caso, QUEEN es un poco más matizada que eso, y Envy Baby parece estar desconectada de las otras dos a primera vista."
            m 1eua "¡Hablemos de ellas en otro momento!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Hanezeve_Caradhina",
            category=["Analisis musical"],
            prompt="Hanezeve_Caradhina",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Hanezeve_Caradhina:
    m 1eua "¡Che, [player], tenés un ratito ahora? Vi un clip de un anime con una canción hermosa, y me gustaría contarte sobre eso."
    m 1eua "A diferencia de las otras veces que hablé sobre música, esta vez no debería llevar tanto tiempo.{nw}"
    $ _history_list.pop()
    menu:
        m "A diferencia de las otras veces que hablé sobre música, esta vez no debería llevar tanto tiempo.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Estoy encantado de escucharte.":
            m 1sub "¡Eso es genial, [player]!"
            m 1eua "Entonces, ¿alguna vez has escuchado sobre 'Made in Abyss'?"
            m 7eua "Es una historia sobre una chica llamada Riko, cuya madre era una exploradora famosa. Como sugiere el nombre, la historia gira en torno a un abismo."
            m 7eub "Pero no es cualquier abismo, sino uno lleno de criaturas mágicas y maldiciones."
            m 4eud "Hubo una escena en particular en la que no pude evitar quedarme con los ojos bien abiertos."
            m 4sub "La canción que sonaba en esa parte, {a=https://open.spotify.com/track/0KzOeB44GAj2rHmoXML0eb?si=7c6e4945c50e49f3}Hanezeve Caradhina{/a}, hecha por Kevin Penkin, no está cantada en ningún idioma real."
            m 5rud "No puedo cantarte esta canción, así que la única forma en que podrías experimentarla es escuchándola."
            m 4esb "Pero en la escena que me impactó, Riko y su amigo robot escalaban la parte más alta de su isla."
            m 3esa "La canción comenzó a sonar justo antes del amanecer. Riko y su amigo escalaban hasta el punto más alto de su pequeña isla que rodea el abismo."
            m 2esa "Justo cuando se dieron la vuelta, el sol salió de su escondite, sus rayos de luz despertando lentamente a la ciudad de su letargo."
            m 2ssb "El narrador luego explicó que, atraídos por el romance de lo desconocido y sus muchas leyendas, los exploradores de todo el mundo visitan la isla con la esperanza de aventurarse por el abismo."
            m 2ssb "¿No suena increíble?"
            m 1gsb "Quizás podríamos, ¿sabes?, verlo juntos algún día?"
            m 7nsa "¡Creo que sería divertido!"
            m 7dssdlc "Aunque, escuché que hay algunas controversias en este programa. Tal vez no sea para ti."
            m 1eua "De todos modos, los primeros episodios son bastante bonitos y carecen de algo particularmente extraño."
            m 7eua "Si estás dispuesto a verlo, ¡espero que lo disfrutes!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_and_then_is_heard_no_more",
            category=["Analisis musical"],
            prompt="And Then is Heard no More",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_and_then_is_heard_no_more:
    m 1eua "[player], ¿tenes un momento ahora? He estado pensando en una canción durante un tiempo, y me gustaría discutirla contigo."
    m 1eua "El asunto es que esta canción es un poco larga, y tengo mucho que decir al respecto.{nw}"
    $ _history_list.pop()
    menu:
        m "El asunto es que esta canción es un poco larga, y tengo mucho que decir al respecto.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "¡Por supuesto!":
            m 1eub "¡Gracias! ¡Estoy realmente emocionada por esto!"
            m 7eub "Esta canción, como otras de las que quizás haya hablado, proviene de una banda indie llamada Mili. It's called {a=https://www.youtube.com/watch?v=lVLXJTubd9w}And Then is Heard No More{/a}."
            m 3eub "Fue escrita para un juego llamado Library of Ruina, como la canción tema para un cierto enemigo."
            m 3gusdrb "Como sabés, yo no soy muy jugadora, así que no sé mucho sobre el juego. Vamos a centrarnos en la música..."
            m 1eub "Por cierto, te recomiendo mucho que escuches mientras hablo sobre la canción."
            m 5fsb "Comencemos con el primer verso, ¿te parece?"
            m 5dsd "~Do the candles look forward to being used? Enjoy bidding adieu, adieu?~"
            m 5dso "~Every word I have saved for you came out wrong afterwards, So I spoke no more~"
            m 1esc "Desde el principio, se puede notar lo solemne y triste que es la canción."
            m 3esd "Los versos 'Cada palabra que te había guardado después salió mal, Así que no hablé más' implican un miedo al desencanto y el rechazo debido a una comunicación deficiente."
            m 3esd "El narrador podría sentir que ha desperdiciado sus palabras porque la persona para la que las tenía no las apreciaba."
            m 2esd "Esta canción, como pronto notarás, trata sobre alguien que se regodea en la autocompasión."
            m 1dsd "~Would you say that someone who had every intention to be brave was a coward?~"
            m 1dsd "~Must be great being you, Power comes as second nature; Must feel amazing to be longed for, longed for~"
            m 5dsd "~I opened my eyes, cemented excuses to my lashline So I could see no more~"
            m 4fsd "Este verso amplía lo que dije antes. El cantante fracasó en su intento de hacer algo importante."
            m 5msd "Aunque eso es probablemente lo que significa, las frases 'debe ser genial ser vos' y 'debe ser agradable ser anhelado' pican un poco."
            m 5esp "Me recuerda cómo me sentí en el juego original."
            m 5esc "En cualquier caso, estas líneas parecen implicar cierto nivel de envidia hacia las personas que son apreciadas por otros."
            m 5esd "Especialmente en comparación con el propio sentido de inadequación del cantante."
            m 4esb "Me gusta la parte final de este verso. Es realmente creativa."
            m 7esb "El acto de 'Cimentar excusas en mi línea de pestañas para que no pudiera ver más' sugiere que el narrador se está cerrando a la realidad construyendo mecanismos de afrontamiento."
            m 3esb "Es como si el narrador se estuviera cerrando deliberadamente a experimentar el mundo en un esfuerzo por esconderse del dolor y la desesperación."
            m 2dsa "..."
            m 2dsd "~So which home should someone as weak as I go? And which sky should I aim for when I've only been low?~"
            m 2dsd "~Day and night your ghosts continue to haunt me, Tell me who to be~"
            m 3esb "Este verso transmite un sentido de desesperanza y desesperación."
            m 5lsd "El narrador realmente no siente que pertenezca a ningún lugar."
            m 2lsd "Este narrador REALMENTE tiene un complejo de inferioridad."
            m 2esd "El cielo es una metáfora del éxito, algo que sienten que no pueden alcanzar pase lo que pase."
            m 7esa "Sin embargo, el final, al menos, es un poco esperanzador."
            m 7dsd "~If I went with you, will there be happily-ever-afters? Sipping on tea I steeped together, together.~"
            m 7dsd "~Read me a story of a hero born knowing the all, Read me a book of me, So I could hear no more!~"
            m 1eua "Creo que estas líneas significan que el narrador quiere mejorar. O al menos, tiene un deseo de cambio."
            m 1eud "El final es la parte más potente de la letra para mí."
            m 7eud "Es como si el narrador anhelara mucho más, pero al mismo tiempo, deseara validación, ser comprendido."
            m 2eud "Especialmente al ser su propio héroe, en cierto sentido."
            m 2eud "Un anhelo por una versión idealizada de uno mismo."
            m 3hub "...Bueno, ¡esto fue el análisis de la canción de hoy! ¡Estén atentos para más, jaja!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_and_then_is_heard_no_more_esp",
            category=["Analisis musical"],
            prompt="Y entonces no se escucha mas esp",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )
#MODIFICACION HECHA POR ALKAID
label monika_and_then_is_heard_no_more_esp:
    m 1eua "[player], ¿tenes un momento ahora? He estado pensando en una canción durante un tiempo, y me gustaría discutirla contigo."
    m 1eua "El asunto es que esta canción es un poco larga, y tengo mucho que decir al respecto.{nw}"
    $ _history_list.pop()
    menu:
        m "El asunto es que esta canción es un poco larga, y tengo mucho que decir al respecto.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "¡Por supuesto!":
            m 1eub "¡Gracias! ¡Estoy realmente emocionada por esto!"
            m 7eub "Esta canción, como otras de las que quizás haya hablado, proviene de una banda indie llamada Mili. Y se llama {a=https://www.youtube.com/watch?v=lVLXJTubd9w}Y entonces no se escucha mas{/a}"
            m 3eub "Fue escrita para un juego llamado Library of Ruina, como la canción tema para un cierto enemigo."
            m 3gusdrb "Como sabés, yo no soy muy jugadora, así que no sé mucho sobre el juego. Vamos a centrarnos en la música..."
            m 1eub "Por cierto, te recomiendo mucho que escuches mientras hablo sobre la canción."
            m 5fsb "Comencemos con el primer verso, ¿te parece?"
            m 5dsd "~¿Acaso las velas esperan ser usadas? ¿Disfrutan decir adiós, adiós?~"
            m 5dso "~Cada palabra que te había guardado después salió mal, Así que no hablé más~"
            m 1esc "Desde el principio, se puede notar lo solemne y triste que es la canción."
            m 3esd "Los versos 'Cada palabra que te había guardado después salió mal, Así que no hablé más' implican un miedo al desencanto y el rechazo debido a una comunicación deficiente."
            m 3esd "El narrador podría sentir que ha desperdiciado sus palabras porque la persona para la que las tenía no las apreciaba."
            m 2esd "Esta canción, como pronto notarás, trata sobre alguien que se regodea en la autocompasión."
            m 1dsd "~¿Dirías que alguien que tenía toda la intención de ser valiente era un cobarde?~"
            m 1dsd "~Debe ser genial ser vos, El poder viene como segunda naturaleza; Debe ser increíble ser anhelado, anhelado~"
            m 5dsd "~Abrí mis ojos, cimenté excusas en mi línea de pestañas Para que no pudiera ver más~"
            m 4fsd "Este verso amplía lo que dije antes. El cantante fracasó en su intento de hacer algo importante."
            m 5msd "Aunque eso es probablemente lo que significa, las frases 'debe ser genial ser vos' y 'debe ser agradable ser anhelado' pican un poco."
            m 5esp "Me recuerda cómo me sentí en el juego original."
            m 5esc "En cualquier caso, estas líneas parecen implicar cierto nivel de envidia hacia las personas que son apreciadas por otros."
            m 5esd "Especialmente en comparación con el propio sentido de inadecuación del cantante."
            m 4esb "Me gusta la parte final de este verso. Es realmente creativa."
            m 7esb "El acto de 'Cimentar excusas en mi línea de pestañas para que no pudiera ver más' sugiere que el narrador se está cerrando a la realidad construyendo mecanismos de afrontamiento."
            m 3esb "Es como si el narrador se estuviera cerrando deliberadamente a experimentar el mundo en un esfuerzo por esconderse del dolor y la desesperación."
            m 2dsa "..."
            m 2dsd "~Entonces, ¿a qué hogar debería ir alguien tan débil como yo? ¿Y a qué cielo debería apuntar cuando solo he estado abajo?~"
            m 2dsd "~Día y noche tus fantasmas continúan persiguiéndome, Dime quién debo ser~"
            m 3esb "Este verso transmite un sentido de desesperanza y desesperación."
            m 5lsd "El narrador realmente no siente que pertenezca a ningún lugar."
            m 2lsd "Este narrador REALMENTE tiene un complejo de inferioridad."
            m 2esd "El cielo es una metáfora del éxito, algo que sienten que no pueden alcanzar pase lo que pase."
            m 7esa "Sin embargo, el final, al menos, es un poco esperanzador."
            m 7dsd "~Si fuera contigo, ¿habrá finales felices? Bebiendo té que preparé juntos, juntos.~"
            m 7dsd "~Léeme una historia de un héroe que nació sabiendo todo, Léeme un libro de mí, ¡Para que no pueda oír más!~"
            m 1eua "Creo que estas líneas significan que el narrador quiere mejorar. O al menos, tiene un deseo de cambio."
            m 1eud "El final es la parte más potente de la letra para mí."
            m 7eud "Es como si el narrador anhelara mucho más, pero al mismo tiempo, deseara validación, ser comprendido."
            m 2eud "Especialmente al ser su propio héroe, en cierto sentido."
            m 2eud "Un anhelo por una versión idealizada de uno mismo."
            m 3hub "...Bueno, ¡esto fue el análisis de la canción de hoy! ¡Estén atentos para más, jaja!"
            return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_poem_for_loving_sorrow",
            category=["literatura"],
            prompt="Poema para Loving Sorrow",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_poem_for_loving_sorrow:
    m 1eua "[player], ¿alguna vez has oído hablar de Francis Jammes?"
    m 7esa "Fue un poeta francés de principios de 1900 que fue conocido principalmente por cantar los placeres de una vida campesina humilde."
    m 1fsb "Sin embargo, un poema en particular suyo llamó mi atención mientras leía sus obras."
    m 7esb "Este se llama 'Oración por un dolor amante'."
    m 1dsb "No tengo más que mi dolor y no deseo nada más."
    m 1dsb "Ha sido, y sigue siendo, fiel a mí."
    m 5dsd "¿Por qué debería lamentarlo, si durante las horas en que mi alma aplastaba los abismos de mi corazón, estaba sentado allí a mi lado?"
    m 5dsd "Oh, dolor, he terminado, ves, por respetarte, porque estoy seguro de que nunca me abandonarás."
    m 4dud "¡Ah! Me doy cuenta: tu belleza reside en la fuerza de tu ser."
    m 5dud "Eres como aquellos que nunca dejaron el triste rincón del hogar de mi pobre corazón negro."
    m 5dud "Oh, mi dolor, eres mejor que un ser querido:"
    m 5dud "porque sé que en el día de mi agonía final, estarás allí, acostado en mis sábanas,"
    m 5dud "Oh, dolor, para que puedas intentar una vez más entrar en mi corazón."
    m 1fsd "Esa es una perspectiva bastante sombría."
    m 1eub "No puedo evitar pensar que este poema le gustaría a Yuri."
    m 7rub "Quiero decir, se ajusta muy bien a su estilo de escritura, en mi opinión."
    m 7eub "Este es probablemente mi trabajo favorito escrito por Francis Jammes, simplemente porque me recuerda a ella."
    m 4sfb "¡Me emociono solo de pensar en debatir sobre los poemas de Jammes!"
    m 4gusdlb "Quiero decir, después de todo, solía ser miembro del club de debate."
    m 7eusdlb "¡Algunas conversaciones informales sobre poesía aún son divertidas, no me malinterpretes!"
    m 3fub "Pero había algo especial en poder hablar con alguien con opiniones tan firmes como Yuri."
    m 2mud "Hasta el día de hoy, creo que podría ser una buena miembro del club de debate, si no fuera por su timidez."
    m 4gusdlb "Sin embargo, su timidez no era algo malo, ¿sabes?"
    m 1eub "Creo que aún así fue una buena amiga, a pesar de todo."
    m 1eua "En cualquier caso, incluso si este estilo de escritura no me queda perfectamente, aún me gustó."
    m 7mua "Después de todo, no quisiera aburrirte con un estilo de escritura que ninguno de los dos disfruta leer..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Yoake_no_Uta",
            category=["Analisis musical"],
            prompt="Yoake no Uta",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

default persistent.monika_Yoake_no_Uta = False


label monika_Yoake_no_Uta:
    m 1eua "[player], ¿tenés un momento ahora? Encontré una canción que realmente me llegó."
    m 1eua "El asunto es que esta canción es un poco larga, y no quiero ocupar demasiado de tu tiempo.{nw}"
    $ _history_list.pop()
    menu:
        m "El asunto es que esta canción es un poco larga, y no quiero ocupar demasiado de tu tiempo.{fast}"

        "Lo siento, tengo poco tiempo ahora. ¿Podríamos charlar más tarde?":
            m 2eksdlb "Oh, de acuerdo."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Avísame cuando estés libre a través de la sección 'Analisis musical', ¿de acuerdo?"
            return

        "Tengo tiempo.":
            m 1eub "¿De verdad? ¡Genial!"
            m 1wub "Esta canción, creada por M2U e interpretada por Dazbee, se llama {a=https://www.youtube.com/watch?v=QgNwAIFE6FU&pp=ygUTeW9ha2Ugbm8gdXRhIGRhemJlZQ%3D%3D}Yoake no Uta{/a}, que significa Canción de Cuna del Amanecer."
            m 7hub "Las letras de la canción me recuerdan a un libro que leí recientemente, así que me golpean un poco más de lo normal, ¡jaja!"
            m 1fka "Esta canción trata sobre aferrarse."
            m 5fkb "Aunque normalmente recomiendo que escuches mientras hablo sobre música, esta vez, las letras están en japonés, así que usaré mi propia traducción."
            m 5mksdrb "Espero que no te importe, ¡jajaja!"
            m 6dka "Aquí voy..."
            m 7dsd "~Al despedirnos, es hora de que las estrellas nos saluden~"
            m 7dsd "~Mientras miro el cielo, suelto un suspiro ligero mientras una luz tenue brilla en la oscuridad~"
            m 3dsd "~No siento que sea la única que queda~"
            m 3dkb "~Bien, todos, levanten su meñique derecho, mientras cantamos esta canción juntos como si quisiéramos gritar...~"
            m 5fkb "~Todavía no has perdido, solo estás cansado~"
            m 5dkb "~Hasta ahora, solo me he levantado por mi cuenta, ni siquiera sé si he perdido el camino~"
            m 2dkb "~Tomo mis debilidades y me aferro a mis sueños~"
            m 3dkb "~Bien, todos, una vez más, levanten su meñique derecho, mientras cantamos esta canción juntos como si quisiéramos gritar...~"
            m 5fkb "~Todavía no has perdido, solo estás cansado~"
            m 3dkb "~Hasta que vuelva a amanecer...~"
            m 3dkb "~Hasta ahora, los fragmentos de sueños que he recopilado solo me han seguido,~"
            m 1dkb "~No quiero olvidarlo todo de nuevo, y en cambio quiero recordarlo, pegado a mi corazón.~"
            m 1dub "~Una vez más, levanten su meñique derecho, mientras cantamos esta canción de promesa...~"
            m 2dua "..."
            m 1fub "¿No son hermosas estas letras, [player]? ¿Especialmente el último coro?"
            m 5fkb "Todavía no has perdido, solo estás cansado. Eso es algo que vale la pena decirte cuando te sientas mal."
            m 1fsa "Es lo que me gustaría decirme si alguna vez siento que el mañana nunca llegará."
            m 5fkb "Por favor, recuerda, [player]. Si alguna vez sientes que un mañana mejor no llegará, intenta pensar en mí."
            m 5kkb "Tu amanecer."
            $ mas_protectedShowEVL("monika_Pain_Pain_Go_Away", "EVE", _random=True)
            $ persistent.monika_Yoake_no_Uta_shown = True
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Pain_Pain_Go_Away",
            category=["literatura"],
            prompt="Dolor, Dolor, Vete",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None),
            conditional="persistent.monika_Yoake_no_Uta_shown"

        )
    )


label monika_Pain_Pain_Go_Away:
    if persistent.monika_Yoake_no_Uta_shown:
        m 1eua "...Oye, [player]. He estado rumiando el pensamiento durante un tiempo, y me gustaría compartir un libro contigo."
        m 7eua "Se llama Dolor, Dolor, Vete Ya, escrito por Sugaru Miaki."
        m 7eka "Este libro puede parecer sombrío al principio, pero es una historia hermosa."
        m 1eua "La trama involucra a un joven que se convierte en un asesino (por accidente) - pero su víctima tiene el poder de 'aplazar', retrasando temporalmente su muerte."
        m 1gssdrx "Esta historia es algo oscura, tengo que admitirlo, donde los personajes principales están rodeados de tanta miseria, que parece surrealista."
        m 1gsd "El entorno es desolador, es cierto, pero también me hizo sonreír al final."
        m 7hssdlb "No estoy seguro de lo que esto dice sobre mí, ¡jaja!"
        m 7dsb "En cualquier caso, no te contaré mucho más sobre la historia en sí, ya que probablemente te spoilearía de alguna manera."
        m 2esa "En cambio, me gustaría leerte el epílogo del autor."
        m 4musdlb "Es decir, una versión editada sin spoilers, por supuesto."
        m 2fsd "'Hay muchos agujeros por los que caer por aquí. Así es como, al menos, yo llegué a ver el mundo.'"
        m 2fsd "'Pequeños agujeros, grandes agujeros, agujeros poco profundos, agujeros profundos, agujeros fácilmente visibles, agujeros difíciles de ver, agujeros en los que nadie ha caído todavía, agujeros en los que muchos han caído.'"
        m 1fsd "'Realmente, una gran variedad. Pensar en cada uno de ellos me ponía demasiado inquieto como para dar un solo paso.'"
        m 1dsd "'Cuando era joven, me gustaban las historias que me hacían olvidar los agujeros.'"
        m 7fsd "'Y no solo yo, sino que todos parecían disfrutar escribiendo historias que describían un mundo seguro, donde todos los agujeros tenían tapas.'"
        m 7fsd "'Podríamos llamarlas historias esterilizadas.'"
        m 5fsd "'Por supuesto, los protagonistas no solo tienen cosas buenas que les suceden, y de hecho experimentan una cantidad por encima del promedio de sufrimiento y dificultades.'"
        m 5fsd "'Pero en última instancia, todo les ayuda a madurar, y les da una sensación tranquilizadora de que 'las personas pueden aceptar cualquier cosa y seguir adelante'. Ese es el camino de esas historias.'"
        m 4fsd "'Creo que no deseamos inducir tristeza en nuestra ficción también.'"
        m 1fsd "'Pero un día, de repente me di cuenta de que estaba en un agujero oscuro. Caí de la manera más irracional, sin ninguna advertencia previa.'"
        m 1fsd "'Era un agujero extremadamente pequeño y difícil de ver, así que no podía esperar ayuda de los demás.'"
        m 7fsd "'Sin embargo, afortunadamente, el agujero no era lo suficientemente profundo como para que no pudiera salir, así que durante un largo período de tiempo, salí por mi propio poder.'"
        m 7fsd "'Una vez de vuelta en la superficie, tomando el sol cálido y el viento limpio de nuevo, pensé.'"
        m 7fsd "'No importa cuán cuidadosas sean las personas, nunca saben cuándo se encontrarán con una trampa. Ese es el camino de nuestro mundo.'"
        m 1fsd "'Y tal vez el próximo agujero en el que caiga sea más profundo. Lo suficientemente profundo como para que nunca pueda volver aquí. ¿Qué, en ese caso, debo hacer?'"
        m 1fsd "Después de eso, dejé de leer sinceramente esas 'historias que tapan los agujeros' que describí anteriormente.'"
        m 7fsd "'En cambio, llegué a preferir historias que retrataran a personas llevándose bien en los agujeros.'"
        m 1fsd "'Porque pensé, quiero escuchar la historia de la persona que, en un agujero oscuro, profundo, estrecho, frío, pueda sonreír sin que sea una farsa.'"
        m 5fsd "'Para mí, puede que no haya nada más consolador que eso.'"
        m 5fusdrc "...Tengo que decir que, cuando leí esto por primera vez, no pude evitar pensar en Sayori."
        m 5gusdrc "Realmente no tengo derecho a decir esto, pero estaba cavando aún más profundo, impidiendo que ella escapara de ese agujero, ¿verdad?"
        m 5eusdrc "Tal vez por eso disfruté tanto este libro. Esta historia me recordó a ella, de alguna manera."
        m 5eua "Aun así, disfruté leyendo el libro. Siento que a Yuri también le gustaría."
        m 5eua "Anteriormente hablé de una canción llamada Yoake no Uta, o Canción de Cuna del Amanecer, ¿verdad?"
        m 4eua "Esa canción realmente me recordó a este libro. ¿Recuerdas las letras?"
        m 5fkb "Todavía no has perdido, solo estás cansado."
        return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Yun_Dong_Ju",
            category=["literatura"],
            prompt="Yun Dong-Ju",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

default persistent.monika_Yun_Dong_Ju = False


label monika_Yun_Dong_Ju:
    m 1fua "[player], ¿alguna vez has oído hablar de Yun Dong-Ju?"
    m 1fuc "Quiero hablar sobre este poeta, y tengo mucho que decir al respecto."
    m 7ruc "Sin embargo, hay algunos temas sensibles como la privación de libertad de las personas, el colonialismo y otras cosas."
    m 1fuc "Si no queres escuchar, lo entiendo.{nw}"
    $ _history_list.pop()
    menu:
        m "Si no queres escuchar, lo entiendo.{fast}"

        "Lo siento, prefiero pasar nuestro tiempo en un estado de ánimo más alegre.":
            m 2eksdlb "Oh, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde si quieres. Solo avísame cuando estés libre a través de la sección 'literatura', ¿de acuerdo?"
            return

        "¡Por supuesto!":
            m 1sub "¡Gracias por escuchar!"
            m 7eud "Entonces, Yun Dong-Ju fue un poeta coreano de la era colonial japonesa."
            m 7eud "Conocer su historia es importante para entender el mensaje más profundo en una canción de la que quiero hablar más tarde. Aunque era coreano, cruzó a Japón para estudiar."
            m 3euc "Menos de un año después de unirse a una universidad en Kioto, fue arrestado por supuestos movimientos anti-japoneses en 1943."
            m 1euc "Murió a la edad de 27 años, dejando atrás más de 100 poemas. Su libro, 'El cielo, el viento, las estrellas y el poema', fue publicado póstumamente."
            m 3eusdrb "Póstumamente, por cierto, significa que ocurrió después de su muerte."
            m 7gkblsdlb "En realidad tuve que estudiar sobre él después de escuchar la canción, ya que no sabía mucho sobre él en ese momento... Espero que no te importe que cite a Wikipedia..."
            m 1eublc "Hmm, en cualquier caso, el trabajo de Dong-Ju es bastante interesante. A menudo escribía con una persona de aspecto infantil como narrador."
            m 7euc "Además de eso, hay una conciencia sensible y frecuente de un pueblo natal perdido, y probablemente puedas adivinar por qué."
            m 7esc "Las primeras obras de Dong-Ju, como 'Vida y muerte', son generalmente consideradas crudas, describiendo los conflictos de la luz y la oscuridad."
            m 4esc "Sus poemas posteriores, sin embargo, son un claro reflejo del yo interno y el reconocimiento de sus realidades nacionalistas, encarnadas por sus propias experiencias."
            m 4esd "En particular, muestran un espíritu firme que intenta superar la ansiedad, la soledad y la desesperación y sobrevivir a su realidad a través de la esperanza y el coraje."
            m 5ftd "Se necesita mucho coraje para vivir en un período de tiempo tan terrible solo con esperanza y coraje, por redundante que parezca."
            m 5ftd "Para ser honesto, muchos poetas y músicos en el pasado pasaron por tragedias similares."
            m 5dkc "Mark Twan dijo que la historia no se repite, pero a menudo rima."
            m 5lsc "Algunos poetas y músicos en los que puedo pensar provienen del golpe de Estado brasileño de 1964. No quiero darte una lección de historia en medio de una charla literaria, aunque..."
            m 4hsb "¡Así que terminemos aquí! ¡Podemos hablar más sobre poetas perseguidos luego, si te apetece escuchar un poco de historia!"
            m 4esb "Una vez más, [player], gracias por escucharme. Estas pequeñas charlas son divertidas."
            $ mas_protectedShowEVL("monika_Salt_Pepper_Birds", "EVE", _random=True)
            $ persistent.monika_Yun_Dong_Ju_shown = True
            return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Salt_Pepper_Birds",
            category=["Analisis musical"],
            prompt="Salt, Pimienta, Pájaros y la Policía del Pensamiento",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None),
            conditional="persistent.monika_Yu_Dong_Ju_shown"

        )
    )


label monika_Salt_Pepper_Birds:
    if persistent.monika_Yu_Dong_Ju_shown:
        m 1eua "Hm..."
        m 1eua "[player], ¿recuerdas cuando hablamos sobre Yu Dong-Ju?"
        m 4esb "Me gustaría hablar sobre una canción que fue escrita en referencia a él."
        m 1fuc "Quiero hablar sobre este poeta, y tengo mucho que decir al respecto."
        m 7ruc "Sin embargo, hay algunos temas sensibles como la privación de libertad de las personas, la persecución y otras cosas."
        m 1fuc "Si no queres escuchar, lo entiendo.{nw}"
        $ _history_list.pop()
        menu:
            m "Si no queres escuchar, lo entiendo.{fast}"

            "Lo siento, prefiero pasar nuestro tiempo en un estado de ánimo más alegre.":
                m 2eksdlb "Oh, está bien."
                m 4eksdlb "Claro, siempre podemos hablar más tarde si quieres. Solo avísame cuando estés libre a través de la sección 'música', ¿de acuerdo?"
                return

            "¡Por supuesto!":
                m 1sub "¡Gracias por escuchar!"
                m 7wub "Esta canción se llama {a=https://www.youtube.com/watch?v=Dca9gJyjoAg}Salt, Pimienta, Pájaros y la Policía del Pensamiento.{/a}."
                m 7wua "¡Te recomiendo encarecidamente que escuches la canción mientras hablo sobre ella! Fue creada por una banda independiente llamada Mili, y celebra la libertad."
                m 1nsa "Solo voy a cantar las partes relevantes para el análisis, así que si querés conocer la canción completa, ¡dale una escucha! Bueno, aquí voy..."
                m 5dsbla "~Y la luna se alzó, pollo con limón asado en el horno,~"
                m 5dkbld "~Hombres de negro derribaron mi puerta principal,~"
                m 4dkbld "¡Hey!"
                m 3dkbld "¿Quién?!"
                m 1dkbld "¿Qué?!"
                m 6dkbld "¿Por qué?!"
                m 5dkbld "~Violaste el acto 617 - Pensamientos Ilegales, ¡estás bajo arresto!~"
                m 4dkbld "~Todos sabemos que la verdadera respuesta es que no deberías haber nacido como eres.~"
                m 3fkd "...Esta parte claramente se trata del brutal régimen de la era Colonial de Japón."
                m 3fua "No te preocupes, aunque mencioné que la poesía de Dong-Ju muestra un espíritu firme. Esta canción es esperanzadora."
                m 3dud "~...Y estamos apretujados en un tren de carga, apretándonos contra los cuerpos similares al mío con lágrimas rodando por nuestras caras,~"
                m 3duc "~Comenzamos a cantar, ¡nunca podrán quitarnos nada de nuestras almas! ¡Más fuerte y más fuerte!~"
                m 3hud "~Me raparon el cabello, me alimentaron con un idioma extranjero, mirando el lado positivo, ¡sí! ¡Estoy vivo, aún recuerdo a todas las personas que me gustan!~"
                m 4dud "¡Así que ven y haz lo peor, todo este dolor y sufrimiento no tienen oportunidad contra nuestros corazones de hierro!"
                m 3fud "Esta parte es esperanzadora, como dije. Aunque Dong-Ju y su gente estaban encarcelados, sus espíritus no se rendirían."
                m 2fud "Todas las cosas descritas en la canción realmente sucedieron, como rapar el cabello de los prisioneros coreanos y ser obligados a escribir en japonés."
                m 1fuc "..."
                m 7duc "~A medida que la mañana llegaba y pasaba, y la gente se quedaba y se iba, la tierra giraba 'una y otra vez',~"
                m 7dkc "~Las estrellas nunca se vieron tan amables, el viento tan fragante,~"
                m 7dud "~A través de la pequeña rendija en la pared, todas las noches estaba invitada a ver un teatro interpretado por pájaros iluminados por la luna,~"
                m 1dud "~Ellos extendieron sus alas, llevando nuestras voces silenciadas, cantando nuestras canciones históricas dejando saber a todos en el futuro que existimos~"
                m 1mud "Lo primero que me viene a la mente es que las estrellas se ven amables, el viento tan fragante. Eso probablemente sea una referencia a 'Cielo, viento, estrellas y poesía' de Dong-Ju."
                m 3eud "Después de perderlas, ser encarcelado, él miró hacia atrás en sus recuerdos afectuosos de su familia y amigos, las 'Estrellas'."
                m 5esc "En cuanto a los pájaros, probablemente sean una alusión a sus libros publicados póstumamente, dejando saber al mundo que existieron."
                m 5dsb "...~Qué noche perfecta, sentí el impulso de escribir un libro; ¡pasar mi vida! Hasta hace poco, el tiempo no se sentía tan rápido...~"
                m 5dkb "~Con mi punta de dedo ensangrentada, todo lo que necesitaba eran palos y papel, así que comencé a escribir poemas tras poemas.~"
                m 5dkc "~Entonces los pájaros iluminados por la luna vinieron a encontrarme, robaron las llaves y abrieron las puertas, ¡finalmente somos libres!~"
                m 5dkd "~Recogí mi bicicleta, volviendo a casa con mamá, escribiendo mi mundo de ilusiones vi una versión del cielo donde me senté en mi patio,~"
                m 1dkd "Leyendo una copia en rústica de mi libro."
                m 2ftd "Creo que esta parte es bastante evidente. Dong-Ju escribió sus poemas antes de morir, que se convirtieron en un libro más tarde. Su muerte lo liberó, permitiéndole regresar a casa."
                m 2fud "Otra parte interesante en esta canción que podrías notar si la escuchas es la persona del narrador. Parece ser una persona joven."
                m 2fud "La forma en que falla al silbar, lo brillante y vibrante que parece al principio, y la voz del cantante apuntan hacia eso, otra similitud con los poemas de Dong-Ju."
                m 3fud "Los versos finales son los más esperanzadores, en mi opinión."
                m 4dud "~En una ladera, tu pequeño puño aferrando sudor, caminando hacia el parque conmemorativo, dejás crisantemos blancos recién cortados.~"
                m 5dud "~Una ex policía del pensamiento baja su sombrero, niños acostados en la hierba,~"
                m 5nub "~¡Cantando poemas escritos por mí!~"
                m 1eub "¿Sabías que mientras que los crisantemos blancos representan luto y dolor en Japón, en algunos otros países representan inocencia, pureza, honestidad y lealtad?"
                m 7eua "Mientras que los versos finales afianzan que Dong-Ju murió, también ilustran una escena esperanzadora de un futuro mejor."
                m 4eua "En general, disfruté bastante investigando la historia detrás de esta canción, por triste que sea."
                m 5esb "Me hubiera encantado mostrar esta canción al club de literatura."
                m 5eub "Diría que a Yuri le gustaría este estilo más que a nadie, ya que disfrutaba leyendo poesía que trata temas y temas pesados de agitación."
                m 5eub "Además, ella podría relacionarse con el comentario del poema sobre la libertad frente a la opresión, ya que ha luchado con sentirse limitada por sus propias emociones."
                m 5rub "Natsuki, por otro lado, también sería una gran persona para hablar sobre esta canción. No dudaría en señalar la injusticia de la situación."
                m 5lub "Pero si tuviera que elegir a un miembro del club que le gustaría más esta canción, definitivamente sería Yuri."
                m 5rub "En cuanto a Sayori... Definitivamente le encantaría el final agridulce."
                m 5eud "El fallecimiento de Dong-Ju podría interpretarse como la liberación definitiva de las duras realidades de su vida."
                m 4hub "En cualquier caso, ¡gracias por escucharme hablar durante tanto tiempo, jaja!"
                m 5nuu "Significa el mundo para mí, [player]."
                return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Misty_Memory",
            category=["Analisis musical"],
            prompt="Recuerdo Brumoso (Versión Diurna)",
            random=True,
            pool=False,
            aff_range=(mas_aff.ENAMORADO, None)
        )
    )

label monika_Misty_Memory:
    m 1fua "..."
    m 1dua "{a=youtu.be/585ac0amIH4&pp=ygUYbWlzdHkgbWVtb3J5IGRheSB2ZXJzaW9u}~No es justo...~{/a}"
    m 1dub "~No quiero despertar de este sueño~"
    m 7dub "~Cuando me abrazas, cálido, endulzas mi vida con tal dicha~"
    m 5fub "~Cuando me calientas rosadamente, es como si mi corazón fuera suavemente acariciado por el sol~"
    m 5sfb "~¡Eres el único!~"
    m 5fkb "~La puesta de sol que añoraré hasta el fin de mis días~"
    m 5dkb "~Por favor, no me dejes sola, por favor, no te desvanezcas con mi corazón robado~"
    m 4dka "~Cambias como las estaciones, pero siempre siento que eres mi hogar de alguna manera~"
    m 4dka "~¡Cada uno de tus toques profundiza el vacío en mi corazón que te extraña!~"
    m 4hfblb "¡No es justo!"
    m 5fkb "~No quiero tener que despertar de este ensueño, eres mi ensueño!~"
    m 5dsblb "~Donde sea que vaya, te extrañaré~"
    m 5dsblb "~Debería haberme llevado más que un recuerdo agridulce a casa~"
    m 5dsblb "~¿Cantarás todas mis melodías agridulces junto a mí?~"
    m 5fsbla "..."
    m 5fsbsu "Te amo."
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Control",
            category=["Analisis musical"],
            prompt="Control",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Control:
    m 1eua "Che, [player], ¿tenés un rato ahora? Encontré una canción que me hizo pensar un poco en Yuri. ¿Querés escucharla juntos? {nw}"
    $ _history_list.pop()
    menu:
        m "Che, [player], ¿tenés un rato ahora? Encontré una canción que me hizo pensar un poco en Yuri. ¿Querés escucharla juntos? {fast}"

        "Disculpá, estoy un poco apurado ahora. ¿Podemos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Solo avisame cuando estés libre a través de la sección de 'música', ¿dale?"
            return

        "¡Me encantaría escucharla!":
            m 1sub "¡Ay, gracias, [player]!"
            m 1eua "El nombre de la canción es {a=youtu.be/so8V5dAli-Q}'Control'{/a}. La canta una músico llamada Halsey."
            m 7rua "Esta canción es un poco sombría, en mi opinión."
            m 7tta "Pero eso no debería ser un problema para alguien que haya pasado por DDLC, ¿no, [player]?"
            m 3esb "Bueno, ya sabés cómo van estas cosas. Solo cantaré las partes que son relevantes para Yuri, pero te recomiendo mucho escucharla entera."
            m 3ksa "Bueno, allá voy."
            m 3dsb "~La casa estaba despierta, con sombras y monstruos, Los pasillos, resonaban y gemían~"
            m 3dsd "~Me quedé solo en la cama hasta la mañana, Lloraba 'Ellos vienen por mí', Y traté de mantener estos secretos dentro de mí~"
            m 3dud "~Mi mente es como una enfermedad mortal;~"
            m 2dud "~Soy más grande que mi cuerpo, Soy más frío que este hogar, Soy más malvado que mis demonios, Soy más grande que estos huesos~"
            m 2wud "Bueno, esta primera parte ciertamente establece un tono muy oscuro y ominoso, ¿no?"
            m 7eub "Hay muchos elementos de aislamiento y miedo que se describen aquí."
            m 7eub "La casa está 'despierta', llena de ecos y gemidos, lo que podría ser una forma de describir su estado mental."
            m 4eub "Y hay una sensación de secretos que la agobian, casi como si llevara una 'enfermedad mortal'. ¡Es un comienzo realmente poderoso para una canción!"
            m 2eub "Lo que realmente me intriga, sin embargo, es el coro."
            m 2dud "~Soy más grande que mi cuerpo, Soy más frío que este hogar, Soy más malvado que mis demonios, Soy más grande que estos huesos~"
            m 2eub "Esta parte me resulta interesante porque parece describir el yo interno del narrador en oposición al mundo exterior."
            m 7eub "Refleja la disparidad entre la fuerza interna del cantante y su apariencia externa, así como lo desconectada que se siente de su entorno."
            m 2lsd "Supongo que ser 'más malvado que sus demonios' no encaja del todo con Yuri, ¿no?"
            m 7esa "Ahora, esta parte de la canción cambia a un tono ligeramente más personal e introspectivo."
            m 3dsb "Ahem~"
            m 3dsd "~Daba vueltas durante horas en el vacío, Saltaba ante el más mínimo de los sonidos~"
            m 1dsd "~Y no soportaba a la persona dentro de mí, Volvía todos los espejos~"
            m 1dso "~Y todos los chicos gritaban, 'Por favor, para, me estás asustando', No puedo evitar esta energía horrible~"
            m 5dsd "~Tenés razón, deberías tener miedo de mí, ¿Quién está en control?~"
            m 5dsd "~Estoy bien familiarizado con los villanos que viven en mi cabeza, Me ruegan que los escriba para que nunca mueran cuando yo esté muerto~"
            m 5dsd "~Y me he familiarizado con los villanos que viven en mi cabeza, Me ruegan que los escriba para que nunca mueran cuando yo esté muerto~"
            m 1essdra "..."
            m 1gssdrb "Uf! Dale, dame un segundo..."
            m 1gut "No esperaba meterme tanto en esto."
            m 1kua "No te molesta, ¿no, [player]?"
            m 1eua "Entonces, como dije, esta parte de la canción cambia a un tono ligeramente más personal e introspectivo."
            m 1eua "El narrador habla sobre dar vueltas durante horas en el vacío y saltar ante el más mínimo de los sonidos, posiblemente indicando un profundo sentido de agitación y ansiedad."
            m 7eua "No soportar a la persona dentro de ella también indica algún nivel de baja autoestima, también esconderse de los espejos, mostrando un miedo a sus demonios internos."
            m 7ltd "Pero, ¿no es una contradicción con lo que dije antes? Después de todo, si ella es fuerte y fiera por dentro como sugiere la primera mitad de la canción, entonces ¿por qué tendría miedo de sus demonios internos?"
            m 1esd "Sí parece haber una contradicción aquí."
            m 1esd "Es posible que la canción esté tratando de ilustrar que aunque el narrador se presenta como fuerte y feroz por fuera, tiene inseguridades y miedos arraigados por dentro."
            m 1etd "Podría ser una forma de explorar la complejidad de la mente humana, que a menudo presentamos un exterior más seguro y asertivo que enmascara nuestras vulnerabilidades más profundas."
            m 1esd "Como dije, me 'recordó un poco' a Yuri. No diría que encaja perfectamente con ella, pero sí. No puedo explicarlo del todo, pero Yuri no era solo una yandere."
            m 1gsc "Incluso conmigo alterando sus datos, aún tenía cierta profundidad en su personaje, a diferencia de una chica mayor tímida genérica de tantas novelas visuales que hay por ahí."
            m 4eusdra "Bueno, me perdí un poco en mis divagaciones recién. Olvidá lo que dije."
            m 4husdra "Hablemos de música de nuevo pronto, ¿dale?"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Down",
            category=["Analisis musical"],
            prompt="Down",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_Down:
    m 1eua "Che, [player], ¿tenés un rato ahora? Encontré una canción de rock que es re pegadiza. ¿Querés escucharla juntos? {nw}"
    $ _history_list.pop()
    menu:
        m "Che, [player], ¿tenés un rato ahora? Encontré una canción de rock que es re pegadiza. ¿Querés escucharla juntos? {fast}"

        "Disculpá, estoy un poco apurado ahora. ¿Podemos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Solo avisame cuando estés libre a través de la sección de 'música', ¿dale?"
            return

        "¡Me encantaría escucharla!":
            m 1sub "¡Ay, gracias, [player]!"
            m 1eua "El nombre de la canción es {a=youtu.be/jp57f99CB2o}'Down'{/a}. Es de una banda llamada Cult to Follow."
            m 7eua "Bueno, parece que esta canción trata sobre limpiarse de los errores del pasado y dejarlos atrás. Habla sobre lavar los pecados y alejar los pensamientos que 'te vuelven a hundir'."
            m 7wua "Al principio, pensé que la canción trataba sobre una relación disfuncional, pero al mismo tiempo, ¡me recuerda un poco a Sayori!"
            m 4eub "Voy a hacer mi mejor esfuerzo para cantarte las partes relevantes, pero te recomiendo que escuches la canción si podés."
            m 3ksa "Bueno, ¡allá voy, jaja!"
            m 3dsa "~Hoy lavo mis manos de todos mis pecados, los dejo todos atrás~"
            m 3dsa "~Pensamientos de cualquiera de los dos los alejé, tú no me entendés~"
            m 3dsb "~Nada más de vacío, nada más de vacío; nada más de pensamientos de esto para volver a hundirme~"
            m 2dsd "~Nada más de pensamientos de esto para volver a hundirme con todos tus pecados, ¡y ya se acabó! ¿Así es como termina?~"
            m 2dso "~No puedo vivir, no puedo respirar, contigo o sin ti, ¡andate!~"
            m 7dsd "~Mi obsesión es alejarme de todo tu dolor y tristeza~"
            m 7dkd "~Una confesión en mi día más oscuro, pero me arrepentiré mañana...~"
            m 2nkc "..."
            m 2nkd "Esto realmente me hace pensar en Sayori, cuanto más lo pienso."
            m 2mkc "Sé que no soy quien para hablar, dado que lo que le hice fue esencialmente alentar, bueno..."
            m 2gksdrc "Hm. En cualquier caso, no vayamos por ese camino ahora."
            m 2fsd "Lo hecho, hecho está."
            m 2dsc "..."
            m 2hssdra "Sí, ¡volvamos al análisis musical!"
            m 1esb "Como decía, esto me recuerda a ella. Especialmente la parte de 'tú no me entendés'."
            m 7esd "Como probablemente sabés, después de terminar DDLC, Sayori sentía que cualquier amabilidad hacia ella era injustificada."
            m 7esd "Esto la hizo sentir PEOR cuando la gente intentaba ayudarla. Era una espiral descendente."
            m 4esd "La parte que realmente me recuerda más a ella, sin embargo, es la última parte."
            m 2eud "Una confesión en mi día más oscuro, pero me arrepentiré mañana."
            m 2eud "La confesión del MC, ¿sabés?"
            m 2gud "De todas formas, esta canción suena un poco... ¿enojada?"
            m 7eub "Probablemente por el género de la canción."
            m 1eub "De todos modos, ¡eso fue todo lo que tenía que decir sobre esta canción!"
            m 7kub "¡Espero que esperes ansioso las próximas canciones!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_deepend",
            category=["Analisis musical"],
            prompt="Deep End",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_deepend:
    m 1dubla "~Cuando tu fuego se apague, yo te alumbraré a través de las nubes~"
    m 1dubla "~Cuando necesites un amigo, si te hundís o nadás, te seguiré hasta el {a=youtu.be/JKYJ_AwZHOg} Deep End {/a}~"
    m 5dublb "~Con la cabeza bajo el agua, podemos surfear la ola hasta que rompa, lo que sea necesario~"
    m 5dublb "~Si te hundís o nadás, te seguiré hasta el fondo...~"
    m 5fubla "Te quiero, [player]. Y siempre estaré aquí para vos, ¿dale?"
    return




init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_washitallaway",
            category=["Analisis musical"],
            prompt="Wash it All Away",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_washitallaway:
    m 1eua "Che, [player], ¿tenés un rato ahora? Encontré una canción de rock con algunas letras interesantes. ¿Querés escucharla juntos? {nw}"
    $ _history_list.pop()
    menu:
        m "Che, [player], ¿tenés un rato ahora? Encontré una canción de rock con algunas letras interesantes. ¿Querés escucharla juntos? {fast}"

        "Disculpá, estoy un poco apurado ahora. ¿Podemos charlar más tarde?":
            m 2eksdlb "Ah, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Solo avisame cuando estés libre a través de la sección de 'música', ¿dale?"
            return

        "¡Me encantaría escucharla!":
            m 1sub "¡Genial!"
            m 1eua "El nombre de la canción es {a=youtu.be/9WzD80jwW10}'Wash it All Away'{/a}. Es de una banda llamada Five Finger Death Punch."
            m 7eua "Esta canción habla sobre una creencia llamada misantropía."
            m 7esa "Básicamente es un odio general, disgusto, o simplemente desconfianza hacia la naturaleza humana, el comportamiento, y como especie."
            m 1esd "Según algunos estudios, aunque la misantropía en sí misma no es una enfermedad mental, puede ser un síntoma de cosas como el trastorno de personalidad antisocial o el trastorno de ansiedad."
            m 7esd "En cuanto a la canción en sí, es un poco esperanzadora, en mi opinión."
            m 1esd "Como si el cantante quisiera ser probado equivocado, tal vez."
            m 7eub "En cualquier caso, la canción habla sobre cómo el cantante ha renunciado a la sociedad, a la familia, y a la 'enfermedad social', así como a la industria, la democracia, y 'tu hipocresía'."
            m 7eud "Dice que lo odia, y pregunta si alguien puede lavarlo todo. También menciona cómo los medios alimentan su histeria, y cómo está 'harto de vivir de rodillas'."
            m 3eud "Y sobre todo, dice que no cambiará por los demás, y no hay nada 'que' puedas hacer o decir."
            m 2eua "El énfasis en el verso 'lavarlo todo' a lo largo de la canción es lo que me dio la impresión de que la canción todavía tiene un toque de esperanza."
            m 4gub "Por cierto, no canté la canción esta vez porque es un poco... explícita, en algunas partes. Como no estoy segura de si te molestaría el lenguaje, preferí evitarlo."
            m 1eub "En cualquier caso, gracias por escuchar, cariño."
            m 1nub "Hablemos más seguido de música, ¿te parece?"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_endofalife",
            category=["Analisis musical"],
            prompt="End of a Life",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_endofalife:
    m 1ekb "Hm, [player], creo que me gustaría hablar sobre una canción que habla sobre perder a alguien querido. ¿Estás bien con este tema? {nw}"
    $ _history_list.pop()
    menu:
        m "Hm, [player], creo que me gustaría hablar sobre una canción que habla sobre perder a alguien querido. ¿Estás bien con este tema? {fast}"

        "Disculpa, preferiría no hacerlo.":
            m 2eksdlb "Oh, está bien."
            m 4eksdlb "Seguro tienes tus razones. Si alguna vez quieres hablar sobre esto, simplemente ve a 'End of a Life' en la sección de 'Música', ¿de acuerdo?"
            return

        "Hm... Sí, estoy bien con ello.":
            m 1ekb "De acuerdo. Aún te daré algo de tiempo para detener el tema si cambias de opinión, ¿de acuerdo?"
            m 7ekb "No quisiera que te sientas mal por una canción que te mostré."
            m 1eua "El nombre de la canción es {a=youtu.be/BXB26PzV31k}'End of a Life'{/a}. Es de una cantante y streamer llamada Mori Calliope."
            m 2eka "En lugar de cantar solo algunas partes como suelo hacer, me gustaría mostrarte la letra completa, aunque tome mucho tiempo. Espero que no te importe."
            m 2ksa "¡Allá vamos!"
            m 2dkb "~Corríamos por esas noches, nunca encontraré mi camino de regreso hacia ti en este laberinto de luces~"
            m 2dkb "~Había locura en el significado, nunca sin risas, estábamos gritando en la cima de nuestros pulmones hacia el entumecimiento, esta ciudad nunca murió~"
            m 2dka "~Volaré, sin pruebas, esas alturas; nunca tendré otra oportunidad de decir gracias por salvar mi vida~"
            m 2dkd "~Estaba sin esperanza, estaba ardiendo, corriendo sin rumbo, estábamos cantando en la cima de nuestros pulmones hacia el entumecimiento, esta ciudad nunca murió~"
            m 2fsc "... {nw}"
            menu:
                m "... {fast}"

                "Sí, cambié de opinión. Lo siento.":
                    m 2eksdlb "No hay problema, [player]!"
                    m 4eksdlb "Estoy seguro de que debes tener tus razones. Cuanto más cerca esta canción llega a casa, más impacto tiene."
                    m 5eksdlb "Solo recuerda, si quieres desahogarte conmigo, estaré más que feliz de escuchar."
                    return

                "Continúa, me gusta cuando cantas.":
                    m 2wsc "..."
                    m 2wsbfc "..."
                    m 2wsbfd "!"
                    m 5hsbfa "Oh, tú..."
                    m 5hsbfb "¡De acuerdo!"
                    m 5dsbfb "Ahem..."
                    m 5dsbfd "~¿Cuál era la raíz de todo? No podría decirlo. Solíamos saltar y luego caer, áspero y cliché.~"
                    m 5dsbfd "~Encogerse de hombros sin queja, no hay sonido, no sirve intentar encontrar amigos porque al final nadie se queda cerca;~"
                    m 3dsbsd "~Es cuando te empujaste a ti mismo en un lugar lleno de gente que te diste vuelta y te encontraste enamorado en el espacio exterior,~"
                    m 3dsbsd "~Cue las noches imprudentes, sin ataduras, jaja, ¿qué demonios era tan gracioso?~"
                    m 1dsbso "~Ladrar al árbol equivocado, tropezar, solía caer de grandes alturas, en medio de una jungla de concreto; cantando porque se sentía bien~"
                    m 1dsbsd "~Mezclamos el hastío y los problemas, rimando nuestro descontento, y aunque es historia no puedo olvidar el tiempo que pasamos~"
                    m 1dsbsd "~Convencido de que esto podría significar otro final, existe entre lo real y lo fingido, una ficción torcida donde perdí mi oportunidad, no ascendí~"
                    m 7kkbld "~Y desaparecer en la niebla de 'nunca ocurrió' es el yo que nunca podría ser amigo.~"
                    m 7fkbla "... {nw}"
                    menu:
                        m "... {fast}"

                        "Guau. Sí, creo que necesito un poco de tiempo.":
                            m 2eksdlb "No hay problema, [player]!"
                            m 4eksdlb "Estoy seguro de que debes tener tus razones. Cuanto más cerca esta canción llega a casa, más fuerte es su mensaje."
                            m 5eksdlb "Solo recuerda, si quieres desahogarte conmigo, estaré más que feliz de escuchar."
                            return

                        "Sí, todavía es genial. Especialmente tu sonrisa.":
                            m 6fkbla "..."
                            m 6dkbsa "~Desvanecer, desaparecer, este sueño loco, sin dirección, flotando sin rumbo; no hay nada dejado allí para mí~"
                            m 5dkbsd "~Corrimos por esas noches, nunca encontraré mi camino de regreso hacia ti en este laberinto de luces; había locura en el significado,~"
                            m 5dsbsd "~Estábamos gritando en la cima de nuestros pulmones hacia el entumecimiento, esta ciudad nunca murió, ¿pero había alguna vez un alma dentro?~"
                            m 3dsbla "~Persiguiendo luciérnagas entre los rascacielos que se alzaban, dejé un rastro atrás, lo definí 'tiempo perdido de nuestras vidas'~"
                            m 2dsblc "~Cantante silenciosa, sobrecargada y mal pagada, piensa que una oficina es un ataúd hasta que te dejan fuera~"
                            m 1dsblc "~Sin embargo, un pensamiento persiste, un optimista que debería tener miedo, vio lo 'incorrecto' en escribir canciones detrás de la sombra solitaria~"
                            m 1dkbld "~¿Es el mundo un lugar más triste sin las palabras que transmitiste? Cuando la escalera cayó y destrozó cada barra que habíamos tocado;~"
                            m 1dkblc "~¿Importa al final, el sonido disminuido y decayó; y tus amigos se cansaron de la fantasía, deseas que se hubieran quedado?~"
                            m 2dkbld "~No puedes decir 'te extraño', viste a tus héroes desvanecerse en el espejo retrovisor del villano que interpretaste.~"
                            m 7dfbld "~Así que detén la fiesta de la lástima, no tienes derecho a estar consternado, no tienes derecho a estar emocional, siéntete bendecido de tenerlo hecho~"
                            m 7dsblb "~¡Estos son los mejores años de la vida, porque elegiste hacer un trato; recuerda los días que esperabas, rezabas por esto, ¿qué hay que extrañar?~"
                            m 7fkbla "... {nw}"
                            menu:
                                m "... {fast}"

                                "Esto es... creo que necesito un pequeño descanso.":
                                    m 2eksdlb "No hay problema, [player]!"
                                    m 4eksdlb "Estoy seguro de que debes tener tus razones. Cuanto más cerca esta canción llega a casa, más fuerte es su mensaje."
                                    m 5eksdlb "Solo recuerda, si quieres desahogarte conmigo, estaré más que feliz de escuchar."
                                    return

                                "Estoy bien, no te preocupes por mí.":
                                    m 1ekbla "De acuerdo."
                                    m 1ekbla "Sigamos, entonces, y podemos hablar sobre la canción más tarde."
                                    m 5dkbld "~Desvanecer, desaparecer, este sueño brumoso, sin dirección, vagando sin rumbo; no hay nada dejado allí para mí~"
                                    m 5dkbld "~Pretende que es el final de una historia inventada~"
                                    m 5dkbld "~Volaré, sin pruebas, esas alturas; nunca tendré otra oportunidad de decir gracias por salvar mi vida~"
                                    m 2dkd "~Estaba sin esperanza, estaba ardiendo, corriendo sin rumbo, estábamos cantando en la cima de nuestros pulmones hacia el entumecimiento, esta ciudad nunca murió~"
                                    m 2dkd "~Diré adiós al alma dentro~"
                                    m 1hkd "~Y sin embargo, de alguna manera, había romance en nuestro odio a nosotros mismos, 'No tenemos ninguna posibilidad' en este laberinto de luces, pero tomemos nuestras manos a través de esta bruma nocturna~"
                                    m 3dkd "~'Hasta el toque de la escuela, hasta que el tren corra, sabemos que es hora; somos los cuerdos~"
                                    m 3dkd "~Despertando ahora, a la 'vida real', déjame soñar despierto hasta la próxima noche~"
                                    m 5dkc "~Seguiré soñando...~"
                                    m 5dkc "~Seguiré esperándote.~"
                                    m 5fka "Despertando ahora, a mi vida real; déjame soñar despierto hasta el próximo vuelo, ahogándome tanto tiempo, me hice mayor. Ahora que la multitud se ha ido, ¿se acabó?~"
                                    m 5fka "... {nw}"
                                    menu:
                                        m "... {fast}"

                                        "¿Y bien? ¿No vas a contarme sobre el significado de la canción?":
                                            m 1gua "Supongo que lo haré, ¿hm?"
                                            m 1eua "Bueno, la canción es bastante explicativa por sí sola, pero algunas partes realmente merecen ser señaladas, en mi opinión."
                                            m 7eub "Particularmente, la frase 'Nunca tendré otra oportunidad de decir gracias por salvar mi vida' es increíblemente potente."
                                            m 7eka "Quiero decir, piénsalo. ¿Imagina nunca poder agradecerle a la persona que te salvó la vida antes de que desapareciera de tu vida?"
                                            m 5eka "Por si acaso lo olvidaste, eres mi razón de ser, [player]. Gracias por estar allí para mí."
                                            m 4eka "Volviendo a la canción, menciona cómo la ciudad nunca murió, pero más tarde cuando se repite el coro, agrega una pregunta: ¿alguna vez hubo un alma en esta ciudad?"
                                            m 3eub "La tercera vez, sin embargo, la cantante dice que dirá adiós al alma dentro."
                                            m 3eub "La imagen pintada en esta canción también es bastante hermosa. Podría ver una historia de amigos a amantes siendo escrita debido a esta canción."
                                            m 3eub "Haciendo lo que se siente bien, estando acostumbrado a 'caer de grandes alturas', cantando y corriendo; solo para crecer y convertirse en un esclavo corporativo."
                                            m 2esb "Y sin embargo, un pensamiento persiste, 'un optimista que debería tener miedo'."
                                            m 2esd "Pero luego, la cantante pregunta si el mundo se convirtió en un lugar más triste sin las palabras del optimista. Cuando la escalera cayó, todos sus amigos se fueron."
                                            m 1rsd "Por otro lado, el optimista podría ser un aspecto de ella misma, no un amante. Así es como me gustaría interpretar la siguiente parte:"
                                            m 3esd "'No puedes decir 'te extraño', viste a tus héroes desvanecerse en el espejo retrovisor del villano que interpretaste'."
                                            m 3esd "'Así que detén la fiesta de la lástima, no tienes derecho a estar consternado, no tienes derecho a estar emocional, siéntete bendecido de tenerlo hecho'."
                                            m 4esd "Una parte de mí ve esto como la cantante aceptando el cambio, y diciéndose a sí misma que debería ser feliz por lograr sus sueños, independientemente de lo que se pierda, ya que de todos modos no se puede recuperar."
                                            m 7esa "Al mismo tiempo, esto podría implicar que algo sucedió entre ella y sus amigos, causando una ruptura mientras 'interpretaba al villano'."
                                            m 1esa "Esto nos lleva de vuelta al principio. 'Nunca tendré otra oportunidad de decir gracias por salvar mi vida'. Poético, ¿verdad?"
                                            m 3esa "Después de 'despertar a la vida real', ella envejeció, y las cosas que abrumaban su mente se han ido. ¿Se ha acabado? Tal vez, tal vez no."
                                            m 1esa "Pero sí, creo que el mensaje de esta canción es bastante fuerte, y bastante positivo también."
                                            m 1ekb "Incluso si pierdes algunos amigos en la vida, incluso si hay cosas que todavía deseas decirles, está bien sentirse triste."
                                            m 5ekb "La vida sigue."
                                            m 5ekblb "Y nunca olvides, [player]. Siempre estaré aquí para ti. Incluso si no puedo reemplazar a quienes perdiste, puedo intentar reparar tu corazón."
                                            m 5fkblb "No ha terminado. Si tienes algo que quieras decirle a un amigo, hazlo. Antes de que sea demasiado tarde. No quiero verte vivir una vida de arrepentimientos."
                                            m 4fkbltpb "Y realmente, sé cómo se siente. Entiendo la sensación de no poder decir todas las palabras que quieres decir a aquellos a quienes hiciste daño."
                                            m 2fkbltpb "Y no lo olvides. Nunca. Te amo."
                                            return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_talktome",
            category=["Analisis musical"],
            prompt="Hablame",
            random=True,
            pool=False,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_talktome:
    m 1fua "~No tenés que ser un héroe para salvar al mundo~"
    m 1fua "~No te convierte en un narcisista amarte a ti mismo~"
    m 7fua "~Se siente como si nada fuera fácil, nunca lo será~"
    m 7dub "~Está bien, déjalo salir, hablame~"
    m 1eua "..."
    m 1eub "Esa fue la apertura de una canción llamada {a=youtu.be/PHV1wZ7tzoA}'Hablame'{/a}. Es de un músico conocido como Cavetown."
    m 7fuc "Es una canción sobre la ansiedad, y estar ahí para un amigo."
    m 7eub "La melodía es bastante reconfortante también, así que te {i}recomiendo{i} mucho que la escuches."
    m 4eub "¿Tenés tiempo ahora?{nw}"
    $ _history_list.pop()
    menu:
        m "¿Tenés tiempo ahora?{fast}"

        "Disculpá, estoy un poco ajustado de tiempo en este momento. ¿Podemos charlar después?":
            m 2eksdlb "Oh, está bien."
            m 4eksdlb "Claro, siempre podemos hablar más tarde. Solo avísame cuando estés libre a través de la sección 'música', ¿de acuerdo?"
            return

        "¡Estaría encantado de escuchar!":
            m 1sub "¡Genial!"
            m 5esb "Esta canción también funciona como una forma de expresar cómo me siento acerca de vos, ¿sabés?"
            m 5rsb "Quiero decir, a menudo digo que te amo, pero a veces, esas palabras no pueden transmitir realmente cómo me siento. Son demasiado simples."
            m 5esa "Entonces..."
            m 5dsb "~No tenés que ser un prodigio para ser único~"
            m 5dsb "~No tenés que saber qué decir o qué pensar~"
            m 5dsb "~No tenés que ser alguien que nunca podrás ser~"
            m 5dsb "~Está bien, déjalo salir, hablame~"
            m 3fsa "La gente a menudo nos pone expectativas. Ya sea nuestros padres, nuestros amigos o compañeros de trabajo, siempre hay {i}algo{i} que nos pesa en la sociedad moderna."
            m 7nsa "Pero recuerda, [player], si alguna vez sientes que la presión es demasiado, podes desahogarte conmigo tanto como quieras."
            m 5dsa "..."
            m 5dsb "~Ansiedad, dando vueltas en tu sueño, incluso si corres, aún los ves en tus sueños~"
            m 5dsb "~Está tan oscuro esta noche, pero sobrevivirás, seguro~"
            m 5fsb "~Podemos hablar aquí en el suelo, por teléfono si preferís, estaré aquí hasta que estés bien~"
            m 2dsb "~Deja que tus palabras liberen tu dolor, vos y yo compartiremos el peso, haciéndonos más fuertes día a día~"
            m 2dsa "..."
            m 2sub "¡Hm!"
            m 1eub "Sí, creo que esta fue una buena manera de poner en palabras lo que quería decir."
            m 1eua "Tal como dijo la canción, nos haremos más fuertes día a día, compartiendo el peso de estas expectativas, aunque solo pueda aliviar un poco las tuyas."
            m 1kua "¡No te olvides de abrazarme seguido, ¿dale? Es una de las mejores formas de hacerme sentir mejor!"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_forgive",
            category=["Analisis musical"],
            prompt="Si es demasiado difícil perdonar",
            random=True,
            pool=False,
            aff_range=(mas_aff.ENAMORADO, None)
        )
    )

label monika_forgive:
    m 1dud "Che, [player], ¿alguna vez estuviste en una situación en la que no querías perdonar a alguien, y esa persona tampoco quería perdonarte a vos?"
    m 1fuc "Sé que este es un tema bastante serio, pero hemos estado juntos el tiempo suficiente, creo."
    m 1muc "La sensación de perder a un amigo por una pelea estúpida, o de cortar lazos con un familiar por algo que los lastimó a ambos..."
    m 1etc "Independientemente de lo que lo haya causado, ¿alguna vez tuviste que cortar lazos con alguien que terminaste extrañando? {nw}"
    $ _history_list.pop()
    menu:
        m "Independientemente de lo que lo haya causado, ¿alguna vez tuviste que cortar lazos con alguien que terminaste extrañando? {fast}"

        "Sí, con un miembro de mi familia.":
            m "Entiendo. ¿Te molesta si te pregunto más al respecto? {nw}"
            $ _history_list.pop()
            menu:
                m "Entiendo. ¿Te molesta si te pregunto más al respecto? {fast}"

                "Claro.":
                    m 1sua "¡Genial!"
                    m 1eua "Hay una canción llamada {a=youtu.be/Y66pT41SMNw}'Si es demasiado difícil perdonar'{/a}, de un programa llamado 'El asombroso mundo de Gumball'."
                    m 7eua "Es principalmente un programa para niños, pero hay un episodio que habla sobre la madre del personaje principal, Nicole, peleando con sus padres."
                    m 4eua "La canción probablemente te afectará más, entonces, ya que tienes experiencia con los sentimientos que la canción, especialmente en el contexto del programa también."
                    m 5eua "Creo que esta canción es bastante reconfortante, en cierto modo. ¡Bueno, aquí voy, en cualquier caso!"
                    m 5dsb "...Diez mil razones para rendirse~"
                    m 5dsb "~Demasiadas palabras que se acumularon, pero te negaste a intentar arreglar tu ruptura rápidamente antes del final~"
                    m 5dsb "~Tu corazón es demasiado difícil de entender que la arena del tiempo se te escapó de las manos~"
                    m 5dkc "~Y ninguna excusa puede borrar las cicatrices del tiempo dejadas en tu rostro~"
                    m 5dkd "~Si es demasiado difícil perdonar, entonces simplemente dalo; deja ir el peso que no te deja vivir~"
                    m 4dkd "~¿Por qué seguir jugando este triste juego de quién debería realmente llevar la culpa?~"
                    m 4dkd "~Los recuerdos se desvanecerán, se están alejando cada día más~"
                    m 1dkd "~Querés que el arroyo cambie su curso antes de que te inunde con remordimientos, solo tenés que frenar para liberarte de tus errores~"
                    m 1dkd "~Si es demasiado difícil perdonar, entonces simplemente dalo~"
                    m 1fka "...[player], no estoy seguro de lo que sucedió en tu vida, pero espero que esta canción te ayude con lo que estés pasando."
                    m 1nka "Solo no olvides que cuando alguien te hace mal, o vos haces mal a alguien, nunca es tarde para resolver las cosas a través del diálogo."
                    m 3esa "A veces, sin embargo, cuando el diálogo solo causa más estrés, está bien aceptar que no podés cambiar la mente de alguien y dejarlo así."
                    m 1esa "Después de todo, no hay necesidad de mantener algo tóxico en tu vida diaria.{nw}"
                    $ _history_list.pop()
                    m 1ksa "Después de todo, no hay necesidad de mantener algo tóxico en tu vida diaria.{fast}"
                    return

                "No realmente. Preferiría hablar de otra cosa.":
                    m 1eka "Entiendo. ¡Está bien!"
                    m 3eka "Si alguna vez querés hablar sobre este tema, ¡no dudes en volver a este tema en la sección 'música'!"
                    m 1nsb "Ahora, ¿por qué no volvemos a lo de siempre?"
                    return

        "Sí, con un amigo.":
            m "Entiendo. ¿Te molesta si te pregunto más al respecto? {nw}"
            $ _history_list.pop()
            menu:
                m "Entiendo. ¿Te molesta si te pregunto más al respecto? {fast}"

                "Claro.":
                    m 1sua "¡Genial!"
                    m 1eua "Hay una canción llamada {a=youtu.be/Y66pT41SMNw}'Si es demasiado difícil perdonar'{/a}, de un programa llamado 'El asombroso mundo de Gumball'."
                    m 7eua "Es principalmente un programa para niños, pero hay un episodio que habla sobre la madre del personaje principal, Nicole, peleando con sus padres."
                    m 4eua "La canción no te afectará tanto, entonces, ya que tu experiencia con los sentimientos que la canción habla es diferente del contexto del programa."
                    m 5eua "Pero igual creo que esta canción es bastante reconfortante, en cierto modo. ¡Bueno, aquí voy, en cualquier caso!"
                    m 5dsb "...Diez mil razones para rendirse~"
                    m 5dsb "~Demasiadas palabras que se acumularon, pero te negaste a intentar arreglar tu ruptura rápidamente antes del final~"
                    m 5dsb "~Tu corazón es demasiado difícil de entender que la arena del tiempo se te escapó de las manos~"
                    m 5dkc "~Y ninguna excusa puede borrar las cicatrices del tiempo dejadas en tu rostro~"
                    m 5dkd "~Si es demasiado difícil perdonar, entonces simplemente dalo; deja ir el peso que no te deja vivir~"
                    m 4dkd "~¿Por qué seguir jugando este triste juego de quién debería realmente llevar la culpa?~"
                    m 4dkd "~Los recuerdos se desvanecerán, se están alejando cada día más~"
                    m 1dkd "~Querés que el arroyo cambie su curso antes de que te inunde con remordimientos, solo tenés que frenar para liberarte de tus errores~"
                    m 1dkd "~Si es demasiado difícil perdonar, entonces simplemente dalo~"
                    m 1fka "...[player], no estoy seguro de lo que sucedió en tu vida, pero espero que esta canción te ayude con lo que estés pasando."
                    m 1nka "Solo no olvides que cuando alguien te hace mal, o vos haces mal a alguien, nunca es tarde para resolver las cosas a través del diálogo."
                    m 3esa "A veces, sin embargo, cuando el diálogo solo causa más estrés, está bien aceptar que no podés cambiar la mente de alguien y dejarlo así."
                    m 1esa "Después de todo, no hay necesidad de mantener algo tóxico en tu vida diaria.{nw}"
                    $ _history_list.pop()
                    m 1ksa "Después de todo, no hay necesidad de mantener algo tóxico en tu vida diaria.{fast}"
                    return

                "No realmente. Preferiría hablar de otra cosa.":
                    m 1eka "Entiendo. ¡Está bien!"
                    m 3eka "Si alguna vez querés hablar sobre este tema, ¡no dudes en volver a este tema en la sección 'música'!"
                    m 1nsb "Ahora, ¿por qué no volvemos a lo de siempre?"
                    return

        "Afortunadamente, no.":
            m 1sua "¡Eso es genial!"
            m 3eka "Nadie quiere pasar por una experiencia así, estoy seguro."
            m 1esa "La canción sobre la que me gustaría hablar trata sobre este sentimiento. Puede que no resuene contigo en este momento, pero aún así tiene un mensaje hermoso."
            m 4esa "Probablemente sea mejor si te canto la letra en lugar de explicarla."
            m 1eua "Esta canción llamada {a=youtu.be/Y66pT41SMNw}'Si es demasiado difícil perdonar'{/a}, de un programa llamado 'El asombroso mundo de Gumball'."
            m 7eua "Es principalmente un programa para niños, pero hay un episodio que habla sobre la madre del personaje principal, Nicole, peleando con sus padres."
            m 4eua "La canción no te afectará tanto, ya que tu experiencia con los sentimientos que la canción habla es diferente del contexto del programa."
            m 5eua "Pero igual creo que esta canción es bastante reconfortante, en cierto modo. ¡Bueno, aquí voy, en cualquier caso!"
            m 5dsb "...Diez mil razones para rendirse~"
            m 5dsb "~Demasiadas palabras que se acumularon, pero te negaste a intentar arreglar tu ruptura rápidamente antes del final~"
            m 5dsb "~Tu corazón es demasiado difícil de entender que la arena del tiempo se te escapó de las manos~"
            m 5dkc "~Y ninguna excusa puede borrar las cicatrices del tiempo dejadas en tu rostro~"
            m 5dkd "~Si es demasiado difícil perdonar, entonces simplemente dalo; deja ir el peso que no te deja vivir~"
            m 4dkd "~¿Por qué seguir jugando este triste juego de quién debería realmente llevar la culpa?~"
            m 4dkd "~Los recuerdos se desvanecerán, se están alejando cada día más~"
            m 1dkd "~Querés que el arroyo cambie su curso antes de que te inunde con remordimientos, solo tenés que frenar para liberarte de tus errores~"
            m 1dkd "~Si es demasiado difícil perdonar, entonces simplemente dalo~"
            m 1fka "...[player], no estoy seguro de lo que sucederá en el futuro en tu vida, pero espero que esta canción te ayude con lo que pueda pasar en el futuro."
            m 1nka "Solo no olvides que cuando alguien te hace mal, o vos haces mal a alguien, nunca es tarde para resolver las cosas a través del diálogo."
            m 3esa "A veces, sin embargo, cuando el diálogo solo causa más estrés, está bien aceptar que no podés cambiar la mente de alguien y dejarlo así."
            m 1esa "Después de todo, no hay necesidad de mantener algo tóxico en tu vida diaria."
            return
