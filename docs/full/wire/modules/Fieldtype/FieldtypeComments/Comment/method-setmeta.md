# $comment->setMeta($key, $value = null): self

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Set meta data (custom fields for comments)

To set multiple properties at once specify an associative array for $key and omit $value.

## Usage

~~~~~
// basic usage
$result = $comment->setMeta($key);

// usage with all arguments
$result = $comment->setMeta($key, $value = null);
~~~~~

## Arguments

- `$key` `string|array` Property name to set or assoc array of them
- `$value` (optional) `null|string|array|int|float|mixed` Value to set for $key or omit of you used an array.

## Return value

- `self`

## Since

3.0.203
