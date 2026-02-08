# Pageimage::maxHeight()

Source: `wire/core/Pageimage.php`

Return an image no larger than the given height.

If source image is equal to or smaller than the requested dimension,
then it will remain that way and the source image is returned (not a copy).

If the source image is larger than the requested dimension, then a new copy
will be returned at the requested dimension.


@param int $n Maximum height

@param array $options See `Pageimage::size()` method for options

@return Pageimage
