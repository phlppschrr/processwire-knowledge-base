# $pageFinder->hasNativeFieldName($fieldNames): bool

Source: `wire/core/PageFinder.php`

Are any of the given field name(s) native to PW system?

This is primarily used to determine whether the getQueryNativeField() method should be called.

## Arguments

- `$fieldNames` `string|array|Selector` Single field name, array of field names or pipe-separated string of field names

## Return value

bool
