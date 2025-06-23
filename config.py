import os;

SECRET_KEY = "Instituição Caramelo";

SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
      SGBD = "mysql+mysqlconnector", 
      usuario =  "root",
      senha =  "15Gns06xx2006*",
      servidor = "localhost",
      database =  "ong"       
    );
    
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads";