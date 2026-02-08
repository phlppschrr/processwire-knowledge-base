# $fieldgroups->saveContext(Fieldgroup $fieldgroup): int

Source: `wire/core/Fieldgroups.php`

Save contexts for all fields in the given fieldgroup

## Usage

~~~~~
// basic usage
$int = $fieldgroups->saveContext($fieldgroup);

// usage with all arguments
$int = $fieldgroups->saveContext(Fieldgroup $fieldgroup);
~~~~~

## Hookable

- Hookable method name: `saveContext`
- Implementation: `___saveContext`
- Hook with: `$fieldgroups->saveContext()`

## Arguments

- `$fieldgroup` `Fieldgroup`

## Return value

- `int` Number of field contexts saved
