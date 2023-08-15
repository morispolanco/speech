import streamlit as st
import openai
import speech_recognition as sr

st.title('Transcriptor de Voz')

api_key = st.text_area('Ingresa tu API key de OpenAI')

if 'transcript' not in st.session_state:
  st.session_state['transcript'] = ''

st.write('Transcripción:')
st.write(st.session_state['transcript'])

if st.button('Grabar'):
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)
      
  openai.api_key = api_key
  
  transcript = openai.Audio.transcribe('whisper-1', audio.get_wav_data())['text']
  st.session_state['transcript'] += f"\n{transcript}"
  
if st.button('Limpiar'):
  st.session_state['transcript'] = ''
