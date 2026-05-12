screen fom_whiteboard_mobile_controls(whiteboard):
    zorder 101  # IMPORTANTE: El original tiene zorder 100. Al poner 101, tus botones siempre estarán "al frente".
    
    frame: # Es como una ventana o caja que agrupa todo.
        xalign 0.98 # Lo pega al borde derecho.
        yalign 0.5  # Lo centra verticalmente.
        background Frame(Solid("#0008"), 4, 4) # Un fondo oscuro semitransparente para que se vea "Pro".

        vbox: # "Vertical Box": Apila los botones uno arriba del otro.
            spacing 15 # Espacio entre botones para que no los presiones por error.

        
label Grosor:
    style "fom_whiteboard_label" # Usa el estilo del mod para que se vea igual.

hbox: # "Horizontal Box": Pone el - y el + a la par.
    # El botón de restar:
    textbutton "[-]" action SetField(whiteboard, "brush_size", max(1, whiteboard.brush_size - 2))
    # EXPLICACIÓN: SetField cambia el valor de la variable. 
    # max(1, ...) evita que el pincel tenga tamaño 0 o negativo (que daría error).

    # El botón de sumar:
    textbutton "[+]" action SetField(whiteboard, "brush_size", min(100, whiteboard.brush_size + 2))
    # EXPLICACIÓN: min(100, ...) pone un límite para que el pincel no cubra toda la pantalla de un clic.

    label "Grosor":
    style "fom_whiteboard_label" # Usa el estilo del mod para que se vea igual.

hbox: # "Horizontal Box": Pone el - y el + a la par.
    # El botón de restar:
    textbutton "[-]" action SetField(whiteboard, "brush_size", max(1, whiteboard.brush_size - 2))
    # EXPLICACIÓN: SetField cambia el valor de la variable. 
    # max(1, ...) evita que el pincel tenga tamaño 0 o negativo (que daría error).

    # El botón de sumar:
    textbutton "[+]" action SetField(whiteboard, "brush_size", min(100, whiteboard.brush_size + 2))
    # EXPLICACIÓN: min(100, ...) pone un límite para que el pincel no cubra toda la pantalla de un clic.

    textbutton "Pegar Color" action [Function(picker.from_clipboard, whiteboard), Hide("fom_whiteboard_color_picker")]

    