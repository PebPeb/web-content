import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="A simple Python script that generates a markdown template")
    parser.add_argument("--category", type=str, help="Category of the article (Post, Project)")
    parser.add_argument("--title", type=int, help="Title of post")

    args = parser.parse_args()          # Parse args from input
    category = args.category
    title = args.title

    if category is None:
        category = input("Enter article Category: ")
    if title is None:
        title = input("Enter article Title: ")

    with open(title.replace(' ','_') + '.md', "w") as file:
        file.write(generate_md(category, title))
    

def generate_md(category, title):
    date = (datetime.now()).strftime("%Y-%m-%d %H:%M")
    content = f"Title: {title}\nDate: {date}\nCategory: {category}\n\n"
    return content

if __name__ == "__main__":
    main()
