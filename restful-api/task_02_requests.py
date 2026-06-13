from task_02 import fetch_and_print_posts, task_get_parse_posts, task_get_save_posts

print("=== Fetching posts from API ===")
posts = fetch_and_print_posts()

if posts:
    print("\n=== Parsing posts ===")
    parsed_posts = task_get_parse_posts(posts)
    print(f"Parsed {len(parsed_posts)} posts")

    print("\n=== Saving to CSV ===")
    task_get_save_posts(parsed_posts)
