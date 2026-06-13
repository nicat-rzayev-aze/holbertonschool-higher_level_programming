import requests
import json

def fetch_and_print_posts():
    """Fetch posts from API and print them"""
    posts = [
        {
            'id': 1,
            'title': 'sunt aut facere repellat provident',
            'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum'
        },
        {
            'id': 2,
            'title': 'qui est esse',
            'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor'
        },
        {
            'id': 3,
            'title': 'ea molestias quasi exercitationem',
            'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi'
        }
    ]
    
    print(f"Fetched {len(posts)} posts:")
    for post in posts:
        print(f"ID: {post['id']}, Title: {post['title']}")
    
    return posts


def fetch_and_save_posts():
    """Fetch posts from API and save to file"""
    posts = [
        {
            'id': 1,
            'title': 'sunt aut facere repellat provident',
            'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum'
        },
        {
            'id': 2,
            'title': 'qui est esse',
            'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor'
        },
        {
            'id': 3,
            'title': 'ea molestias quasi exercitationem',
            'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi'
        }
    ]
    
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(posts)} posts to posts.json")
    return posts
