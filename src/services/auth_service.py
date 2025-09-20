from persistence.data_manager import load_users_data, save_users_data

def authenticate_user(user_id, pin):
    """Verifica el PIN del usuario y lo autentica si es correcto."""
    users = load_users_data()
    if str(user_id) in users and users[str(user_id)]["pin"] == pin:
        users[str(user_id)]["is_authenticated"] = True
        save_users_data(users)
        return True
    return False

def is_authenticated(user_id):
    """Verifica si el usuario ya está autenticado."""
    users = load_users_data()
    return users.get(str(user_id), {}).get("is_authenticated", False)