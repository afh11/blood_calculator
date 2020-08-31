foods = ["apples", "bananas", "cherries", "donuts", "eggplants"]

amounts = [11, 22, 33, 44, 55]

#do_I_like_it = [True, False, False, True]

#for i, food in enumerate(foods): #enumerate returns the index and the item
#	print("{} - {}".format(amounts[i],food))

#for amount, food, liked in zip(amounts, foods, do_I_like_it): #zip used to iterate over arrays up to smallest list size
#	print("{} - {} - {}".format(amount, food, liked ))

def how_many(input):
	for amount, food in zip(amounts, foods):
		if food == input:
			answer = amount
			break
	print("I found my fruit")
	return answer


if __name__ == "__main__":
	x = how_many("donuts")
	print(x)