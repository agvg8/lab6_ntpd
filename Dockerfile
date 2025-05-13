# Używamy oficjalnego obrazu Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Kopiowanie plików aplikacji do kontenera
COPY . .

# Instalacja wymaganych pakietów
RUN pip install --no-cache-dir -r requirements.txt

# Definiowanie portu, na którym aplikacja będzie nasłuchiwać
EXPOSE 8080

# Komenda uruchamiająca aplikację
CMD ["python", "app.py"]
