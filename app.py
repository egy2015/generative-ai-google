import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Konfigurasi API (Ganti 'API_KEY_KAMU' dengan key asli)
genai.configure(api_key=os.getenv("API_KEY"))

# 2. Inisialisasi Model
model = genai.GenerativeModel(os.getenv("MODEL"))
chat = model.start_chat(history=[])

print("--- AI Chatbot Terminal (Ketik 'keluar' untuk berhenti) ---")

while True:
    user_input = input("Kamu: ")
    
    if user_input.lower() in ['keluar', 'exit', 'quit']:
        print("AI: Dadah!")
        break

    try:
        # 3. Kirim pesan ke AI
        response = chat.send_message(user_input)
        print(f"AI: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}")