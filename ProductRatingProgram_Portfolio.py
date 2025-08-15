import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#Keep a consistent seed to train model accurately long-term
np.random.seed(42)
random.seed(42)

genAdj = ["Sneaky", "Epic", "Fluffy", "Angry", "Spicy", "Quantum", "Turbo"]
genNoun = ["Penguin", "Noodle", "Wizard", "Taco", "Slushie", "Cactus", "Whopper"]

user_list = []
user_preferences = []
categories = ["tech", "fashion", "books", "games", "food"]

def createUsername(i):
    getAdj = genAdj[i % len(genAdj)]
    getNoun = genNoun[i % len(genNoun)]
    number = np.random.randint(0,999)
    return f"{getAdj}{getNoun}{number}"

for i in range(1,21):
    userId = createUsername(i)
    categoriesPref = random.choice(categories)
    user_list.append(userId)
    user_preferences.append(categoriesPref)


#Creating random products to use
productID = []

for i in range(1,31): #Setting each product with its own ID
    product = f"prod_{i}"
    productID.append(product)

productCategories = np.random.choice(categories, size=30)
productPrices = np.random.randint(10,100,size=30)
products = pd.DataFrame({"Product ID" : productID, "Category" : productCategories, "Product Price" : productPrices})

#User rating system
ratings = []
for i in range(len(user_list)):
    user = user_list[i]
    userPreference = user_preferences[i]
    for j in range(len(products)):
        product_ID = products.loc[j, "Product ID"]
        product_Category = products.loc[j, "Category"]
        #Higher product rating if category matche preference, else lower rating
        if product_Category == userPreference:
            rating = np.random.randint(5,11) #5-10
        else:
            rating = np.random.randint(1,6) #1-5
        ratings.append([user, product_ID, rating])

ratingsToDataFrame = pd.DataFrame(ratings, columns=["User ID", "Product ID", "Rating"])
fullDataFrame = ratingsToDataFrame.merge(products, on="Product ID")
FullDataFrame_Sorted = fullDataFrame.sort_values(by="User ID")
print(FullDataFrame_Sorted.to_string(index=False))

#Ratings v Price Graph drawing
avgPriceByCategory = products.groupby("Category")["Product Price"].mean()
plt.figure(figsize=(8,5))
avgPriceByCategory.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Avg. Product Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price in $")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

    
