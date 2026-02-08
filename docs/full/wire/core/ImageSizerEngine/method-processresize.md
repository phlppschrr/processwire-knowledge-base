# ImageSizerEngine::processResize()

Source: `wire/core/ImageSizerEngine.php`

Process the image resize

Processing is as follows:
   1. first do a check if the given image(type) can be processed, if not do an early return false
   2. than (try) to process all required steps, if one failes, return false
   3. if all is successful, finally return true

@param string $srcFilename Source file

@param string $dstFilename Destination file

@param int $fullWidth Current width

@param int $fullHeight Current height

@param int $finalWidth Requested final width

@param int $finalHeight Requested final height

@return bool True if successful, false if not

@throws WireException
