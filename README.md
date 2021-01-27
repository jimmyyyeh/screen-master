# screen-master

**A cli tool for interact with GNU screen more easily.**

## Description:
A cli tool for interact with GNU screen more easily.

What can screen-master do?
- It can make you build project in [GNU screen](https://www.gnu.org/software/screen/) more easily.
- It can make you enter into the screen or kill it faster.

## Config Template
```editorconfig
[section]
window title = command (allow multiple lines)
```

## How To Use:

1. Set up your config:
```ini
[hello]
window01 = python3
window02 = echo \"HELLO world\"
window03 = echo \"HELLO WORLD\";echo \"hello world\";
window04 = echo \"hello world\"
           echo \"hey python\"
```

2. CLI command:
- Build screen -> `sbuild -s section`
```commandline
sbuild -s hello
```

3. Enter into the screen -> `srun -s screen name`
```commandline
srun -s hello
```

4. Kill the screen -> `skill -s screen name`
```commandline
skill -s world
```
*you can also kill all screen if you don't choose any screen by screen index*


---
<a href="https://www.buymeacoffee.com/jimmyyyeh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="40" width="175"></a>

**Buy me a coffee, if you like it!**
