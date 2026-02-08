# $wireSaveableItems->renameReady(Saveable $item, $oldName, $newName)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be renamed.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->renameReady($item, $oldName, $newName);

// usage with all arguments
$result = $wireSaveableItems->renameReady(Saveable $item, $oldName, $newName);
~~~~~

## Hookable

- Hookable method name: `renameReady`
- Implementation: `___renameReady`
- Hook with: `$wireSaveableItems->renameReady()`

## Arguments

- `$item` `Saveable`
- `$oldName` `string`
- `$newName` `string`
