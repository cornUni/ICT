# Password manager app with crud functionality using AES encryption


## List of commands you can use 

### CREATE
```
    python main.py create -n <name> -c <description> -key <key>

    eg.

    python main.py create -n portal -c my student portal key -key 1234
```
### UPDATE
```
    python main.py update <name> -key <key>

    eg.

    python main.py update portal -key 54321
```

### DELETE
```
    python main.py delete <name>

    eg.

    python main.py delete portal
```
### READ
```
    python main.py read <name>

    eg.

    python main.py read portal
```
### LIST
```
    python main.py list

    eg.

    python main.py list
```

### generate a big volume of encrypted values from one key
```
    python main.py mass -key <key>

    eg.

    python main.py mass -key 0000

```