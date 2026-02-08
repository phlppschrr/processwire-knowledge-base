# $fieldgroup->getFieldContext($key, $namespace = ''): Field|null

Source: `wire/core/Fieldgroup.php`

Get a Field that is part of this Fieldgroup, in the context of this Fieldgroup.

Returned Field will be a clone of the original with additional context data
already populated to it.

## Arguments

- string|int|Field $key Field object, name or id.
- string $namespace Optional namespace string for context

## Return value

Field|null
