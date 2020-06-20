import pyodbc
import pandas as pd
import matplotlib as plt
from graphData.SalesOrdersData import SalesOrders


class Visualizer:

    def __init__(self, salesOrder):
        self.salesOrder = salesOrder

    def generate_graphs(self):
        self.salesOrder.generate_graph()


if __name__ == '__main__':
    salesData = SalesOrders()

    v = Visualizer(salesData)
    v.generate_graphs()
