# ImageSizerEngine::setOptions()

Source: `wire/core/ImageSizerEngine.php`

Alternative to the above set* functions where you specify all in an array

@param array $options May contain the following (show with default values):
   'quality' => 90,
   'webpQuality' => 90,
   'cropping' => true,
   'upscaling' => true,
   'autoRotation' => true,
   'sharpening' => 'soft' (none|soft|medium|string)
   'scale' => 1.0 (use 2.0 for hidpi or 1.0 for normal-default)
   'hidpi' => false, (alternative to scale, specify true to enable hidpi)
   'rotate' => 0 (90, 180, 270 or negative versions of those)
   'flip' => '', (vertical|horizontal)

@return self
