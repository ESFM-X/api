##### Installed packages
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData

##### Local
from databases import db

##### Tables names 
tables = {}
tables_name = ['Aspirantes', 'Confirmaciones', 'Equipos' ]

##### DB config
engine = db.get_engine(bind='hackathon')
database = MetaData(bind=engine)
Base = automap_base(metadata=database)
Base.prepare(reflect=True)

for table_name in tables_name:
    tables[table_name] = dict(Base.classes)[table_name]
