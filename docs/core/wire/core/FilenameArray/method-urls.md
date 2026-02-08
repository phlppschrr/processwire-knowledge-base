# FilenameArray::urls()

Source: `wire/core/FilenameArray.php`

Get cache-busting URLs for this FilenameArray

This is the same as iterating this FilenameArray except that it appends cache-busting
query strings to the URLs that resolve to physical files.

@param bool|null|string $useVersion See Config::versionUrls() for arument details

@return array

@throws WireException

@see Config::versionUrls()

@since 3.0.227
