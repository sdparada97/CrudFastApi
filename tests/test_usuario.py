from fastapi.testclient import TestClient

from routes.usuario import app

client = TestClient(app)

#Se requiere crear un usuario y que devuelva un STATUS 200

#Se requiere obtener un usuario y que devuelva un STATUS 200

#Se requiere obtener todos los usuarios y que devuelva un STATUS 200

#Se requiere actualizar un usuario y que devuelva un STATUS 200

#Se requiere eliminar un usuario y que devuelva un STATUS 204
