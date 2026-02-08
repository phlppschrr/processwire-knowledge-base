# WireSaveableItems::___saveReady()

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be saved.

Unlike before(save), when this runs, it has already been confirmed that the item will indeed be saved.

@param Saveable $item
