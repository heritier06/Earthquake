from etl.extract import fetch_earthquake_data
from etl.transform import transform_data
from etl.load import load_to_mongodb

def run_etl():
    raw_data = fetch_earthquake_data()
    print("✅ Données extraites")

    cleaned_data = transform_data(raw_data)
    print(f"✅ {len(cleaned_data)} enregistrements nettoyés")

    load_to_mongodb(cleaned_data)
    print("✅ Données chargées dans MongoDB Atlas")