# FAQ Management System

## Features
- Multi-language FAQ support (English, Hindi, Bengali)
- WYSIWYG editor for answers
- Automated translations using Google Translate
- Redis-based caching
- REST API with language parameter support

## Installation
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run Redis: `redis-server`
4. Migrate database: `python manage.py migrate`
5. Run server: `python manage.py runserver`

## API Usage
- Get all FAQs: `GET /api/faqs/`
- Filter by language: `GET /api/faqs/?lang=hi`

## Admin Interface
Access `/admin` and manage FAQs with rich text editing.

## Testing
Run tests with: `python manage.py test`
