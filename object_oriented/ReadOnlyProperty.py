# Readonly property and caching property value
import urllib.request
class WebPage:
    def __init__(self,url):
        self._url = url
        self._page_size = None
        self._time_in_secs = None

    @property
    def url(self):
        return self._url

    @property
    def page_size(self):
        if self._page_size is None:
            self.download()
        return self._page_size

    @property
    def time_in_secs(self):
        if self._time_in_secs is None:
            self.dowload()
        return self._time_in_secs

    def download(self):
        print("Page is downloading...")
        self._page_size = None
        self._time_in_secs = None
        import time
        start_time = time.perf_counter()
        with urllib.request.urlopen(self.url) as f:
            data = f.read()
        end_time = time.perf_counter()
        self._time_in_secs = end_time - start_time
        self._page_size= len(data)

urls = ['https://www.google.com','https://www.yahoo.co.in',"https://www.facebook.com"]
for url in urls:
    page = WebPage(url)
    print("accessing url - ",page.url)
    print("page size in bytes - ",page.page_size)
    print("time taken in seconds -",page.time_in_secs)
    print("============================================")