# ImageSizerEngineGD::___imSaveReady()

Source: `wire/core/ImageSizerEngineGD.php`

Called before saving of image, returns true if save should proceed, false if not

Also Creates a webp file when settings indicate it should.

@param resource $im

@param string $filename Source filename

@return bool
