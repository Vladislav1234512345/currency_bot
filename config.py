from pydantic_settings import BaseSettings, SettingsConfigDict
from currency_converter import CurrencyConverter
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )
    bot_token: str

class Sum:
    number: float = 0

settings = Settings()

sum = Sum()

currency = CurrencyConverter()