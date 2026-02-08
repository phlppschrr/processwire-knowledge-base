# $fieldgroups->save(Saveable $item): bool

Source: `wire/core/Fieldgroups.php`

Save the Fieldgroup to DB

If fields were removed from the Fieldgroup, then track them down and remove them from the associated field_* tables

## Usage

~~~~~
// basic usage
$bool = $fieldgroups->save($item);

// usage with all arguments
$bool = $fieldgroups->save(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$fieldgroups->save()`

## Arguments

- `$item` `Saveable` Fieldgroup to save

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
