import pandas as pd
import matplotlib.pyplot as plt

houseprices_data = pd.read_csv("HousingPrices-Amsterdam.csv")
houseprices_data = houseprices_data[['Zip', 'Price', 'Area', 'Room']]

houseprices_data['PriceperSqm'] = houseprices_data['Price'] / houseprices_data['Area']

houseprices_sorted = houseprices_data.sort_values('Price', ascending=False)

fig, ax = plt.subplots(figsize=(40, 18))
x = houseprices_sorted['Zip'][0:10]
y = houseprices_sorted['Price'][0:10]
y1 = houseprices_sorted['PriceperSqm'][0:10]
plt.subplot(1, 2, 1)
plt.bar(x, y)
plt.xticks(fontsize=17)
plt.ylabel('House prices in millions', fontsize=25)
plt.yticks(fontsize=20)
plt.title('Top 10 Areas with the highest house prices',
          fontsize=25)
plt.subplot(1, 2, 2)
plt.bar(x, y1)

plt.xticks(fontsize=17)
plt.ylabel('House prices per sqm', fontsize=25)
plt.yticks(fontsize=20)
plt.title('Top 10 Areas with the highest house prices per sqm', fontsize=25)
plt.show()
