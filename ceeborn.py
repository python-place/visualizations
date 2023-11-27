import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

houseprices_data = pd.read_csv("HousingPrices-Amsterdam.csv")
houseprices_data = houseprices_data[['Zip', 'Price', 'Area', 'Room']]

houseprices_data['PriceperSqm'] = houseprices_data['Price'] / houseprices_data['Area']

houseprices_sorted = houseprices_data.sort_values('Price', ascending=False)

plt.figure(figsize=(12, 6))
data = houseprices_sorted[0:10]
ax = sns.barplot(data=data, x='Zip', y='Price')
ax.set_xlabel('Zip code', fontsize=15)
ax.set_ylabel('House prices in millions', fontsize=15)
ax.set_title('Top 10 Areas with the highest house prices', fontsize=20)
plt.show()
