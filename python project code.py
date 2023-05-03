# -*- coding: utf-8 -*-
"""
Created on Thu May  4 01:17:15 2023

@author: User
"""

import pandas as pd
import numpy as np
import datetime as dt
import glob


#abdul Samad

"""---Directory Path---"""
csv_files = glob.glob('*.csv')
csv_data_cleaned = {}
for file in csv_files:
    df = pd.read_csv(file)
    csv_data_cleaned[file] = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


for file in csv_data_cleaned:
    print(f"Missing values in file {file}:")
    print(csv_data_cleaned[file].isna().sum())
    
# """---import all data sets---"""

#This dataset has information about the customer and its location
# customer_data = csv_data_cleaned['olist_customers_dataset.csv']

# #This dataset has information Brazilian zip codes and its lat/lng coordinates
# location_data = csv_data_cleaned['olist_geolocation_dataset.csv']

# #This dataset includes data about the items purchased within each order.
# order_items_data = csv_data_cleaned['olist_order_items_dataset.csv']

# #This dataset includes data about the orders payment options.
# payments_data = csv_data_cleaned['olist_order_payments_dataset.csv']

# #This dataset includes data about the reviews made by the customers.
# reviews_data = csv_data_cleaned['olist_order_reviews_dataset.csv']

# #This is the core dataset
# orders_data = csv_data_cleaned['olist_orders_dataset.csv']

# #This dataset includes data about the products sold by Olist.
# product_data = csv_data_cleaned['olist_products_dataset.csv']

# #This dataset includes data about the sellers that fulfilled orders made at Olist.
# sellers_data = csv_data_cleaned['olist_sellers_dataset.csv']

# #Translates the product_category_name to english.
# translation_data = csv_data_cleaned['product_category_name_translation.csv']




# """---dealing with null values---"""



# """---customer_data---"""
# print(customer_data.isna().sum())    # no null values found

# """---location_data---"""
# print(location_data.isna().sum())    # no null valuesfound

# """---order_items_data---"""
# print(order_items_data.isna().sum())    # no null values found

# """---payments_data---"""
# print(payments_data.isna().sum())    # no null values found

# """---reviews_data---"""
# print(reviews_data.isna().sum())    # null values found in two coloums 'review_comment_title'; 'review_comment_message'

# # dropping the two coloums with null values as we only need review scores not the commments, also, the comments are in brazlian language

# print(reviews_data.head())

# reviews_data = reviews_data.drop(["review_comment_title","review_comment_message"], axis='columns')

# print(reviews_data.head())

# print(reviews_data.isna().sum())    # two columns with null values removed as we didn't need them

# """---orders_data---"""
# print(orders_data.isna().sum())    # null values found in three coloums date, time colums

# #  we shall be dropping rows will null values as they are negligible 2965 out of 99441 rows i.e. less than 3 percent

# print(orders_data.shape) 

# orders_data.dropna(inplace=True)

# print(orders_data.shape)

# print(orders_data.isna().sum())   # rows with null values removed as we didn't need them


# """---product_data---"""
# print(product_data.isna().sum())    
# # null values in product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, weight, length, height

# # where product name is missing, we shall use "Name not avaiable"

# product_data['product_category_name'] =  product_data['product_category_name'].fillna('Name not avaiable')

# # for other columns we shall fill with the mean of those columns

# x = product_data["product_name_lenght"].mean()
# product_data["product_name_lenght"].fillna(x, inplace = True)

# y = product_data["product_description_lenght"].mean()
# product_data["product_description_lenght"].fillna(y, inplace = True)

# z = product_data["product_photos_qty"].mean()
# product_data["product_photos_qty"].fillna(z, inplace = True)


# # for last three columns i.e. height, weight and lenght we shall drop null values, since there are only two rows with null values

# product_data.dropna(inplace=True)

# print(product_data.isna().sum())   # null values dealt with


# """---sellers_data---"""
# print(sellers_data.isna().sum())     # no null values found

# """---translation_data---"""

# print(translation_data.isna().sum())     # no null values found

# # null values dealt with, in all data frames


# """---dealing with duplicate values---"""


# """---customer_data---"""
# print(customer_data.duplicated().sum())  # no duplicates found

# """---location_data---"""
# print(location_data.duplicated().sum())        # duplicates found
# location_data.drop_duplicates(inplace = True)
# print(location_data.duplicated().sum())     # duplicates removed


# """---order_items_data---"""
# print(order_items_data.duplicated().sum())    # no duplicates found

# """---payments_data---"""
# print(payments_data.duplicated().sum())      # no duplicates found

# """---reviews_data---"""
# print(reviews_data.duplicated().sum())    # no duplicates found

# """---orders_data---"""
# print(orders_data.duplicated().sum())    # no duplicates found

# """---product_data---"""
# print(product_data.duplicated().sum())    # no duplicates found

# """---sellers_data---"""
# print(sellers_data.duplicated().sum())      # no duplicates found

# """---translation_data---"""
# print(translation_data.duplicated().sum())       # no duplicates found

# # duplicates dealt with, in all data frames




# """---standardization---"""

# """---standardizing all date columns, converting them to datetime objects---"""


# reviews_data['review_answer_timestamp'] = pd.to_datetime(reviews_data['review_answer_timestamp'])
# order_items_data['shipping_limit_date'] = pd.to_datetime(order_items_data['shipping_limit_date'])
# orders_data['order_purchase_timestamp'] = pd.to_datetime(orders_data['order_purchase_timestamp'])
# orders_data['order_approved_at'] = pd.to_datetime(orders_data['order_approved_at'])
# orders_data['order_delivered_carrier_date'] = pd.to_datetime(orders_data['order_delivered_carrier_date'])
# orders_data['order_delivered_customer_date'] = pd.to_datetime(orders_data['order_delivered_customer_date'])
# orders_data['order_estimated_delivery_date'] = pd.to_datetime(orders_data['order_estimated_delivery_date'])

# # dates standardized in all data frames

# #abdul Samad


# """---Checking DataTypes of All Columns---"""
# for file in csv_data_cleaned:
#     print(f"Data Types of columns from {file}:")
#     print(csv_data_cleaned[file].dtypes)

# pd.options.display.max_columns = None
# print(orders_data.head())


# # order_data[]

# orders_data["approval_dur(Hrs)"] = np.where(orders_data["order_status"] != "canceled", 
#                                              (orders_data["order_approved_at"] - orders_data["order_purchase_timestamp"]).astype('timedelta64[h]'), 
#                                              np.nan)

# print(orders_data[orders_data['order_status'] == 'canceled']['order_status'])
# canceled_orders = orders_data[orders_data["order_status"] == "canceled"][["order_status", "approval_dur(Hrs)"]]
# print(canceled_orders)


# orders_data["Purchase Vs Delivered(Days)"] = np.where(orders_data["order_status"] == "delivered", 
#                                               (pd.to_datetime(orders_data["order_delivered_customer_date"]) - pd.to_datetime(orders_data["order_purchase_timestamp"]).astype('timedelta64[h]')), 
#                                              np.nan)

# orders_data["Purchase Vs Delivered(Days)"] = orders_data["Purchase Vs Delivered(Days)"].dt.days

# print(orders_data.dtypes)








 





