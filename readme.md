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

This is an example snippet to slice up your 3D image into a list of images stored in the list `multi_matrix`. The position of each of the small images is stored in `codex`. Keep track of the `codex` as it will be required to rebuild your original image.

For the moment, the code **only works on 3D images**. But you can cut the up in all three dimensions or only in the xy plane by modifying the `cut_in_z_direction` variable.

```
from saucisson import cutter

multi_image_list, codex = cutter.image_cutter(
    example_image,
    max_image_size = 100,
    cut_in_z_direction = True)

reconstructed_image = cutter.image_recompose(
    multi_image_list,
    example_image,
    max_image_size = 100,
    codex = codex,
    cut_in_z_direction = True)

```

![Here is an example reconstruction result of a sample image](https://github.com/gronteix/saucisson/blob/main/images/example_saucisson.png)

You can also rebuild other matrixes or images of the same size using the same function. Here is the example code for rebuilding an image from the list of images `other_multi_image_list`

```
reconstructed_other_image = cutter.image_recompose(
    other_multi_image_list,
    example_image,
    max_image_size = 100,
    codex = codex,
    cut_in_z_direction = True)

```