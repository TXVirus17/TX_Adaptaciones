default mb_open = False

screen fom_whiteboard_mobile_toolbar(whiteboard, mb_open):

    if renpy.android:

        $ mb_open = True

    if mb_open:

        vbox:
            style_prefix "fom_whiteboard"
            spacing 10
            xalign 1.0
            yalign 0.0
            xoffset 0.0
            yoffset 10
                        
            textbutton "↩ Deshacer" action Function(whiteboard.undo)
            textbutton "↪ Rehacer" action Function(whiteboard.redo)
            textbutton "+ Tamaño" action Function(whiteboard.brush.increment_size)
            textbutton "- Tamaño" action Function(whiteboard.brush.decrement_size)
            textbutton "  Guardar" action Function(whiteboard.save_as_png)
                    

            
        