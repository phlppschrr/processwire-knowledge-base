# $wireFileTools->renameCopy($oldName, $newName, $options = array()): bool

Source: `wire/core/WireFileTools.php`

Rename by first copying files to destination and then deleting source files

The operation is considered successful so long as the source files were able to be copied to the destination.
If source files cannot be deleted afterwards, the warning is logged, plus a warning notice is also shown when in debug mode.

## Arguments

- string $oldName Old pathname, must be full disk path.
- string $newName New pathname, must be full disk path OR can be basename to assume same path as $oldName.
- array $options See options for rename() method

## Return value

bool

## Throws

- WireException

## Meta

- @since 3.0.178
