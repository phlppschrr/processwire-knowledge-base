# $fieldtypes->get($key): Fieldtype|null

Source: `wire/core/Fieldtypes.php`

Given a Fieldtype name (or class name) return the instantiated Fieldtype module.

If the requested Fieldtype is not already installed, it will be installed here automatically.

## Arguments

- string $key Fieldtype name or class name, or dynamic property of Fieldtypes

## Return value

Fieldtype|null
