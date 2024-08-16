from fastapi import FastAPI, Query
from .cache import get_cached_top_news

app = FastAPI()

@app.get("/top-news")
async def top_news(count: int = Query(10, description="Number of top news items to return")):
    return get_cached_top_news(count)
