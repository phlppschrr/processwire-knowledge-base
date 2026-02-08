# $wireSaveableItems->___renamed(Saveable $item, $oldName, $newName)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been renamed.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___renamed($item, $oldName, $newName);

// usage with all arguments
$result = $wireSaveableItems->___renamed(Saveable $item, $oldName, $newName);
~~~~~

## Arguments

- `$item` `Saveable`
- `$oldName` `string`
- `$newName` `string`
