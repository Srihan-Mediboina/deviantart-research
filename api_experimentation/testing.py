import deviantart
from bs4 import BeautifulSoup

da = deviantart.Api(29316, "4ed6af8f905b519e6e05f82247ee7dee")

dailydeviations = da.browse_dailydeviations()

for deviation in dailydeviations:
    print(deviation.author)

print("-----")

populardeviations = da.browse(endpoint="popular")
popular_results = populardeviations["results"]
for deviation in popular_results:
    print(deviation.content)

print("-----")

morelikethis = da.browse(endpoint="morelikethis", seed=popular_results[2], timerange="100hr")
morelikethis_results = morelikethis["results"]
for deviation in morelikethis_results:
    print(deviation.title)

print("-----")

whofaved_list = da.whofaved_deviation(deviationid=morelikethis_results[2])
faved_results = whofaved_list["results"]
for user in faved_results:
    print(user['user'])

print("-----")

''' Returns HTTP Error 400: Bad Request, merits further investigation '''
#f = da.download_deviation(popular_results[2])['src']
#print(f)

galleryfolder = da.get_gallery_folder(faved_results[0]['user'])
galleryfolder_results = galleryfolder['results']
for deviation in galleryfolder_results:
    print(deviation.title)

print("-----")

watchers = da.get_watchers(faved_results[0]['user'])
watchers_results = watchers['results']
for watcher in watchers_results:
    print(watcher['user'])

print("-----")

friends = da.get_friends(faved_results[0]['user'])
friends_results = friends['results']
for friend in friends_results:
    print(friend['user'])

print("-----")

comments = da.get_comments(deviationid=morelikethis_results[2])
comments_thread = comments['thread']
for comment in comments_thread:
    soup = BeautifulSoup(comment.body, 'html.parser')
    print(soup.text)