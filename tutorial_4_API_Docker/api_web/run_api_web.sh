DATABASE_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' database)
DATABASE_IP=$DATABASE_IP docker-compose up --build -d
