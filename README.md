# Personal Website Template

A clean, modern personal website template built with Flask and Python.

## Features

- Responsive design
- Social media links (GitHub, Twitter, LinkedIn, Email)
- Modern UI with smooth animations
- Easy to customize

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Update your social links in `app.py`
5. Add your profile picture to `static/img/profile.jpg`
6. Run the development server:
   ```bash
   python app.py
   ```

## Deployment

This application is configured to be deployed on platforms that support Python web applications (like Heroku, DigitalOcean, etc.).

1. Make sure you have the required dependencies installed
2. The application uses Gunicorn as the production server
3. Update your social links in `app.py`
4. Deploy using your preferred platform

## Customization

- Update the social links in `app.py`
- Modify the colors in `static/css/style.css`
- Update the profile picture in `static/img/profile.jpg`
- Edit the bio and name in `templates/index.html`
