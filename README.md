# Jekyll Author Metadata Implementation

## Author Metadata Feature

This implementation adds a flexible author metadata system to Jekyll blog posts.

### Features
- Optional author information in post front matter
- Default site-wide author configuration
- Supports rich author metadata (name, bio, avatar, social links)

### Usage

#### In Post Front Matter
```yaml
---
layout: post
title: "Your Post Title"
author: 
  name: "Your Name"
  bio: "Optional author bio"
  avatar: "/path/to/avatar.jpg"
---
```

#### Default Author
If no author is specified, the site will use the default author from `_config.yml`.

### Configuration

Edit `_config.yml` to set default and additional author information:

```yaml
defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      author:
        name: "Site Default Author"
```

### Best Practices
- Always provide an author name or use site default
- Use consistent avatar image sizes
- Keep bios concise

### Compatibility
- Works with existing Jekyll posts
- Minimal configuration required