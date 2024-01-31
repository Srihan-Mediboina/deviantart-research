import deviantart
from datetime import datetime
import json
from scrape import get_deviations
import pandas as pd
import matplotlib.pyplot as plt
import time

def n_stars_diff(url, da):
    
    all_works = {}
    all_works['title'] = []
    all_works['comments'] = []
    all_works['favourites'] = []
    all_works['published_date'] = []
    all_works['tags'] = []
    all_works['daily_deviation_status'] = []
    
    username = url.split('/')[-1]
    work_count = get_deviations(url)
    offset_count = 0
    
    while work_count > 0:
        #try:
        works = None
        try:
            works = da.get_gallery_folder(username=username, limit=24, offset=offset_count)
        except Exception as e:
            print("Erorr!", e)
            print("Pausing...")
            time.sleep(3600)
            print("Unpaused!")
            works = da.get_gallery_folder(username=username, limit=24, offset=offset_count)
        for work in works['results']:
            tags = []
                #try:
            #tag_data = da.get_deviation_metadata(work.deviationid)[0]['tags']
            #for tag in tag_data:
                #tags.append(tag['tag_name'])
                #except Exception as e:
                    #print("Error:", e)
                    #print("Pausing...")
                    #time.sleep(1200)
                    #print("Unpaused!")
            all_works['title'].append(work.title)
            all_works['comments'].append(work.stats['comments'])
            all_works['favourites'].append(work.stats['favourites'])
            all_works['published_date'].append(str(datetime.utcfromtimestamp(int(work.published_time))).split(' ')[0])
            all_works['tags'].append(tags)
            all_works['daily_deviation_status'].append((None != work.daily_deviation))
        work_count -= 24
        offset_count += 24
        #except Exception as e:
            #print("Erorr:", e)
            #print("Pausing...")
            #time.sleep(1200)
            #print("Unpaused!")
        
    df = pd.DataFrame(all_works)
    df = df.sort_values(by='published_date')
    
    n_star = (df['favourites'][0], 0)
    for i in range(1, len(df['favourites'])):
        if df['favourites'][i] > n_star[0]:
            n_star = (df['favourites'][i], i)
            
    n_doublestar = (df['favourites'][0], 0)
    for i in range(1, len(df['favourites'])):
        if df['favourites'][i] > n_doublestar[0] and i != n_star[1]:
            n_doublestar = (df['favourites'][i], i)
            
    return abs(n_star[1] - n_doublestar[1])