# $wireSaveableItems->renamed(Saveable $item, $oldName, $newName)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been renamed.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->renamed($item, $oldName, $newName);

// usage with all arguments
$result = $wireSaveableItems->renamed(Saveable $item, $oldName, $newName);
~~~~~

## Hookable

- Hookable method name: `renamed`
- Implementation: `___renamed`
- Hook with: `$wireSaveableItems->renamed()`

## Arguments

- `$item` `Saveable`
- `$oldName` `string`
- `$newName` `string`
