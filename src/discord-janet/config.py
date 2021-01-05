def read_auth_key():
    file = open('auth.key')
    auth_key = file.readline()
    file.close()
    return auth_key