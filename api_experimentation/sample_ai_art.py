import deviantart
import json
from datetime import datetime

da = deviantart.Api(29316, "4ed6af8f905b519e6e05f82247ee7dee")

ai_works = {}

work_count = 250
offset_count = 0

while work_count > 0:
    works = da.browse(endpoint='tags', tag='ai', limit=24, offset=offset_count)
    for work in works['results']:
        tag_data = da.get_deviation_metadata(work.deviationid)[0]['tags']
        tags = []
        for tag in tag_data:
            tags.append(tag['tag_name'])
        ai_works[work.title] = [work.stats, str(datetime.utcfromtimestamp(int(work.published_time))), tags, (None != work.daily_deviation)]
    
    work_count -= 24
    offset_count += 24

file_path = 'ai_works.json'
with open(file_path, 'w') as json_file:
    json.dump(ai_works, json_file)
