# Projet 11 — Fruits! Chaîne de traitement Big Data

Stéphanie Duhem — Master AI Engineer

Mise en place d'une chaîne de traitement Big Data (PySpark) pour la start-up Fruits! avec une architecture cloud AWS (S3, IAM, EMR).

## Structure du dépôt

- notebooks/
  - `00_projet_11.ipynb` — énoncé de la mission
  - `01_pipeline_local.ipynb` — chaîne de traitement complète (chargement, transfer learning MobileNetV2, broadcast des poids, featurisation, PCA distribuée), exécutée et validée en local
  - `02_pipeline_cloud.ipynb` — même chaîne de traitement, adaptée pour AWS EMR (chemins S3, région eu-north-1 conforme RGPD)
- scripts/
  - `prepare_sample.py` — génère l'échantillon local de développement (300 images, 10 classes)
  - `bootstrap_emr.sh` — script de bootstrap du cluster EMR
- documentation_presentation/
  - `presentation_projet.pptx.pdf` — présentation du projet complet
  - `schema_architecture_spark.svg` — schéma de l'architecture Spark 
  - `schema_pipeline_pyspark.svg` — schéma de la chaîne de traitement PySpark
- P8_Mode_opératoire/ — récupération du notebook et de la documentation de l'alternant
  - `P8_Notebook_Linux_EMR_PySpark_V1.0.ipynb` — travaux préliminaires de l'alternant 
  - `img/` — captures d'écran
- `requirements.txt` — dépendances Python
