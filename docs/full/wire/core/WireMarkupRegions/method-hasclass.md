# $wireMarkupRegions->hasClass($class, array $classes): bool|string

Source: `wire/core/WireMarkupRegions.php`

Does the given class exist in given $classes array?

## Arguments

- `$class` `string` May be class name, or class prefix if $class has "*" at end.
- `$classes` `array`

## Return value

bool|string Returns false if no match, or class name if matched
