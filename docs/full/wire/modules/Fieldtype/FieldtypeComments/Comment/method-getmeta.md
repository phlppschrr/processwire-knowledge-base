# $comment->getMeta($key = null): string|array|int|float|mixed|null

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Get meta data property value (custom fields for comments)

Note: values returned are exactly as they were set and do not go through any runtime
formatting for HTML entities or anything like that. Be sure to provide your own formatting
where necessary.

## Usage

~~~~~
// basic usage
$string = $comment->getMeta();

// usage with all arguments
$string = $comment->getMeta($key = null);
~~~~~

## Arguments

- `$key` (optional) `null|string` Name of property to get

## Return value

- `string|array|int|float|mixed|null` Returns value or null if not found

## Since

3.0.203
