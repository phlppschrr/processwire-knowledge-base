# $wireSaveableItems->___renameReady(Saveable $item, $oldName, $newName)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be renamed.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___renameReady($item, $oldName, $newName);

// usage with all arguments
$result = $wireSaveableItems->___renameReady(Saveable $item, $oldName, $newName);
~~~~~

## Arguments

- `$item` `Saveable`
- `$oldName` `string`
- `$newName` `string`
