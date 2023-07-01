#creator rezzt - plural aplication
#-------------------------------------------------------------------------

#importamos librerias
import os
import typer
from rich import print
from rich.table import Table
from sc import scripts, help

#creacion del modulo principal
#-------------------------------------------------------------------------
def main():
  help.__helptable()
  while True:
    content = __prompt()

    #opcion de seleccion
    if content == 'disk':
      scripts.__analyzer()

    elif content == 'diccionario':
      scripts.__dictionary()

    elif content == 'acortador':
      scripts.__shorturl()

    elif content == 'traductor':
      scripts.__translation()

    elif content == 'net-conf':
      scripts.__net_conf()

    elif content == 'net-ping':
      scripts.__conect_net('www.google.com')

    elif content == 'help':
      os.system('cls' if os.name == 'nt' else 'clear')
      help.__helptable()


def __prompt():
  prompt = typer.prompt('\n  + Escribe lo que quieres hacer')

  if prompt == 'exit':
    if exit:
      os.system('cls' if os.name == 'nt' else 'clear')
      raise typer.Abort()
    return __prompt()
  return prompt

#run en entorno seguro
#-------------------------------------------------------------------------
if __name__ == '__main__':
  typer.run(main)