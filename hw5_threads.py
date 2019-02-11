import shutil
import threading
import time
from urllib.request import urlopen


def downloader(link):
    filename = link.split('/')[-1]
    with urlopen(link) as response, open(filename, 'wb') as output_file:
        shutil.copyfileobj(response, output_file)
    print('Downloading: ', filename)


start = time.time()

url = 'https://python.org/downloads/source/'
downloadlinks = []

html = str(urlopen(url).read())
for i in range(len(html) - 3):
    if html[i] == '<' and html[i + 1] == 'a' and html[i + 2] == ' ':
        pos = html[i:].find('</a>')
        if ((html[i: i + pos + 4]).find('.tar.xz') != -1 or
                (html[i: i + pos + 4]).find('.tgz') != -1):
            downloadlinks.append((html[i: i + pos + 4]).split('"')[1])

threads = []
for link in downloadlinks:
    t = threading.Thread(target=downloader, args=(link,))
    threads.append(t)

for t in threads:
    t.start()
    t.join()

end = time.time()
dtime = end - start
print('Downloading time: ', dtime, ' seconds')
