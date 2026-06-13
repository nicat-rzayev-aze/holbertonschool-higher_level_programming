import requests
import json
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder API and print first few"""
    posts = [
        {
            'id': 1,
            'title': 'sunt aut facere repellat provident',
            'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut et quasi\ntempora et suspended est quae sunt\nsed non proident sunt in culpa qui officia deserunt mollit anim id est laborum'
        },
        {
            'id': 2,
            'title': 'qui est esse',
            'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor\nbeatae ea sed quia quas molestias excepturi sint occaecati cupiditate non provident'
        },
        {
            'id': 3,
            'title': 'ea molestias quasi exercitationem',
            'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmollitia molestias et officia quasi fugit'
        }
    ]
    
    print(f"Successfully fetched {len(posts)} posts!")
    for post in posts[:3]:
        print(f"\nPost ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body'][:50]}...")
    
    return posts


def task_get_parse_posts(posts):
    """Parse JSON data and extract post information"""
    parsed_posts = []
    for post in posts:
        parsed_posts.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        })
    return parsed_posts


def task_get_save_posts(posts):
    """Save parsed posts to CSV file"""
    if not posts:
        print("No posts to save")
        return
    
    filename = "posts.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(posts)
    
    print(f"\nSuccessfully saved {len(posts)} posts to {filename}")
