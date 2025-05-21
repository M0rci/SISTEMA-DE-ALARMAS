FROM ubuntu:22.04

# Actualiza los repositorios e instala Apache
RUN apt-get update && apt-get install -y apache2

# Limpia los archivos temporales creados por apt-get
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Exponer el puerto 80
EXPOSE 80

# Comando por defecto al iniciar el contenedor
CMD ["apache2ctl", "-D", "FOREGROUND"]

