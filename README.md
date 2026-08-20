# Portfolio Marc-Axel KOM SILATCHOM — Django + Tailwind CSS

## 🚀 Lancer le projet en local

```bash
pip install -r requirements.txt
python manage.py runserver
```

Puis ouvrir : http://127.0.0.1:8000

## 📁 Structure
```
portfolio/          # Config Django
core/
  views.py          # Données + vues
  urls.py
  templates/core/
    base.html       # Layout + Navbar + Footer
    home.html       # Page d'accueil
    about.html      # À propos + compétences
    projets.html    # Liste des projets
    contact.html    # Formulaire de contact
static/images/      # Votre photo
```

## 🌐 Déploiement sur Render 
1. Pusher sur GitHub
2. Nouveau "Web Service" sur render.com
3. Build command : `pip install -r requirements.txt`
4. Start command : `gunicorn portfolio.wsgi`
