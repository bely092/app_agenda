# Base de la Agenda

import sqlite3
import re
from sqlite3 import Error


class BaseApp:
    """
    Clase administradora de la Base... 
    """
    def __init__(self):
        """
         CRUD de la app 
        """
    @staticmethod
    def cre_tabla():
        """
        ---------------------  *  ---------------------
        Funcion encargada de verificar y crear
        una tabla en la base de datos si no existe,
        De no lograrse cargar retornara --> Error
        """
        try:
            m_con = sqlite3.connect('base_agenda')
            m_cursor = m_con.cursor()

            m_cursor.execute(
                "CREATE TABLE IF NOT EXISTS TABLA (ID INTEGER PRIMARY KEY AUTOINCREMENT, usuario text, mail text)")

            m_con.commit()
            m_con.close()
            print(" ** Iniciando ** ")
        except Error:
            print(Error)

    @staticmethod
    def ent_dat():
        """
        ---------------------  *  ---------------------
        Funcion encargada de verificar y subir los datos
        del usuario cargados correctamente
        En caso contrario se solicitara que vuelva a ingresar los datos
        o mostrara error
        """
        try:
            m_con = sqlite3.connect('base_agenda')
            m_cursor = m_con.cursor()

            name_user = input(" Ingrese nombre de Usuario  > ")

            mail_valid = True
            while mail_valid:

                mail_user = input(" Ingrese Mail  > ")
                val_dats = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

                if not (re.search(val_dats, mail_user)):
                    print(" * Error Mail Invalido * ")

                    mail_valid = True

                else:
                    m_cursor.execute("INSERT INTO TABLA (usuario, mail) VALUES ( ?, ?)", (name_user, mail_user))
                    m_con.commit()
                    m_con.close()
                    print("- Datos Cargados Corectamente -")
                    print("  ")

                    mail_valid = False
            else:
                pass

        except Error:
            print(Error)

    @staticmethod
    def most_agenda():
        """
        ---------------------  *  ---------------------
        Funcion encargada de Mostrar Los datos 
        cargados de los contactos en la base de datos
        retorna <error> en caso de no lograr conectarse
        """
        try:
            print(" - Contactos Almacenados - ")
            print("  ")
            m_con = sqlite3.connect('base_agenda')
            m_cursor = m_con.cursor()

            m_cursor.execute("SELECT * FROM TABLA")
            cols = m_cursor.fetchall()

            for col in cols:
                print(col)

            m_con.commit()
            m_con.close()
            print(" ------------------------- ")
            print("  ")

        except Error:
            print(Error)

    @staticmethod
    def bor_dat():
        """
        ---------------------  *  ---------------------
        Funcion encargada de eliminar el ID del
        contacto seleccionado       
        """
        try:
            m_con = sqlite3.connect('base_agenda')
            m_cursor = m_con.cursor()

            id_user = input(" Ingrese el ID del Contacto a eliminar  > ")

            m_cursor.execute("DELETE FROM TABLA WHERE ID = ?", id_user,)
            m_con.commit()
            m_con.close()

            print(" - Datos Borrados Correctamente - ")

        except Error:
            print(Error)

    @staticmethod
    def modifier_dat():
        """
        ---------------------  *  ---------------------
        Funcion encargada de modificar los datos del ID 
        seleccionado.
        verificara y cargara los datos
        o lanzara --> Error
        """
        try:
            m_con = sqlite3.connect('base_agenda')
            m_cursor = m_con.cursor()

            sel_id = input(" Ingrese el ID del contacto a Modificar > ")
            nuevo_user = input(" Usuario Nuevo > ")

            mail_valid = True
            while mail_valid:

                nuevo_mail = input(" Mail Nuevo > ")
                val_dats = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

                if not (re.search(val_dats, nuevo_mail)):
                    print(" * Error Mail Invalido * ")

                    mail_valid = True

                else:
                    m_cursor.execute(
                        "UPDATE TABLA SET usuario = ?, mail = ? WHERE ID = ?",
                        (nuevo_user, nuevo_mail, sel_id),
                    )
                    m_con.commit()
                    m_con.close()
                    print("  ")
                    print(" - Datos Actualizados - ")
                    print("  ")
                    mail_valid = False
            else:
                pass

        except Error:
            print(Error)
