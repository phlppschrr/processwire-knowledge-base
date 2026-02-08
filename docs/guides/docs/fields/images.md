# FieldtypeImage (for images fields)

Source: https://processwire.com/docs/fields/images/

## Summary

This page outlines using and manipulating image fields — one of the most commonly used in ProcessWire.

## Key Points

- This page outlines using and manipulating image fields — one of the most commonly used in ProcessWire.
- To interact with the images field. Create a new field (under Setup > Fields) and call it whatever you want, like "images" for example. Set the field type as "image". Save. On the details tab, you may set the maximum quantity of images the field may contain. Please note that if you set it to one (1), the field will usually behave as a single image rather than an array of images, and this affects how you access it from the API. Add this new images field to a template (under Setup > Templates). Then edit a page using that template and upload some images.
- In your template files, you can loop through the images field and output each image:

## Sections


### How to access the images field from your templates

In your template files, you can loop through the images field and output each image:


### How to tell if a page has images present

It is a good idea to check if an image(s) field has something in it before attempting to output it. When set to contain multiple images, you can tell if a page contains one or more images by using the count() function:


## Resizing images


### ProcessWire will create your images at any size on the fly and then keep a cache of them.

For instance, lets say we want to cycle through all the images, create a large image at 500 pixel width with proportional height, and a thumbnail at 100x100, and then have the thumbnail link to the large:


### Image resize functions

- $img = $image->width($x) — Create a new image at width $x, and proportional in height to the original.
- $img = $image->width($x, $options) — Same as above, except with additional array of options* specified.
- $img = $image->height($y) — Create a new image at height $y, and proportional in width to the original.
- $img = $image->height($y, $options) — Same as above, except with additional array of options* specified.
- $img = $image->size($x, $y) — Create a new image at exactly the given width ($x) and height ($y). If necessary either dimension will be cropped to reach the target size. By default crop is to the center in both axis.
- $img = $image->size($x, $y, $options) — Same as above, except with additional array of options* specified.
- $img = $image->size($x, $y, "north") — Same as above, except crop to the "north" (top center). Options for cropping are: northwest, north, northeast, west, center, east, southwest, south, and southeast. If you prefer, you may specify shorter versions: nw, n, ne, w, c, e, sw, s, se.
- $img = $image->size($x, $y, "50%,30%") — Same as above, except target your own x and y regions as percentages. Percentages may be 0–100%. Note that "0%,0%" is northwest, "50%,50%" is center, and "100%,100%" is southeast. This feature is in beta.
- $img = $image->size($x, $y, "100,200"); — Same as above, except target your own x and y regions as number of pixels. This feature is in beta.


### $options array

Some of the resize functions above include an $options array. You can use the $options array like this:

- quality — Quality setting of 1–100 (integer), where 1 is worst and 100 is best. Default is 90.
- upscaling — Allow upscaling? (boolean). If set to false, options sent to width(), height() and size() functions become maximum values rather than absolutes. Meaning, if you ask for an image 900 pixels wide and this is larger than the original image, it won't be upscaled to reach that dimension. The default setting is true, meaning you'll always get an image at the sized you asked for, even if upscaling is required.
- cropping (as a boolean) — The default value of 'cropping' is true, meaning cropping is allowed to reach target dimensions. If you want to disallow cropping, set to false.
- cropping (as a direction) — If a direction string is specified, any necessary cropping will target the given direction. Valid values are: northwest, north, northeast, west, center, east, southwest, south and southeast. If you prefer, you may specify shorter versions: nw, n, ne, w, c, e, sw, s, se. Default is center.
- cropping (as a percent) — If you specify two percent values in a string, like "50%,30%" then the crop will target those regions in the image. Note that "0%,0%" is northwest, "50%,50%" is center, and "100%,100%" is southeast. You may specify any percentage values between 0 and 100. This feature is in beta.
- cropping (as pixels) — If you specify two pixels values in a string, like "100,200" then the crop will target those regions in the image (in pixel quantity). This feature is in beta.


## Image properties


### The above examples only refer to $image->url, but note that there are several other image properties you may wish to access.

For instance, $image->description refers to the description text entered for the image, which you may want to include as an alt attribute:

- $image->url — Full URL to the image
- $image->filename — Image filename, including server path
- $image->basename — Image filename, without server path
- $image->description — Image description text (typically for "alt" attribute)
- $image->width — Image width in pixels
- $image->height — Image height in pixels
- $image->original — Reference to the original image, if this is a resized image
- $image->tags — String of space separated image tags, if used
- $image->ext — Image extension (jpg, jpeg, gif, png)
- $image->page — Reference to the Page object that contains this image
- $image->modified — Unix timestamp of last image modification time
- $image->created — Unix timestamp of date image was added to system
- $image->pagefiles — Reference to the array of images containing this image
- $image->filesize — File size in bytes
- $image->filesizeStr — Formatted filesize string
