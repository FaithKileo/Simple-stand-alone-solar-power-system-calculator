## Compiling to .exe
Install Nuitka

```shell
python -m pip install nuitka
```

Compile

```shell
python -m nuitka --onefile --disable-console --enable-plugin=tk-inter --windows-icon-from-ico=image.png main.py --output-filename=solar-calculator.exe
```

Find solar-calculator.exe in the same folder
