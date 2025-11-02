
# RAM (ID Fictif: 1)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjI2NDM0MTV9.LanPG-LEYH8CDwltuiO9Hre7qhGGZLiEQf4YarrWF44' \
-d '{
  "name": "RAM",
  "type": "text"
}'

# Processeur (ID Fictif: 2)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjI2NDM0MTV9.LanPG-LEYH8CDwltuiO9Hre7qhGGZLiEQf4YarrWF44' \
-d '{
  "name": "Processeur",
  "type": "text"
}'

# Stockage (ID Fictif: 3)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjI2NDM0MTV9.LanPG-LEYH8CDwltuiO9Hre7qhGGZLiEQf4YarrWF44' \
-d '{
  "name": "Stockage",
  "type": "text"
}'

# Taille Écran (ID Fictif: 4)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjI2NDM0MTV9.LanPG-LEYH8CDwltuiO9Hre7qhGGZLiEQf4YarrWF44' \
-d '{
  "name": "Taille Écran",
  "type": "number"
}'

# Réseau 5G (ID Fictif: 5)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjI2NDM0MTV9.LanPG-LEYH8CDwltuiO9Hre7qhGGZLiEQf4YarrWF44' \
-d '{
  "name": "Réseau 5G",
  "type": "boolean"
}'

# Résolution (ID Fictif: 6)
curl -X POST 'http://localhost:8000/api/v1/attributes' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJkeWxhbkBhZG1pbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NjI2NDM0MTV9.LanPG-LEYH8CDwltuiO9Hre7qhGGZLiEQf4YarrWF44' \
-d '{
  "name": "Résolution",
  "type": "list"
}'