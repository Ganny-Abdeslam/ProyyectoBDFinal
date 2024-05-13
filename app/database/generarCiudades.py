import pycountry
from database.conexion import conexionBD

class Countries:
    def __init__(self):
        pass

    def insert_countries(self):
        conexion = conexionBD().conectar()
        cursor = conexion.cursor()

        country_names = [country.name for country in pycountry.countries]

        for id_country, country_name in enumerate(country_names, start=1):
            query = "INSERT INTO pais (id_pais, nombre) VALUES (%s, %s)"
            data = (id_country, country_name)
            cursor.execute(query, data)

        conexion.commit()
        conexion.close()

    def count_countries(self):
        conexion = conexionBD().conectar()
        cursor = conexion.cursor()

        query = "SELECT COUNT(*) FROM pais"
        cursor.execute(query)

        country_count = cursor.fetchone()[0]

        conexion.close()

        return country_count

class Departamentos:
    def __init__(self):
        pass

    def insert_states(self):
        conexion = conexionBD().conectar()
        cursor = conexion.cursor()

        consulta = "SELECT id_pais FROM pais WHERE nombre = 'Colombia' "
        cursor.execute(consulta)

        id_country = cursor.fetchone()[0]
        us_states = [state.name for state in pycountry.subdivisions.get(country_code='CO')]

        for id_state, state_name in enumerate(us_states, start=1):
           query = "INSERT INTO departamento (id_departamento, nombre, id_pais) VALUES (%s, %s, %s)"
           data = (id_state, state_name, id_country)
           cursor.execute(query, data)

        conexion.commit()
        conexion.close()

class Ciudades:
    def __init__(self):
        pass

    def insert_ciudades(self):
        conexion = conexionBD().conectar()
        cursor = conexion.cursor()
        i = 0

        consulta = "SELECT id_departamento FROM departamento WHERE nombre = 'Valle del Cauca' "
        cursor.execute(consulta)
        id_departamento = cursor.fetchone()[0]

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Cali", id_departamento)
        cursor.execute(query, data)

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Toro", id_departamento)
        cursor.execute(query, data)

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Cartago", id_departamento)
        cursor.execute(query, data)

        consulta = "SELECT id_departamento FROM departamento WHERE nombre = 'Amazonas' "
        cursor.execute(consulta)
        id_departamento = cursor.fetchone()[0]

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Leticia", id_departamento)
        cursor.execute(query, data)

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Borba", id_departamento)
        cursor.execute(query, data)

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Anori", id_departamento)
        cursor.execute(query, data)

        consulta = "SELECT id_departamento FROM departamento WHERE nombre = 'Risaralda' "
        cursor.execute(consulta)
        id_departamento = cursor.fetchone()[0]

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Pereira", id_departamento)
        cursor.execute(query, data)

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Santa Rosa", id_departamento)
        cursor.execute(query, data)

        query = "INSERT INTO ciudad (id_ciudad, nombre, id_departamento) VALUES (%s, %s, %s)"
        i+=1
        data = (i, "Dosquebradas", id_departamento)
        cursor.execute(query, data)

        conexion.commit()
        conexion.close()