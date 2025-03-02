# Python 3.9 alapimage használata
FROM python:3.9-slim

# Munkakönyvtár beállítása
WORKDIR /app

# Függőségek telepítése
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Az add-on fájlok bemásolása
COPY . /app

# run.sh futtathatóvá tétele
RUN chmod +x /app/run.sh

# Az entrypoint script beállítása
CMD ["/app/run.sh"]
