


class UrlManager(object):
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_url) != 0

    def get_new_url(self):
        new_url = self.new_url.pop()
        self.old_url.add(new_url)
        return new_url