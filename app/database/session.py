from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ("firebird+fdb://sysdba:masterkey@localhost:3050/C:/DB/TICKET.FDB?charset=UTF8&fb_library_name=C:/DB"
                "/fbclient.dll")

engine = create_engine(DATABASE_URL, echo=True)

try:
    with engine.begin():
        pass
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
