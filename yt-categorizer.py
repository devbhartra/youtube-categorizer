import requests
api_key = '<PLEASE ENTER YOUR API KEY HERE>'
DEVELOPER_KEY = api_key
# from apiclient.discovery import build

url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}"
while(True):
    inputURL = input("Enter the URL of the YouTube Video: ")
    videoID = inputURL.split("=", 1)
    _id = videoID[1]
    # print(_id)
    r = requests.get(url.format(id=_id, api_key=DEVELOPER_KEY))

    # print(r.json())
    # r = requests.get(url.format(id=_id, api_key=DEVELOPER_KEY))
    js = r.json()
    items = js["items"][0]
    # print(items["snippet"]["categoryId"])
    print(items["snippet"]["title"])
    cat = int(items["snippet"]["categoryId"])
    # print(cat)
    dictOfCategories = {
        2: "Autos & Vehicles",
        1: "Film & Animation",
        10: "Music",
        15: "Pets & Animals",
        17: "Sports",
        18: "Short Movies",
        19: "Travel & Events",
        20: "Gaming",
        21: "Videoblogging",
        22: "People & Blogs",
        23: "Comedy",
        24: "Entertainment",
        25: "News & Politics",
        26: "Howto & Style",
        27: "Education",
        28: "Science & Technology",
        29: "Nonprofits & Activism",
        30: "Movies",
        31: "Anime/Animation",
        32: "Action/Adventure",
        33: "Classics",
        34: "Comedy",
        35: "Documentary",
        36: "Drama",
        37: "Family",
        38: "Foreign",
        39: "Horror",
        40: "Sci-Fi/Fantasy",
        41: "Thriller",
        42: "Shorts",
        43: "Shows",
        44: " Trailers"
    }
    print(dictOfCategories[cat])
    choice = input("Once more? (y/n)")
    if choice == 'y':
        continue
    else:
        exit()
