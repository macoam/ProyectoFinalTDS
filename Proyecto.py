from tkinter import *
import pyaudio 
import numpy as np  
import wave 
from matplotlib import pyplot as plt 

ventana = Tk()
ventana.title("Afinador de guitarra")
ventana.geometry("300x700")

textcuerda = StringVar()
textcuerda.set("")

textfreqafinacion = StringVar()
textfreqafinacion.set("")

textfreq = StringVar()
textfreq.set("")

textafina = StringVar()
textafina.set("")
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100
SEGUNDOS_GRABACION = 1
CHUNK = 2048
window = np.blackman(CHUNK)


def Afinar():
    FrecuenciaActual = "Frecuencia actual"

    def analizar(stream):
        data = stream.read(CHUNK, exception_on_overflow=False)
        #"2048h"
        waveData = wave.struct.unpack("%dh"%(CHUNK), data)
        npData = np.array(waveData)

        dataEntrada = npData * window

        fftData = np.abs(np.fft.rfft(dataEntrada))

        indiceFrecuenciaDominante = fftData[1:].argmax() + 1

        y0,y1,y2 = np.log(fftData[indiceFrecuenciaDominante-1:indiceFrecuenciaDominante+2])
        x1 = (y2-y0) * 0.5 / (2 * y1 - y2 - y0)
        frecuenciaDominante = (indiceFrecuenciaDominante+x1) * FRECUENCIA_MUESTREO / CHUNK
        Frecuencia = str(frecuenciaDominante)
        print("Frecuencia Dominante: " + str(frecuenciaDominante) + " Hz", end='\r')
        textfreq.set(Frecuencia)

        aaaaaaaaaaaaafuncionaplz = 13.0
        Diferencia = 1.3
        
        if  frecuenciaDominante > 82.4 - aaaaaaaaaaaaafuncionaplz and frecuenciaDominante < 82.4 + aaaaaaaaaaaaafuncionaplz :
            cuerda = "6ta Mi(E) 82.4 Hz"
            if  frecuenciaDominante > 82.4 - Diferencia and frecuenciaDominante < 82.4 + Diferencia :
                Afinacion = "La afinación es correcta."
            elif  frecuenciaDominante < 82.4 + Diferencia :
                Afinacion = "Es necesario apretar la cuerda."
            else:
                Afinacion = "Es necesario aflojar la cuerda."
        elif  frecuenciaDominante > 110.0 - aaaaaaaaaaaaafuncionaplz and frecuenciaDominante < 110.0 + aaaaaaaaaaaaafuncionaplz :
            cuerda = "5ta La(A) 110.00 Hz"
            if  frecuenciaDominante > 110.0 - Diferencia and frecuenciaDominante < 110.0 + Diferencia :
                Afinacion = "La afinación es correcta."
            elif  frecuenciaDominante < 110.0 + Diferencia :
                Afinacion = "Es necesario apretar la cuerda."
            else:
                Afinacion = "Es necesario aflojar la cuerda."
        elif  frecuenciaDominante > 146.83 - aaaaaaaaaaaaafuncionaplz and frecuenciaDominante < 146.83 + aaaaaaaaaaaaafuncionaplz :
            cuerda = "4ta Re(D) 146.83 Hz"
            if  frecuenciaDominante > 146.83 - Diferencia and frecuenciaDominante < 146.83 + Diferencia :
                Afinacion = "La afinación es correcta."
            elif  frecuenciaDominante < 146.83 + Diferencia :
                Afinacion = "Es necesario apretar la cuerda."
            else:
                Afinacion = "Es necesario aflojar la cuerda."
        elif  frecuenciaDominante > 196.0 - aaaaaaaaaaaaafuncionaplz and frecuenciaDominante < 196.0 + aaaaaaaaaaaaafuncionaplz :
            cuerda = "3ra Sol(G) 196.0 Hz"
            if  frecuenciaDominante > 196.0 - Diferencia and frecuenciaDominante < 196.0 + Diferencia :
                Afinacion = "La afinación es correcta."
            elif  frecuenciaDominante < 196.0 + Diferencia :
                Afinacion = "Es necesario apretar la cuerda."
            else:
                Afinacion = "Es necesario aflojar la cuerda."
        elif  frecuenciaDominante > 246.94 - aaaaaaaaaaaaafuncionaplz and frecuenciaDominante < 246.94 + aaaaaaaaaaaaafuncionaplz :
            cuerda = "2da Si(B) 246.94 Hz"
            if  frecuenciaDominante > 246.94 - Diferencia and frecuenciaDominante < 246.94 + Diferencia :
                Afinacion = "La afinación es correcta."
            elif  frecuenciaDominante < 246.94 + Diferencia :
                Afinacion = "Es necesario apretar la cuerda."
            else:
                Afinacion = "Es necesario aflojar la cuerda."
        elif  frecuenciaDominante > 329.63 - aaaaaaaaaaaaafuncionaplz and frecuenciaDominante < 329.63 + aaaaaaaaaaaaafuncionaplz :
            cuerda = "1ra Mi(E2) 329.63 Hz"
            if  frecuenciaDominante > 329.63- Diferencia and frecuenciaDominante < 329.63 + Diferencia :
                Afinacion = "La afinación es correcta."
            elif  frecuenciaDominante < 329.63 + Diferencia :
                Afinacion = "Es necesario apretar la cuerda."
            else:
                Afinacion = "Es necesario aflojar la cuerda."
        else:
            cuerda = "La cuerda no se identificó, presione 'Afinar' Otra vez."
            Afinacion = ""

        textcuerda.set(cuerda)
        textfreqafinacion.set(FrecuenciaActual)
        textafina.set(Afinacion)

    if __name__ == "__main__":
        p = pyaudio.PyAudio()
        stream = p.open(format=PROFUNDIDAD_BITS, channels=CANALES, rate=FRECUENCIA_MUESTREO, input=True, frames_per_buffer=CHUNK)
        
        for i in range(0, int(FRECUENCIA_MUESTREO * SEGUNDOS_GRABACION / CHUNK)):
            analizar(stream)
        
        stream.stop_stream()
        stream.close()
        p.terminate()

etiquetanota = Label(ventana, textvariable = textcuerda)
etiquetanota.pack()

etiquetafreqafinacion = Label(ventana, textvariable = textfreqafinacion)
etiquetafreqafinacion.pack()

etiquetafreq = Label(ventana, textvariable = textfreq)
etiquetafreq.pack()

etiquetaafina = Label(ventana, textvariable = textafina)
etiquetaafina.pack()

Afinar = Button(ventana, text="Afinar", command = Afinar)
Afinar.pack()

ventana.mainloop()