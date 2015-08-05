#robot = {"price":900, "count":2,"vat":1.25}
#book = {"price":100, "count":1, "vat":1.06}

#print robot["price"]*robot["count"]*robot["vat"]+book["price"]*book["count"]*book["vat"]

class Product(object):
	price = 0
	count = 0
	vat = 0

robot = Product()
robot.price = 900
robot.count = 2
robot.vat = 1.25

book = Product()
book.price = 100
book.count = 1
book.vat = 1.06

print robot.price * robot.count * robot.vat + book.price * book.count * book.vat
