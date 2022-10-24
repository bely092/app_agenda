# Diseño de la Agenda

class Carteles:
    """
    Clase que contiene la Parte Visual Del Programa...
    """
    @staticmethod
    def cartel_agenda():
        """
        ---------------------  *  ---------------------
        Cartel de Inicio
        """       
        print("  ")
        print("------------------------------")
        print("|          AGENDA            |")
        print("------------------------------")
        print("  ")

    @staticmethod
    def menu_agenda():
        """
        ---------------------  *  ---------------------
        Muestra una lista con diferentes acciones a
        realizar en la base de datos
        """
        print("   ")
        print(" ____________________________")
        print("|    ** Menu de Agenda **    |")
        print(" ---------------------------- ")
        print("|  1 - Mostrar Agenda        |")
        print("|  2 - Agregar un contacto   |")
        print("|  3 - Borrar un contacto    |")
        print("|  4 - Modificar un contacto |")
        print("|  0 - Salir                 |")
        print("  ----------------------------")
        print("   ")
        print("* Para modificar o Borrar un contacto use el Nº ID")
        print("* Para conocerlo, use la opcion > 1")
        print("  ")

    @staticmethod
    def sal_agenda():
        """
        ---------------------  *  ---------------------
        Cartel Salida del Programa
        """
        print("  ")
        print(" ___________________________")
        print("|* AGENDA x Riquelme Belen *|")
        print(" ---------------------------")
        print("  ")
