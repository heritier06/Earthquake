# Projet ETL & Visualisation des Séismes

Ce projet propose un pipeline ETL complet en Python pour extraire, transformer et charger des données sismiques mondiales (fournies par l'USGS), puis les visualiser sur une carte interactive Leaflet via une API Flask et une base MongoDB Atlas.

---

## 📦 Fonctionnalités

- 🔄 Pipeline ETL en Python
- ☁️ Stockage dans MongoDB Atlas
- 🧠 Structure prête pour MapReduce
- 🗺️ Carte interactive Leaflet :
  - Cercles proportionnels à la magnitude
  - Code couleur selon l’intensité
  - Filtre dynamique par magnitude

---

## 🗂️ Structure du projet

```
earthquake_etl_project/
├── etl/                     # Modules ETL
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── api/                     # Serveur Flask
│   ├── server.py
│   ├── static/
│   │   └── script.js        # Leaflet + filtre magnitude
│   └── templates/
│       └── index.html       # Interface HTML
│
├── config.py                # Configuration MongoDB et USGS
├── run_etl.py               # Lance le pipeline ETL
├── requirements.txt         # Dépendances Python
└── README.md
```

---

## 🚀 Démarrage rapide

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Configurer la base MongoDB

Dans `config.py`, remplis ton URI MongoDB Atlas :

```python
MONGO_URI = "mongodb+srv://<utilisateur>:<motdepasse>@cluster0.mongodb.net/?retryWrites=true&w=majority"
```

### 3. Exécuter le pipeline ETL

```bash
python run_etl.py
```

> Cela télécharge les derniers séismes mondiaux et les stocke dans ta base MongoDB.

### 4. Lancer le serveur Flask

```bash
python -m api.server
```

Puis ouvre ton navigateur sur 👉 http://localhost:5000

---

## 🗺️ Carte Leaflet interactive

- ✅ Cercles colorés :
  - **Vert** : < 3.0
  - **Orange** : 3.0 – 4.9
  - **Rouge** : 5.0 – 6.9
  - **Violet** : ≥ 7.0
- ✅ Slider pour filtrer par magnitude minimale

---

## 📚 Source des données

[API GeoJSON des séismes USGS](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)

---