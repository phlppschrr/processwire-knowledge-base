# $pageimage->maxWidth($n, array $options = array()): Pageimage

Source: `wire/core/Pageimage.php`

Return an image no larger than the given width.

If source image is equal to or smaller than the requested dimension,
then it will remain that way and the source image is returned (not a copy).

If the source image is larger than the requested dimension, then a new copy
will be returned at the requested dimension.

## Arguments

- `$n` `int` Maximum width
- `$options` (optional) `array` See `Pageimage::size()` method for options

## Return value

Pageimage
