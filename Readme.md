# Python

## Linux Commands

| Linux / macOS | Windows | Description |
|---|---|---|
| `ls` | `dir` | List files and directories |
| `ls myfolder` | `dir myfolder` | List files and directories inside a folder |
| `pwd` | `cd` | Get current directory path |
| `clear` | `-same-` | Clear the terminal |
| `touch example.txt` | `echo > example.txt` | Create new file |
| `mkdir myfolder` | `-same-` | Create new directory |
| `cd myfolder` | `-same-` | Change directory to myfolder |
| `cd ..` | `-same-` | Go back one directory |
| `cp example.txt myfolder/` | `copy example.txt myfolder\` | Copy example.txt file to myfolder |
| `mv example.txt myfolder/` | `move example.txt myfolder\` | Move example.txt file to myfolder |
| `rm example.txt` | `del example.txt` | Delete example.txt |
| `rm -r myfolder` | `del /Q /S myfolder` | Delete myfolder and its content |
| `mv example.txt myexample.txt` | `move example.txt myexample.txt` | Rename example.txt to myexample.txt |
| `tree` | `tree /F` | Get current directory structure |
| `find . -name example.txt` | `dir example.txt /s /p` | Find file or directory |
| `cat example.txt` | `type example.txt` | Display file content |
| `du example.txt` | `-none-` | Get file or directory size |
| `zip example.zip example.txt` | `-none-` | Compress example.txt to example.zip |
| `unzip example.zip` | `-none-` | Unzip example.zip to current directory |
| `zip -r example.zip myfolder` | `-none-` | Compress all files of myfolder to example.zip |
| `help pwd` | `-same-` | Show help message for a command |
| `man pwd` | `-none-` | Show manual text for a command |
| `pip3 install --user library` | `-same-` | Install a package for Python 3 |
| `pip3 uninstall library` | `-same-` | Uninstall a package for Python 3 |

- `nano` is the text editor.

### Built In Functions

- `3 ** 3` => Exponential multiplication
- `dir(__builtins__)` => to list all the available python built in functions.
- `divmod(15, 3)` => returns division(quotient) and modulus(remainder).
- round(34.4412, 2) => 35.44
- `chr(97)` => 'a'
- `ord('A')` => 65

### List
- Python is Upper Bound Exclusive.
- Accessing order is from left to right only.
- To access last element, use Negative.
- Tuple is also a datatype in Python, it have paranthesis instead of square brackets.
- Tuple is immutable
- values = (1, 2, "Three")

### Function
- If the function doesn't return anything then it's type is **NoneType**
- `isinstance(variable, datatype)` => will return true or false, if the variable is in the same type.

### File
- type of file is `fileObject`.
- To know all the functions in the object, we have to use `dir(object)`.
- **myFile.read()** will return the cotent from the Cursor to the end of the file.
- At the first time, the cursor at the top left corner.
- When we use the myFile.read(), it will read and come to the end of the file.
- Then, if we read it again, it will return the empty string only.
- To make to go at the Top left corner, we have to use `myFile.seek(0)`.
- Once we read the file, we need to close the file connection also => `object.clos()`.
- To write a file need to pass the **mode argument** into it.
- `w` for write, `a` for append and `a+` for append and edit.
- `glob` module is used to get the fileNames as list