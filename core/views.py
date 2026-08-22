from datetime import date
from types import SimpleNamespace

from django.http import Http404, JsonResponse
from django.shortcuts import render


def _localized(request, items, translations):
    """Return shallow copies with translated display fields when English is active."""
    if request.LANGUAGE_CODE != 'en':
        return items
    localized_items = []
    for index, item in enumerate(items, start=1):
        key = item.get('id', index) if isinstance(item, dict) else item.slug
        values = translations.get(key, {})
        if isinstance(item, dict):
            localized_items.append({**item, **values})
        else:
            localized_items.append(SimpleNamespace(**{**item.__dict__, **values}))
    return localized_items


ARTICLES = [
    SimpleNamespace(
        titre='Les étapes essentielles pour déployer Django',
        slug='deployer-django',
        extrait='Préparer une application Django pour un hébergement fiable.',
        contenu='Un déploiement Django doit utiliser des réglages de production.\n\nCommencez par protéger les variables secrètes, configurer les fichiers statiques et choisir un hébergement adapté. Vérifiez ensuite les migrations et les journaux avant de mettre le site en ligne.',
        image='images/article1.jpg',
        categorie='Django',
        date_publication=date(2026, 8, 20),
    ),
    SimpleNamespace(
        titre='Créer une interface web claire et efficace',
        slug='interface-web-claire-efficace',
        extrait='Quelques principes pour concevoir une expérience utilisateur simple et agréable.',
        contenu='Une bonne interface commence par une hiérarchie visuelle lisible.\n\nChaque écran doit guider l’utilisateur vers l’action principale, avec des espacements cohérents, des contrastes suffisants et une navigation prévisible sur mobile comme sur ordinateur.',
        image='images/article2.jpg',
        categorie='Design web',
        date_publication=date(2026, 8, 15),
    ),
    SimpleNamespace(
        titre='Pourquoi utiliser Git dans chaque projet',
        slug='pourquoi-utiliser-git',
        extrait='Git permet de suivre les évolutions d’un projet et de travailler avec méthode.',
        contenu='Git conserve l’historique du code et facilite les retours en arrière.\n\nDes commits courts et explicites rendent le travail plus lisible et permettent de déployer une version stable avec davantage de confiance.',
        image='images/article3.jpg',
        categorie='Développement',
        date_publication=date(2026, 8, 10),
    ),
]

PROJETS = [
    {
        'id': 1,
        'titre': 'Gestion de poulets de chair',
        'type': 'Projet personnel (terminé)',
        'description': "Application web complète de gestion d'inventaire avec entrées/sorties, alertes de seuil minimal, tableau de bord interactif et génération de rapports PDF.",
        'technos': ['PHP', 'MySQL','Blade' , 'Laravel'],
        'github': 'https://github.com/marckom500-hue/gestion-stock',
        'image': 'images/dash.jpeg',
        'icon': 'fa-boxes',
    },
    {
        'id': 2,
        'titre': 'Cabinet Dentaire — SMILE',
        'type': 'Projet personnel (terminé)',
        'description': "Logiciel complet de gestion pour cabinet dentaire. Gestion des patients, rendez-vous avec calendrier interactif, facturation, ordonnance et tableau de bord pour le praticien.",
        'technos': ['React', 'Vite', 'Tailwind CSS', 'Supabase'],
        'github': 'https://github.com/marckom500-hue/SMILE',
        'image': 'images/dashboard.jpg',
        'icon': 'fa-tooth',
    },
    {
        'id': 3,
        'titre': 'CHIC DECOR',
       'type': 'Projet réalisé pour une entreprise',
        'description': "Site web complet de l'entreprise MUSEE ZE MKWUING:CHIC DECOR",
        'technos': ['React', 'Vite', 'Tailwind CSS', 'Express'],
        'github': 'https://github.com/marckom500-hue/chic-decor',
        'image': 'images/dashchicdecor.png',
        'icon': 'fa-tooth',
    },
    {
        'id': 4,
        'titre': 'TFC SHOP',
       'type': 'Projet réalisé pour une entreprise',
        'description': "Site e-commerce complet pour TFC SHOP Cameroun",
        'technos': ['Next.js', 'Tailwind CSS'],
        'github': 'https://github.com/marckom500-hue/TFC-SHOP',
        'image': 'images/dashtfcshop.png',
        'icon': 'fa-tooth',
    },
       {
        'id': 5,
        'titre': 'BiblioGestion',
        'type': 'Projet réalisé dans le cadre academique',
        'description': "Application mobile de gestion de bibliothèque scolaire",
        'technos': ['Dart', 'Kotlin'],
        'github': 'https://github.com/marckom500-hue/bibliotheque_scolaire',
        'image': 'images/dashbiblio.jpg',
        'icon': 'fa-tooth',
    },
    {
        'id': 6,
        'titre': 'SOGECO-CONNECT',
        'type': 'Projet réalisé dans le cadre academique',
        'description': "Plateforme de gestion de stock multi-magasins avec rôles, signature électronique, traçabilité et un espace fournisseur intégré de SOGECO SARL dans la ville de Bafoussam",
       'technos': ['React', 'Vite', 'Tailwind CSS', 'React Context API', 'Lucide React', 'Recharts', 'PostCSS', 'Autoprefixer', 'Oxlint'],
        'github': 'https://github.com/marckom500-hue/sogeco-connect.git',
        'image': 'images/dashsogeco.png',
        'icon': 'fa-tooth',
    },

]

COMPETENCES = [
    {'nom': 'HTML / CSS', 'icon': 'fa-code', 'niveau': 90},
    {'nom': 'Tailwind CSS', 'icon': 'fa-wind', 'niveau': 80},
    {'nom': 'JavaScript', 'icon': 'fa-js', 'niveau': 75},
    {'nom': 'PHP / Laravel', 'icon': 'fa-php', 'niveau': 85},
    {'nom': 'Python / Django', 'icon': 'fa-python', 'niveau': 70},
    {'nom': 'MySQL / PostgreSQL', 'icon': 'fa-database', 'niveau': 80},
    {'nom': 'Git / GitHub', 'icon': 'fa-git-alt', 'niveau': 85},
    {'nom': 'Figma / Photoshop', 'icon': 'fa-figma', 'niveau': 70},
]

VALEURS = [
    {'titre': 'Rigueur', 'desc': "J'aborde chaque projet avec méthode et précision pour livrer un code propre et maintenable.", 'icon': 'fa-bullseye'},
    {'titre': 'Autonomie', 'desc': "Capable d'apprendre seul grâce aux projets, tutoriels et recherches pour monter en compétences rapidement.", 'icon': 'fa-rocket'},
    {'titre': 'Créativité', 'desc': "J'aime créer des interfaces propres, accessibles et esthétiques qui offrent une vraie expérience utilisateur.", 'icon': 'fa-lightbulb'},
]

PROJECT_TRANSLATIONS = {
    1: {'titre': 'Broiler Chicken Management', 'type': 'Personal project (completed)', 'description': 'Complete inventory management web application with stock entries/exits, minimum threshold alerts, interactive dashboard and PDF report generation.'},
    2: {'titre': 'Dental Clinic - SMILE', 'type': 'Personal project (completed)', 'description': 'Complete dental clinic management software with patient records, interactive appointment calendar, billing, prescriptions and practitioner dashboard.'},
        3: {'titre': 'CHIC DECOR', 'type': 'Project delivered for a company', 'description': 'Complete website for MUSEE ZE MKWUING: CHIC DECOR.'},
        4: {'titre': 'TFC SHOP', 'type': 'Project delivered for a company', 'description': 'Complete e-commerce website for TFC SHOP Cameroon.'},
        5: {'titre': 'BiblioGestion', 'type': 'Academic project', 'description': 'Mobile application for managing a school library.'},
        6: {'titre': 'SOGECO-CONNECT', 'type': 'Academic project', 'description': 'Multi-store inventory management platform with roles, electronic signature, traceability and an integrated supplier area for SOGECO SARL in Bafoussam.'},
}

VALUE_TRANSLATIONS = {
    1: {'titre': 'Rigor', 'desc': 'I approach every project with method and precision to deliver clean, maintainable code.'},
    2: {'titre': 'Independence', 'desc': 'I learn independently through projects, tutorials and research to build skills quickly.'},
    3: {'titre': 'Creativity', 'desc': 'I enjoy creating clean, accessible and attractive interfaces that offer a genuine user experience.'},
}

ARTICLE_TRANSLATIONS = {
    'deployer-django': {'titre': 'Essential steps for deploying Django', 'extrait': 'Preparing a Django application for reliable hosting.', 'contenu': 'A Django deployment should use production-ready settings.\n\nStart by protecting secret variables, configuring static files and choosing suitable hosting. Then check migrations and logs before putting the site online.', 'categorie': 'Django'},
    'interface-web-claire-efficace': {'titre': 'Creating a clear and effective web interface', 'extrait': 'A few principles for designing a simple and pleasant user experience.', 'contenu': 'A good interface starts with a clear visual hierarchy.\n\nEach screen should guide users toward the primary action, with consistent spacing, sufficient contrast and predictable navigation on mobile and desktop.', 'categorie': 'Web design'},
    'pourquoi-utiliser-git': {'titre': 'Why use Git in every project', 'extrait': 'Git tracks project changes and makes teamwork more disciplined.', 'contenu': 'Git preserves code history and makes it easy to roll back changes.\n\nShort, descriptive commits make work easier to understand and allow a stable version to be deployed with greater confidence.', 'categorie': 'Development'},
}

def home(request):
    projets = _localized(request, PROJETS[:2], PROJECT_TRANSLATIONS)
    return render(request, 'core/home.html', {'projets': projets})

def about(request):
    valeurs = _localized(request, VALEURS, VALUE_TRANSLATIONS)
    return render(request, 'core/about.html', {'competences': COMPETENCES, 'valeurs': valeurs})

def projets(request):
    return render(request, 'core/projets.html', {'projets': _localized(request, PROJETS, PROJECT_TRANSLATIONS)})

def contact(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'ok', 'message': 'Message reçu ! Je vous réponds très vite.'})
    return render(request, 'core/contact.html')

def blog(request):
    return render(request, 'core/blog.html', {'articles': _localized(request, ARTICLES, ARTICLE_TRANSLATIONS)})

def blog_detail(request, slug):
    article = next((article for article in ARTICLES if article.slug == slug), None)
    if article is None:
        raise Http404('Article introuvable')
    recents = [article for article in ARTICLES if article.slug != slug][:3]
    if request.LANGUAGE_CODE == 'en':
        article = _localized(request, [article], ARTICLE_TRANSLATIONS)[0]
        recents = _localized(request, recents, ARTICLE_TRANSLATIONS)
    return render(request, 'core/blog_detail.html', {'article': article, 'recents': recents})
