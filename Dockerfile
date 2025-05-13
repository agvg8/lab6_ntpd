# Bazowy obraz z Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików do kontenera
COPY . /app

# Instalacja zależności
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Wystawienie portu dla aplikacji Flask
EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "app.py"]
