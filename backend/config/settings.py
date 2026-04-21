# FastAPI Configuration

## Database Configuration
DATABASE_URL = "sqlite:///./sql_app.db"

## Storage Configuration
STORAGE_PATH = "./storage"

## JWT Configuration
JWT_SECRET_KEY = "mysecretkey"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

## Logging Configuration
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("my_fastapi_app")
logger.info("FastAPI app is starting...")
