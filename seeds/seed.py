import json
import os
import mongoengine
from warehouse.models import Product, Category
from django.utils.timezone import make_aware, is_naive
from datetime import datetime

mongoengine.disconnect() 
mongoengine.connect(db="New", host="mongodb://localhost:27017/")

def seed_categories():
    with open(os.path.join('seeds', 'category.json'))as f:
        data = json.load(f)
        for item in data:
            dt = datetime.fromisoformat(item['published_date'].replace("Z", "+00:00"))
            if is_naive(dt):
                dt = make_aware(dt)
            item['published_date']= dt
            Category(**item).save()
        print(f"Seeded {len(data)} categories.")

def seed_products():
    with open(os.path.join('seeds', 'product.json'))as f:
        data = json.load(f)
        for item in data:
            dt = datetime.fromisoformat(item['published_date'].replace("Z", "+00:00"))
            if is_naive(dt):
                dt = make_aware(dt)
            item['published_date']= dt
            
            Product(**item).save()
        print(f"Seeded {len(data)} products")

def run_seed_data():  # ✅ Use this in tests
    Product.drop_collection()
    Category.drop_collection()
    seed_categories()
    seed_products()


if __name__ =='__main__':
    run_seed_data()