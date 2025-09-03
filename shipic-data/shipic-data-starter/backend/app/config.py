from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # App
    app_name: str = Field("ShipPic Data API", alias="APP_NAME")
    debug: bool = Field(True, alias="DEBUG")
    mock_mode: bool = Field(False, alias="MOCK_MODE")

    # DB
    database_url: str = Field("sqlite:///./shipic.db", alias="DATABASE_URL")

    # Shopify
    shopify_store_domain: str | None = Field(default=None, alias="SHOPIFY_STORE_DOMAIN")
    shopify_admin_api_access_token: str | None = Field(default=None, alias="SHOPIFY_ADMIN_API_ACCESS_TOKEN")

    # Printful
    printful_api_key: str | None = Field(default=None, alias="PRINTFUL_API_KEY")

    # Google Trends
    google_trends_geo: str = Field("US", alias="GOOGLE_TRENDS_GEO")
    google_trends_timeframe: str = Field("now 7-d", alias="GOOGLE_TRENDS_TIMEFRAME")

    # TikTok (optional)
    tiktok_api_key: str | None = Field(default=None, alias="TIKTOK_API_KEY")
    tiktok_api_base: str | None = Field(default=None, alias="TIKTOK_API_BASE")

    # Keepa (optional)
    keepa_api_key: str | None = Field(default=None, alias="KEEPA_API_KEY")

    # Etsy (optional)
    etsy_api_key: str | None = Field(default=None, alias="ETSY_API_KEY")
    etsy_api_base: str | None = Field(default=None, alias="ETSY_API_BASE")

    # Search (optional)
    serpapi_key: str | None = Field(default=None, alias="SERPAPI_KEY")
    dataforseo_login: str | None = Field(default=None, alias="DATAFORSEO_LOGIN")
    dataforseo_password: str | None = Field(default=None, alias="DATAFORSEO_PASSWORD")

    # pydantic-settings v2 config
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

settings = Settings()
