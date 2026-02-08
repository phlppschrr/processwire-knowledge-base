# $fieldgroup->add($item): $this

Source: `wire/core/Fieldgroup.php`

Add a field to this Fieldgroup

~~~~~
$field = $fields->get('body');
$fieldgroup->add($field);
~~~~~

## Arguments

- Field|string $item Field object, field name or id.

## Return value

$this

## Throws

- WireException
