# $comment->meta($key = null, $value = null): array|string|int|mixed

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Get or set meta data property

## Usage

~~~~~
// basic usage
$array = $comment->meta();

// usage with all arguments
$array = $comment->meta($key = null, $value = null);
~~~~~

## Arguments

- `$key` (optional) `string|array` Property to get/set or omit to get all.
- `$value` (optional) `mixed|null` Value to set for given property ($key) or omit if getting.

## Return value

- `array|string|int|mixed` Returns value for $key or null if it does not exist. Returns array when getting all.

## Since

3.0.203
