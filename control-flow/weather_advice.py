# Creating a variable to ask the user to input the current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# creating a if statement to recommend clothes for each weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendation for this weather.")