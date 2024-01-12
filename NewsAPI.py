import requests
def news(cate):
       response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={cate}&apiKey=57b3d49680ef46149e2f418004313e95")
       news_dict = response.json()  # they can provide news dict.
       global aritcles    # to acces in two functions~
       aritcles = news_dict["articles"]
       print("-------------Headlines-------------".upper().center(50))
       print(" ")  # print blank line
       i = 0
       for n in aritcles:
              i = i + 1
              print(f"{i}. {n.get('title')}")  # to get news title

def about_news(number):
       print("------------About The News------------".center(50))
       print(" ")  # printing blank line
       global aritcles
       i = 0
       for n in aritcles:
              i = i + 1
              if i == number:  # jo number hoga us number ki news details
                     print(f"{i}. {n.get('title')}")
                     print(f"description: {n.get('description')}")
                     print(f"url: {n.get('url')}")
                     print(f"publishedAt: {n.get('publishedAt')}")
                     break
                     # for key, value in n.items():
                     #        print(f"{key}: {value}")  # to get about news

print("--------welcome to news api---------".upper().center(50))

print("""---Categires---
1 for: Business
2 for: Entertainmetns
3 for: Health
4 for: Science
5 for: Sports
6 for: Technology""")

user = int(input("What type of news you read? : ".title()))
print("loding......................")

match user:

       case 1:
              news("business""")
       case 2:
              news("entertainment")
       case 3:
              news("health")
       case 4:
              news("health")
       case 5:
              news("sports")
       case 6:
              news("technology")


while True:
       print("")
       see_more = int(input("See more about a news , type news number: "))
       about_news(see_more)

