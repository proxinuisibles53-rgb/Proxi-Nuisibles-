# -*- coding: utf-8 -*-
"""Fabrique les images de partage (1200x630, JPEG) à partir des médias du site.

Ces images ne servent qu'aux aperçus de lien sur Facebook, WhatsApp, LinkedIn
et X. Elles ne sont jamais affichées sur le site lui-même : ce format est
imposé par les réseaux, et le JPEG est le seul que tous savent lire.

À relancer après l'ajout d'un média : python3 partage.py
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

MEDIA = "/home/claude/assets/media"
ASSETS = "/home/claude/assets"
SORTIE = "/home/claude/assets/partage"
L, H = 1200, 630

ORANGE = (255, 133, 27)
SOMBRE = (36, 38, 26)
BLANC = (255, 255, 255)

F_TITRE = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
F_TEXTE = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"

# fichier source, nom de sortie, titre, sous-titre
VISUELS = [
    ("frelons-nid-primaire-poster.webp", "frelons", "Frelons et guêpes",
     "Destruction de nids · Mayenne et Ille-et-Vilaine"),
    ("deratisation-rats-poster.webp", "deratisation", "Dératisation",
     "Rats et souris · particuliers, commerces, syndics"),
    ("punaises-lit-reelle-poster.webp", "punaises", "Punaises de lit",
     "Traitement thermique · Mayenne et Ille-et-Vilaine"),
    ("chenilles-nid-pin.webp", "chenilles", "Chenilles processionnaires",
     "Échenillage et écopièges · de novembre à février"),
    ("desinsectisation-fourmis-poster.webp", "desinsectisation", "Désinsectisation",
     "Cafards, puces, fourmis, mouches"),
    ("depigeonnage-pigeons-toit-poster.webp", "depigeonnage", "Dépigeonnage",
     "Protection des bâtiments · pose de dispositifs"),
    ("taupinieres-prairie.webp", "taupes", "Taupes et nuisibles des jardins",
     "Piégeur agréé · Mayenne et Ille-et-Vilaine"),
    ("piegeage-ragondin-poster.webp", "piegeage", "Piégeage agréé",
     "Ragondins, fouines, nuisibles classés"),
    ("badigeon-mouches.webp", "mouches", "Mouches",
     "Badigeon intérieur · actif de mai à décembre"),
    ("contrat-deratisation-pro.webp", "professionnels", "Métiers de bouche",
     "Contrats de 1 à 12 passages · registre HACCP"),
    ("gwendal-portrait.webp", "qui-suis-je", "Gwendal, votre technicien",
     "Indépendant depuis 2024 · dans le métier depuis 2016"),
    ("gwendal-intervention.webp", "defaut", "Proxinuisibles",
     "Dératisation, désinsectisation, frelons · Mayenne et Ille-et-Vilaine"),
    ("gwendal-salon.webp", "debarras", "Débarras",
     "Maison, cave, grenier · nuisibles traités dans le même passage"),
]


def cadrer(im, l, h):
    """Recadre en couvrant la zone, sans déformer."""
    im = im.convert("RGB")
    r = max(l / im.width, h / im.height)
    n = im.resize((max(l, int(im.width * r + .5)), max(h, int(im.height * r + .5))),
                  Image.LANCZOS)
    if r > 1.3:  # source modeste : on rattrape un peu de netteté
        n = n.filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=3))
    x = (n.width - l) // 2
    y = int((n.height - h) * 0.35)  # un peu au-dessus du centre : les visages
    return n.crop((x, y, x + l, y + h))


def voile(im):
    """Assombrit le bas pour le texte, et le haut pour que le logo ressorte
    même sur un ciel clair."""
    v = Image.new("L", (1, H))
    for y in range(H):
        t = y / H
        bas = min(1, max(0, (t - 0.25) / 0.75) ** 1.4 * 0.92)
        haut = max(0, (0.24 - t) / 0.24) ** 1.2 * 0.62
        v.putpixel((0, y), int(255 * max(bas, haut)))
    masque = v.resize((L, H))
    noir = Image.new("RGB", (L, H), SOMBRE)
    return Image.composite(noir, im, masque)


def couper(d, texte, police, large):
    mots, lignes, cur = texte.split(), [], ""
    for m in mots:
        essai = (cur + " " + m).strip()
        if d.textlength(essai, font=police) <= large:
            cur = essai
        else:
            if cur:
                lignes.append(cur)
            cur = m
    if cur:
        lignes.append(cur)
    return lignes


def fabriquer(source, nom, titre, sous_titre):
    chemin = os.path.join(MEDIA, source)
    if not os.path.exists(chemin):
        print("  manquant :", source)
        return None
    im = voile(cadrer(Image.open(chemin), L, H))
    d = ImageDraw.Draw(im)

    # bande orange en pied
    d.rectangle([0, H - 12, L, H], fill=ORANGE)

    marge = 64
    f_t = ImageFont.truetype(F_TITRE, 62)
    f_s = ImageFont.truetype(F_TEXTE, 30)
    lignes = couper(d, titre, f_t, L - 2 * marge)
    y = H - 60 - 38 - len(lignes) * 74
    for ligne in lignes:
        d.text((marge, y), ligne, font=f_t, fill=BLANC)
        y += 74
    d.text((marge, y + 6), sous_titre, font=f_s, fill=(238, 232, 214))

    # logo en haut à gauche
    logo = Image.open(os.path.join(ASSETS, "logo.webp")).convert("RGBA")
    logo.thumbnail((999, 96), Image.LANCZOS)
    texte = Image.open(os.path.join(ASSETS, "logo-texte.webp")).convert("RGBA")
    texte.thumbnail((999, 70), Image.LANCZOS)
    im.paste(logo, (marge, 42), logo)
    im.paste(texte, (marge + logo.width + 16, 42 + (logo.height - texte.height) // 2), texte)

    os.makedirs(SORTIE, exist_ok=True)
    dest = os.path.join(SORTIE, "og-%s.jpg" % nom)
    im.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
    return dest


if __name__ == "__main__":
    total = 0
    for src, nom, titre, st in VISUELS:
        dest = fabriquer(src, nom, titre, st)
        if dest:
            ko = os.path.getsize(dest) / 1024
            total += ko
            print("  %-26s %6.0f ko" % (os.path.basename(dest), ko))
    print("%d visuels, %.0f ko au total" % (len(os.listdir(SORTIE)), total))
