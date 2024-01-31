import deviantart
from datetime import datetime
import json
from collections import Counter

da = deviantart.Api(29316, "4ed6af8f905b519e6e05f82247ee7dee")

dailydeviations = da.browse_dailydeviations()

# https://www.deviantart.com/innocentium/art/Laughing-Kookaburra-986887872
kookaburraid = '83414BDC-9586-583C-3B79-4F554968A469'
kookaburra_metadata = da.get_deviation_metadata(kookaburraid)
tags = kookaburra_metadata[0]['tags']
for t in tags:
    #print(t['tag_name'])
    pass

#print("-----") 

kookaburra_deviation = da.get_deviation(kookaburraid)
watchers = da.get_watchers(kookaburra_deviation.author.username, limit=50, offset=49)
for w in watchers['results']:
    #print(w['user'])
    pass

all_tags = []

innocentium_all_works = {}
works = da.get_gallery_folder(username=kookaburra_deviation.author.username, limit=24)
for work in works['results']:
    tag_data = da.get_deviation_metadata(work.deviationid)[0]['tags']
    tags = []
    for tag in tag_data:
        tags.append(tag['tag_name'])
        all_tags.append(tag['tag_name'])
    innocentium_all_works[work.title] = [work.stats, str(datetime.utcfromtimestamp(int(work.published_time))), tags, (None != work.daily_deviation)]

work_count = 561
offset_count = 24
while work_count > 0:
    works = da.get_gallery_folder(username=kookaburra_deviation.author.username, limit=24, offset=offset_count)
    for work in works['results']:
        tag_data = da.get_deviation_metadata(work.deviationid)[0]['tags']
        tags = []
        for tag in tag_data:
            tags.append(tag['tag_name'])
            all_tags.append(tag['tag_name'])
        innocentium_all_works[work.title] = [work.stats, str(datetime.utcfromtimestamp(int(work.published_time))), tags, (None != work.daily_deviation)]
    work_count -= 24
    offset_count += 24

file_path = 'innocentium.json'
with open(file_path, 'w') as json_file:
    json.dump(innocentium_all_works, json_file)

with open ('all_tags.json', 'w') as json_file:
    json.dump(dict(Counter(all_tags)), json_file)