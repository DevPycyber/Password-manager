
import sqlite3
import inspect

def max_len(liste_str):
    l0 = liste_str[0]
    for element in liste_str:
        if len(element) > len(l0):
            l0 = element
    return len(l0)



class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.db_name = db_name
        self.cur = self.connection.cursor()

    def select_datas(self, table, datas):
        assert sqlite3.OperationalError, "champs inexistant dans la table"
        print(f"{datas}")
        print('----------')
        for row in self.cur.execute(f"SELECT {datas} FROM {table}"):
            print(row[0])


    def select_all(self, table):
        print("Identifiants   Mots de passes")
        print("------------------------------")
        liste_ids = []
        for row in self.cur.execute(f"SELECT * FROM {table}"):
            liste_ids.append(row[1])
        max_longueur = max_len(liste_ids)
        for row in self.cur.execute(f"SELECT * FROM {table}"):
            if len(row[1]) < max_longueur:
                print(row[1], ' '*(max_longueur-len(row[1])), '|', row[2])
            else:
                print(row[1], '|', row[2])

    def create(self, table):
        self.cur.execute(f"""
            CREATE TABLE {table}(
                id_count INTEGER NOT NULL,
                username STRING(64),
                password STRING(64),
                CONSTRAINT pk_id primary key (id_count)
            );
            """
        )
        self.connection.commit()

    def list_databases(self):
        i = 0
        for row in self.cur.execute("SELECT name FROM sqlite_master WHERE type= 'table'"):
            print("table ", i,":",  row[0])
            i+=1

    def delete(self, table, num_entry):
        self.cur.execute(f"DELETE FROM {table} WHERE id_count = {num_entry};")
        self.connection.commit()
        
    def insert_datas(self, table):
        self.datas = []
        nb = int(input('Combien d\'entrées voulez-vous ajouter ?'))
        assert nb >= 1, "le nombre d\'entrées est > ou = à 1 !!"
        for i in range(nb):
            username = input('username: ')
            password = input('password: ')
            ids = (username, password)
            self.datas.append(ids)
        datas_str = ''
        if len(self.datas) > 1:
            for e in self.datas:
                datas_str += str(e)
                if self.datas[-1] != e:
                    datas_str += ','
        else:
            datas_str += str(self.datas[0])
        self.cur.execute(f"""
            INSERT INTO {table}(username, password)
        VALUES {datas_str};

        """)
        self.connection.commit()

    def delete_table(self, table):
        self.cur.execute(f"""
            DROP TABLE {table}
    """)
        self.connection.commit()

    def help(self):
        print("Commandes disponibles : ")
        print("open <database>, permet d\'établir une connexion avec une base de donnée")
        print("create <table>, permet d\'insérer une nouvelle table dans une base de donnée")
        print("delete <num_entree>: supprime l\'entrée sélectionnée de la table ")
        print("add <table> : permet d\'ajouter une ou plusieurs entrées dans la base de donnée : un dictatiel vous guidera")
        print("close : permet de rompre la connexion avec la base de donnée courante")
        print("affiche : permet d\'afficher les données de la table rangées par identifiant et mot de passe")
        print("affiche <table> <champs> : permet d\'afficher des données spécifiques de la table en fonction du champs spécifié")



    def close_table(self):
        self.connection.close()
        

print(inspect.Signature(Database.insert_datas))

