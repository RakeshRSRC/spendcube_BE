from main_app import db


class Vendor(db.Model):
    vendor_id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(200), unique=False, nullable=False)
    vendor_username = db.Column(db.String(200), unique=False, nullable=False)
    vendor_password = db.Column(db.String(200), unique=False, nullable=False)