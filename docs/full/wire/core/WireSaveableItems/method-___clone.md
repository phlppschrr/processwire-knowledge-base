# WireSaveableItems::___clone()

Source: `wire/core/WireSaveableItems.php`

Create and return a cloned copy of this item

If no name is specified and the new item uses a 'name' field, it will contain a number at the end to make it unique

@param Saveable $item Item to clone

@param string $name Optionally specify new name

@return bool|Saveable $item Returns the new clone on success, or false on failure
