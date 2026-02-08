# $fields->___applySetupName(Field $field, $setupName = ''): bool

Source: `wire/core/Fields.php`

Setup a new field using predefined setup name(s) from the Field’s fieldtype

If no setupName is provided then this method doesn’t do anything, but hooks to it might.

## Usage

~~~~~
// basic usage
$bool = $fields->___applySetupName($field);

// usage with all arguments
$bool = $fields->___applySetupName(Field $field, $setupName = '');
~~~~~

## Arguments

- `$field` `Field` Newly created field
- `$setupName` (optional) `string` Setup name to apply

## Return value

- `bool` True if setup was appled, false if not

## Since

3.0.213
