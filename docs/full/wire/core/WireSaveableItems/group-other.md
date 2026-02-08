# WireSaveableItems: other

Source: `wire/core/WireSaveableItems.php`

@method WireArray load(WireArray $items, $selectors = null)

@method bool save(Saveable $item)

@method bool delete(Saveable $item)

@method WireArray find($selectors)

@method void saveReady(Saveable $item)

@method void deleteReady(Saveable $item)

@method void cloneReady(Saveable $item, Saveable $copy)

@method array saved(Saveable $item, array $changes = array())

@method void added(Saveable $item)

@method void deleted(Saveable $item)

@method void cloned(Saveable $item, Saveable $copy)

@method void renameReady(Saveable $item, $oldName, $newName)

@method void renamed(Saveable $item, $oldName, $newName)
