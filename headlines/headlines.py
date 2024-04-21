import feedparser
import argparse
from pathlib import Path
from datetime import datetime,timedelta

parser = argparse.ArgumentParser(
    prog="headlines.py",
    description="Your News Today!",
    epilog="Created by Katherine Russell (https://github.com/KatRuss)"
)
parser.add_argument('-a','--add',dest='new_url',action='store')
parser.add_argument('-l','--limit',dest='limit',action='store')

args = parser.parse_args()

now = datetime.now()  
time_range = timedelta(days=1)  

directory = Path(__file__).parent.resolve()
urlPath = directory.joinpath("urls.txt")

if args.new_url:
    with open(urlPath,'a') as file:
        file.write('\n' + args.new_url)
        print(f"'{args.new_url}' has been added to the rss list.")
else:
    urls = []

    # Get all urls
    with open(urlPath,'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            urls.append(line.strip())

    # Get all the Headlines
    for url in urls:
        entry_int = 1
        feed = feedparser.parse(url)
        print(f"=== {(feed.feed.title).upper()} ===".center(16))
        print(f"{feed.feed.description} -> {feed.feed.link}".center(16))
        print("------------------------------------------".center(16))    
        for entry in feed.entries:
            if args.limit and entry_int > int(args.limit): # set limit for how many articles can be printed per feed. If there is no limit, just try to print everything.
                break
            else:
                entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")  
                if now - entry_date <= time_range: 
                    print(f"{entry_int}. {entry.title}")  
                    print("Published:", entry.published)  
                    print("Link:", entry.link)
                    print("..\n")
                    entry_int += 1


