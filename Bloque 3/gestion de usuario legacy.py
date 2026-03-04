import hashlib

def process(username, password, role, database):
    # 1. Generar el hash una sola vez
    hashed_pw = hashlib.md5(password.encode()).hexdigest()
    
    # 2. Mapeo de roles a niveles y mensajes para evitar muchos 'if/else'
    role_config = {
        'admin': {'lvl': 3, 'msg': 'Admin OK'},
        'user':  {'lvl': 1, 'msg': 'User OK'}
    }

    # 3. Buscar coincidencia en la base de datos
    for db_user, db_hash in database:
        if db_user == username and db_hash == hashed_pw:
            # Obtener datos del rol o valores por defecto para 'guest'
            config = role_config.get(role, {'lvl': 0, 'msg': 'Guest OK'})
            return {'ok': True, **config}

    # 4. Caso de error (si no encuentra al usuario)
    return {'ok': False, 'msg': 'Credenciales inválidas'}