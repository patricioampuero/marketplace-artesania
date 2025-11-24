from database import SessionLocal
import models

# Imágenes seguras generadas automáticamente con texto
productos_iniciales = [
    {
        "title": "Manta de lana de alpaca",
        "description": "Manta tejida en telar mapuche con lana de alpaca 100% natural. Colores tierra.",
        "price": 65000,
        "category": "Textil",
        "stock": 5,
        "image_url": "https://placehold.co/600x400/e67e22/white?text=Manta+Alpaca"
    },
    {
        "title": "Juego de Greda de Pomaire",
        "description": "Set de 6 platos de greda y una fuente. Ideal para pastel de choclo. Curado.",
        "price": 25000,
        "category": "Alfarería",
        "stock": 12,
        "image_url": "https://placehold.co/600x400/8e44ad/white?text=Greda+Pomaire"
    },
    {
        "title": "Aros de Lapislázuli y Plata",
        "description": "Joya de plata 950 con incrustaciones de lapislázuli chileno original.",
        "price": 35000,
        "category": "Orfebrería",
        "stock": 3,
        "image_url": "https://placehold.co/600x400/2980b9/white?text=Aros+Lapislazuli"
    },
    {
        "title": "Indio Pícaro de Madera",
        "description": "Clásica artesanía de madera tallada a mano. Souvenir típico de la zona sur.",
        "price": 8000,
        "category": "Madera",
        "stock": 20,
        "image_url": "https://placehold.co/600x400/27ae60/white?text=Indio+Picaro"
    },
    {
        "title": "Cestería en Crin de Rari",
        "description": "Mariposa decorativa tejida con crin de caballo teñido. Artesanía única en el mundo.",
        "price": 12000,
        "category": "Cestería",
        "stock": 8,
        "image_url": "https://placehold.co/600x400/c0392b/white?text=Crin+Rari"
    }
]

db = SessionLocal()
print("🌱 Reparando imágenes de los productos...")

try:
    for item in productos_iniciales:
        # Buscamos el producto
        producto_existente = db.query(models.Product).filter(models.Product.title == item["title"]).first()
        
        if producto_existente:
            # Si existe, LE ACTUALIZAMOS LA FOTO
            producto_existente.image_url = item["image_url"]
            print(f"   -> Foto arreglada: {item['title']}")
        else:
            # Si no existe, lo creamos
            nuevo = models.Product(**item)
            db.add(nuevo)
            print(f"   -> Creado nuevo: {item['title']}")

    db.commit()
    print("✅ ¡Tienda reparada! Ahora las fotos sí se verán.")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    db.close()