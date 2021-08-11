##### Installed packages
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData

##### Local
from databases import db

##### Tables names 
tables = {}
tables_name = ['alumnos','cursos', 'curso_alumno_cdp', 'constancias']#,'Aspirantes', 'Confirmaciones', 'Equipos' ]

##### DB config
Base = automap_base()
Base.prepare(db.engine, reflect=True)

for table_name in tables_name:
    #tables[column] = db.Table(column, db.metadata, autoload = True, autoload_with = db.engine)
    
    tables[table_name] = dict(Base.classes)[table_name]
