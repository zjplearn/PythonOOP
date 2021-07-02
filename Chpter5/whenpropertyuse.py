from urllib.request import urlopen

class WebPage:
	def __init__(self, url):
		self.url = url
		self._content = None

	@property
	def content(self):
		if not self._content:
			print("Retrieving New Page")
			self._content = urlopen(self.url).read()
		return self._content

webpage = WebPage("https://www.bilibili.com/bangumi/play/ep333950?spm_id_from=333.851.b_7265706f7274466972737431.4")
content1 = webpage.content
print(type(content1))
print(content1)
	