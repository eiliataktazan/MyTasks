from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=MARDIN\\SQLEXPRESS;DATABASE=practice;Trusted_Connection=yes;'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    features = db.relationship('Feature', backref='product', lazy=True, cascade="all, delete-orphan")

class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

with app.app_context():
    db.create_all()

    new_prod = Product(name="Smartphone")
    feat1 = Feature(key="Color", value="Black", product=new_prod)
    feat2 = Feature(key="Storage", value="128GB", product=new_prod)
    db.session.add(new_prod)
    db.session.commit()

    prod = Product.query.filter_by(name="Smartphone").first()
    print(f"Product: {prod.name}")
    for f in prod.features:
        print(f"Feature: {f.key} - {f.value}")

    feat_to_update = Feature.query.filter_by(product_id=prod.id, key="Color").first()
    feat_to_update.value = "Silver"
    db.session.commit()
    print(f"Updated: {feat_to_update.key} is now {feat_to_update.value}")

    db.session.delete(prod)
    db.session.commit()
    print("Deleted: Product and its features removed")