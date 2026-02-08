# $fieldgroups->getNumTemplates(Fieldgroup $fieldgroup): int

Source: `wire/core/Fieldgroups.php`

Get the number of templates using the given fieldgroup.

Primarily used to determine if the Fieldgroup is deleteable.

## Usage

~~~~~
// basic usage
$int = $fieldgroups->getNumTemplates($fieldgroup);

// usage with all arguments
$int = $fieldgroups->getNumTemplates(Fieldgroup $fieldgroup);
~~~~~

## Arguments

- `$fieldgroup` `Fieldgroup`

## Return value

- `int`
