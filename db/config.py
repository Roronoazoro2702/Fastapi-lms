from pydantic_settings import BaseSettings  # ConfigDict


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
   

    class Config:
        env_file = ".env"
    # model_config = ConfigDict(env_file=".env")


settings = Settings()