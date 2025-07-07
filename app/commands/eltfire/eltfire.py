from utils.insert_data import DataInserter


# Create an instance of DataInserter to handle data insertion
elt = DataInserter()


# Command-line interface function to initialize the database
def cli():
    elt.run()