# ImageSizerEngine::prepare()

Source: `wire/core/ImageSizerEngine.php`

Prepare the ImageSizer (this should be the first method you call)

This is used as a replacement for __construct() since modules can't have required arguments
to their constructor.

@param string $filename

@param array $options

@param null|array $inspectionResult
