# DXF Ruler Generator
![Ruler that has been manufactured from a dxf produced by this script.](https://user-images.githubusercontent.com/9170476/42137934-5cd12522-7d4b-11e8-955a-fc03ae0d657a.jpeg)

Generate DXF files for laser cutting and engraving custom sized rulers, which can then be easily manufactured at the nearest FabLab.

## Description
This project consists of a Python script that takes an Integer as argument to draw a ruler's 2D profile of the given size, in centimeters.

The output file uses the **.dxf** extension, which can be used for laser cutting and engraving.

![Drawing of a 7cm ruler.](https://user-images.githubusercontent.com/9170476/31572344-5b1c9016-b07a-11e7-9cd1-1e7f935b248e.png)

## Known issue
You might need to enable the importing of dxf text on the laser cutting software. Here's an example on RDWorksV8:

![Configuration](https://user-images.githubusercontent.com/9170476/31572357-9d378c94-b07a-11e7-893d-8040f095141a.png)

## Links
- Repository: https://github.com/umluizlima/dxf-ruler-generator
- Issue tracker: https://github.com/umluizlima/dxf-ruler-generator/issues
- References:
  - Mozman's **ezdxf** package: https://github.com/mozman/ezdxf
  - RDWorksV8: http://www.thunderlaser.com/laser-download

## Licensing
This project is licensed under MIT license.
