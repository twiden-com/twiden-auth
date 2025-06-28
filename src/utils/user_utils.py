

def generate_user_org_email(user_email: str, org_id: str):
    return f"{user_email.split('@')[0]}+{org_id}@{user_email.split('@')[1]}"