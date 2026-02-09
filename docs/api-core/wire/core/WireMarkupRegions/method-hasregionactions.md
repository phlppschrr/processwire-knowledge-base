# $wireMarkupRegions->hasRegionActions(&$html): bool

Source: `wire/core/WireMarkupRegions.php`

Does the given HTML markup have references to any pw-actions?

## Usage

~~~~~
// basic usage
$bool = $wireMarkupRegions->hasRegionActions($html);

// usage with all arguments
$bool = $wireMarkupRegions->hasRegionActions(&$html);
~~~~~

## Arguments

- `$html` `string`

## Return value

- `bool`
