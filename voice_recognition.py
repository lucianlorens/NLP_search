import streamlit as st
import sounddevice as sd
import numpy as np
import voice_recognition as sr

### -----------------------------------------
#TODO: implement feature of capturing audio
def capture_audio(duration=5, sample_rate=16000):
    st.write("🎙️ Gravando áudio...")
    ###
    audio_data = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate, channels=1,
        dtype='int16'
    )
    
    ###
    sd.wait()  # Espera a gravação terminar
    st.write("✅ Gravação finalizada!")
    
    return np.squeeze(audio_data)  # Remove a dimensão extra

def recognize_speech_from_audio(audio_data, sample_rate=16000):
    recognizer = sr.Recognizer()
    
    # Converte o numpy array para o formato AudioData do SpeechRecognition
    audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)
    
    try:
        st.write("📝 Reconhecendo fala...")
        text = recognizer.recognize_google(audio, language="pt-BR")  # Reconhece em português
        st.success(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        st.error("❌ Não entendi o que você disse. Tente novamente.")
    except sr.RequestError as e:
        st.error(f"❌ Erro com o serviço de reconhecimento: {e}")
        return ""

def get_speech_input():
    audio_data = capture_audio(duration=5, sample_rate=16000)  # Captura 5 segundos de áudio
    return recognize_speech_from_audio(audio_data)
    
