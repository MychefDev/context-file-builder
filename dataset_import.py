import os
from dotenv import load_dotenv
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

load_dotenv()

project_id = os.getenv("GCP_PROJECT_ID")
location = "global"
data_store_id = os.getenv("DATA_STORE_ID")
gcs_uri = os.getenv("GCS_URI")

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    gcs_source=discoveryengine.GcsSource(
        input_uris=[gcs_uri],
        data_schema="content",
    ),
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
print(request)
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
