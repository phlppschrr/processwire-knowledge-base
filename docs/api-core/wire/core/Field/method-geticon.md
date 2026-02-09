# $field->getIcon($prefix = false): mixed|string

Source: `wire/core/Field.php`

Return the icon used by this field, or blank if none.

## Usage

~~~~~
// basic usage
$result = $field->getIcon();

// usage with all arguments
$result = $field->getIcon($prefix = false);
~~~~~

## Arguments

- `$prefix` (optional) `bool` Whether or not you want the icon prefix included (i.e. "fa-")

## Return value

- `mixed|string`
