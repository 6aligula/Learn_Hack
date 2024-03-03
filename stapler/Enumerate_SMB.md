Listar los recursos compartidos
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ smbclient -L 10.0.2.4
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        kathy           Disk      Fred, What are we doing here?
        tmp             Disk      All temporary files should be stored here
        IPC$            IPC       IPC Service (red server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            RED

```

Hi ha 2 comparticions actives: kathy i tmp. El comentari: "Fred, què estem fent aquí?" em fa creure que Fred té accés a la part de Kathy. 

Intentem connectar-nos al recurs compartit de Kathy mitjançant l’usuari fred.
```bash
┌──(kali㉿kali)-[~/stapler]
└─$ smbclient //fred/kathy -I 10.0.2.4 -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Jun  3 12:52:52 2016
  ..                                  D        0  Mon Jun  6 17:39:56 2016
  kathy_stuff                         D        0  Sun Jun  5 11:02:27 2016
  backup                              D        0  Sun Jun  5 11:04:14 2016

                19478204 blocks of size 1024. 16393708 blocks available
smb: \> cd kathy_stuff
smb: \kathy_stuff\> ls
  .                                   D        0  Sun Jun  5 11:02:27 2016
  ..                                  D        0  Fri Jun  3 12:52:52 2016
  todo-list.txt                       N       64  Sun Jun  5 11:02:27 2016

                19478204 blocks of size 1024. 16393700 blocks available
```

### Me llevo el fichero todo-list.txt
```bash
smb: \kathy_stuff\> get todo-list.txt
getting file \kathy_stuff\todo-list.txt of size 64 as todo-list.txt (8.9 KiloBytes/sec) (average 8.9 KiloBytes/sec)
smb: \kathy_stuff\> cd backup
cd \kathy_stuff\backup\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \kathy_stuff\> cd ..
smb: \> ls
  .                                   D        0  Fri Jun  3 12:52:52 2016
  ..                                  D        0  Mon Jun  6 17:39:56 2016
  kathy_stuff                         D        0  Sun Jun  5 11:02:27 2016
  backup                              D        0  Sun Jun  5 11:04:14 2016

                19478204 blocks of size 1024. 16393692 blocks available
smb: \> cd backup
smb: \backup\> ls
  .                                   D        0  Sun Jun  5 11:04:14 2016
  ..                                  D        0  Fri Jun  3 12:52:52 2016
  vsftpd.conf                         N     5961  Sun Jun  5 11:03:45 2016
  wordpress-4.tar.gz                  N  6321767  Mon Apr 27 13:14:46 2015

                19478204 blocks of size 1024. 16393688 blocks available
```

### Me llevo la informacion de la carpeta backup

```bash
smb: \backup\> get vsftpd.conf
getting file \backup\vsftpd.conf of size 5961 as vsftpd.conf (646.8 KiloBytes/sec) (average 367.7 KiloBytes/sec)
smb: \backup\> get wordpress-4.tar.gz
getting file \backup\wordpress-4.tar.gz of size 6321767 as wordpress-4.tar.gz (2228.7 KiloBytes/sec) (average 2218.0 KiloBytes/sec)
smb: \backup\> 

Intentem connectar-nos al recurs compartit de temp mitjançant l’usuari fred.
                                                                                                                                                                                                                                     
┌──(kali㉿kali)-[~/stapler]
└─$ smbclient //fred/tmp -I 10.0.2.4 -N    
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Jun  7 04:08:39 2016
  ..                                  D        0  Mon Jun  6 17:39:56 2016
  ls                                  N      274  Sun Jun  5 11:32:58 2016

                19478204 blocks of size 1024. 16393640 blocks available
smb: \> get ls
getting file \ls of size 274 as ls (53.5 KiloBytes/sec) (average 53.5 KiloBytes/sec)
smb: \> exit
```
  
