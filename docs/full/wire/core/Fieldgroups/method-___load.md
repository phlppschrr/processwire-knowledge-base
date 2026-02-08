# Fieldgroups::___load()

Source: `wire/core/Fieldgroups.php`

Load all the Fieldgroups from the database

The loading is delegated to WireSaveableItems.
After loaded, we check for any 'global' fields and add them to the Fieldgroup, if not already there.

@param WireArray $items

@param Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

@return WireArray Returns the same type as specified in the getAll() method.
