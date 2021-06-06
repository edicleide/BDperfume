#VISUALIZANDO DADOS

import sqlite3

def titulo(n,s):
    print("="*n)
    print(f'{s}'.center(n))
    print("=" * n)


path = r"C:\SQLite\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()
#id integer, nome text, quantidade integer, id_volume_FK integer,id_marca_FK integer, id_fixacao_FK integer

#PERFUMES
cursor.execute("SELECT * FROM Perfumes AS P JOIN Marcas AS M JOIN Fixacoes AS F ON P.ID = M.ID AND P.ID = F.ID ")
tabela=cursor.fetchall()
titulo(60,"PERFUMES")
print("ID".ljust(5)+"Nome".ljust(15)+"Marca".ljust(15)+"Fixação".ljust(15)+"Quantidade")
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(15), end="")
    print(linha[7].ljust(15), end="")
    print(linha[9].ljust(15), end="")
    print(linha[2])

#ESSENCIA
cursor.execute("SELECT * FROM Essencia AS E JOIN Perfumes AS P ON E.ID = P.ID")
tabela=cursor.fetchall()
titulo(60,"ESSENCIA")
print("ID".ljust(5)+"PERFUME".ljust(10)+"ESSENCIA")
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print((linha[3]).ljust(10), end="")
    print((linha[1]))



