# $commentForm->arrayOption($property, $name = '', $value = null): string|array

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentForm.php`

Get or set array property

## Usage

~~~~~
// basic usage
$string = $commentForm->arrayOption($property);

// usage with all arguments
$string = $commentForm->arrayOption($property, $name = '', $value = null);
~~~~~

## Arguments

- `$property` `string` Name of array property: labels, markup, classes, attrs, presets
- `$name` (optional) `string|array` Name of item to get or set or omit to get all, or assoc array to set all/multiple (and omit $value)
- `$value` (optional) `string|null` Value to set (if setting) or omit if getting

## Return value

- `string|array`

## Exceptions

- `WireException`

## Since

3.0.153
