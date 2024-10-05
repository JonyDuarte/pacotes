# instalar biblioteca winapps  = No terminal digite pip install winapps

# bibliotecas
import platform as p
import winapps as w
 
 # exibir o sistema operacional do usuário
print(f"Sistema operacional do usuário: {p.system()} {p.release()}.")

# listas todos os programas instalados no computador
print("\n Lista de todos os programas instalados: ")
for programa in w.list_installed():
    print(f"Programa: {programa.name}.")
    print(f"Versão: {programa.version}.")
    print(f"Data da instalação: {programa.install_date}.")
    print(f"Data de publicação: {programa.publisher}.")
    print(f"Local de desinstalação: {programa.publisher}.")
    print(f"{'==-'*30}")
