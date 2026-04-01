# automated-data-pipline-ADP
Clean-up messy csv-files, load them into a SQLite database and connect the database with Microsoft Power BI Desktop

data_cleaning.py:  Python script for cleaning up CSV files. !!Important: If the Script doesn't clean some collumns, try adding the collumnnames into the coresponding Lists!!

database_load.py:  Creates a SQLite Database sales.db and allows the user to choose a csv-file (preferably one that is cleaned by data_cleaning.py) to import into the Database.

queries.sql:  Analytical SQL queries for evaluating business data

!!Important: The idea was to establish a connection between Power BI Desktop and the database sales.db to create interactive BI dashboards from the data inside the database. To connect a SQLite Database you need to download a SQLite-ODBC-Driver!!



