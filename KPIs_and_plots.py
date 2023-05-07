# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:47:00 2023

@author: Brain Hacker
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

"""---import all data sets---"""

#This dataset has information about the customer and its location
customer_data = pd.read_csv('olist_customers_dataset.csv')

#This dataset has information Brazilian zip codes and its lat/lng coordinates
location_data = pd.read_csv('olist_geolocation_dataset.csv')

#This dataset includes data about the items purchased within each order.
order_items_data = pd.read_csv('olist_order_items_dataset.csv')

#This dataset includes data about the orders payment options.
payments_data = pd.read_csv('olist_order_payments_dataset.csv')

#This dataset includes data about the reviews made by the customers.
reviews_data = pd.read_csv('olist_order_reviews_dataset.csv')

#This is the core dataset
orders_data = pd.read_csv('olist_orders_dataset.csv')

#This dataset includes data about the products sold by Olist.
product_data = pd.read_csv('olist_products_dataset.csv')

#This dataset includes data about the sellers that fulfilled orders made at Olist.
sellers_data = pd.read_csv('olist_sellers_dataset.csv')

#Translates the product_category_name to english.
translation_data = pd.read_csv('product_category_name_translation.csv')

"""---dealing with null values---"""



"""---customer_data---"""
# print(customer_data.isna().sum())    # no null values found

"""---location_data---"""
# print(location_data.isna().sum())    # no null valuesfound

"""---order_items_data---"""
# print(order_items_data.isna().sum())    # no null values found

"""---payments_data---"""
# print(payments_data.isna().sum())    # no null values found

"""---reviews_data---"""
# print(reviews_data.isna().sum())    # null values found in two coloums 'review_comment_title'; 'review_comment_message'

# dropping the two coloums with null values as we only need review scores not the commments, also, the comments are in brazlian language

#print(reviews_data.head())

reviews_data = reviews_data.drop(["review_comment_title","review_comment_message"], axis='columns')

#print(reviews_data.head())

# print(reviews_data.isna().sum())    # two columns with null values removed as we didn't need them

"""---orders_data---"""
# print(orders_data.isna().sum())    # null values found in three coloums date, time colums

#  we shall be dropping rows with null values as they are negligible 2965 out of 99441 rows i.e. less than 3 percent

# print(orders_data.shape) 

orders_data.dropna(inplace=True)

# print(orders_data.shape)

# print(orders_data.isna().sum())   # rows with null values removed as we didn't need them


"""---product_data---"""
# print(product_data.isna().sum())    
# null values in product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, weight, length, height

# where product name is missing, we shall use "Name not avaiable"

product_data['product_category_name'] =  product_data['product_category_name'].fillna('Name not avaiable')

# for other columns we shall fill with the mean of those columns

x = product_data["product_name_lenght"].mean()
product_data["product_name_lenght"].fillna(x, inplace = True)

y = product_data["product_description_lenght"].mean()
product_data["product_description_lenght"].fillna(y, inplace = True)

z = product_data["product_photos_qty"].mean()
product_data["product_photos_qty"].fillna(z, inplace = True)


# for last three columns i.e. height, weight and lenght we shall drop null values, since there are only two rows with null values

product_data.dropna(inplace=True)

# print(product_data.isna().sum())   # null values dealt with


"""---sellers_data---"""
# print(sellers_data.isna().sum())     # no null values found

"""---translation_data---"""

# print(translation_data.isna().sum())     # no null values found

# null values dealt with, in all data frames


"""---dealing with duplicate values---"""


"""---customer_data---"""
# print(customer_data.duplicated().sum())  # no duplicates found

"""---location_data---"""
# print(location_data.duplicated().sum())        # duplicates found
location_data.drop_duplicates(inplace = True)
# print(location_data.duplicated().sum())     # duplicates removed


"""---order_items_data---"""
# print(order_items_data.duplicated().sum())    # no duplicates found

"""---payments_data---"""
# print(payments_data.duplicated().sum())      # no duplicates found

"""---reviews_data---"""
# print(reviews_data.duplicated().sum())    # no duplicates found

"""---orders_data---"""
# print(orders_data.duplicated().sum())    # no duplicates found

"""---product_data---"""
# print(product_data.duplicated().sum())    # no duplicates found

"""---sellers_data---"""
# print(sellers_data.duplicated().sum())      # no duplicates found

"""---translation_data---"""
# print(translation_data.duplicated().sum())       # no duplicates found

# duplicates dealt with, in all data frames

"""---standardization---"""

"""---standardizing all date columns, converting them to datetime objects---"""


reviews_data['review_answer_timestamp'] = pd.to_datetime(reviews_data['review_answer_timestamp'])
order_items_data['shipping_limit_date'] = pd.to_datetime(order_items_data['shipping_limit_date'])
orders_data['order_purchase_timestamp'] = pd.to_datetime(orders_data['order_purchase_timestamp'])
orders_data['order_approved_at'] = pd.to_datetime(orders_data['order_approved_at'])
orders_data['order_delivered_carrier_date'] = pd.to_datetime(orders_data['order_delivered_carrier_date'])
orders_data['order_delivered_customer_date'] = pd.to_datetime(orders_data['order_delivered_customer_date'])
orders_data['order_estimated_delivery_date'] = pd.to_datetime(orders_data['order_estimated_delivery_date'])

# KPIs Coding by Ammar

# KPI 1: Customer Satisfaction Score = Sum of all Scores / Total Number of Respondents


num_respondents = reviews_data['review_id'].count()


sum_scores = reviews_data['review_score'].sum()


customer_satisfaction_score = round(sum_scores/num_respondents)


print('Customer Satisfaction Score:', customer_satisfaction_score)

reviews_data = reviews_data.sort_values('review_answer_timestamp')

# calculate the total score for each year
yearly_scores = reviews_data.groupby(reviews_data['review_answer_timestamp'].dt.year)['review_score'].sum()

# calculate the average score for each year
yearly_average = reviews_data.groupby(reviews_data['review_answer_timestamp'].dt.year)['review_score'].mean().round(2)

# print("Total score for each year:")
# print(yearly_scores)
# print("Average score for each year:")
# print(yearly_average)

# Making a line plot with the average score for each year

yearly_average.plot(kind='line')

# set the title and axis labels
plt.title('Average Score by Year')
plt.xlabel('Year')
plt.ylabel('Average Score')

# show the plot
plt.show()


# Making a bar plot for the average score of each year


yearly_averages = {'2016':3.54, '2017':4.11, '2018':4.07}
years = list(yearly_averages.keys())
averages = list(yearly_averages.values())
  
bar_plot = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(years, averages, color ='maroon',
        width = 0.4)
 
plt.xlabel("Years")
plt.ylabel("Average score")
plt.title("Average score of each year")
plt.show()


# KPI 2: Purchase Frequency = Total Number of Orders / Total Number of Unique Customers

total_number_of_orders = orders_data['order_id'].count()

num_of_uniq_cust = orders_data['customer_id'].nunique()

purchase_frequency = total_number_of_orders / num_of_uniq_cust





