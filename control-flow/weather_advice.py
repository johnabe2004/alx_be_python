<<<<<<< HEAD:control-flow/weather_advice.py
def weather_advice():
    weather = input("What's the weather like today? (sunny, rainy, cold): ").lower()
=======
weather = input("What's the weather like today? (sunny, rainy, cold): ").lower()
>>>>>>> 848c64d29711230b75a75b4ffc7274bf40463a6d:weather_advice.py
    # Provide clothing recommendations based on the weather input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")
weather_advice()
