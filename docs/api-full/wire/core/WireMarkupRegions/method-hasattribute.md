# $wireMarkupRegions->hasAttribute($name, $value, &$html): bool

Source: `wire/core/WireMarkupRegions.php`

Does the given attribute name and value appear somewhere in the given html?

## Usage

~~~~~
// basic usage
$bool = $wireMarkupRegions->hasAttribute($name, $value, $html);

// usage with all arguments
$bool = $wireMarkupRegions->hasAttribute($name, $value, &$html);
~~~~~

## Arguments

- `$name` `string`
- `$value` `string|bool` Value to find, or specify boolean true for boolean attribute without value
- `$html` `string`

## Return value

- `bool` Returns false if it doesn't appear, true if it does
