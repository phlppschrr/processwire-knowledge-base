# Fieldgroup::add()

Source: `wire/core/Fieldgroup.php`

Add a field to this Fieldgroup

~~~~~
$field = $fields->get('body');
$fieldgroup->add($field);
~~~~~


@param Field|string $item Field object, field name or id.

@return $this

@throws WireException
