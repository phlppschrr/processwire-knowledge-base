# $wireArray->implode($delimiter, $property = '', array $options = array()): string

Source: `wire/core/WireArray.php`

Combine all elements into a delimiter-separated string containing the given property from each item

Similar to PHP's `implode()` function.

[Introduction of implode method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

## Usage

~~~~~
// basic usage
$string = $wireArray->implode($delimiter);

// usage with all arguments
$string = $wireArray->implode($delimiter, $property = '', array $options = array());
~~~~~

## Arguments

- `$delimiter` `string` The delimiter to separate each item by (or the glue to tie them together). If not needed, this argument may be omitted and $property supplied first (also shifting $options to 2nd arg).
- `$property` (optional) `string|callable` The property to retrieve from each item, or a function that returns the value to store. If a function/closure is provided it is given the $item (argument 1) and the $key (argument 2), and it should return the value (string) to use. If delimiter is omitted, this becomes the first argument.
- `$options` (optional) `array` Optional options to modify the behavior: - `skipEmpty` (bool): Whether empty items should be skipped (default=true) - `prepend` (string): String to prepend to result. Ignored if result is blank. - `append` (string): String to append to result. Ignored if result is blank. - Please note that if delimiter is omitted, $options becomes the second argument.

## Return value

- `string`

## See Also

- [WireArray::each()](method-each.md)
- [WireArray::explode()](method-explode.md)
