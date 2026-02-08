# HasLookupItems

Source: `wire/core/Interfaces.php`

For classes that contain lookup items, as used by WireSaveableItemsLookup

## getLookupItems()

Get all lookup items, usually in a WireArray derived type, but specified by class

## addLookupItem()

Add a lookup item to this instance

@param int $item The ID of the item to add

@param array $row The row from which it was retrieved (in case you want to retrieve or modify other details)
