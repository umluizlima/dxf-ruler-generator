# DXF Ruler Generator
> Quickly create rulers for digital fabrication.

Generate DXF files for laser cutting and engraving custom sized rulers, which can then be easily manufactured at the nearest FabLab.

![Ruler that has been manufactured from a dxf produced by this script.](https://user-images.githubusercontent.com/9170476/42137934-5cd12522-7d4b-11e8-955a-fc03ae0d657a.jpeg)

## Description

This project consists of a Python script that takes an Integer as argument to draw a ruler's 2D profile of the given size, in centimeters.

The output file uses the **.dxf** extension, which can be used for laser cutting and engraving.

## Requirements

- Python 3.6+

## Installation

```sh
pip install dxf-ruler-generator
```

## Usage

The following command will create a file `ruler_7cm.dxf` on the current working directory:

```sh
dxf-ruler-generator 7
```

This is how the file looks like when imported on a laser fabrication software:
![DXF file when imported on a laser fabrication software.](https://user-images.githubusercontent.com/9170476/31572344-5b1c9016-b07a-11e7-9cd1-1e7f935b248e.png)

## Changelog

- 0.0.4: specify Python 3.6+ as required version;
- 0.0.3: print generated file abspath;
- 0.0.2: 'dxf-ruler-generator' works on CLI;
- 0.0.1: Initial release;

## Quick tip
You might need to enable the importing of dxf text on the laser fabrication software. Here's an example on RDWorksV8:

![Configuration](https://user-images.githubusercontent.com/9170476/31572357-9d378c94-b07a-11e7-893d-8040f095141a.png)

## Links
- Repository: https://github.com/umluizlima/dxf-ruler-generator
- Issue tracker: https://github.com/umluizlima/dxf-ruler-generator/issues
- References:
  - Mozman's **ezdxf** package: https://github.com/mozman/ezdxf
  - RDWorksV8: http://www.thunderlaser.com/laser-download

## Licensing
Distributed under the MIT license. See `LICENSE` for more information.
