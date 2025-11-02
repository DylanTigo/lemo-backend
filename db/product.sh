# Produit 1: Laptop Pro 15 (ID: LAP-001)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Laptop professionnel haut de gamme",
  "price": 780000,
  "model": "Pro 15",
  "condition": 10,
  "stock_quantity": 40,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "LAP-001",
  "image_urls": ["url_laptop_pro15_1.jpg"],
  "brand_id": 1,
  "category_id": 3,
  "attributes": [
    {"attribute_id": 2, "value": "Intel i7"},
    {"attribute_id": 1, "value": "16GB"},
    {"attribute_id": 3, "value": "512GB SSD"}
  ]
}'

# Produit 2: Laptop Budget 14 (ID: LAP-002)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Laptop abordable pour l'\''utilisation quotidienne",
  "price": 330000,
  "model": "Budget 14",
  "condition": 10,
  "stock_quantity": 85,
  "is_featured": false,
  "is_daily_promo": true,
  "promo_percentage": 10,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-11-05T14:20:32.866Z",
  "id": "LAP-002",
  "image_urls": ["url_laptop_budget14_1.jpg"],
  "brand_id": 1,
  "category_id": 3,
  "attributes": [
    {"attribute_id": 2, "value": "Intel i3"},
    {"attribute_id": 1, "value": "8GB"},
    {"attribute_id": 3, "value": "256GB SSD"}
  ]
}'

# Produit 3: Laptop Gaming X1 (ID: LAP-003)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Puissante machine de jeu portable",
  "price": 120000,
  "model": "Gaming X1",
  "condition": 10,
  "stock_quantity": 20,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "LAP-003",
  "image_urls": ["url_laptop_gamingx1_1.jpg"],
  "brand_id": 1,
  "category_id": 3,
  "attributes": [
    {"attribute_id": 2, "value": "AMD Ryzen 9"},
    {"attribute_id": 1, "value": "32GB"},
    {"attribute_id": 3, "value": "1TB SSD"}
  ]
}'

# Produit 4: Laptop Ultra Slim (ID: LAP-004)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Design fin et léger pour la mobilité",
  "price": 60000,
  "model": "Ultra Slim",
  "condition": 10,
  "stock_quantity": 60,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "LAP-004",
  "image_urls": ["url_laptop_ultraslim_1.jpg"],
  "brand_id": 1,
  "category_id": 3,
  "attributes": [
    {"attribute_id": 2, "value": "Intel i5"},
    {"attribute_id": 1, "value": "16GB"},
    {"attribute_id": 3, "value": "512GB SSD"}
  ]
}'

# Produit 5: Laptop 2-en-1 (ID: LAP-005)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Convertible tablette/ordinateur portable",
  "price": 48000,
  "model": "Convertible M1",
  "condition": 10,
  "stock_quantity": 35,
  "is_featured": false,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "LAP-005",
  "image_urls": ["url_laptop_convertible_1.jpg"],
  "brand_id": 1,
  "category_id": 3,
  "attributes": [
    {"attribute_id": 2, "value": "Intel Pentium"},
    {"attribute_id": 1, "value": "8GB"},
    {"attribute_id": 4, "value": "13.3"}
  ]
}'

# Produit 6: Smartphone Elite 5G (ID: TEL-006)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Téléphone phare avec capacités 5G",
  "price": 540000.00,
  "model": "Elite 5G",
  "condition": 10,
  "stock_quantity": 120,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "TEL-006",
  "image_urls": ["url_phone_elite_1.jpg"],
  "brand_id": 2,
  "category_id": 1,
  "attributes": [
    {"attribute_id": 3, "value": "256GB"},
    {"attribute_id": 5, "value": "true"},
    {"attribute_id": 4, "value": "6.7"}
  ]
}'

# Produit 7: Smartphone Mini (ID: TEL-007)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Compact et puissant",
  "price": 390000,
  "model": "Mini V2",
  "condition": 10,
  "stock_quantity": 150,
  "is_featured": false,
  "is_daily_promo": true,
  "promo_percentage": 15,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-11-10T14:20:32.866Z",
  "id": "TEL-007",
  "image_urls": ["url_phone_mini_1.jpg"],
  "brand_id": 2,
  "category_id": 1,
  "attributes": [
    {"attribute_id": 3, "value": "128GB"},
    {"attribute_id": 5, "value": "false"},
    {"attribute_id": 4, "value": "5.4"}
  ]
}'

# Produit 8: Smartphone Pro Max (ID: TEL-008)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Le plus grand écran, les meilleures caméras",
  "price": 710000,
  "model": "Pro Max Z",
  "condition": 10,
  "stock_quantity": 90,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "TEL-008",
  "image_urls": ["url_phone_promax_1.jpg"],
  "brand_id": 2,
  "category_id": 1,
  "attributes": [
    {"attribute_id": 3, "value": "512GB"},
    {"attribute_id": 5, "value": "true"},
    {"attribute_id": 4, "value": "6.9"}
  ]
}'

# Produit 9: Téléphone Économique (ID: TEL-009)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Téléphone de base, excellent rapport qualité-prix",
  "price": 130000,
  "model": "Eco 4G",
  "condition": 10,
  "stock_quantity": 200,
  "is_featured": false,
  "is_daily_promo": true,
  "promo_percentage": 5,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-11-01T14:20:32.866Z",
  "id": "TEL-009",
  "image_urls": ["url_phone_eco_1.jpg"],
  "brand_id": 2,
  "category_id": 1,
  "attributes": [
    {"attribute_id": 3, "value": "64GB"},
    {"attribute_id": 5, "value": "false"},
    {"attribute_id": 4, "value": "6.1"}
  ]
}'

# Produit 10: Téléphone Robuste (ID: TEL-010)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Conçu pour les environnements difficiles",
  "price": 4000,
  "model": "Rugged V3",
  "condition": 10,
  "stock_quantity": 55,
  "is_featured": false,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "TEL-010",
  "image_urls": ["url_phone_rugged_1.jpg"],
  "brand_id": 2,
  "category_id": 1,
  "attributes": [
    {"attribute_id": 3, "value": "128GB"},
    {"attribute_id": 5, "value": "true"},
    {"attribute_id": 4, "value": "6.3"}
  ]
}'

# Produit 11: Écran 27" 4K (ID: ECR-011)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Moniteur professionnel 4K",
  "price": 270000,
  "model": "UHD-27",
  "condition": 10,
  "stock_quantity": 70,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ECR-011",
  "image_urls": ["url_monitor_uhd27_1.jpg"],
  "brand_id": 3,
  "category_id": 5,
  "attributes": [
    {"attribute_id": 4, "value": "27"},
    {"attribute_id": 6, "value": "3840x2160"},
    {"attribute_id": 1, "value": "Non applicable"}
  ]
}'

# Produit 12: Écran 24" Full HD (ID: ECR-012)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Moniteur standard pour le bureau",
  "price": 90000,
  "model": "FH-24B",
  "condition": 10,
  "stock_quantity": 150,
  "is_featured": false,
  "is_daily_promo": true,
  "promo_percentage": 10,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-11-03T14:20:32.866Z",
  "id": "ECR-012",
  "image_urls": ["url_monitor_fh24b_1.jpg"],
  "brand_id": 3,
  "category_id": 5,
  "attributes": [
    {"attribute_id": 4, "value": "24"},
    {"attribute_id": 6, "value": "1920x1080"}
  ]
}'

# Produit 13: Écran Gaming 144Hz (ID: ECR-013)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Écran rapide pour le jeu compétitif",
  "price": 180000,
  "model": "Gamer-27F",
  "condition": 10,
  "stock_quantity": 45,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ECR-013",
  "image_urls": ["url_monitor_gamer_1.jpg"],
  "brand_id": 3,
  "category_id": 5,
  "attributes": [
    {"attribute_id": 4, "value": "27"},
    {"attribute_id": 6, "value": "2560x1440"}
  ]
}'

# Produit 14: Écran Ultra-Large (ID: ECR-014)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Moniteur ultra-large pour le multitâche",
  "price": 420000,
  "model": "Ultrawide 34",
  "condition": 10,
  "stock_quantity": 30,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ECR-014",
  "image_urls": ["url_monitor_uw_1.jpg"],
  "brand_id": 3,
  "category_id": 5,
  "attributes": [
    {"attribute_id": 4, "value": "34"},
    {"attribute_id": 6, "value": "3440x1440"}
  ]
}'

# Produit 15: Écran Tactile (ID: ECR-015)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Écran tactile pour des applications interactives",
  "price": 240000,
  "model": "Touch 22",
  "condition": 10,
  "stock_quantity": 25,
  "is_featured": false,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ECR-015",
  "image_urls": ["url_monitor_touch_1.jpg"],
  "brand_id": 3,
  "category_id": 5,
  "attributes": [
    {"attribute_id": 4, "value": "22"},
    {"attribute_id": 6, "value": "1920x1080"}
  ]
}'

# Produit 16: Desktop Gamer (ID: DESK-016)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Tour de bureau haute performance pour le jeu",
  "price": 1080000,
  "model": "Gamer-Tower V2",
  "condition": 10,
  "stock_quantity": 15,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "DESK-016",
  "image_urls": ["url_desktop_gamer_1.jpg"],
  "brand_id": 1,
  "category_id": 4,
  "attributes": [
    {"attribute_id": 2, "value": "Intel i9"},
    {"attribute_id": 1, "value": "64GB"},
    {"attribute_id": 3, "value": "2TB NVMe"}
  ]
}'

# Produit 17: Desktop Mini-PC (ID: DESK-017)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Petit ordinateur de bureau pour le travail",
  "price": 300000,
  "model": "Mini-Office",
  "condition": 10,
  "stock_quantity": 50,
  "is_featured": false,
  "is_daily_promo": true,
  "promo_percentage": 20,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-11-15T14:20:32.866Z",
  "id": "DESK-017",
  "image_urls": ["url_desktop_mini_1.jpg"],
  "brand_id": 1,
  "category_id": 4,
  "attributes": [
    {"attribute_id": 2, "value": "Intel Core i3"},
    {"attribute_id": 1, "value": "8GB"},
    {"attribute_id": 3, "value": "256GB SSD"}
  ]
}'

# Produit 18: Souris Ergonomique (ID: ACC-018)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Souris sans fil pour une utilisation confortable",
  "price": 21000,
  "model": "Ergo Wireless",
  "condition": 10,
  "stock_quantity": 300,
  "is_featured": false,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ACC-018",
  "image_urls": ["url_mouse_ergo_1.jpg"],
  "brand_id": 1,
  "category_id": 6,
  "attributes": [
    {"attribute_id": 5, "value": "Non applicable"},
    {"attribute_id": 4, "value": "Non applicable"}
  ]
}'

# Produit 19: Clavier Mécanique (ID: ACC-019)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Clavier mécanique rétroéclairé pour le jeu",
  "price": 54000,
  "model": "Mech Keys V4",
  "condition": 10,
  "stock_quantity": 110,
  "is_featured": true,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ACC-019",
  "image_urls": ["url_keyboard_mech_1.jpg"],
  "brand_id": 2,
  "category_id": 6,
  "attributes": [
    {"attribute_id": 5, "value": "Non applicable"}
  ]
}'

# Produit 20: Disque Dur Externe 1TB (ID: ACC-020)
curl -X POST 'http://localhost:8000/api/v1/products' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjIzNjk2NDB9.fh4K-Jpp7MRhk-tle5C24LHCKuewCw9Jwky41ZxtbJQ' \
-d '{
  "description": "Stockage externe rapide et portable",
  "price": 36000.00,
  "model": "External 1TB",
  "condition": 10,
  "stock_quantity": 250,
  "is_featured": false,
  "is_daily_promo": false,
  "promo_percentage": 0,
  "promo_start_date": "2025-10-29T14:20:32.866Z",
  "promo_end_date": "2025-10-29T14:20:32.866Z",
  "id": "ACC-020",
  "image_urls": ["url_hdd_external_1.jpg"],
  "brand_id": 3,
  "category_id": 6,
  "attributes": [
    {"attribute_id": 3, "value": "1TB HDD"},
    {"attribute_id": 5, "value": "Non applicable"}
  ]
}'