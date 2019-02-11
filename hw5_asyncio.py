import aiohttp
import asyncio
import time
from urllib.request import urlopen


async def get_all_files(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        for link in downloadlinks:
            await downloader(session, link)


async def downloader(session, link):
    async with session.get(link) as response:
        filename = link.split('/')[-1]
        print('Downloading: ', filename)

        with open(filename, 'wb') as f_handle:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f_handle.write(chunk)
        return await response.release()


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

loop = asyncio.get_event_loop()
loop.run_until_complete(get_all_files(loop))
loop.close()

end = time.time()
dtime = end - start
print('Downloading time: ', dtime, ' seconds')
