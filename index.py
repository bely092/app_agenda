# Admin de la Agenda

from visual import Carteles
from agendabase import BaseApp
import sys


class Main:
    """
    Clase que se encarga de administrar ...
    Menu --> visual
    CRUD --> agendabase
    """
    def __init__(self):
        """
        --------------- * ---------------
        Lanza las Opciones del 0 al 4 
      
        - 0 Salida agenda
        - 1 muestra la agenda
        - 2 ingreso de datos
        - 3 elimina datos
        - 4 edita datos
        """
        self.banner = Carteles()
        self.base = BaseApp()
        self.banner.cartel_agenda()
        self.banner.menu_agenda()

        self.select = True
        while self.select:

            self.opn = input(">  ")
            if self.opn == "0":
                self.banner.sal_agenda()
                sys.exit()

            if self.opn == "1":
                self.base.cre_tabla()
                self.base.most_agenda()
                self.select = True

            if self.opn == "2":
                self.base.cre_tabla()
                self.base.ent_dat()
                self.select = True

            if self.opn == "3":
                self.base.cre_tabla()               
                self.base.bor_dat()
                self.select = True

            if self.opn == "4":
                self.base.cre_tabla()
                self.base.modifier_dat()
                self.select = True

        else:
            print("Ingrese una Opcion")
            self.select = True


if __name__ == "__main__":
    principal = Main()
