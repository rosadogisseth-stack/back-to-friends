define chuuya= Character("Chuuya Nakahara", color="#780F1E")
define Ranpo= Character("Ranpo Edogawa", color="#346a35")
define kunikida= Character("Doppo Kunikida", color= "#FFFC42")
define yosano= Character("Yosano Rosado", color="#6F3181")

#inf del jugador con nombre = nombreXD
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
        
        "Port_mafia":
            $ruta = "Port_mafia"
            jump Port_mafia


label Agencia:
    scene fond_in
    "cualquier error del codigo es culpa del gobierno"
    "Cualquier recurso fue sacado de la serie de bungou stray dog"
    "espero que disfruten del juego"

    play music "audio/kola_io.mp3"

    scene fondo2

    kunikida "Bienvenida [nombreXD]"
    kunikida "Esta es la agecia aqui es donde trabajaras"
    


    scene fondo1


    
    #Desde esta escena faltan sprites

    scene fondo1

    nombreXD"hola kunikida"
    kunikida "Hola [nombreXD]"

    kunikida "Este debe ser tu primer dia"
    kunikida "Espero que logres acostumbrarte al lugar"
    kunikida "Como puedes ver hay personas fuera de lo comun pero eso no significa que seas como ellos"
    kunikida "¿En fin quieres empezar tu primera tarea?"
    
    menu:
        "no":
            jump pagina_agencia
            
            label pagina_agencia:
                scene fondo2
                kunikida "es entendible, eres nueva no te preocupes este trabajo no es para todos"
            
        "si":
            jump pagina_mision
            
            label pagina_mision:

                scene fondoag
            #escena beta antes de añadir la historia principal para que no quede vacio
                kunikida "[nombreXD] Muy bien primero conoce al personal este año muy poco personal se unio aun asi espero que te relaciones muy bien con las personas"
                nombreXD "(Aun que tenia ganas de empezar una mision no queda de mas conocer a todos lo de esta agencia)"    
                nombreXD "(probablemente mis compañeros sean agarables no lo se la verdad estoy emocionada por mi primer dia)" 
                nombreXD "(veo alrededor del salon y noto un chico particular, es muy sonriente para trabajar en esta oficina aburrida)"
                nombreXD "donde esta la gente no veo nadie aqui a quien voy a conocer si no hay nadie"
                Ranpo "Quizas todos estan descansando es festivo asi que deben estar afuera"
                nombreXD "¿Que hacen aqui?"
                Ranpo "¿Que kunikida no te explico? somos una agencia de detectives nos encargamos de casos dificiles y proteger a las personas"
                Ranpo "Soy Ranpo Edogawa tu debes ser [nombreXD]"
                nombreXD "como rayos lo sup..."
                Ranpo "Por que puedo leer tu mente ¡JAJAJAJAJA!"
                Ranpo "es chiste kunikida me conto y por tu comportamiento perdido es obvio que eres nueva"
                nombreXD "Que chiste raro en fin un gusto ¿hay alguien mas al que deba conocer?"
                Ranpo "No hay nadie mas que aqui con podria ser Dazai pero el desaparecio hace unos Dias"
                Ranpo "no te preocupes por el debe estar bien"
                nombreXD "(Que poco interes tiene parece que no le importa mucho)"
                nombreXD "esta bien entonces ¿que debemos hacer?"
                Ranpo "No te preocupes kunikida esta buscando a atsushi el es nuevo pero es agradble tenerlo cerca deberias conocerlo"
                Ranpo "aunque no lo hemos visto desde un tiempo por eso kunikida lo esta buscando"
                nombreXD "se nota que este es un trabajo muy problematico"
                nombreXD "no te preocupes esta agencia de hecho es bastante relajante"


    "se acaba el juego"
    "XD"
return 

label Port_mafia:
    
"En desarollo"

return


