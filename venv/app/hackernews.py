import requests

HACKER_NEWS_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json"

def get_top_news(count=10):
    try:
        response = requests.get(HACKER_NEWS_URL)
        response.raise_for_status()
        top_story_ids = response.json()[:count]
        top_stories = []
        
        for story_id in top_story_ids:
            story = requests.get(ITEM_URL.format(id=story_id)).json()
            top_stories.append(story)
        
        return top_stories
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch top news", "details": str(e)}
