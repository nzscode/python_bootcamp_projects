def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    assert minlen > 0, "minlen must be at least 1"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

print(validate_user("rurjhgiofjo", 5))
