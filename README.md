# Projet de scoring de crédit pour "Prêt à dépenser"

![Image d'illustration](https://github.com/MarionDed02/Projet_7/raw/main/16794938722698_Data_Scientist-P7-01-banner.png)

## Introduction
Dans le monde de la finance, l'octroi de crédits à la consommation représente un défi majeur, surtout pour les clients ayant peu ou pas d'historique de crédit. Notre entreprise, "Prêt à dépenser", se lance dans le développement d'un outil innovant de scoring crédit afin de répondre à cette problématique. Ce projet vise à construire un modèle prédictif efficace, permettant d'évaluer la probabilité de remboursement d'un crédit par un client.

## Objectifs
1. **Développement d'un algorithme de classification :** Utilisation de diverses sources de données pour construire un modèle de scoring précis.
2. **Analyse de l'importance des features :** Comprendre quels facteurs influencent le plus les prédictions du modèle, tant au niveau global que local.
3. **Mise en production et interface API :** Déployer le modèle de scoring via une API et créer une interface pour tester cette API.
4. **Approche MLOps globale :** Mettre en place un processus complet de MLOps, allant du suivi des expérimentations à l'analyse du data drift en production.

## Stratégie et Outils
- Utilisation de Kernels Kaggle pour l'analyse exploratoire, la préparation des données, et le feature engineering.
- MLOps et outils open source: Incorporation de MLFlow pour le tracking d'expériences, la gestion des modèles, et le serving. Utilisation de Git pour la gestion de version et de Github pour l'intégration et le déploiement continus, en plus de Pytest pour les tests unitaires.
- Prise en compte du déséquilibre des données : Importance de considérer le déséquilibre entre les bons et les mauvais clients ainsi que les coûts associés aux faux négatifs et faux positifs.
- Optimisation et validation du modèle : Utilisation de techniques comme Cross-Validation et RandomSearchCV pour affiner le modèle.
- Surveillance de la performance en production: Utilisation de la librairie 'evidently' pour détecter le Data Drift.

## Livrables
- Lien de l'application Streamlit déployée sur le cloud via Heroku : https://fierce-everglades-55385-d1cc166ae1d0.herokuapp.com
- Notebooks Jupyter: Du prétraitement et à la modélisation, intégrant MLFlow.
- Gestion du code et documentation: Via Git et Github.
- Tableau HTML de Data Drift généré avec 'evidently'.
- Présentation de la soutenance: Incluant des éléments visuels et des liens vers les ressources clés.

---

## Contenu du Repository

## Analyse exploratoire des données (EDA) & Modélisation

- **Dedieu_Marion_1_EDA_preprocessing_012024.ipynb** : Notebook Jupyter pour l'analyse exploratoire des données et le prétraitement.
- **Dedieu_Marion_2_modelisation_012024.ipynb** : Notebook Jupyter pour la modélisation et la construction du modèle.
- **saved_model/** : Répertoire contenant le modèle pré-entraîné utilisé pour le scoring des clients.
- **scoring_model/** : Répertoire contenant les enregistrements MLflow pour le suivi et la gestion des modèles.

## Tableau de bord intéractif (Streamlit)

- **preprocessing.py** : Script Python contenant les fonctions de prétraitement des données.
- **dashboard.py** : Code source du tableau de bord interactif développé avec Streamlit.
- **df_dashboard_final.csv** : Données finales à afficher dans le tableau de bord.
- **df_feature_importance_25.csv** : Fichier contenant l'importance des variables pour la modélisation.
- **logo.jpg** : Logo utilisé dans le tableau de bord ou la documentation.
- **test_dashboard.py** : Script de test Pytest pour le tableau de bord.

## Data Drift

- **datadrift.py** : Script Python pour l'analyse et la détection du Data Drift entre les jeux de données.
- **Datadrift_report.html** : Rapport HTML généré pour l'analyse du Data Drift.

## Configuration et Déploiement

- **Procfile** : Fichier nécessaire pour le déploiement de l'application sur Heroku.
- **requirements.txt** : Liste des dépendances Python nécessaires pour exécuter le projet.
- **runtime.txt** : Spécification de la version de Python utilisée dans le projet.
- **setup.sh** : Script de configuration nécessaire pour le déploiement sur Heroku.

## Ressources supplémentaires

- **16794938722698_Data_Scientist-P7-01-banner.png** : Image utilisée dans la documentation.
- **README.md** : Fichier présentant le contenu et l'utilisation du repository.
