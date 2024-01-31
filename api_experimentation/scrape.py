import requests
from bs4 import BeautifulSoup

def get_deviations(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

    specific_spans = soup.find_all('span', class_='_1thFP')

    if specific_spans[1].text.split(' ')[0][-1] == 'K':
        num = specific_spans[1].text.split(' ')[0].replace('.' , '')
        num = num[0 : len(num) - 1]
        return int(num + "00")

    else:
        return int(specific_spans[1].text.split(' ')[0])

animal_artists = ["https://www.deviantart.com/thrumyeye", 
"https://www.deviantart.com/innocentium",
 "https://www.deviantart.com/hadissima",
 "https://www.deviantart.com/sergey-ryzhkov",
 "https://www.deviantart.com/thunderi",
 "https://www.deviantart.com/arkus83",
 "https://www.deviantart.com/metalwolf13fh",
 "https://www.deviantart.com/v-k-photography",
 "https://www.deviantart.com/kristynakvapilova",
 "https://www.deviantart.com/glenn0o7",
 "https://www.deviantart.com/quiet-bliss",
 "https://www.deviantart.com/patricksworld",
 "https://www.deviantart.com/zwergloh",
 "https://www.deviantart.com/trablamonron",
 "https://www.deviantart.com/hoofbeatsnpawprints",
 "https://www.deviantart.com/sorance",
 "https://www.deviantart.com/roisabborrar",
 "https://www.deviantart.com/charlyjade",
 "https://www.deviantart.com/hiiakay",
 "https://www.deviantart.com/ducondona",
 "https://www.deviantart.com/monsterbrand",
 "https://www.deviantart.com/azph", 
 "https://www.deviantart.com/huskana"]

