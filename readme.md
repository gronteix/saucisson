# Saucisson, the image slices

Saucisson is the new module to cut up your images in smaller bits and rebuild them after.

## Installing the module

Download the package from github"

```
https://github.com/gronteix/saucisson
```

Install the packages:
```
pip install .
```

## Example code

This is an example snippet to slice up your image into a list of images stored in the list `multi_matrix`. The position of each of the small images is stored in `codex`. Keep track of the `codex` as it will be required to rebuild your original image.

```
from saucisson import cutter

multi_matrix, codex = cutter.image_cutter(
    example_image,
    max_image_size = 100,
    cut_in_z_direction = True)

```

![Here is an example reconstruction result of a sample image](https://github.com/gronteix/saucisson/blob/main/images/example_saucisson.png)
