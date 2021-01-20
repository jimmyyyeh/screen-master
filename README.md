# screen-master

**A tool for build GNU screen automatically.**

## Description:
A tool for build GNU screen automatically.

This package can make you build project in [GNU screen](https://www.gnu.org/software/screen/) more easily.

## Config Template
```editorconfig
[section]
window title = command (allow multiple lines)
```

## How To Use:

1. Set up your config:
```editorconfig
[hello]
window01 = python3
window02 = echo \"HELLO world\"
window03 = echo \"HELLO WORLD\";echo \"HEY PYTHON\"
window04 = echo \"hello world\"
           echo \"hey python\"
```

2. Execute command through CLI - `sbuild -s section`
```commandline
sbuild -s hello
```

---
<a href="https://www.buymeacoffee.com/jimmyyyeh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="40" width="175"></a>

**Buy me a coffee, if you like it!**