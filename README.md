bulk image resizer using python

```
pip install reebulk

reebulk -h
```

resize from another folder/drive
```
# resize image with 50% of default size
reebulk "c:\users\pictures\images" -p 50
```

resize from current opened folder
```
reebulk images -p 50 -o saved # with custom output folder

or

reebulk images -p 50 # default output folder
```