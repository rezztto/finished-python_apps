import typer
from rich import print
from rich.table import Table

def __helptable():
  help_table = Table('COMANDO', 'DESCRIPCION')
  help_table.add_row('acortador', "Acortar URL's\n")
  help_table.add_row('diccionario', 'Definicion de una palabra\n')
  help_table.add_row('disk', 'Informacion de los discos de tu pc\n')
  help_table.add_row('net-conf', 'Informacion de la red del equipo\n')
  help_table.add_row('net-ping', 'Prueba de conectividad\n')
  help_table.add_row('traductor', 'Traductor de textos\n')
  help_table.add_row('help', 'Tabla de ayuda, esta misma\n')
  help_table.add_row('exit', 'Salir de la aplicacion')

  print(help_table)