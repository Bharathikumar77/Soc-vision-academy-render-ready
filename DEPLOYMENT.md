# SOC Vision Academy - Production Deployment Guide

## Environment Variables

Set these in your production environment:

```bash
FLASK_ENV=production
FLASK_APP=app.py
SECRET_KEY=<generate-strong-random-key>
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Database Setup

### PostgreSQL

```sql
CREATE DATABASE soc_vision;
CREATE USER soc_user WITH PASSWORD 'secure_password';
ALTER ROLE soc_user SET client_encoding TO 'utf8';
ALTER ROLE soc_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE soc_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE soc_vision TO soc_user;
```

## Application Server

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 --timeout 120 app:app
```

### Using uWSGI

```bash
pip install uwsgi
uwsgi --http :5000 --wsgi-file app.py --callable app --processes 4 --threads 2
```

## Reverse Proxy Setup

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /static/ {
        alias /path/to/app/static/;
        expires 30d;
    }
}
```

### SSL/HTTPS with Let's Encrypt

```bash
certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com
```

## Systemd Service File

Create `/etc/systemd/system/soc-vision.service`:

```ini
[Unit]
Description=SOC Vision Academy
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/soc-vision
Environment="PATH=/var/www/soc-vision/venv/bin"
ExecStart=/var/www/soc-vision/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable soc-vision
sudo systemctl start soc-vision
sudo systemctl status soc-vision
```

## Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t soc-vision-academy .
docker run -d -p 5000:5000 --env-file .env soc-vision-academy
```

## Database Migrations

```bash
flask db upgrade
```

## Backup Strategy

### Database Backup

```bash
pg_dump -U soc_user -h localhost soc_vision > backup.sql
```

### Restore from Backup

```bash
psql -U soc_user -h localhost soc_vision < backup.sql
```

## Security Checklist

- [ ] Update SECRET_KEY with strong random value
- [ ] Set DEBUG=False
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS properly
- [ ] Set up database backups
- [ ] Configure firewall rules
- [ ] Enable logging and monitoring
- [ ] Regular security updates
- [ ] Rate limiting on authentication endpoints
- [ ] Session timeout configuration

## Monitoring

### Application Logs

```bash
tail -f /var/log/soc-vision/app.log
```

### Database Monitoring

```sql
-- Active connections
SELECT datname, count(*) FROM pg_stat_activity GROUP BY datname;

-- Slow queries
SELECT query, mean_time FROM pg_stat_statements ORDER BY mean_time DESC LIMIT 10;
```

## Performance Optimization

1. Enable database indexing on frequently queried columns
2. Implement caching with Redis
3. Use CDN for static assets
4. Configure compression (gzip)
5. Optimize database queries
6. Use connection pooling

## Troubleshooting

### Database Connection Issues

```bash
# Test PostgreSQL connection
psql -U soc_user -h localhost -d soc_vision -c "SELECT version();"
```

### Application Not Starting

```bash
# Check logs
journalctl -u soc-vision -n 50

# Test application
python app.py
```

### High Memory Usage

```bash
# Restart application
sudo systemctl restart soc-vision

# Check memory usage
free -h
```

## Support

For production support, please contact the development team.
