import os
import requests
from dotenv import load_dotenv
from google.cloud import storage  # Importa la biblioteca de Google Cloud Storage

# Load environment
load_dotenv()
token = os.getenv("BEARER_TOKEN")
bucket_name = os.getenv("GCS_BUCKET_NAME")
url = "https://alpha-api.mychef-cloud.com/context"

headers = {"Authorization": f"Bearer {token}"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    filename = "CONTEXTS.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for item in data:
            question = item.get("question", "Any question available")
            answer = item.get("answer", "Any answer available")

            file.write(f"[PREGUNTA]: {question}\n")
            file.write(f"[RESPUESTA]: {answer}\n")
            file.write("---\n")

    print("File CONTEXTS.txt created successfully.")

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("CONTEXTS/CONTEXTS.txt")

    blob.upload_from_filename(filename)
    print(f"File {filename} uploaded to {bucket_name}.")

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("\nContenido del archivo CONTEXTS.txt:\n")
        print(content)

    os.remove(filename)
    print(f"File {filename} deleted successfully.")

except requests.exceptions.RequestException as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
