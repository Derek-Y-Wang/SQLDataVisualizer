import pyodbc
import pandas as pd


class HREmployee:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-URORR13O;'
                                   'Database=TSQL2012;'
                                   'Trusted_Connection=yes;')

        self.sql_query = pd.read_sql_query('SELECT * FROM HR.Employees',
                                           self.conn)
        self.columns = [i for i in self.sql_query]

    def show_table_attributes(self):
        return self.columns

    def show_all_data(self):
        return self.sql_query


a = HREmployee()
a.show_table_attributes()
print(a.show_all_data())

