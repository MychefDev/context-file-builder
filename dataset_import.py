import os
from google.cloud import storage
from google.cloud import aiplatform
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración del bucket y archivo en Google Cloud Storage
bucket_name = os.getenv("GCS_BUCKET_NAME")
blob_name = "CONTEXTS/CONTEXTS.txt"  # El nombre del archivo en GCS

# Inicializar el cliente de Google Cloud Storage
storage_client = storage.Client()

# Obtener el bucket y el archivo (blob) en Google Cloud Storage
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(blob_name)

# Verificar si el archivo existe en el bucket
if blob.exists():
    print(f"El archivo {blob_name} existe en el bucket {bucket_name}.")
else:
    print(f"El archivo {blob_name} no se encuentra en el bucket {bucket_name}.")
    exit(1)  # Salir si el archivo no existe

# Inicializar Vertex AI
aiplatform.init(project="mychef-chatbot", location="us-central1")  # Verifica que la ubicación sea correcta

# URI del archivo en Google Cloud Storage
gcs_file_uri = f"gs://{bucket_name}/{blob_name}"

# Crear un Dataset de Texto en Vertex AI
dataset_service_client = aiplatform.gapic.DatasetServiceClient()

# Crear el dataset (en este caso, un Dataset de texto)
dataset_create_request = aiplatform.gapic.CreateDatasetRequest(
    parent=f"projects/{os.getenv('PROJECT_ID')}/locations/us-central1",
    dataset=aiplatform.gapic.Dataset(
        display_name="Text Dataset from CONTEXTS.txt",
        metadata={
            "input_data_config": {
                "gcs_source": {
                    "input_uris": [gcs_file_uri]  # URI del archivo en GCS
                }
            }
        },
    ),
)

# Crear el dataset en Vertex AI
try:
    response = dataset_service_client.create_dataset(dataset_create_request)
    print(f"Dataset creado exitosamente: {response.name}")
except Exception as e:
    print(f"Ocurrió un error al crear el dataset: {e}")
