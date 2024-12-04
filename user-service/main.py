from fastapi import FastAPI
import boto3

app = FastAPI()

# Configurer le client S3 pour LocalStack
s3_client = boto3.client(
    "s3",
    endpoint_url="http://localstack:4566",
    aws_access_key_id="fakeAccessKey",
    aws_secret_access_key="fakeSecretKey",
    region_name="us-east-1",
)

BUCKET_NAME = "user-service-bucket"

@app.on_event("startup")
async def startup_event():
    try:
        # Crée un bucket au démarrage
        s3_client.create_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' créé avec succès")
    except Exception as e:
        print(f"Erreur lors de la création du bucket : {e}")


# Route pour obtenir un utilisateur par ID
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"message": f"My name is Ossama, and my ID is {user_id}"}
