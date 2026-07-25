#!/bin/bash
# Bootstrap action EMR : installe les dépendances Python absentes de l'AMI EMR par défaut.
# pyspark, pandas, numpy, pyarrow sont déjà présents sur l'AMI EMR (Spark) — inutile de les réinstaller.
set -e
sudo pip3 install tensorflow pillow
