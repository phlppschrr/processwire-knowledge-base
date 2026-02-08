# Fieldgroups::___clone()

Source: `wire/core/Fieldgroups.php`

Create and return a cloned copy of this item

If the new item uses a 'name' field, it will contain a number at the end to make it unique

@param Saveable $item Item to clone

@param string $name

@return Fieldgroup|false $item Returns the new clone on success, or false on failure
