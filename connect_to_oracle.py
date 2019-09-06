import cx_Oracle
from sqlalchemy import create_engine
import base64
  
class OraEngine:
  
    """
    Oracle engine in sqlalchemy and cx_Oracle
    """
      
      
    def __init__(self):
        self.dbhost='somehost.com'
        self.dbport='1521'
        self.dbuser='someusername'
        self.dbpass=b'yourBase64encodedPassword'
        self.dbsid='DBSID'
        self.password=base64.b64decode(self.dbpass)
        self.dsnStr = cx_Oracle.makedsn(self.dbhost, self.dbport, self.dbsid)  
        self.cstr = 'oracle+cx_oracle://{user}:{password}@{sid}'.format(
                user=self.dbuser,
                password=self.password,
                sid=self.dsnStr
        )
    def engine(self):
        return create_engine(
                self.cstr,
                encoding = 'utf-8',
                convert_unicode=False,
                pool_recycle=10,
                pool_size=50,
                echo=True
            )
    def cx_cursor(self):
        self.dsnStr = cx_Oracle.makedsn(self.dbhost, self.dbport, self.dbsid)
        self.connection = cx_Oracle.connect(user=self.user, password=self.password, dsn = self.dsnStr)
        return self.connection.cursor()
