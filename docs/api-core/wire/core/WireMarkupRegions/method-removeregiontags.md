# $wireMarkupRegions->removeRegionTags(&$html): bool

Source: `wire/core/WireMarkupRegions.php`

Remove any <region> or <pw-region> tags present in the markup, leaving their innerHTML contents

Also removes data-pw-id and pw-id attributes

## Usage

~~~~~
// basic usage
$bool = $wireMarkupRegions->removeRegionTags($html);

// usage with all arguments
$bool = $wireMarkupRegions->removeRegionTags(&$html);
~~~~~

## Arguments

- `$html` `string`

## Return value

- `bool` True if tags or attributes were removed, false if not
