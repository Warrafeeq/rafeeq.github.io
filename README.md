# Rafeeq Website - Django Portfolio

This is a Django-based portfolio website converted from the original Jekyll al-folio theme, preserving all the original data and functionality.

## Features

- **Profile Management**: Personal information, education, experience, and awards
- **Blog System**: Research insights and articles
- **Project Showcase**: Research and development projects
- **Publications**: Academic publications with BibTeX support
- **Responsive Design**: Bootstrap-based responsive layout
- **Admin Interface**: Django admin for content management

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Populate Data**:
   ```bash
   python populate_data.py
   ```

4. **Create Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Website**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

- `main/` - Profile, CV, and home page functionality
- `blog/` - Blog posts and articles
- `projects/` - Project showcase
- `publications/` - Academic publications
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, and images
- `media/` - User-uploaded files

## Data Migration

All data from the original Jekyll site has been preserved:
- Profile information from `_config.yml`
- CV data from `_data/cv.yml`
- Blog posts from `_posts/`
- Projects from `_projects/`
- Publications from `_bibliography/papers.bib`
- Static assets from `assets/`

## Admin Access

- Username: admin
- Password: admin123

## Customization

The website can be customized through:
- Django admin interface for content
- CSS files in `static/css/`
- Templates in `templates/`
- Models in each app's `models.py`