# $wireMarkupRegions->mergeTags($htmlTag, $mergeTag): string

Source: `wire/core/WireMarkupRegions.php`

Merge attributes from one HTML tag to another

- Attributes (except class) that appear in $mergeTag replace those in $htmlTag.
- Attributes in $mergeTag not already present in $htmlTag are added to it.
- Class attribute is combined with all classes from $htmlTag and $mergeTag.
- The tag name from $htmlTag is used, and the one from $mergeTag is ignored.

## Arguments

- string $htmlTag HTML tag string, optionally containing attributes
- array|string $mergeTag HTML tag to merge (or attributes array)

## Return value

string Updated HTML tag string with merged attributes
