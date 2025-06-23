from supabase import create_client, Client

url = "https://zwbyjsdlpdwubkbriwea.supabase.co"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3Ynlqc2RscGR3dWJrYnJpd2VhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA0NzIxMDEsImV4cCI6MjA2NjA0ODEwMX0.aLytDhKgdbDO60M8_xCtZVxUjCQJ1CQB_LAdqklib4c"

db_client: Client = create_client(url, api_key)

def get_db_client() -> Client:
    return db_client