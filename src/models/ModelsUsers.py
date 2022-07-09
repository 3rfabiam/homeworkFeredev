from models.entities.User import User

@classmethod
class ModelUser():

    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql ="""SELECT id, email, password, fullname FROM users 
                    WHERE email= '{}'""".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2], user.password),row[3])
                return user
        except Exception as ex:
            raise Exception(ex)

@classmethod
class ModelUser():

    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql ="""SELECT id, email, fullname FROM users 
                    WHERE id= '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None,row[2])
                
        except Exception as ex:
            raise Exception(ex)