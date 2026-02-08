# WireMarkupRegions::getTagRegion()

Source: `wire/core/WireMarkupRegions.php`

Given all markup after a tag, return just the portion that is the tag body/region

@param string $region Markup that occurs after the ">" of the tag you want to get the region of.

@param array $tagInfo Array returned by getTagInfo method.

@param array $options Options to modify behavior, see getMarkupRegions $options argument.
 - `verbose` (bool): Verbose mode (default=false)
 - `wrap` (bool): Whether or not wrapping markup should be included (default=false)

@return array|string Returns string except when verbose mode enabled it returns array.
