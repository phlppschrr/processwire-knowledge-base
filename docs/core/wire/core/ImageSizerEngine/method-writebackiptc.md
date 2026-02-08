# $imageSizerEngine->writeBackIPTC($filename, $includeCustomTags = false): bool|null

Source: `wire/core/ImageSizerEngine.php`

Default IPTC Handling

If we've retrieved IPTC-Metadata from sourcefile, we write it into the variation here but we omit
custom tags for internal use (@horst)

## Arguments

- `$filename` `string` the file we want write the IPTC data to
- `$includeCustomTags` (optional) `bool` default is FALSE

## Return value

bool|null
