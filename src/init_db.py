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
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR79BrGwdidUTdJjXTYdc7iJe7XlCcOqgKEWQ&s"),
    ("iPhone 16", "A18 chip, Camera Control, 48MP Fusion camera.", 799.00, "iPhone",
     "https://pngimg.com/uploads/iphone16/iphone16_PNG3.png"),
    ("iPhone 15 Pro", "A17 Pro chip, titanium design, 48MP camera system.", 999.00, "iPhone",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP6mkFtCHcnvG_55fRC912F9NAn-5YnQXztw&s"),
    ("iPhone 15", "Dynamic Island, 48MP camera, USB-C.", 699.00, "iPhone",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUZw2YHaftwvnUWKo4j93NQVwcGHbjYu5vqkzjCD-3ipIIllvCF6APujQ&s=10"),
    ("iPhone 14", "Crash Detection, Emergency SOS via satellite.", 599.00, "iPhone",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSm4kqfzVLqaFpryqim6shu9SgX4YPFyRc8sOyy9UuQ1A&s=10"),
    ("iPhone SE (3rd gen)", "A15 Bionic chip in a compact 4.7\" design.", 429.00, "iPhone",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPjVzSldqCT9P2SmztRWLE048k9Z4ze8Uec2C-S8XG_Q&s=10"),

    # Mac
    ("MacBook Pro 16\" M4", "M4 Pro chip, 24GB RAM, 512GB SSD, Liquid Retina XDR display.", 2499.00, "Mac",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpx-vhedhgUQ_FbHlKRPSVxvgLTAqPg3RmcA&s"),
    ("MacBook Pro 14\" M4", "M4 chip, 16GB RAM, up to 22 hours battery life.", 1599.00, "Mac",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpx-vhedhgUQ_FbHlKRPSVxvgLTAqPg3RmcA&s"),
    ("MacBook Air 15\" M3", "M3 chip, 15.3\" Liquid Retina display, up to 18 hours battery.", 1299.00, "Mac",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReLHKfFrMK9oQ5kbEwXGUH3UEqHKxxbZlv7g&s"),
    ("MacBook Air 13\" M3", "Supercharged by M3, fanless design, all-day battery life.", 1099.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-midnight-select-20220606?wid=400"),
    ("Mac mini M4", "Smallest Mac ever. M4 chip, 16GB RAM, Thunderbolt 4.", 599.00, "Mac",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Apple_Mac_Mini_M4.svg/960px-Apple_Mac_Mini_M4.svg.png"),

    # iPad
    ("iPad Pro 13\" M4", "Ultra Retina XDR OLED display, M4 chip, Apple Pencil Pro support.", 1299.00, "iPad",
     "https://www.bhphotovideo.com/images/fb/apple_mvx23ll_a_13_ipad_pro_wifi_1826781.jpg"),
    ("iPad Air 11\" M2", "M2 chip, 11\" Liquid Retina display, all-day battery.", 599.00, "iPad",
     "https://www.digimap.co.id/cdn/shop/files/iPad_Air_11_M2_WiFi_Space_Gray_PDP_Image_Position_1b__GBEN_3d6194a5-82ff-4098-98ff-489b44c2acdc.jpg?v=1721801486&width=823"),
    ("iPad mini (7th gen)", "A17 Pro chip in a compact 8.3\" design, Apple Pencil Pro.", 499.00, "iPad",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMCTXCbUZE4LkBn0klu7QVV_DbGjlb2q6zIA&s"),

    # Watch
    ("Apple Watch Ultra 2", "Titanium case, up to 60 hours battery, built for extreme adventure.", 799.00, "Watch",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkaCD5YFV1MxY2FVVJwkaYipHelWyqSzbO1A&s"),
    ("Apple Watch Series 10", "Thinnest Apple Watch ever, faster charging, sleep apnea detection.", 399.00, "Watch",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOSqVH9nCoJspq2t3Gr4yHEsvIs4ahpJMxQw&s"),
    ("Apple Watch SE (2nd gen)", "The essential Apple Watch. Affordable, powerful, safe.", 249.00, "Watch",
     "https://cdsassets.apple.com/live/SZLF0YNV/images/sp/112022_cer-white.jpg"),

    # AirPods
    ("AirPods Pro (2nd gen)", "Adaptive Audio, Active Noise Cancellation, USB-C.", 249.00, "AirPods",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MQD83?wid=400"),
    ("AirPods 4", "Active Noise Cancellation, personalised Spatial Audio, USB-C.", 129.00, "AirPods",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/airpods-4-select-202409?wid=400"),
    ("AirPods Max (USB-C)", "Over-ear headphones, high-fidelity audio, Adaptive Transparency.", 549.00, "AirPods",
     "https://www.istore.com.ng/cdn/shop/files/airpods_max_2024_midnight_pdp_image_position_03__wwenLarge_1200x.png?v=1728578891"),

    # Accessories
    ("Apple TV 4K (3rd gen)", "A15 Bionic chip, 4K HDR, Dolby Atmos, Wi-Fi 6E.", 129.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/apple-tv-4k-hero-select-202210?wid=400"),
    ("HomePod (2nd gen)", "Breakthrough sound, S7 chip, Matter smart home hub.", 299.00, "Accessories",
     "https://www.dxomark.com/wp-content/uploads/medias/post-144016/Apple-HomePod_2nd-Gen_featured-image-packshot-review.jpg"),
    ("HomePod mini", "Room-filling sound in a small package, smart home hub.", 99.00, "Accessories",
     "https://www.assistivetech.com.au/cdn/shop/files/homepod_white.png?v=1772790147"),
    ("Apple Pencil Pro", "Find My, squeeze gesture, barrel roll, magnetic charging.", 129.00, "Accessories",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7vBxb7MfZBLZTRs4go4xiZlPuCktoDuwDnKX6yj7t7A&s"),
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