# Theorem Cropper

This utility helps me to automate part of the process of creating learning guides for mathematical topics.

The idea is fairly simple:
1. I make screenshots of the theorems I want to learn
2. I make a rough crop using GIMP
3. **The *theorem cropper* allows me to crop all the extra white space in the borders of the theorem screenshot**
4. I'm happy because now I can turn these images into beautiful cards to be learned with Anki :blush: 🤓


## How To Use

1. Place the rough screenshots inside the `input/` directory
2. Run this:
```
> python3 cropper.py
```
3. Profit! (you'll find the cropped files inside the `output/` directory)