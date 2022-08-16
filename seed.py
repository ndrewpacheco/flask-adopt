from app import db
from models import Pet

db.drop_all()
db.create_all()

p1 = Pet(name="Jane", species="dog", available=True,
         photo_url="https://media.istockphoto.com/id/168819909/photo/british-shorthair-cat-in-front-of-blue-background.webp?s=612x612&w=is&k=20&c=fsjFK_RUmtsJ3C-PkVyAde64cqfV9BSbDuzNOxXI_rs=")
db.session.add(p1)


p2 = Pet(name="Libby", species="cat", available=False)

db.session.add(p2)
db.session.commit()
