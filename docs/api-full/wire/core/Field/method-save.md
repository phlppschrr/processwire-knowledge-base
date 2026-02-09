# $field->save(): bool

Source: `wire/core/Field.php`

Save this field’s settings and data in the database.

To hook this save, hook to `Fields::save()` instead.

## Usage

~~~~~
// basic usage
$bool = $field->save();
~~~~~

## Return value

- `bool`
