# $wireMarkupRegions->stripRegions($tag, $markup, $getRegions = false): string|array

Source: `wire/core/WireMarkupRegions.php`

Strip the given region non-nested tags from the document

Note that this only works on non-nested tags like HTML comments, script or style tags.

## Arguments

- string $tag Specify "<!--" to remove comments or "<script" to remove scripts, or "<tag" for any other tags.
- string $markup Markup to remove the tags from
- bool $getRegions Specify true to return array of the strip regions rather than the updated markup

## Return value

string|array
