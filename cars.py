import random
def select_random():
	car_brands = ["Toyota","Nissan","Ford"]
	model_year = [1996,2020,2024]
	random_brand = random.choice(car_brands)
	random_year = random.choice(model_year)
	return random_year
	return random_brand

if __name__ = "__main"":
	random_car_brand = select_random()
	random_car_year = select_random()
	print("Random car and date are: ", random_car_brans, random_car_year)
