# ImageSizer::resizeFallback()

Source: `wire/core/ImageSizer.php`

GD is the fallback ImageEngine, it gets invoked if there is no other Engine defined,

or if a defined Engine is not available,
or if an invoked Engine failes with the image manipulation.

@param mixed $targetWidth

@param mixed $targetHeight

@return bool
