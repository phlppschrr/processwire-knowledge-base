# ImageSizerEngine::writeBackIPTC()

Source: `wire/core/ImageSizerEngine.php`

Default IPTC Handling

If we've retrieved IPTC-Metadata from sourcefile, we write it into the variation here but we omit
custom tags for internal use (@horst)

@param string $filename the file we want write the IPTC data to

@param bool $includeCustomTags default is FALSE

@return bool|null
