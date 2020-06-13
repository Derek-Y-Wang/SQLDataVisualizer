import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


class SalesOrders:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-URORR13O;'
                                   'Database=TSQL2012;'
                                   'Trusted_Connection=yes;')

        self.sql_query = pd.read_sql_query('SELECT * FROM Sales.Orders',
                                           self.conn)
        self.columns = [i for i in self.sql_query]

    def show_table_attributes(self):
        return self.columns

    def show_all_data(self):
        return self.sql_query

    def generate_graph(self):

        sql_query = pd.read_sql_query(
            "SELECT hr.firstname + N' '+ hr.lastname AS fullname, sum(freight) AS total_freight FROM Sales.Orders AS so LEFT OUTER JOIN HR.Employees AS hr ON hr.empid = so.empid GROUP BY hr.firstname + N' '+ hr.lastname",
            self.conn)

        x_axis = [i for i in sql_query["fullname"]]
        data = [float(i) for i in sql_query["total_freight"]]

        x_pos = [i for i, _ in enumerate(x_axis)]

        plt.bar(x_pos, data, color='green')
        plt.xlabel("Person Name")
        plt.ylabel("Amount of Freight Ordered")
        plt.title("Freight of Each Employee")

        plt.xticks(x_pos, x_axis)

        plt.show()

a = SalesOrders()
a.generate_graph()
