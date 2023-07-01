#scripts de los programas
#===================================================================================================================

#importamos las librerias
#===================================================================================================================
import pyshorteners
from rich import print
from rich.table import Table
from mtranslate import translate
import wikipedia
import psutil
import os
import socket
import ipaddress


#definimos las funciones de los scripts
#===================================================================================================================

#ACORTADOR DE URL
#-------------------------------------------------------------------------------------------------------
def __shorturl():
  url = input('Introduce la URL a acortar: ')
  s = pyshorteners.Shortener()
  short = s.tinyurl.short(url)

  print('\n[bold bright_blue]  + URL inicial > [/bold bright_blue]' + url)
  print('[bold bright_green]  + URL acortada > [/bold bright_green]' + short)


#TRADUCTOR DE TEXTOS
#-------------------------------------------------------------------------------------------------------
def __translation():
  language_table = Table("IDIOMA", "ACORTACION", "IDIOMA", "ACORTACION")
  language_table.add_row("Arabe", "ar", "Chino Simplifaco", "zs")
  language_table.add_row("Holandes", "cs", "Ingles EE.UU.", "en")
  language_table.add_row("Ingles UE", "ue", "Finlandes", "fi")
  language_table.add_row("French", "fr", "Danes", "da")
  language_table.add_row("Aleman", "de", "Italiano", "it")
  language_table.add_row("Japones", "ja", "Coreano", "ko")
  language_table.add_row("Noruego", "no", "Polaco", "pl")
  language_table.add_row("Portugues", "pb", "Ruso", "ru")
  language_table.add_row("Español", "es", "Sueco", "sv")
  language_table.add_row("Tailandes", "th", "Vietnamita", "vi")

  print(language_table)

  text = input("\n - Introduce el texto a traducir > ")
  lang_input = input(" - Introduce el idioma inicial > ")
  lang_output = input(" - Introduce el idioma a traducir > ")
  translator = translate(text, from_language=lang_input, to_language=lang_output)

  print("\n[bold bright_yellow]  + El texto inicial es: [/bold bright_yellow]\n     " + text)
  print("[bold bright_blue]  + El texto traducido es: [/bold bright_blue]\n     " + translator)


#DICCIONARIO CON WIKIPEDIA
#-------------------------------------------------------------------------------------------------------
def __dictionary():
  try:
    consult = input("\n Introduce la palabra a buscar: ")
    wikipedia.set_lang("es")

    result = wikipedia.summary(consult, sentences=1)
    print('[bold bright_red]' + consult + ':[/bold bright_red] \n', result)

  except:
    print('[bold bright_red]ERROR')


#VISUALIZAR DE DISCOS
#-------------------------------------------------------------------------------------------------------
def __analyzer() -> str:
  def print_progress_bar(percent):
    # Calcular el ancho de la barra de carga
    bar_width = 15
    # Calcular el número de caracteres que corresponden al porcentaje
    num_chars = int(bar_width * percent / 100)
    # Crear la barra de carga
    bar = '[' + '█' * num_chars + ' ' * (bar_width - num_chars) + ']'
    # Mostrar la barra de carga y el porcentaje
    print(bar, percent, '%')

  for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      if os.path.exists(f'{drive_letter}:'):
        print('\n[bold red]Disco[/bold red] [blue]>[/blue] [bold purple]' + f'{drive_letter}:/[/bold purple]')
        disk_usage = psutil.disk_usage(f'{drive_letter}:/')

        def to_gb(bytes):
          #Transforma los bytes a gigabyte
          return bytes / 1024**3

        print("[blue] - Espacio Total:[/blue] {:.2f} GB".format(to_gb(disk_usage.total)))
        print("[green] - Espacio Libre:[/green] {:.2f} GB".format(to_gb(disk_usage.free)))
        print("[cyan] - Espacio En Uso:[/cyan] {:.2f} GB".format(to_gb(disk_usage.used)))
        print("[bright_yellow]  >> Porcentaje de Uso:[/bright_yellow] {}%".format(disk_usage.percent))
        percent = disk_usage.percent
        print_progress_bar(percent)


#CONFIGURACION DE RED
#-------------------------------------------------------------------------------------------------------
def __net_conf():
  hostname = socket.gethostname()
  ip = socket.gethostbyname(hostname)
  ip_puntos = socket.inet_ntoa(socket.inet_aton(ip))
  mascara = ipaddress.ip_network(ip_puntos).netmask

  print("Informacion sobre el equipo: \n")
  print(" - Nombre del equipo: ", hostname)
  print(" - Direccion del equipo: ", ip)
  print(" - Mascara de la red: ", mascara)


#PRUEBA DE CONECTIVIDAD
#-------------------------------------------------------------------------------------------------------
def __conect_net(host):
  response = os.system("ping " + host)

  if response == 0:
    print("[bold green]Ningun fallo en la red[/bold green]")
    return True
        
  else:
    print("[bold red]Ha habido fallos en la red[/bold red]")
    return False
  
#PRUEBA DE VELOCIDAD DE INTERNET
#-------------------------------------------------------------------------------------------------------
