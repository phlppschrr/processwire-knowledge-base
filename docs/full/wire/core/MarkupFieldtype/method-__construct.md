# $markupFieldtype->__construct(?Page $page = null, ?Field $field = null, $value = null)

Source: `wire/core/MarkupFieldtype.php`

Construct the MarkupFieldtype

If you construct without providing page and field, please populate them
separately with the setPage and setField methods before calling render().

## Usage

~~~~~
// basic usage
$result = $markupFieldtype->__construct();

// usage with all arguments
$result = $markupFieldtype->__construct(?Page $page = null, ?Field $field = null, $value = null);
~~~~~

## Arguments

- `$page` (optional) `Page|null`
- `$field` (optional) `Field|null`
- `$value` (optional) `mixed`
