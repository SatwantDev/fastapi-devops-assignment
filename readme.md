# SSL Setup

This project is designed for local development. In production, SSL should be configured using NGINX with Let's Encrypt certificates. Since no public domain was available, HTTPS is documented but not configured.

# Security Measures

* JWT Authentication
* Environment variables for secrets
* PostgreSQL authentication
* Docker network isolation
* NGINX reverse proxy

# Logging Strategy

* FastAPI/Uvicorn application logs
* Docker container logs
* NGINX access and error logs
* PostgreSQL logs

# Backup & Restart Strategy

* PostgreSQL data is stored in a Docker volume.
* Docker Compose restart policies can be used for automatic recovery.
* Database backups can be created using `pg_dump`.
* Containers can be restarted using `docker compose restart`.

# Deployment Instructions

1. Clone the repository.
2. Create a `.env` file from `.env.example`.
3. Run `docker compose up --build`.
4. Open `http://localhost:8000/docs`.
5. Test the Register, Login, and Notes APIs.

# CI/CD

GitHub Actions automatically builds the application on every push to the repository. In a production environment, the workflow can be extended to deploy to a VPS using SSH.
