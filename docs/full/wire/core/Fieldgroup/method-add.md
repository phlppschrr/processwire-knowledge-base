# $fieldgroup->add($item): $this

Source: `wire/core/Fieldgroup.php`

Add a field to this Fieldgroup

## Example

~~~~~
$field = $fields->get('body');
$fieldgroup->add($field);
~~~~~

## Usage

~~~~~
// basic usage
$result = $fieldgroup->add($item);
~~~~~

## Arguments

- `$item` `Field|string` Field object, field name or id.

## Return value

- `$this`

## Exceptions

- `WireException`
