from googlesearch import search
# search is a function in googlesearch module, it takes 5 arguments. they are:
# query, tld, num, stop, pause
# query is the string we want to search
query = "loafers"

for url in search(query, tld="com", num=10, stop=10, pause=2):
    print(url)

# tld stands for top level domain which means we want to search our result on google.com
# num stands for number of results we want
# stop stands for after how many results we want to stop
# pause stands for how much time we want to pause between two requests. It is 2 seconds here.