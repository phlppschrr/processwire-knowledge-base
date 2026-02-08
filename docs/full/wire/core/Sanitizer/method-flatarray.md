# Sanitizer::flatArray()

Source: `wire/core/Sanitizer.php`

Given a potentially multi-dimensional array, return a flat 1-dimensional array


@param array $value

@param array $options
 - `preserveKeys` (bool): Preserve associative array keys where possible? (default=false)
 - `maxDepth` (int): Max depth of nested arrays to flatten into value, after which they are discarded (default=0).
    The default value of 0 removes any nested arrays, so specify 1 or higher to include them.

@return array

@since 3.0.160
