#robot = {"price":900, "count":2,"vat":1.25}
#book = {"price":100, "count":1, "vat":1.06}

#print robot["price"]*robot["count"]*robot["vat"]+book["price"]*book["count"]*book["vat"]

#---

# class Product(object):
# 	price = 0
# 	count = 0
# 	vat = 0	

# class Product(object):
# 	def __init__(self, price, count, vat):
# 		self.price = price
# 		self.count = count
# 		self.vat = vat 
# 	def price_with_vat(self):
# 		return self.price*self.count*self.vat
			

# robot = Product(price=900, count=2, vat=1.25)
# book = Product(price=100, count=1, vat=1.06)



# print robot.price_with_vat()+book.price_with_vat()

#--


class Product(object):
	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat 
	def price_with_vat(self):
		return self.price*self.count*self.vat
	

products = [
	Product(price=900,count=2,vat=1.25), 
	Product(price=100, count=1, vat=1.06)
]

total_price = products[0].price_with_vat() + products[1].price_with_vat()

print total_price







