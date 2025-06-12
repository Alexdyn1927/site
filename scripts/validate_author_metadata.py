#!/usr/bin/env python3
import sys
import yaml
import os

def validate_author_metadata(file_path):
    """
    Validate author metadata in Jekyll post front matter
    
    Args:
        file_path (str): Path to the markdown file
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Extract front matter
        if not content.startswith('---'):
            return True  # No front matter, skip validation
        
        front_matter_end = content.find('---', 1)
        if front_matter_end == -1:
            print(f"Invalid front matter in {file_path}")
            return False
        
        front_matter_str = content[3:front_matter_end].strip()
        front_matter = yaml.safe_load(front_matter_str)
        
        # Check author metadata
        if 'author' in front_matter:
            author = front_matter['author']
            
            # Validate name
            if isinstance(author, dict) and 'name' in author:
                name = author['name']
                if not name or len(name) > 100:
                    print(f"Invalid author name in {file_path}: must be 1-100 characters")
                    return False
            
            # Optional additional validations can be added here
        
        return True
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Validate all markdown files in _posts directory
    posts_dir = '_posts'
    if not os.path.exists(posts_dir):
        print(f"No {posts_dir} directory found.")
        sys.exit(0)
    
    invalid_files = []
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md') or filename.endswith('.markdown'):
            file_path = os.path.join(posts_dir, filename)
            if not validate_author_metadata(file_path):
                invalid_files.append(file_path)
    
    if invalid_files:
        print("Invalid author metadata in the following files:")
        for file in invalid_files:
            print(f" - {file}")
        sys.exit(1)
    
    print("All post author metadata is valid.")
    sys.exit(0)

if __name__ == '__main__':
    main()