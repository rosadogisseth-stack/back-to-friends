#actualiza el código Gisseth y no olvides comentar

define chuuya= Character("chuuya nakahara", color="#28e989")

default jugador = Character("jugador", color="#2e2aeb")

default ruta =""
default nombreXD = ""

screen nombre_jugador():
    modal True

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 15

            text "Escribe tu nombre:"

            input:
                default nombreXD
                length 20
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
                value VariableInputValue("nombreXD")

            textbutton "Aceptar":
                action Return(nombreXD)

label start:

    $ nombreXD = renpy.call_screen("nombre_jugador")

    "Hola [nombreXD]!"

    "escoje que ruta vas a hacer"
    
    menu:
        "Agencia":
            $ruta = "Agencia"
            jump Agencia
        
        "Pormafia":
            $ruta = "Pormafia"
            jump Pormafia


label Agencia:


    play music "audio/kola_io.mp3"

    scene fondo2

    chuuya "pendeja no dura nada"

    scene fondo1

    image dazai0 = "dazai.PNG"
    show dazai0
    with fade

    chuuya "te amo"
    chuuya "me voy"
    nombreXD "¿Y este random?"
    hide dazai0
    with dissolve

    "se acaba el juego"
    "XD"
return 

label Pormafia:
    
"En desarollo"

return
