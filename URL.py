#...........Recuperation des Url...........#
import requests
from bs4 import BeautifulSoup

# Liste pour stocker les URLs
urls = []

# .........................................#
for i in range(1, 5):

    #................. URL de la page..................
    url = f"https://www.vaticannews.va/fr/pape.html#{i}"

    # Envoi de la requête HTTP
    response = requests.get(url)

    # Vérification que la requête a réussi
    if response.status_code == 200:
        # Parsing du contenu HTML de la page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Recherche des éléments contenant les URLs des articles
        elements = soup.find_all('div', class_='article-url')

        # Ajout des URLs à la liste
        for element in elements:
            urls.append(element.get('href""'))

# Affichage des URLs récupérées
for url in urls:
    print(url)

    

        