bulk image resizer using python

# setup
using git
```
python setup.py install -e .
```

using pip
```
pip install reebulk

reebulk -h
```

# usage
resize from another folder/drive
```
# resize image with 50% of default size

reebulk "c:\users\pictures\images" -p 50
```

resize from current opened folder
```
# with custom output folder

reebulk images -p 50 -o saved
```
or
```
# resize with 50% of size and 100% of quality of the image
# default -q is 50

$reebulk images -p 50 -q 100
```
