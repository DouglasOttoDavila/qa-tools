import os
from dotenv import load_dotenv
from infisical_sdk import InfisicalSDKClient

load_dotenv()

client = InfisicalSDKClient(host=os.getenv("INFISICAL_APP_BASE_URL"))

client.auth.universal_auth.login(
    client_id=os.getenv("INFISICAL_CLIENT_ID"), 
    client_secret=os.getenv("INFISICAL_CLIENT_SECRET")
)

secrets = client.secrets.list_secrets(project_id=os.getenv("INFISICAL_PROJECT_ID"), environment_slug="dev", secret_path="/")

def get_infisical_secret(folder_path:str, secret_name:str, environment:str):
    secret = client.secrets.get_secret_by_name(
        secret_name=secret_name,
        project_id=os.getenv("INFISICAL_PROJECT_ID"),
        environment_slug=environment,
        secret_path=folder_path,
        expand_secret_references=True,
        include_imports=True,
        version=None  # Optional
    )
    return secret.secretValue

