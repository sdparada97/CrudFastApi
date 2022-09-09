def userEntity(usuario) -> dict:
    return {
        "user_id": str(usuario["_id"]),
        "first_name": usuario["first_name"],
        "last_name": usuario["last_name"],
        "email": usuario["email"],
        "years_previous_experience": usuario["years_previous_experience"],
        "skills":usuario["skills"]
    }

def usersEntity(usuarios) -> list:
    return [userEntity(usuario) for usuario in usuarios]