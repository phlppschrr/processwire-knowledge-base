# $pageimage->maxSize($width, $height, $options = array()): Pageimage

Source: `wire/core/Pageimage.php`

Return an image no larger than the given width and height

## Arguments

- `$width` `int` Max allowed width
- `$height` `int` Max allowed height
- `$options` (optional) `array` See `Pageimage::size()` method for options, or these additional options: - `allowOriginal` (bool): Allow original image to be returned if already within max requested dimensions? (default=false)

## Return value

Pageimage
