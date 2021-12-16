import feedparser


class MediaRssService:
    rss_flux_data = {}

    def get_rss_flux(self, link: str) -> feedparser.util.FeedParserDict:
        if link not in self.rss_flux_data:
            self.rss_flux_data[link] = feedparser.parse(link)

        return self.rss_flux_data[link]

    def get_rss_infos(self, link: str):
        return self.get_rss_flux(link).feed

    def get_rss_articles(self, link: str, start = 0, end = 3):
        return self.get_rss_flux(link).entries[start:end]
