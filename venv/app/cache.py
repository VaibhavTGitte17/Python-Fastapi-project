from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=600)  # Cache up to 100 items for 10 minutes

@cached(cache)
def get_cached_top_news(count):
    from .hackernews import get_top_news
    return get_top_news(count)
