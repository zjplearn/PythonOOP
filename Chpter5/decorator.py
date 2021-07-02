#使用装饰器创建属性
class Silly:
	@property
	def silly(self):
		"This is a silly property"
		return self._silly

	@silly.setter
	def silly(self, value):
		print("You are making a silly {}".format(value))
		self._silly = value

	@silly.deleter
	def silly(self):
		print("Whoah, you killed silly!")
		del self._silly

x = Silly()
x.silly = "21121"
del x.silly
x.silly = "草泥马"
print(x.silly)