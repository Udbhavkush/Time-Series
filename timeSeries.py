#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import itertools
import statsmodels.api as sm

#%%
df = pd.read_excel("Superstore.xls")
# %%
df.head()
# %%
df.rename(columns={'Row ID': 'row_id',
                    'Order ID': 'order_id',
                    'Order Date': 'order_date',
                    'Ship Date': 'ship_date',
                    'Ship Mode': 'ship_mode',
                    "Customer ID": 'customer_id',
                    'Customer Name': 'customer_name',
                    'Segment': 'segment',
                    'Country': 'country',
                    'City': 'city',
                    'State': 'state',
                    'Postal Code': 'postal_code',
                    'Region': 'region',
                    'Product ID': 'product_id',
                    'Category': 'category',
                    'Sub-Category': 'sub_category',
                    'Product Name': 'product_name',
                    'Sales': 'sales',
                    'Quantity': 'quantity',
                    'Discount': 'discount',
                    'Profit': 'profit'}, inplace=True)
# %%
