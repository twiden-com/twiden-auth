

class Settings:
    host = ""
    is_development = True
    port = 8080
    log_level = 'DEBUG'
    is_production = False
    environment='test'

def get_settings():
    return Settings()