# $wireInput->setUrlSegment($num, $value)

Source: `wire/core/WireInput.php`

Set a URL segment value

- This is typically only used by the core.
- To unset, specify NULL as the value.

## Arguments

- int $num Number of this URL segment (1 based)
- string|null $value Value to set, or NULL to unset.
