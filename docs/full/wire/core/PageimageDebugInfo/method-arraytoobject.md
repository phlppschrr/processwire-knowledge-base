# $pageimageDebugInfo->arrayToObject($array, &$object, $multidim = true): object

Source: `wire/core/PageimageDebugInfo.php`

Helper method that converts a multidim array to a multidim object for the getDebugInfo method

## Arguments

- `$array` `array` the input array
- `$object` `object` the initial object, gets passed recursive by reference through all loops
- `$multidim` (optional) `bool` set this to true to avoid multidimensional object

## Return value

object the final multidim object
