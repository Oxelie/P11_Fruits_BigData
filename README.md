# Projet 11 — Fruits! Chaîne de traitement Big Data

Stéphanie Duhem — Master AI Engineer — Juillet 2026

## Dépôt en deux temps

Ce dépôt est **partiel**, avec l'accord préalable de mon jury/évaluateur : le support de présentation (livrable n°3) n'est pas encore finalisé au moment de ce premier dépôt. Un second dépôt, regroupant l'ensemble des livrables (ceux ci-dessous + la présentation), sera effectué ce soir.

L'objectif de ce premier dépôt est de permettre à l'évaluateur de consulter dès maintenant le code et les preuves d'exécution cloud, sans attendre la finalisation du support.

## Contenu de ce dépôt

| Fichier | Description |
|---|---|
| `Duhem_Stephanie_1_notebook_local_072026.ipynb` | Chaîne de traitement PySpark complète, exécutée et validée en local (chargement, transfer learning MobileNetV2, broadcast des poids, featurisation, PCA distribuée, sauvegarde). |
| `Duhem_Stephanie_1_notebook_cloud_072026.ipynb` | Même chaîne de traitement, adaptée pour une exécution sur AWS EMR (chemins S3, région eu-north-1 conforme RGPD). |
| `Duhem_Stephanie_2_images_bucket_072026.png` | Capture d'écran du bucket S3 utilisé pour le stockage cloud. |
| `Duhem_Stephanie_2_images_contenu_bucket_072026.png` | Capture d'écran du contenu du bucket S3 (données et résultats). |
| `Duhem_Stephanie_2_images_echantillon_072026.png` | Capture d'écran de l'échantillon de données utilisé pour la démonstration. |
| `Duhem_Stephanie_00_requirements_072026.txt` | Dépendances Python du projet. |
| `Duhem_Stephanie_00_depot_git_072026.txt` | Lien vers le dépôt GitHub complet du projet (historique, scripts, documentation). |

## À venir dans le second dépôt (ce soir)

- `Duhem_Stephanie_3_presentation_072026` : support de présentation (briques d'architecture cloud, démarche de mise en œuvre, chaîne de traitement PySpark).
