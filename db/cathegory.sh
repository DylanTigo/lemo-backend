eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4

# Téléphones (ID Fictif: 1)
curl -X POST 'http://localhost:8000/api/v1/categories' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Téléphones",
  "description": "Smartphones et téléphones mobiles",
  "parent_id": null
}'

# Ordinateurs (ID Fictif: 2)
curl -X POST 'http://localhost:8000/api/v1/categories' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Ordinateurs",
  "description": "Systèmes informatiques complets (Laptops et Desktops)",
  "parent_id": null
}'

# Laptop (ID Fictif: 3, Parent: 2)
curl -X POST 'http://localhost:8000/api/v1/categories' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Laptop",
  "description": "Ordinateurs portables",
  "parent_id": 2
}'

# Desktop (ID Fictif: 4, Parent: 2)
curl -X POST 'http://localhost:8000/api/v1/categories' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Desktop",
  "description": "Ordinateurs de bureau et tours",
  "parent_id": 2
}'

# Ecran (ID Fictif: 5)
curl -X POST 'http://localhost:8000/api/v1/categories' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Ecran",
  "description": "Moniteurs et écrans d''affichage",
  "parent_id": null
}'

# Accessoires (ID Fictif: 6)
curl -X POST 'http://localhost:8000/api/v1/categories' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Accessoires",
  "description": "Périphériques, câbles et gadgets",
  "parent_id": null
}'