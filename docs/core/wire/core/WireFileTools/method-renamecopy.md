# WireFileTools::renameCopy()

Source: `wire/core/WireFileTools.php`

Rename by first copying files to destination and then deleting source files

The operation is considered successful so long as the source files were able to be copied to the destination.
If source files cannot be deleted afterwards, the warning is logged, plus a warning notice is also shown when in debug mode.


@param string $oldName Old pathname, must be full disk path.

@param string $newName New pathname, must be full disk path OR can be basename to assume same path as $oldName.

@param array $options See options for rename() method

@return bool

@throws WireException

@since 3.0.178
