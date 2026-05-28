from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {
        "title": "Morning Coffee",
        "content": "Nothing beats a strong coffee on a quiet morning."
    },
    2: {
        "title": "Weekend Plans",
        "content": "Thinking about going to the beach this weekend."
    },
    3: {
        "title": "Movie Night",
        "content": "Watched an amazing sci-fi movie yesterday."
    },
    4: {
        "title": "Favorite Food",
        "content": "Pizza will always be my comfort food."
    },
    5: {
        "title": "Gym Routine",
        "content": "Trying to stay consistent with workouts lately."
    },
    6: {
        "title": "Rainy Days",
        "content": "Rainy weather makes everything feel calmer."
    },
    7: {
        "title": "Music Playlist",
        "content": "Found a new playlist that's been on repeat all day."
    },
    8: {
        "title": "Travel Dreams",
        "content": "Would love to visit Japan someday."
    },
    9: {
        "title": "Gaming Session",
        "content": "Spent the whole evening playing online games with friends."
    },
    10: {
        "title": "Late Night Thoughts",
        "content": "Sometimes late nights are the most peaceful part of the day."
    }
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(id)

