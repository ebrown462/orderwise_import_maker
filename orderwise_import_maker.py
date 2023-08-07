import pandas as pd

# read in the two CSV files
old_data = pd.read_csv('data_before.csv')
new_data = pd.read_csv('pricelist.csv')

# merge the two dataframes on the "productCode" column
merged_data = pd.merge(old_data, new_data, on='productCode', how='outer')

# create a new column called "updatedPrice"
merged_data['updatedPrice'] = merged_data.apply(lambda x: x['Price_y'] if pd.notnull(x['Price_y']) else x['Price_x'], axis=1)

# drop the "Price_y" column and rename the "Price_x" column to "Price"
merged_data.drop('Price_y', axis=1, inplace=True)
merged_data.rename(columns={'Price_x': 'Price'}, inplace=True)

# write the updated data to a new CSV file
merged_data.to_csv('updated_data.csv', index=False)