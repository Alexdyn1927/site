import os
import re

def update_post_frontmatter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Regex to handle front matter parsing
    front_matter_match = re.match(r'^---\n(.*?\n)---', content, re.DOTALL)
    
    if front_matter_match:
        front_matter = front_matter_match.group(1)
        
        # Check if author is already present
        if 'author:' not in front_matter:
            # Add author line
            updated_front_matter = front_matter.rstrip() + '\nauthor: Anonymous\n'
            
            # Replace the original front matter
            updated_content = re.sub(
                r'^---\n.*?---', 
                f'---\n{updated_front_matter}---', 
                content, 
                flags=re.DOTALL
            )
            
            with open(file_path, 'w') as f:
                f.write(updated_content)
            print(f"Updated {file_path} with default author")

def main():
    posts_dir = '_posts'
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(posts_dir, filename)
            update_post_frontmatter(file_path)

if __name__ == '__main__':
    main()