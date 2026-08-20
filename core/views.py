from django.shortcuts import render
from django.http import JsonResponse

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

def home(request):
    return render(request, 'core/home.html', {'projets': PROJETS[:2]})

def about(request):
    return render(request, 'core/about.html', {'competences': COMPETENCES, 'valeurs': VALEURS})

def projets(request):
    return render(request, 'core/projets.html', {'projets': PROJETS})

def contact(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'ok', 'message': 'Message reçu ! Je vous réponds très vite.'})
    return render(request, 'core/contact.html')
