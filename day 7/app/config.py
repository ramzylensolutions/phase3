from pydantic_settings import BaseSettings,SettingsConfigDict
class DataBaseDetails(BaseSettings):
    db_host:str
    db_port:int
    db_user:str
    db_pwd :str
    db_name:str
    token_id :str
    model_config = SettingsConfigDict(
        env_file="details.env",
    )
settings = DataBaseDetails()