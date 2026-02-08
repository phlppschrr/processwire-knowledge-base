# $wireMarkupFileRegions->populateRegions(array $fileRegions, &$html, array $options = []): string

Source: `wire/core/WireMarkupFileRegions.php`

Populate file regions

## Usage

~~~~~
// basic usage
$string = $wireMarkupFileRegions->populateRegions($fileRegions, $html);

// usage with all arguments
$string = $wireMarkupFileRegions->populateRegions(array $fileRegions, &$html, array $options = []);
~~~~~

## Arguments

- `$fileRegions` `array` Regions found by findRegions()
- `$html` `string` HTML to populate them into
- `$options` (optional) `array`

## Return value

- `string` Returned value only useful if autoInsert=true

## Since

3.0.254
