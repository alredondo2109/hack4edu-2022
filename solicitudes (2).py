# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:22:37 2022

@author: QUILLOS
"""

import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import datetime
import wikipedia





#escuchamos el microfono y devuelve el audio como texto al código de python
def trasformar_audio_en_texto():

    #almacenamos el recognizer en una variable
    r = sr.Recognizer()

    #configuramos el microfono
    with sr.Microphone() as origen:
        #establecemos un tiempo de espera para despues empezar a escuchar
        #treshold: umbral de espera
        
        # tiempo de espera
        r.pause_threshold = 1

        #informamos que inicio la grabación del micro
        print("ya puedes hablar")

        #creamos una variable para guardar el audio
        #r.listen = comando para escuchar
        #origen= variable que creamos para escuchar el microfono del pc
        audio = r.listen(origen)
        
        #hacemos un try para prepararnos para errores que puedan ocurrir con el micro
        try:
            #buscamos en google lo que escucho y convertirlo en texto
            #llamamos a audio(el archivo que escucho y colocamos el lenguaje
            #que seria es-co "español de colombia")
            pedido = r.recognize_google(audio, language="es-es")

            #imprimimos en pantalla lo que se escucho y se convirtio en texto
            print("Dijiste: " + pedido)

            #devolvemos la solicitud (variable pedido)
            return pedido

        # en caso de que no comprenda el audio, devolvemos el siguiente error
        except sr.UnknownValueError:
            #realizamos una prueba para saber si no comprendio el audio
            # prueba de que no comprendio el audio
            print("Sorry ... no te entendí")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Sorry ... no pude transformar tu voz en texto")

            # devolver error
            return "sigo esperando"

        #tambien podemos encontrar errores que NI IDEA
        #errores inesperados
        except:

            # prueba de que no comprendio el audio
            print("Sorry ... Ni idea.. algo debio salir mal")

            # devolver error
            return "sigo esperando"


#Vamos a crear una función para que yulexa pueda ser escuchada
def hablar(mensaje):
    #encendemos el motor de pyttsx3
    engine = pyttsx3.init()
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
"""    
engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)
"""
#Opciones de voz disponibles



#Función para que yulexa informe el día de la semana
def solicitar_dia():
    #creamos una variable que contenga el día
    dia = datetime.date.today()
    print(dia)
    
    #creamos una variable para almacenar el dia de hoy
    dia_semana = dia.weekday()
    print(dia_semana)
    
    #vamos a crear un diccionario para definir correctamente los días 
    semana = {0:"Lunes", 1:"Martes", 2:"Miércoles",
              3:"Jueves",4:"Viernes",5:"Sábado",6:"Domingo"}
    

    hablar(f'Hola. Hoy es {semana[dia_semana]}')


def solicitar_hora():
    #creamos una variable que contenga la hora
    hora = datetime.datetime.now()
    hora = f'dejame contarte que son exactamente las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    
    hablar(hora)


def saludo_yulexa():
    
    #hora
    hora = datetime.datetime.now()
    if hora.hour <6 or hora.hour > 20:
        saludo = "Buenas Noches"
    elif hora.hour >= 6 or hora.hour <13:
        saludo = "Buenos días"
    else:
        saludo = "Buenas Tardes"
    #saludamos
    hablar('Hola. Esta es una iniciativa de los estudiantes del programa de ingenería informática de la universidad pontifícia de salamanca')
    hablar(' a continuación realizaremos un test diagnóstico de inteligencia emocional')
    





    
def preguntas_iniciales():
    
    hablar('Espera 5 segundos y dime ¿cúal es tu nombre?')
    global nombre
    nombre = trasformar_audio_en_texto().lower()
    print(nombre)
    hablar('hola '+nombre)
    hablar(nombre + ' a continuación realizaré unas preguntas y despues haremos el test diagnóstico')
    hablar("¿cuantos años tienes?")
    global edad
    edad = trasformar_audio_en_texto().lower()
    hablar("Perfecto. A continuación daremos inicio al test... voy a hacerte una serie de preguntas")
    hablar("primero. Responde si o no...	¿Te sientes incómodo en tu entorno de trabajo?")
    global p1
    p1= trasformar_audio_en_texto().lower()
    if p1 == "si":
        p1 = 1
    else:
        p1 = 0
    hablar("segunda pregunta. Responde si o no ... ¿Te sientes tenso o alterado la mayor parte del tiempo?")
    global p2
    p2= trasformar_audio_en_texto().lower()
    if p2 == "si":
        p2 = 1
    else:
        p2 = 0
    hablar("¿Tienes dificultad para concentrarte?")
    global p3
    p3= trasformar_audio_en_texto().lower()
    if p3 == "si":
        p3 = 1
    else:
        p3 = 0
    global p4
    hablar("¿Te rondan pensamientos negativos?")
    p4= trasformar_audio_en_texto().lower()
    if p4 == "si":
        p4 = 1
    else:
        p4 = 0
    
    global respuestas
    respuestas = [p1,p2,p3,p4]
    print(respuestas)
    
    if respuestas[0] == 0 and respuestas[1] ==0  and respuestas[2] and respuestas[3] == 0:
        hablar("Te propongo realizar el siguiente ejercicio de yoga")
        webbrowser.open("https://www.youtube.com/watch?v=i4dwATyTcCk&ab_channel=AnabelOtero")
        
    if respuestas[0] == 0 and respuestas[1] ==0  and respuestas[2] and respuestas[3] == 1:
        hablar("Te propongo realizar el siguiente ejercicio de respiración 4x4")
        webbrowser.open("https://www.youtube.com/watch?v=DmJvQEjyQFs")
        
    
    if respuestas[0] == 0 and respuestas[1] ==1 and respuestas[2] and respuestas[3] == 0:
        hablar("Te propongo escuchar el siguiente video")
        webbrowser.open("https://www.youtube.com/watch?v=zRvsRjqi5yE")
        
    if respuestas[0] == 0 and respuestas[1] ==1  and respuestas[2] and respuestas[3] == 1:
        hablar("Te propongo escuhar el siguiente vídeo")
        webbrowser.open("")
        
    if respuestas[0] == 1 and respuestas[1] ==0  and respuestas[2] and respuestas[3] == 0:
        hablar("Te propongo realizar el siguiente ejercicio de respiración 4x4")
        webbrowser.open("https://www.youtube.com/watch?v=DmJvQEjyQFs")
        
    if respuestas[0] == 1 and respuestas[1] ==0  and respuestas[2] and respuestas[3] == 1:
        hablar("Te propongo realizar el siguiente ejercicio de respiración 4x4")
        webbrowser.open("https://www.youtube.com/watch?v=DmJvQEjyQFs")
        
    if respuestas[0] == 1 and respuestas[1] ==1  and respuestas[2] and respuestas[3] == 0:
        hablar("Te propongo realizar el siguiente ejercicio de respiración 4x4")
        webbrowser.open("https://www.youtube.com/watch?v=DmJvQEjyQFs")
            
    if respuestas[0] == 1 and respuestas[1] ==1  and respuestas[2] and respuestas[3] == 1:
        hablar("Te propongo realizar el siguiente ejercicio de respiración 4x4")
        webbrowser.open("https://www.youtube.com/watch?v=DmJvQEjyQFs")
        
        
        
    



def preguntas_ansiedad():
    hablar("probando probando... esta es la sección de preguntas de ansiedad")
    
    
def centro_solicitudes():
    
    # 1. Activamos el saludo de yulexa
    saludo_yulexa()
    
    #2 preguntas iniciales
    preguntas_iniciales()
    
    # 2. creamos una variable que inicie el loop
    comenzar = True
    
    # 3. creamos el loop central de la función
    
    while comenzar:
        #Activamos el microfono y guardamos la solicitud en un string
        #con la función lower lo paso a miniscula para evitar problemas
        solicitud = trasformar_audio_en_texto().lower()
                    
        
        if 'abrir youtube' in solicitud:
            hablar(" claro que si. ya mismo abrimos youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir navegador'in solicitud:
            hablar("Hablas muy rarito. Pero creo que entendí lo que quieres")
            webbrowser.open("https://www.google.com")
            continue
        elif 'qué día es hoy' in solicitud:
            solicitar_dia()
            continue
        elif 'qué hora es' in solicitud:
            solicitar_hora()
            continue
        elif 'busca en wikipedia' in solicitud:
            hablar('Buscando eso en wikipedia')
            #dejamos la solicitud vacia
            #llamamos al objeto wikipedia de la libreria wikipedia
            solicitud = solicitud.replace('busca en wikipedia', "")
            #setlang me permite establecer el lenguaje de busqueda de wikipedia
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(solicitud, sentences=4)
            hablar('La profe Yuli ¡odia wikipedia pero, deja te cuento que:')
            hablar(resultado)
            continue
        elif 'busca en internet' in solicitud:
            hablar('Ya mismo estoy en eso')
            solicitud = solicitud.replace('busca en internet', '')
            pywhatkit.search(solicitud)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in solicitud:
            hablar('Amo escuchar música.. tienes buen gusto, y dice!')
            pywhatkit.playonyt(solicitud)
            continue
       
        elif 'luis' in solicitud:
            hablar("luis no viene a clase.. ¿quieres que le avise?")
        elif 'bucaramanga' in solicitud:
            hablar("La ciudad mas linda de colombia. Tambien venden las hamburguesas mas delis")
        elif 'adios' in solicitud:
            hablar("chauuu, cualquier cosa me avisas")
            break
            
centro_solicitudes()
        
    







