# WireSaveableItems::___saved()

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been saved.

Unlike after(save), when this runs, it has already been confirmed that the item has been saved (no need to error check).

@param Saveable $item

@param array $changes
