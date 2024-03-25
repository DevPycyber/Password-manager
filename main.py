import commandes


def main():
    stop = False
    while stop == False:
        commande = input('> ')
        if commande != '':
            keyword = commande.split()[0]
            try:
                arg = commande.split()[1]
            except IndexError:
                arg = keyword
            finally:
                if keyword == 'open':
                    com = commandes.Database(arg)
                if keyword == 'create':
                    com.create(arg)
                elif keyword == "close":
                    com.close_table()
                elif keyword == 'add':
                    com.insert_datas(arg)
                elif keyword == "affiche":
                    com.select_all(arg)
                elif keyword == 'affichec':
                    com.select_datas(arg, commande.split()[2])
                elif keyword == "delete":
                    com.delete(arg, commande.split()[2])
                elif keyword == 'help':
                    com.help()
                elif keyword == "affichet":
                    com.list_databases()
                else:
                    print("La commande entrée n\'existe pas !!!")

if __name__ == '__main__':
    main()




