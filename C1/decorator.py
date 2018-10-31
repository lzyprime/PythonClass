def check_usr(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("usrname", "") == "admin":
            return func(*args, **kwargs)
        return False
    return wrapper

@check_usr
def read(usrname = '', passwd = ''):
    return True

print(read())

print(read(usrname = 'admin'))

def write(usrname = '', passwd = ''):
    return True

write = check_usr(write)

print(write())

print(write(usrname = "admin"))