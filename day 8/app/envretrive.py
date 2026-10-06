from  pydantic_settings import BaseSettings,SettingsConfigDict
class Details(BaseSettings):
    db_name : str
    db_passwrod: str
    db_user : str
    db_host : str
    db_port : int
    token_key : str
    model_config = SettingsConfigDict(
        env_file='details.env'
    )
settings = Details()