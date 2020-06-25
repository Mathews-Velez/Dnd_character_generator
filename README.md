[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4)](./CODE_OF_CONDUCT.md)

# DND Character Generator

Generate race, class, and backgrounds for DND characters.

# Setup

## Requirements
- [GNU Make](https://www.gnu.org/software/make/)
- [setuptools](https://pypi.org/project/setuptools/)

Clone the repo, then run `make` to build and install the package. This will install the package to your local site-packages as defined by your `pip` installation.

```sh
git clone https://github.com/Mathews-Velez/Dnd-_Character_Generator/
cd Dnd-_character_generator
make
```

## `make` Arguments
- build: create the build files
- clean: remove the build files
- install: install the package
- uninstall: uninstall the package
- wheel/source: only build the wheel/source distribution

## Notes
`make` will build from source instead of wheel by default. Source `.tar.gz` files are simply much smaller than wheels `.whl`. Run `make clean wheel install` to build and install from a wheel.

# Usage

The setup installs a shell script `dcg`. Typing this anywhere into your terminal will run the program. Note: the Python Scripts Entry-point may not exist on your path. If this is the case, `pip` will likely detect it and warn you to update your path. If typing `dcg` does not work, either the file cannot be found on your path, or something has gone wrong with the install. Try running `make install` again before opening an issue.

---

© 2020 Mathews Velez
