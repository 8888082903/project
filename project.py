import matplotlib
import pandas as pd

import inline as inline

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline



zomato_data = pd.read_csv("/home/sunbeam/Downloads/zomato.csv")

data = zomato_data.head()
# print(data)
#show first 5 rows of data

# dtypes = zomato_data.dtypes
col = zomato_data.columns
# print(dtypes)
# print(col)

# check data duplication
dup = zomato_data.duplicated().sum()
# print(dup)

missing_value = pd.DataFrame(round(zomato_data.isnull().sum()/zomato_data.shape[0] * 100, 3), columns=["Missing"])
# print(missing_value)

drop = zomato_data.drop(["url", "address", "phone"], axis=1, inplace=True)
# print(zomato_data)


rename = zomato_data.rename(columns={"approx_cost(for two people)": "cost_two", "listed_in(type)":"service_type", "listed_in(city)":"serve_to"}, inplace = True)
# print(rename)

# zomato_data.cost_two = zomato_data.cost_two.apply(lambda x: int(x.replace(',', '')))
# zomato_data.cost_two = zomato_data.cost_two.astype('int')


plt.rcParams['figure.figsize'] = 14,7
sns.countplot(zomato_data["rate"], palette="Set1")
plt.title("Count plot of rate variable")
plt.show()

#joint plot for 'rate' and 'votes'
sns.jointplot(x = "rate", y = "votes", data = zomato_data, height=8, ratio=4, color="g")
plt.show()

#analyze the number of restaurants in a location
zomato_data.location.value_counts().nlargest(10).plot(kind = "barh")
plt.title("Number of restaurants by location")
plt.xlabel("Count")
plt.show()

#seaborn heatmap function to plot the correlation grid
sns.heatmap(zomato_data.corr(), annot = True, cmap = "viridis",linecolor='white',linewidths=1)
plt.show()

#restaurants serve to
zomato_data.serve_to.value_counts().nlargest(10).plot(kind = "barh")
plt.title("Number of restaurants listed in a particular location")
plt.xlabel("Count")
plt.show()

#count plot for online_order analysis
sns.countplot(zomato_data["online_order"], palette = "Set2")
plt.show()

sns.countplot(hue = zomato_data["online_order"], palette = "Set1", x = zomato_data["rate"])
plt.title("Distribution of restaurant rating over online order facility")
plt.show()

plt.rcParams['figure.figsize'] = 14,7
plt.subplot(1,2,1)
zomato_data.name.value_counts().head().plot(kind = "barh", color = sns.color_palette("hls", 5))
plt.xlabel("Number of restaurants")
plt.title("Biggest Restaurant Chain (Top 5)")

plt.subplot(1,2,2)
zomato_data[zomato_data['rate']>=4.5]['name'].value_counts().nlargest(5).plot(kind = "barh", color = sns.color_palette("Paired"))
plt.xlabel("Number of restaurants")
plt.title("Best Restaurant Chain (Top 5) - Rating More than 4.5")
plt.tight_layout()