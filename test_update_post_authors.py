import os
import re
import unittest
from update_post_authors import update_post_frontmatter

class TestPostAuthorUpdate(unittest.TestCase):
    def setUp(self):
        # Create a temporary test markdown file
        self.test_file = '_posts/test_post.md'
        with open(self.test_file, 'w') as f:
            f.write('''---
layout: post
title: Test Post
date: 2024-01-01
---
Test content''')
    
    def test_update_frontmatter(self):
        update_post_frontmatter(self.test_file)
        
        # Read the updated file
        with open(self.test_file, 'r') as f:
            content = f.read()
        
        # Use regex to parse front matter
        front_matter_match = re.match(r'^---\n(.*?\n)---', content, re.DOTALL)
        self.assertIsNotNone(front_matter_match)
        
        front_matter = front_matter_match.group(1)
        
        # Check author is added
        self.assertIn('author: Anonymous', front_matter)
    
    def tearDown(self):
        # Remove test file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()