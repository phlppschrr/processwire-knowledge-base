# $adminTheme->getClass($name = '', $getArray = false): string|array

Source: `wire/core/AdminTheme.php`

Return class for a given named item or blank if none available

Omit the first argument to return all classes in an array.

## Arguments

- `$name` (optional) `string` Tag or item name, i.e. “input”, or omit to return all defined [tags=classes]
- `$getArray` (optional) `bool` Specify true to return array of class name(s) rather than string (default=false). $name argument required.

## Return value

string|array Returns string or array of class names, or array of all [tags=classes] or $tagName argument is empty.
