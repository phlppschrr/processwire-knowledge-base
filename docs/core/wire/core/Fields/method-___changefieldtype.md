# $fields->___changeFieldtype(Field $field1, $keepSettings = false): bool

Source: `wire/core/Fields.php`

Change a field's type

## Usage

~~~~~
// basic usage
$bool = $fields->___changeFieldtype($field1);

// usage with all arguments
$bool = $fields->___changeFieldtype(Field $field1, $keepSettings = false);
~~~~~

## Arguments

- `$field1` `Field` Field with the new type already assigned
- `$keepSettings` (optional) `bool` Whether or not to keep custom $data settings (default=false)

## Return value

- `bool`

## Exceptions

- `WireException`
