
# RAM (ID Fictif: 1)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "RAM",
  "type": "list",
  "list_values": ["4Go", "8Go", "16Go", "32Go", "64Go"]
}'

# Processeur (ID Fictif: 2)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Processeur",
  "type": "text",
}'

# Stockage (ID Fictif: 3)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Stockage",
  "type": "text",
  "list_values": ["4Go", "8Go", "16Go", "32Go", "64Go", "128Go"]
}'

# Taille Écran (ID Fictif: 4)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Taille Écran",
  "type": "list",
  "list_values": ["13 pouces", "14 pouces", "15 pouces", "17 pouces", "19 pouces", "21 pouces", "24 pouces", "27 pouces", "32 pouces"]
}'

# Réseau 5G (ID Fictif: 5)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Réseau 5G",
  "type": "boolean"
}'

curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Bluetooth",
  "type": "boolean"
}'


# Résolution (ID Fictif: 6)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjM1NjA5NzB9.ih46tvetbwwvUqmIyK4-kNucys5G3vkVZA-GmkIZQE4' \
-d '{
  "name": "Résolution",
  "type": "list",
  "list_values": ["720p", "1080p", "1440p", "4K", "8K"]
}'