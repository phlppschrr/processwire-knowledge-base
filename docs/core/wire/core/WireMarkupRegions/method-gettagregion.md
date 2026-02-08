# $wireMarkupRegions->getTagRegion($region, array $tagInfo, array $options): array|string

Source: `wire/core/WireMarkupRegions.php`

Given all markup after a tag, return just the portion that is the tag body/region

## Arguments

- string $region Markup that occurs after the ">" of the tag you want to get the region of.
- array $tagInfo Array returned by getTagInfo method.
- array $options Options to modify behavior, see getMarkupRegions $options argument. - `verbose` (bool): Verbose mode (default=false) - `wrap` (bool): Whether or not wrapping markup should be included (default=false)

## Return value

array|string Returns string except when verbose mode enabled it returns array.
