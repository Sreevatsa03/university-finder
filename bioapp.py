

# conda install -c anaconda mysql-connector-python
# Might take a few minutes!


from dbutils import DBUtils
import os


class BioApplication:

    def __init__(self):
        self.db = DBUtils()

    def authenticate(self, user, password, database="bio", host="localhost"):
        self.db.authenticate(user, password, database, host)


    def local_phenotype_network(self, phenotype, min_pubs=2):

        query = f"""
            select *
            from gad_pubs
            where gene_symbol in (
                select gene_symbol
                from gad_pubs
                where phenotype = '{phenotype}'
                and num_pubs >= {min_pubs}
            )
            and num_pubs >= {min_pubs}
            order by gene_symbol, phenotype;
            """

        return self.db.execute(query)

    def local_gene_network(self, gene_symbol, min_pubs=2):

        query = f"""
            select *
            from gad_pubs
            where phenotype in (
                select phenotype
                from gad_pubs
                where gene_symbol = '{gene_symbol}'
                and num_pubs >= {min_pubs}
            )
            and num_pubs >= {min_pubs}
            order by gene_symbol, phenotype;
            """

        return self.db.execute(query)

    def shutdown(self):
        self.db.close()




def main():

    bio = BioApplication()
    bio.authenticate(os.environ["BIO_USER"], os.environ["BIO_PW"])
    bio.shutdown()






if __name__ == '__main__':
    main()



