import time
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


def create_db_connection():
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        #host="localhost",
        port="5432",
        database="coding_challenge"  
    )
    return connection


# Function to insert data into the database
def insert_data_to_db(dataframe, connection, table_name):
    engine = create_engine(connection)
    
    try:
        dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully inserted into {table_name}.")
    except Exception as e:
        print(f"Error during insertion: {str(e)}")

start_time = time.time()

file_path = "PropertyData_R.txt"
delimiter = "|"

#ETL process starts here,  Read the text file into a Pandas DataFrame
df = pd.read_csv(file_path, delimiter=delimiter, low_memory=False)

# perform transforamtion, select columns needed
new_df = df[['Account_Num', 'Owner_Name', 'Owner_Address', 'Owner_CityState', 'Owner_Zip','Situs_Address', 'Property_Class' ]]

#print(new_df.head())

# Connect to the PostgreSQL database
connection = create_db_connection()

# Insert data into the database
insert_data_to_db(new_df, connection, 'Tarrant_Residential')

# Close the database connection
connection.close()





# Record the end time
end_time = time.time()       
       
              
# Calculate the elapsed time
elapsed_time = end_time - start_time       

# Print the elapsed time
print(f"Script took {elapsed_time:.2f} seconds to run.")       