@echo off
cd backend

python -m venv venv
call venv\Scripts\activate

pip install -r requirements.txt

flask run
