 c.execute(“””create table empleados (dni text, # type: ignore
             nombre text,
             departamento text)”””)
              c.execute(“””insert into empleados
             values (‘12345678-A’, ‘Manuel Gil’, ‘Contabili
dad’)”””)
import sqlite3 as dbapi
 bbdd = dbapi.connect(“bbdd.dat”)
 cursor = bbdd.cursor()
 cursor.execute(“””create table empleados (dni text,
                  nombre text,
                  departamento text)”””)
 cursor.execute(“””insert into empleados
                  values (‘12345678-A’, ‘Manuel Gil’, ‘Con
tabilidad’)”””)
 bbdd.commit()
 cursor.execute(“””select * from empleados
                  where departamento=’Contabilidad’”””)
 for tupla in cursor.fetchall():
    print tupla
    