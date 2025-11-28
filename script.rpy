define chuuya= Character("chuuya nakahara", color="#780F1E")
define ranpo= Character("ranpo edogawa", color="#346a35")
define kunikida= Character("Doppo kunikida", color= "#FFFC42")
define yosano= Character("yosano rosado", color="#6F3181")




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

    kunikida "Bienvenida [nombreXD]"

    scene fondo1

    image dazai0 = "dazai.PNG"
    show dazai0
    with fade

    kunikida "te amo"
    kunikida"..."
    nombreXD "muchas gracias"
    
    scene fondo1
    jugador"hola kunikida"
    kunikida "¿Quieres ir a esta mision?"
    
    menu:
        "no":
            jump pagina_mision
            
            label pagina_agencia:
                scene fondo2
                kunikida "es entendible, eres nueva asi que nos quedamos"
            
        "si":
            jump pagina_agencia
            
            label pagina_mision:
                scene mapa_mision
                kunikida "[nombreXD] esto sera tu primera mision, quisiera disculparme, es inisual enviar personal sin experiencia a una mision pero estamos algo cortos de personal"
            
            
    hide dazai0
    with dissolve

    "se acaba el juego"
    "XD"
return 

label Pormafia:
    
"En desarollo"

return

