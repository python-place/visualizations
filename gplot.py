import pandas as pd
from plotnine import *

houseprices_data = pd.read_csv("HousingPrices-Amsterdam.csv")
houseprices_data = houseprices_data[['Zip', 'Price', 'Area','Room']]

houseprices_data['PriceperSqm'] = houseprices_data['Price']/houseprices_data['Area']

houseprices_sorted = houseprices_data.sort_values('Price',ascending = False)

chart_data = houseprices_sorted[0:10]
test = ggplot(chart_data,aes(x='Zip',y = 'Price')) + geom_bar(stat ='identity') \
+ scale_x_discrete(limits=chart_data['Zip'].tolist()) +theme(figure_size=(16, 8))

print(test)

