import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Custom CSS for bubble chat styling
st.markdown("""
<style>
/* User message - right side */
.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) {
    flex-direction: row-reverse;
    background: transparent !important;
}

.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 14px 18px 20px 18px;
    border-radius: 18px 18px 4px 18px;
    margin-left: auto;
    margin-right: 8px;
}

/* Assistant message - left side */
.stChatMessage:has([data-testid="stChatMessageAvatarAssistant"]) {
    background: transparent !important;
}

.stChatMessage:has([data-testid="stChatMessageAvatarAssistant"]) .stMarkdown {
    background: #374151;
    padding: 14px 18px 20px 18px;
    border-radius: 18px 18px 18px 4px;
    margin-left: 8px;
}

/* Ensure text is visible */
.stChatMessage p, .stChatMessage span {
    color: white !important;
}

/* Add spacing between messages */
.stChatMessage {
    margin-bottom: 12px;
}

/* Style the chat input */
[data-testid="stChatInput"] textarea {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

def get_ai_response(messages_payload, model):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        st.error("API Key tidak ditemukan. Pastikan OPENROUTER_API_KEY ada di file .env")
        return None
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        data=json.dumps({
            "model": model,
            "messages": messages_payload,
            "max_tokens": 1000,
            "temperature": 0.7,
        })
    )
    if response.status_code != 200:
        st.error("Error: " + response.text)
        return None
    answer = response.json()["choices"][0]["message"]["content"]
    return answer

st.title("🤖 Chatbot seperti ChatGPT")

model_options = {
    "Mistral 7B (Free)": "mistralai/mistral-7b-instruct:free",
    "DeepSeek V3 (Free)": "deepseek/deepseek-chat-v3-0324:free",
    "Llama 3.1 8B (Free)": "meta-llama/llama-3.1-8b-instruct:free"
}

#Model Selector
selected_model_name = st.selectbox(
    "Pilih Model",
    options=list(model_options.keys()),
    index=0,
)
selected_model = model_options[selected_model_name]


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Tulis pesan..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI Response (outside user message block)
    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            messages_for_api = st.session_state.messages.copy()
            ai_response = get_ai_response(messages_for_api, selected_model)
            if ai_response:
                st.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                st.error("Error: Gagal mendapatkan respons dari AI")
