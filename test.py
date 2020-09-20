import math

class CJBot():

	def parsing(self):

		PEOPLE_PER_PAGE = 25

		pages_count = int(math.ceil(262 / PEOPLE_PER_PAGE))

		print(pages_count)
		#print("Hello World")

		url = 'https://candyjar.io/search/vacancy/5420/1/W1sicG9zdGdyZXNxbCJdLFtdLCIiLFtdXQ=='
		split_url = url.split("/")
		count = 'Hello!'
		cur_page_url = split_url[0]+'/'+split_url[1]+'/'+split_url[2]+'/'+split_url[3]+'/'+split_url[4]+'/'+split_url[5]+'/'+count+'/'+split_url[7]
		print(cur_page_url)

		user_name = 'Andrey'


my_bot = CJBot()
my_bot.parsing()
