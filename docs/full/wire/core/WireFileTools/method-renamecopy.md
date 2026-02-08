# $wireFileTools->renameCopy($oldName, $newName, $options = array()): bool

Source: `wire/core/WireFileTools.php`

Rename by first copying files to destination and then deleting source files

The operation is considered successful so long as the source files were able to be copied to the destination.
If source files cannot be deleted afterwards, the warning is logged, plus a warning notice is also shown when in debug mode.

## Arguments

- `$oldName` `string` Old pathname, must be full disk path.
- `$newName` `string` New pathname, must be full disk path OR can be basename to assume same path as $oldName.
- `$options` (optional) `array` See options for rename() method

## Return value

bool

## Throws

- WireException

## Since

3.0.178
