import yaml
from collections import Counter
import os

os.chdir('/home/user/Code/AI-Enthusiast.github.io/')
print(os.getcwd())

# Load the YAML file
with open('_data/projects.yml', 'r') as file:
    projects = yaml.safe_load(file)

# Initialize a Counter to count tags
tag_counter = Counter()

# Iterate through the projects and count tags
for project in projects:
    tags = project.get('tags', [])
    tag_counter.update(tags)

# Print the tag counts
for tag, count in tag_counter.items():
    print(f'{tag}: {count}')