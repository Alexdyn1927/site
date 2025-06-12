import os
import re

def update_post_frontmatter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if author is already present
    if 'author:' not in content:
        # Insert author just after the first line with '---'
        lines = content.split('\n')
        frontmatter_end_index = lines.index('---', 1)
        lines.insert(frontmatter_end_index, 'author: Anonymous')
        
        updated_content = '\n'.join(lines)
        
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