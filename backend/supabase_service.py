from supabase import create_client

SUPABASE_URL = "https://tkymjsnegtztyjwlrtiw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRreW1qc25lZ3R6dHlqd2xydGl3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MDgxOTA4NywiZXhwIjoyMDg2Mzk1MDg3fQ.ycHWj4C107KvDhxSB9tKgQIOVqNkf4pK0rqiIgqT6vA"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def log_import(file_name, created_count, updated_count, status):
    data = {
        "file_name": file_name,
        "created_count": created_count,
        "updated_count": updated_count,
        "status": status
    }
    print("Logging to Supabase:", data)  
    response = supabase.table("imports").insert(data).execute()
    print("Supabase response:", response)  
    return response
