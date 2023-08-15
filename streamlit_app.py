import streamlit as st
import sounddevice as sd
import soundfile as sf
from whisper import Whisper

def record_audio(filename, duration):
    # Configurar la grabación de audio
    sample_rate = 16000
    channels = 1

    # Grabar audio
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()

    # Guardar el archivo de audio
    sf.write(filename, audio, sample_rate)

def transcribe_audio(filename):
    # Cargar el modelo de Whisper
    whisper = Whisper()

    # Transcribir el audio
    transcription = whisper.transcribe(filename)

    return transcription

def main():
    st.title("Aplicación de Transcripción de Voz")

    # Configurar la duración de la grabación
    duration = st.slider("Duración de la grabación (segundos)", 1, 10, 3)

    # Botón para iniciar la grabación
    if st.button("Iniciar Grabación"):
        st.info("Grabando...")

        # Nombre del archivo de audio
        filename = "audio.wav"

        # Grabar audio
        record_audio(filename, duration)

        st.success("Grabación finalizada")

        # Transcribir el audio
        transcription = transcribe_audio(filename)

        # Mostrar la transcripción
        st.subheader("Transcripción:")
        st.write(transcription)

if __name__ == "__main__":
    main()
