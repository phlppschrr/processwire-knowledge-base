# ImageSizerEngine::resize()

Source: `wire/core/ImageSizerEngine.php`

Resize the image

The resize method does all pre and post-processing for the engines + calls the engine's
processResize() method.

Pre-processing is:
  Calculate and set dimensions, create a tempfile.

Post-processing is:
  Copy back and delete tempfile, write IPTC if necessary, reload imageinfo, set the modified flag.

@param int $finalWidth

@param int $finalHeight

@return bool
