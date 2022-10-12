# Carlee project 🚗
This is backend of project [carlee-frontend](https://github.com/NicolasBoulard/carlee-frontend)

## How to use this app ?
### Without docker

1. Clone this repo `git clone https://github.com/NicolasBoulard/carlee.git`
2. Create venv `python -m venv .venv`
3. Activate venv `.venv\Script\Activate`
4. Install requirements `pip install -r requirements.txt`
5. Launch project `python charge_server.py`

### With docker 🐋
1. Clone this repo `git clone https://github.com/NicolasBoulard/carlee.git`
2. Build file with using dockerfile `docker build . -t carlee-backend`
3. Run this image `docker run PORT=Your_port carlee-backend`

### Question ?
If you want to contribute to this project/improve code open an issue