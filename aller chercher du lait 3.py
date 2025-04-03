import pygame
import sys
import os  # Ajout pour vérifier la présence des fichiers

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur, hauteur = 1000, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mon Jeu")

# Couleur de fond
couleur_fond = (255, 255, 0)  # Jaune

# Chemins des images
image_path = "C:/Users/Vladimir/OneDrive - SUP DE VINCI/Bureau/cours/apprentissage python perso/aller chercher du lait 1/version 3/vache.jpg"
image_petite_path = "C:/Users/Vladimir/OneDrive - SUP DE VINCI/Bureau/cours/apprentissage python perso/aller chercher du lait 1/version 3/vache2.jpg"

# Vérification de la présence des fichiers avant de les charger
if not os.path.exists(image_path):
    print(f"Image non trouvée à l'emplacement : {image_path}")
    sys.exit()

if not os.path.exists(image_petite_path):
    print(f"Image non trouvée à l'emplacement : {image_petite_path}")
    sys.exit()

# Charger les images
image = pygame.image.load(image_path)
rect_vache = image.get_rect(topleft=(0, -100))

image_petite = pygame.image.load(image_petite_path)
rect_petite = image_petite.get_rect(center=(rect_vache.centerx, rect_vache.centery))  # Centre la petite image sur la vache

# Redimensionner la petite image (facteur 0.5)
image_petite = pygame.transform.scale(image_petite, (rect_petite.width // 3, rect_petite.height // 3))
rect_petite.width = image_petite.get_width()
rect_petite.height = image_petite.get_height()

# Déplacer la petite image (50 pixels vers la droite, 20 pixels vers le bas)
rect_petite.x += 500
rect_petite.y += 100

# Compteur
compteur = 0

# Initialisation du lait par clic
laitparclic = 1

# Créer la police pour afficher le compteur
police = pygame.font.Font(None, 36)

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Fermeture de la fenêtre.")
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clic détecté.")
            if rect_vache.collidepoint(event.pos):
                print("Clic sur la grande vache")
                compteur += laitparclic
            if rect_petite.collidepoint(event.pos):
                print("Clic sur la petite vache")
                if compteur >= 10:
                    laitparclic = 1 + laitparclic
                    compteur = compteur - 10
                else:
                    compteur = compteur

    # Afficher l'image et autres éléments
    fenetre.fill(couleur_fond)
    fenetre.blit(image, rect_vache)
    fenetre.blit(image_petite, rect_petite)

    # Afficher le compteur
    texte_compteur = police.render(f"Compteur : {compteur}", True, (255, 255, 255))
    fenetre.blit(texte_compteur, (10, 10))

    # Mettre à jour l'affichage
    pygame.display.flip()
