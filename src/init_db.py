import sqlite3

# Connect to (or create) the database file
# SQLite will create "catalog.db" in the same folder if it doesn't exist yet
connection = sqlite3.connect("catalog.db")

# A cursor lets us send SQL commands to the database
cursor = connection.cursor()

# Create the products table
# IF NOT EXISTS means running this script twice won't cause an error
cursor.execute("""
               CREATE TABLE IF NOT EXISTS products (
                                                       id          INTEGER PRIMARY KEY AUTOINCREMENT,
                                                       name        TEXT    NOT NULL,
                                                       description TEXT,
                                                       price       REAL    NOT NULL,
                                                       category    TEXT    NOT NULL,
                                                       image_url   TEXT
               )
               """)

# Add some sample Apple products so the app isn't empty on first run
sample_products = [
    ("iPhone 15 Pro", "A17 Pro chip, titanium design, 48MP camera system.", 999.99, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch-naturaltitanium?wid=200"),
    ("MacBook Air M3", "Supercharged by M3, up to 18 hours battery life.", 1099.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-midnight-select-20220606?wid=200"),
    ("iPad Pro 13\"", "The ultimate iPad experience with M4 chip.", 1299.00, "iPad",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipad-pro-finish-unselect-gallery-1-202405?wid=200"),
    ("Apple Watch Series 9", "Smarter. Brighter. Mightier.", 399.00, "Watch",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MR9A3ref_VW_34FR+watch-45-alum-midnight-nc-9s_VW_34FR_WF_CO?wid=200"),
    ("AirPods Pro (2nd gen)", "Adaptive Audio. Now in USB-C.", 249.00, "AirPods",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MQD83?wid=200"),

    ("Apple Vision Pro", "Revolutionary spatial computer with immersive experiences.", 3499.00, "Vision",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/vision-pro-gallery-1?wid=200"),

    ("Mac Mini M4", "Compact desktop powered by Apple Silicon.", 699.00, "Mac",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-202410?wid=200"),

    ("iPhone 16 Pro", "Next-generation iPhone with enhanced AI features.", 1199.00, "iPhone",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-16-pro-finish-select?wid=200"),

    ("Apple Watch Ultra 2", "The most rugged and capable Apple Watch.", 799.00, "Watch",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/watch-ultra-2?wid=200"),

    ("Magic Keyboard", "Wireless keyboard with Touch ID for Mac.", 199.00, "Accessories",
     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MK2A3?wid=200"),
]

cursor.executemany("""
                   INSERT INTO products (name, description, price, category, image_url)
                   VALUES (?, ?, ?, ?, ?)
                   """, sample_products)

# Save changes and close the connection
connection.commit()
connection.close()

print("Database created successfully!")
print("Table 'products' is ready with sample data.")
