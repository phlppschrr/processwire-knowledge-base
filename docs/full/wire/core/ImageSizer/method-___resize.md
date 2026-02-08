# ImageSizer::___resize()

Source: `wire/core/ImageSizer.php`

Resize the image proportionally to the given width/height

@param int $targetWidth Target width in pixels, or 0 for proportional to height

@param int $targetHeight Target height in pixels, or 0 for proportional to width. Optional-if not specified, 0
    is assumed.

@return bool True if the resize was successful, false if not

@throws WireException when not enough memory to load image or missing required data
