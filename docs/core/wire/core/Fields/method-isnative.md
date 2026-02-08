# $fields->isNative($name): bool

Source: `wire/core/Fields.php`

Is the given field name native/permanent to the database?

Such fields are disallowed from being used for custom field names.

## Usage

~~~~~
// basic usage
$bool = $fields->isNative($name);
~~~~~

## Arguments

- `$name` `string` Field name you want to check

## Return value

- `bool` True if field is native (and thus should not be used) or false if it's okay to use
