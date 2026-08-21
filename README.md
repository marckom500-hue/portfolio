# Portfolio Marc-Axel KOM SILATCHOM — Django + Tailwind CSS

## 🚀 Lancer le projet en local

```bash
pip install -r requirements.txt
python manage.py runserver
```

Puis ouvrir : http://127.0.0.1:8000

## Déploiement sur Vercel

SQLite ne peut pas être utilisé comme base de production sur Vercel : le système de fichiers du déploiement est en lecture seule et éphémère. Connecter une base PostgreSQL (Neon, Supabase ou Vercel Postgres), puis ajouter ces variables d'environnement dans Vercel :

```text
DATABASE_URL=postgresql://...
# ou POSTGRES_URL selon le fournisseur
DJANGO_SECRET_KEY=une-cle-secrete-longue
DJANGO_DEBUG=False
```

Après la première installation, exécuter les migrations contre cette base distante :

```bash
python manage.py migrate
```

Créer ensuite un compte administrateur avec `python manage.py createsuperuser` et ajouter les articles depuis `/admin/`.

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
