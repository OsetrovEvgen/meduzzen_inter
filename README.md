# HOWTO build and run server

```sh
pip install -r requirements.txt
cd src && python -m healthcheck

docker-compose --env-file src/.env up -d
```
