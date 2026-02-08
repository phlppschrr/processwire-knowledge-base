# $wireInput->setUrlSegment($num, $value)

Source: `wire/core/WireInput.php`

Set a URL segment value

- This is typically only used by the core.
- To unset, specify NULL as the value.

## Usage

~~~~~
// basic usage
$result = $wireInput->setUrlSegment($num, $value);
~~~~~

## Arguments

- `$num` `int` Number of this URL segment (1 based)
- `$value` `string|null` Value to set, or NULL to unset.
