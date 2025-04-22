# Personal Website Template

A clean, modern personal website template built with Flask and Python. Perfect for showcasing your social media links and professional profile.

## 🚀 Quick Start

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python app.py
   ```

## 🛠️ Customization

1. Update your social links in `app.py`
2. Add your profile picture to `static/img/profile.jpg`
3. Edit your name and bio in `templates/index.html`
4. Customize colors in `static/css/style.css`

## 🌐 Deployment

The application is configured for production deployment with Gunicorn. Deploy to any platform that supports Python web applications (Heroku, DigitalOcean, etc.).

## 📦 Dependencies

- Flask 3.0.2
- Gunicorn 21.2.0
- python-dotenv 1.0.1
