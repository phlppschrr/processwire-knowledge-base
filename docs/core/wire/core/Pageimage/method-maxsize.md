# Pageimage::maxSize()

Source: `wire/core/Pageimage.php`

Return an image no larger than the given width and height


@param int $width Max allowed width

@param int $height Max allowed height

@param array $options See `Pageimage::size()` method for options, or these additional options:
 - `allowOriginal` (bool): Allow original image to be returned if already within max requested dimensions? (default=false)

@return Pageimage
