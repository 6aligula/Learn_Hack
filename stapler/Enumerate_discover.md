
### Primero debo averiguar en que red estoy con ip addr
```bash
┌──(kali㉿kali)-[~]
└─$ ip addr

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:a1:d4:bc brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.5/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 376sec preferred_lft 376sec
    inet6 fe80::1bcc:189a:4c89:8a5f/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

### Busco las maquinas en mi rango de ip
```bash
┌──(kali㉿kali)-[~]
└─$ sudo netdiscover -r 10.0.2.0/24  

salida

Currently scanning: Finished!   |   Screen View: Unique Hosts                                                                                                                                                                        
                                                                                                                                                                                                                                      
 4 Captured ARP Req/Rep packets, from 4 hosts.   Total size: 240                                                                                                                                                                      
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 10.0.2.1        52:54:00:12:35:00      1      60  Unknown vendor                                                                                                                                                                     
 10.0.2.2        52:54:00:12:35:00      1      60  Unknown vendor                                                                                                                                                                     
 10.0.2.3        08:00:27:01:de:42      1      60  PCS Systemtechnik GmbH                                                                                                                                                             
 10.0.2.4        08:00:27:cb:1c:6e      1      60  PCS Systemtechnik GmbH  
 ```
 
 ### Escaneo de puertos con nmap
 ```bash 
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sT -sV -A -O -v -p 1-65535 10.0.2.4
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-29 06:02 EST
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 06:02
Completed NSE at 06:02, 0.00s elapsed
Initiating NSE at 06:02
Completed NSE at 06:02, 0.00s elapsed
Initiating NSE at 06:02
Completed NSE at 06:02, 0.00s elapsed
Initiating ARP Ping Scan at 06:02
Scanning 10.0.2.4 [1 port]
Completed ARP Ping Scan at 06:02, 0.06s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 06:02
Completed Parallel DNS resolution of 1 host. at 06:02, 0.01s elapsed
Initiating Connect Scan at 06:02
Scanning 10.0.2.4 (10.0.2.4) [65535 ports]
Discovered open port 80/tcp on 10.0.2.4
Discovered open port 21/tcp on 10.0.2.4
Discovered open port 3306/tcp on 10.0.2.4
Discovered open port 53/tcp on 10.0.2.4
Discovered open port 22/tcp on 10.0.2.4
Discovered open port 139/tcp on 10.0.2.4
Connect Scan Timing: About 20.23% done; ETC: 06:05 (0:02:02 remaining)
Connect Scan Timing: About 48.72% done; ETC: 06:04 (0:01:04 remaining)
Discovered open port 12380/tcp on 10.0.2.4
Discovered open port 666/tcp on 10.0.2.4
Completed Connect Scan at 06:04, 104.33s elapsed (65535 total ports)
Initiating Service scan at 06:04
Scanning 8 services on 10.0.2.4 (10.0.2.4)
Completed Service scan at 06:04, 11.06s elapsed (8 services on 1 host)
Initiating OS detection (try #1) against 10.0.2.4 (10.0.2.4)
Retrying OS detection (try #2) against 10.0.2.4 (10.0.2.4)
Retrying OS detection (try #3) against 10.0.2.4 (10.0.2.4)
Retrying OS detection (try #4) against 10.0.2.4 (10.0.2.4)
Retrying OS detection (try #5) against 10.0.2.4 (10.0.2.4)
NSE: Script scanning 10.0.2.4.
Initiating NSE at 06:04
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 06:05, 32.54s elapsed
Initiating NSE at 06:05
Completed NSE at 06:05, 0.13s elapsed
Initiating NSE at 06:05
Completed NSE at 06:05, 0.00s elapsed
Nmap scan report for 10.0.2.4 (10.0.2.4)
Host is up (0.0021s latency).
Not shown: 65523 filtered tcp ports (no-response)
PORT      STATE  SERVICE     VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp         vsftpd 2.0.8 or later
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.0.2.5
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 550 Permission denied.
22/tcp    open   ssh         OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 81:21:ce:a1:1a:05:b1:69:4f:4d:ed:80:28:e8:99:05 (RSA)
|   256 5b:a5:bb:67:91:1a:51:c2:d3:21:da:c0:ca:f0:db:9e (ECDSA)
|_  256 6d:01:b7:73:ac:b0:93:6f:fa:b9:89:e6:ae:3c:ab:d3 (ED25519)
53/tcp    open   domain      dnsmasq 2.75
| dns-nsid: 
|_  bind.version: dnsmasq-2.75
80/tcp    open   http        PHP cli server 5.5 or later
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: 404 Not Found
123/tcp   closed ntp
137/tcp   closed netbios-ns
138/tcp   closed netbios-dgm
139/tcp   open   netbios-ssn Samba smbd 4.3.9-Ubuntu (workgroup: WORKGROUP)
666/tcp   open   tcpwrapped
3306/tcp  open   mysql       MySQL 5.7.12-0ubuntu1
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.12-0ubuntu1
|   Thread ID: 10
|   Capabilities flags: 63487
|   Some Capabilities: Support41Auth, Speaks41ProtocolOld, SupportsTransactions, SupportsCompression, IgnoreSigpipes, IgnoreSpaceBeforeParenthesis, ODBCClient, LongColumnFlag, LongPassword, ConnectWithDatabase, DontAllowDatabaseTableColumn, FoundRows, SupportsLoadDataLocal, InteractiveClient, Speaks41ProtocolNew, SupportsMultipleResults, SupportsAuthPlugins, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: \x16r%p\x0C&W@-s-Vg\x0F("1t\x0Bw
|_  Auth Plugin Name: mysql_native_password
12380/tcp open   http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:CB:1C:6E (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=2/29%OT=21%CT=20%CU=30462%PV=Y%DS=1%DC=D%G=Y%M=0800
OS:27%TM=65E064E3%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=107%TI=Z%CI=I%
OS:TS=8)OPS(O1=M5B4ST11NW7%O2=M5B4ST11NW7%O3=M5B4NNT11NW7%O4=M5B4ST11NW7%O5
OS:=M5B4ST11NW7%O6=M5B4ST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=
OS:7120)ECN(R=Y%DF=Y%T=40%W=7210%O=M5B4NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=N)

Uptime guess: 0.012 days (since Thu Feb 29 05:47:20 2024)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host: RED; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.9-Ubuntu)
|   Computer name: red
|   NetBIOS computer name: RED\x00
|   Domain name: \x00
|   FQDN: red
|_  System time: 2024-02-29T12:04:36+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| nbstat: NetBIOS name: RED, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   RED<00>              Flags: <unique><active>
|   RED<03>              Flags: <unique><active>
|   RED<20>              Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-02-29T12:04:35
|_  start_date: N/A
|_clock-skew: mean: 1h00m00s, deviation: 0s, median: 59m59s

TRACEROUTE
HOP RTT     ADDRESS
1   2.07 ms 10.0.2.4 (10.0.2.4)

NSE: Script Post-scanning.
Initiating NSE at 06:05
Completed NSE at 06:05, 0.00s elapsed
Initiating NSE at 06:05
Completed NSE at 06:05, 0.00s elapsed
Initiating NSE at 06:05
Completed NSE at 06:05, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 160.56 seconds
           Raw packets sent: 141 (13.808KB) | Rcvd: 61 (4.648KB)
```

Hemos descubierto una serie de servicios y puertos abiertos que son críticos para entender la configuración y posibles vulnerabilidades de la máquina objetivo. Por ejemplo, el puerto 21 está abierto para FTP con la posibilidad de acceso anónimo, lo cual podría ser un vector de ataque. SSH está activo en el puerto 22, mostrando que es posible una conexión segura. El puerto 80 está abierto para HTTP, indicando un servidor web, y el puerto 3306 sugiere que MySQL está corriendo, lo cual podría contener bases de datos importantes. Además, hay un servicio Samba en el puerto 139, lo que podría indicar recursos compartidos en la red. Cada uno de estos puntos es un inicio potencial para pruebas de penetración más profundas.
 Además, hay otro servidor web en el puerto 12380, que podría ser utilizado para aplicaciones específicas o para administración. Ambos puertos abiertos para servicios HTTP sugieren la presencia de sitios web o aplicaciones web en la máquina objetivo.


### Conectandome al ftp con el usuario  y contrasena > anonymous

```bash
┌──(kali㉿kali)-[~]
└─$ ftp 10.0.2.4
Connected to 10.0.2.4.
220-
220-|-----------------------------------------------------------------------------------------|
220-| Harry, make sure to update the banner when you get a chance to show who has access here |
220-|-----------------------------------------------------------------------------------------|
220-
220 
Name (10.0.2.4:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
con el comando ls listo los ficheros del ftp
ftp> ls
550 Permission denied.
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             107 Jun 03  2016 note
226 Directory send OK.
Con el comando get note me descargo el fichero
ftp> get note
local: note remote: note
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note (107 bytes).
100% |******************************************************************************************************************************************************************************************|   107       46.17 KiB/s    00:00 ETA
226 Transfer complete.
107 bytes received in 00:00 (22.02 KiB/s)
ftp> 
```


### Muestro el contenido del fichero note
```bash

┌──(kali㉿kali)-[~/stapler]
└─$ ls
note
                                                                                                                                                                                                                                        
┌──(kali㉿kali)-[~/stapler]
└─$ cat note  
Elly, make sure you update the payload information. Leave it in your FTP account once your are done, John.
```

No hi ha molt per continuar, però sí que hem obtingut el nom d’un usuari. Els noms podrien ser importants més endavant per fer més enumeració i força bruta.