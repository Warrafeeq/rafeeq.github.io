from django.core.management.base import BaseCommand
from django.utils.text import slugify
import os
import re
from datetime import datetime
from pathlib import Path

from main.models import Profile, Education, Experience, Award, News
from blog.models import Post
from projects.models import Project
from publications.models import Publication

class Command(BaseCommand):
    help = 'Import data from Jekyll site'

    def add_arguments(self, parser):
        parser.add_argument(
            '--jekyll-path',
            type=str,
            default='../Warrafeeq.github.io',
            help='Path to Jekyll site directory'
        )

    def handle(self, *args, **options):
        jekyll_path = Path(options['jekyll_path'])
        
        if not jekyll_path.exists():
            self.stdout.write(
                self.style.ERROR(f'Jekyll path {jekyll_path} does not exist')
            )
            return

        self.stdout.write('Starting Jekyll data import...')
        
        # Import posts
        self.import_posts(jekyll_path)
        
        # Import projects
        self.import_projects(jekyll_path)
        
        self.stdout.write(
            self.style.SUCCESS('Successfully imported Jekyll data')
        )

    def import_posts(self, jekyll_path):
        """Import blog posts from Jekyll _posts directory"""
        posts_dir = jekyll_path / '_posts'
        if not posts_dir.exists():
            return

        for post_file in posts_dir.glob('*.md'):
            try:
                with open(post_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse front matter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        front_matter = parts[1]
                        post_content = parts[2].strip()
                        
                        # Extract metadata
                        title = self.extract_field(front_matter, 'title')
                        date_str = self.extract_field(front_matter, 'date')
                        description = self.extract_field(front_matter, 'description')
                        tags = self.extract_field(front_matter, 'tags')
                        categories = self.extract_field(front_matter, 'categories')
                        
                        if title:
                            slug = slugify(title)
                            
                            # Parse date
                            post_date = datetime.now()
                            if date_str:
                                try:
                                    post_date = datetime.strptime(date_str.split()[0], '%Y-%m-%d')
                                except:
                                    pass
                            
                            Post.objects.get_or_create(
                                slug=slug,
                                defaults={
                                    'title': title,
                                    'content': post_content,
                                    'description': description or '',
                                    'date': post_date,
                                    'tags': tags or '',
                                    'categories': categories or '',
                                }
                            )
                            self.stdout.write(f'Imported post: {title}')
                            
            except Exception as e:
                self.stdout.write(f'Error importing {post_file}: {e}')

    def import_projects(self, jekyll_path):
        """Import projects from Jekyll _projects directory"""
        projects_dir = jekyll_path / '_projects'
        if not projects_dir.exists():
            return

        for project_file in projects_dir.glob('*.md'):
            try:
                with open(project_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse front matter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        front_matter = parts[1]
                        project_content = parts[2].strip()
                        
                        # Extract metadata
                        title = self.extract_field(front_matter, 'title')
                        description = self.extract_field(front_matter, 'description')
                        category = self.extract_field(front_matter, 'category') or 'work'
                        importance = self.extract_field(front_matter, 'importance') or '1'
                        
                        if title:
                            try:
                                importance = int(importance)
                            except:
                                importance = 1
                                
                            Project.objects.get_or_create(
                                title=title,
                                defaults={
                                    'description': description or '',
                                    'content': project_content,
                                    'category': category,
                                    'importance': importance,
                                }
                            )
                            self.stdout.write(f'Imported project: {title}')
                            
            except Exception as e:
                self.stdout.write(f'Error importing {project_file}: {e}')

    def extract_field(self, front_matter, field_name):
        """Extract a field from YAML front matter"""
        pattern = rf'^{field_name}:\s*(.+)$'
        match = re.search(pattern, front_matter, re.MULTILINE)
        if match:
            value = match.group(1).strip()
            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            return value
        return None