#INSERINDO REGISTRO

import sqlite3

path = r"C:\SQLite\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

#PERFUMES
cursor.execute("INSERT INTO Perfumes VALUES(1,'ROSA',10, 250, 1, 1)")
cursor.execute("INSERT INTO Perfumes VALUES(2,'AZUL',5, 250, 2, 2)")
cursor.execute("INSERT INTO Perfumes VALUES(3,'LILÁS',15, 250, 3, 3)")

#id integer, nome text, quantidade integer, id_volume_FK integer,id_marca_FK integer, id_fixacao_FK integer

#VOLUME
cursor.execute("INSERT INTO Volume VALUES(1,'ROSA')")
cursor.execute("INSERT INTO Volume VALUES(2,'AZUL')")
cursor.execute("INSERT INTO Volume VALUES(3,'LILÁS')")

#id integer, nome text

#Essencia
cursor.execute("INSERT INTO Essencia VALUES(1,'ABC')")
cursor.execute("INSERT INTO Essencia VALUES(2,'DEF')")
cursor.execute("INSERT INTO Essencia VALUES(3,'GHI')")
#id integer, nome text

#ESSENCIA PERFUME
cursor.execute("INSERT INTO Essencia_Perfume VALUES(1,1)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES(2,2)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES(3,3)")

# id_essencia_FK integer, id_perfume_FK integer

#MARCAS
cursor.execute("INSERT INTO Marcas VALUES(1,'BOTI')")
cursor.execute("INSERT INTO Marcas VALUES(2,'QDB')")
cursor.execute("INSERT INTO Marcas VALUES(3,'EUDO')")
#id integer, nome text

#FIXACAO
cursor.execute("INSERT INTO FIXACOES VALUES(1,'BOM')")
cursor.execute("INSERT INTO FIXACOES VALUES(2,'EXCELENTE')")
cursor.execute("INSERT INTO FIXACOES VALUES(3,'BOM')")

#id integer, nome text

banco.commit()