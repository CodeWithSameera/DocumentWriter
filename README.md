# DocumentWriter
Quote Generation

The goal of this task is to have an output document generated containing information about the quote.
Please refer to the example document generated, you can use it as reference.
For the given task an SQLite database with all the necessary data will be provided.

You will need to:
1) Establish connection to the sqlite database
2) Write a queries to read the necessary data from the database (you can use Mozilla Firefox extension SQLITEMANAGER to open database and run query)
3) Read the data from database using previously built queries
3.1) Optional: Create separate class with methods to read data from database
4) Write data to the document
4.1) Optional: before writing the data to the document, parse to class objects: Quote, Quote item, Customer 
4.2) Optional: Create separate class with methods to write data for output document
