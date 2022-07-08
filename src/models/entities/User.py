import email


from werkzeug.security import check_password_hash #codifica el password

class User():

    def __init__(self, id,email,password,fullname='')-> None:
        self.id = id
        self.email = email
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)