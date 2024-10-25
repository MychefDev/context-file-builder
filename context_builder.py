import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BEARER_TOKEN")
url = "https://alpha-api.mychef-cloud.com/context"

headers = {
    "Authorization": f"Bearer {token}"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    data = response.json()       
    
    with open("COMMON_QUESTIONS.txt", "w", encoding="utf-8") as file:
        for item in data:
            question = item.get("question", "Pregunta no disponible")
            answer = item.get("answer", "Respuesta no disponible")
            
            file.write(f"[PREGUNTA]: {question}\n")
            file.write(f"[RESPUESTA]: {answer}\n")
            file.write("---\n")
    
    print("Archivo COMMON_QUESTIONS.txt creado con éxito.")

except requests.exceptions.RequestException as e:
    print("Ocurrió un error:", e)
