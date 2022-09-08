def userEntity(usuario) -> dict:
    return {
        "UserId": usuario["id"],
        "FirstName": usuario["FirstName"],
        "LastName": usuario["LastName"],
        "Email": usuario["Email"],
        "YearsPreviousExperience": usuario["YearsPreviousExperience"],
        "skills":usuario["skills"]
    }

def usersEntity(usuarios) -> list:
    [userEntity(usuario) for usuario in usuarios]