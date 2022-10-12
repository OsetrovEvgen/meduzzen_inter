# HOWTO build and run server

```sh
pip install -r requirements.txt
cd src && python -m healthcheck

sudo docker build -t img . 
sudo docker run -d -t --name img -p 8000:8000 img
```
