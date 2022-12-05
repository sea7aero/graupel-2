# graupel-2
This repository contains jupyter notebooks for calculations involving High Altitude Balloon launched named "Graupel-2".

It uses [Jupyter-book](https://jupyterbook.org/intro.html) to publish those notebooks into a 
[simple website](https://sea7aero.space/graupel-2)

# Contributing

## Building the documentation

```
poetry install
poetry shell
poe build-book
poe open
```

Changes to the book are automatically published when the `main` branch is pushed.