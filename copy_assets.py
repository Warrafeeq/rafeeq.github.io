import os
import shutil
from pathlib import Path

# Paths
jekyll_path = Path("../Warrafeeq.github.io")
django_path = Path(".")

def copy_assets():
    """Copy additional assets from Jekyll to Django"""
    
    # Copy CSS files if they exist
    jekyll_css = jekyll_path / "assets" / "css"
    django_css = django_path / "static" / "css"
    
    if jekyll_css.exists():
        for css_file in jekyll_css.glob("*.css"):
            shutil.copy2(css_file, django_css)
            print(f"Copied {css_file.name}")
    
    # Copy JavaScript files if they exist
    jekyll_js = jekyll_path / "assets" / "js"
    django_js = django_path / "static" / "js"
    
    if jekyll_js.exists():
        for js_file in jekyll_js.glob("*.js"):
            shutil.copy2(js_file, django_js)
            print(f"Copied {js_file.name}")
    
    # Copy PDF files to media
    jekyll_pdf = jekyll_path / "assets" / "pdf"
    django_media = django_path / "media" / "publications"
    django_media.mkdir(exist_ok=True)
    
    if jekyll_pdf.exists():
        for pdf_file in jekyll_pdf.glob("*.pdf"):
            shutil.copy2(pdf_file, django_media)
            print(f"Copied {pdf_file.name}")

if __name__ == "__main__":
    copy_assets()
    print("Asset copying completed!")