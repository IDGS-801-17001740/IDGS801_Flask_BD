from db import get_connection

def agregar_maestros(nombre,apaterno,amaterno,matricula):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call agregar_maestros(%s,%s,%s,%s)',(nombre,apaterno,amaterno,matricula))
        connection.commit()
        connection.close()    
    except Exception as ex:
        print(ex)

def modificar_maestros(nombre,apaterno,amaterno,id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call actualizar_maestros(%s,%s,%s,%s)',(nombre,apaterno,amaterno,id))
        connection.commit()
        connection.close()
    except Exception as ex:
        print(ex)

def eliminar_maestros(id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call eliminar_maestros(%s)',(id))
        connection.commit()
        connection.close()
    except Exception as ex:
        print(ex)
        
        
def getAllMaestros():
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call consultar_maestros()')
        resultado = curso.fetchall()
        for row in resultado:
            print(row)
        return row   
        connection.close()
    except Exception as ex:
        print(ex)
""" try:
    connection = get_connection()
    with connection.cursor() as curso:
        curso.execute('call insertar_alumnos(%s, %s, $s)')
        resultado = curso.fetchall()
        for row in resultado:
            print(row)
    connection.close()
except Exception as ex:
    print(ex) """
""" try:
    connection = get_connection()
    with connection.cursor() as curso:
        curso.execute('call consultar_alumno(%s)',(5))
        resultado = curso.fetchall()
        for row in resultado:
            nombre = row[1]
            print(nombre)
    connection.close()
except Exception as ex:
    print(ex) """
    
""" try:
    connection = get_connection()
    with connection.cursor() as curso:
        curso.execute('call consultar_alumnos()')
        resultado = curso.fetchall()
        for row in resultado:
            print(row)
    connection.close()
except Exception as ex:
    print(ex) """