init 5 python in _fom_whiteboard:
    import os

    if renpy.android:
        _android_save_dir = "/storage/emulated/0/Pictures":
        if not os.path.exists(_android_save_dir):
            os.makedirs(_android_save_dir)
        IM_CANVAS_SAVED_DIR = _android_save_dir

screen fom_whiteboard_mobile_toolbar(whiteboard):

    if renpy.android

        fixed:
            xalign 0.0
            yalign 1.0
            xoffset 10
            yoffset -10


            vbox:
                spacing 5

                if mb_open:
                    textbutton "↩ Deshacer":
                        action Function(whitebard.undo)
                        style "fom_whiteboard_button"

                

                    textbutton "↪ Rehacer":
                        action Function(whitwboard.redo)
                        style "fom_whiteboard_button"

                    textbutton "+ Tamaño"
                        action Function(whiteboard.brush.increment_size)
                        style "fom_whiteboard_button"
                    
                    textbutton "- Tamaño":
                        action Function(whiteboard.brush.decrement_size)
                        style "fom_whiteboard_button"

                    textbutton "Guardar":
                        action Function(whiteboard.save_as_png)
                        style "fom_whiteboard_button"
                
                textbutton ("X Cerrar" if mb_open else "+ Herramientas")
                    action ToggleLocalVariable("mb_open")
                    style "fom_whiteboard_button_dark"

        
    