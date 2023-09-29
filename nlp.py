import streamlit as st
import requests
import tempfile

st.title("Audio summarizer")
st.write("using: whisper-tiny & pegasus_summarizer from Huggingface")

def query_whisper(filename, API_URL):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

def query_pegasus(payload,API_URL):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(uploaded_file.read())
        audio_file_path = temp_file.name

        headers = {"Authorization": "Bearer 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"}
        API_URL_whisper = "https://api-inference.huggingface.co/models/openai/whisper-tiny"
        output = query_whisper(audio_file_path,API_URL_whisper)

        text = output["text"]
        st.header("Text")
        st.write(text)
    st.divider()

    API_URL_pegasus = "https://api-inference.huggingface.co/models/tuner007/pegasus_summarizer"
    output = query_pegasus({"inputs": text,},API_URL_pegasus)
    st.header("Summarized Text")
    st.write(output)
