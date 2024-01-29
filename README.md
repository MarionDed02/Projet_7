# Projet de scoring de crédit pour "Prêt à dépenser"

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
- Optimisation et validation du modèle : Utilisation de techniques comme Cross-Validation et GridsearchCV pour affiner le modèle.
- Surveillance de la performance en production: Utilisation de la librairie 'evidently' pour détecter le Data Drift.

## Livrables
- API de prédiction de score sur le cloud.
- Notebook Jupyter: De la modélisation au prétraitement et à la prédiction, intégrant MLFlow.
- Gestion du code et documentation: Via un outil de versioning et Github.
- Tableau HTML de Data Drift généré avec 'evidently'.
- Interface de test API: Réalisée via un Notebook ou une application Streamlit.
- Présentation de la soutenance: Incluant des éléments visuels et des liens vers les ressources clés.
