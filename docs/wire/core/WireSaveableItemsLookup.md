# WireSaveableItemsLookup

Source: `wire/core/WireSaveableItemsLookup.php`

ProcessWire WireSaveableItemsLookup

Provides same functionality as WireSaveableItems except that this class includes joining/modification of a related lookup table

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## getLookupTable()

If a lookup table should be left joined, this method should return the table name

## getLookupField()

If a lookup table should be left joined, this method returns the name of the array field in $data that contains multiple values

i.e. roles_permissions becomes permissions_id if getTable() returns roles
Does not need to be overridden unless the table naming structure doesn't follow existing logic.

## getLoadQuery()

Get the DatabaseQuerySelect to perform the load operation of items

@param Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

@return DatabaseQuerySelect

## ___load()

Load items from the database table and return them in the same type class that getAll() returns

A selector string or Selectors may be provided so that this can be used as a find() by descending classes that don't load all items at once.

@param WireArray $items

@param Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

@return WireArray Returns the same type as specified in the getAll() method.

## initItem()

Create a new Saveable/Lookup item from a raw array ($row) and add it to $items

@param array $row

@param WireArray|null $items

@return Saveable|HasLookupItems|WireData|Wire

@since 3.0.194

## saveItemKey()

Should the given item key/field be saved in the database?

Template method used by ___save()

@param string $key

@return bool

## ___save()

Save the provided item to database

@param Saveable $item

@return bool

@throws WireException

## ___delete()

Delete the provided item from the database

@param Saveable $item

@return bool

## __debugInfo()

debugInfo PHP 5.6+ magic method

This is used when you print_r() an object instance.

@return array
