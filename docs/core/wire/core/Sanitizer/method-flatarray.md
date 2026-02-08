# $sanitizer->flatArray($value, $options = array()): array

Source: `wire/core/Sanitizer.php`

Given a potentially multi-dimensional array, return a flat 1-dimensional array

## Arguments

- array $value
- array $options - `preserveKeys` (bool): Preserve associative array keys where possible? (default=false) - `maxDepth` (int): Max depth of nested arrays to flatten into value, after which they are discarded (default=0). The default value of 0 removes any nested arrays, so specify 1 or higher to include them.

## Return value

array

## Meta

- @since 3.0.160
