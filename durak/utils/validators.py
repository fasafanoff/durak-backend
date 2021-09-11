def is_password_valid(password):
    return True


def is_login_valid(login):
    if not 4 < len(login) < 25:
        return False

    if not str.isalnum(login):
        return False

    str.isal
