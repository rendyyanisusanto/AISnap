import streamlit as st
import google.generativeai as ai
st.title("AI Snap - Kelompok 1")
foto = st.camera_input("Ambil gambar")
if foto:
    
    ai.configure(api_key=st.secrets["token"])
    model = ai.GenerativeModel('gemini-2.0-flash')
    prompt = model.generate_content([
            "Jelaskan detail object yang dipegang oleh orang di gambar",
            {
                "data": foto.getvalue(),
                "mime_type": "image/jpeg"
            }
        ]
    )
    st.write(prompt.text)