import pandas as pd
import matplotlib.pyplot as plt

class RetailSalesAnalyzer:
    def __init__(self):
        self.data=pd.read_csv('retail_sales.csv')

    def data_clean(self):
        return self.data.dropna(inplace=True)

    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()

    def best_selling_product(self):
        return self.total_sales_per_product().sort_values(ascending=False).index[0]

    def average_sales(self):
        return self.data['Sales'].mean()

    def sales_trend(self):
        self.data.groupby('Date')['Sales'].sum().plot(kind='line')
        plt.title('Sales trend over time')
        plt.xlabel('Date')
        plt.ylabel('Total sales')
        plt.show()

    def sales_per_product(self):
        self.data.groupby('Product')['Sales'].sum().plot(kind='bar')
        plt.title('Sales Per Product')
        plt.xlabel('Product')
        plt.ylabel('Total sales')
        plt.show()



analyzer = RetailSalesAnalyzer()
print('Total Sales Per Product: \n',analyzer.total_sales_per_product() )
print('Best Selling Product: \n', analyzer.best_selling_product())
print('Average Sales per Day: \n', analyzer.average_sales())
analyzer.sales_trend()
analyzer.sales_per_product()
