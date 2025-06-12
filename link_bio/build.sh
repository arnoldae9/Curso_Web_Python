source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex run --env prod --backend-only --backend-port 8000 && reflex run --env prod --frontend-only --frontend-port 3000

