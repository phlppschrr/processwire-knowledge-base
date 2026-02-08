# ImageSizerEngine::getSupportedFormats()

Source: `wire/core/ImageSizerEngine.php`

Get an array of image file formats this ImageSizerModule can use as source or target

Unless using the $type argument, returned array contains 'source' and 'target' indexes,
each an array of image file types/extensions in uppercase.

@param string $type Specify 'source' or 'target' to get just those formats, or omit to get all.

@return array

@since 3.0.138
