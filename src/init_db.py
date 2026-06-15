import sqlite3

connection = sqlite3.connect("catalog.db")
cursor = connection.cursor()

# Удаляем старую таблицу и создаём заново — чистый старт
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("""
               CREATE TABLE products (
                                         id          INTEGER PRIMARY KEY AUTOINCREMENT,
                                         name        TEXT    NOT NULL,
                                         description TEXT,
                                         price       REAL    NOT NULL,
                                         category    TEXT    NOT NULL,
                                         image_url   TEXT
               )
               """)

sample_products = [

    # iPhone
    ("iPhone 16 Pro Max", "A18 Pro chip, 5x optical zoom, titanium design, 6.9\" display.", 1199.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-16-pro-finish-select-202409-6-9inch-deserttitanium?wid=400"),
    ("iPhone 16", "A18 chip, Camera Control, 48MP Fusion camera.", 799.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-16-finish-select-202409-6-1inch-black?wid=400"),
    ("iPhone 15 Pro", "A17 Pro chip, titanium design, 48MP camera system.", 999.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=400"),
    ("iPhone 15", "Dynamic Island, 48MP camera, USB-C.", 699.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-finish-select-202309-6-1inch-black?wid=400"),
    ("iPhone 14", "Crash Detection, Emergency SOS via satellite.", 599.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-finish-select-202209-6-1inch-midnight?wid=400"),
    ("iPhone SE (3rd gen)", "A15 Bionic chip in a compact 4.7\" design.", 429.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-se-finish-select-202203-midnight?wid=400"),

    # Mac
    ("MacBook Pro 16\" M4", "M4 Pro chip, 24GB RAM, 512GB SSD, Liquid Retina XDR display.", 2499.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp16-spaceblack-select-202410?wid=400"),
    ("MacBook Pro 14\" M4", "M4 chip, 16GB RAM, up to 22 hours battery life.", 1599.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp14-spaceblack-select-202410?wid=400"),
    ("MacBook Air 15\" M3", "M3 chip, 15.3\" Liquid Retina display, up to 18 hours battery.", 1299.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-15-midnight-select-20230606?wid=400"),
    ("MacBook Air 13\" M3", "Supercharged by M3, fanless design, all-day battery life.", 1099.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-midnight-select-20220606?wid=400"),
    ("Mac mini M4", "Smallest Mac ever. M4 chip, 16GB RAM, Thunderbolt 4.", 599.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-202410?wid=400"),

    # iPad
    ("iPad Pro 13\" M4", "Ultra Retina XDR OLED display, M4 chip, Apple Pencil Pro support.", 1299.00, "iPad",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipad-pro-finish-unselect-gallery-1-202405?wid=400"),
    ("iPad Air 11\" M2", "M2 chip, 11\" Liquid Retina display, all-day battery.", 599.00, "iPad",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipad-air-finish-unselect-gallery-1-202405?wid=400"),
    ("iPad mini (7th gen)", "A17 Pro chip in a compact 8.3\" design, Apple Pencil Pro.", 499.00, "iPad",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipad-mini-finish-unselect-gallery-1-202409?wid=400"),

    # Watch
    ("Apple Watch Ultra 2", "Titanium case, up to 60 hours battery, built for extreme adventure.", 799.00, "Watch",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/watch-ultra2-titanium-select-202309?wid=400"),
    ("Apple Watch Series 10", "Thinnest Apple Watch ever, faster charging, sleep apnea detection.", 399.00, "Watch",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/watch-s10-aluminum-jetblack-select-202409?wid=400"),
    ("Apple Watch SE (2nd gen)", "The essential Apple Watch. Affordable, powerful, safe.", 249.00, "Watch",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/watch-se-aluminum-midnight-select-202309?wid=400"),

    # AirPods
    ("AirPods Pro (2nd gen)", "Adaptive Audio, Active Noise Cancellation, USB-C.", 249.00, "AirPods",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MQD83?wid=400"),
    ("AirPods 4", "Active Noise Cancellation, personalised Spatial Audio, USB-C.", 129.00, "AirPods",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/airpods-4-select-202409?wid=400"),
    ("AirPods Max (USB-C)", "Over-ear headphones, high-fidelity audio, Adaptive Transparency.", 549.00, "AirPods",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/airpods-max-select-midnight-202409?wid=400"),

    # Accessories
    ("Apple TV 4K (3rd gen)", "A15 Bionic chip, 4K HDR, Dolby Atmos, Wi-Fi 6E.", 129.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/apple-tv-4k-hero-select-202210?wid=400"),
    ("HomePod (2nd gen)", "Breakthrough sound, S7 chip, Matter smart home hub.", 299.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/homepod-select-202301-midnight?wid=400"),
    ("HomePod mini", "Room-filling sound in a small package, smart home hub.", 99.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/homepod-mini-select-yellow-202110?wid=400"),
    ("Apple Pencil Pro", "Find My, squeeze gesture, barrel roll, magnetic charging.", 129.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/apple-pencil-pro-select-202405?wid=400"),
    ("Magic Keyboard with Touch ID", "Wireless keyboard with Touch ID and numeric keypad.", 179.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MK2C3?wid=400"),
]

cursor.executemany("""
                   INSERT INTO products (name, description, price, category, image_url)
                   VALUES (?, ?, ?, ?, ?)
                   """, sample_products)

connection.commit()
connection.close()

print(f"Database created successfully with {len(sample_products)} products!")