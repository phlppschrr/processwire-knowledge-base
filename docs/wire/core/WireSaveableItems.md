# WireSaveableItems

Source: `wire/core/WireSaveableItems.php`

ProcessWire WireSaveableItems

Wire Data Access Object, provides reusable capability for loading, saving, creating, deleting,
and finding items of descending class-defined types.

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## other

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

## getAll()

Return the WireArray that this DAO stores it's items in

@return WireArray

## makeBlankItem()

Return a new blank item

@return Saveable|Wire

## makeItem()

Make an item and populate with given data

@param array $a Associative array of data to populate

@return Saveable|WireData|Wire

@throws WireException

@since 3.0.146

## getTable()

Return the name of the table that this DAO stores item records in

@return string

## getSort()

Return the default name of the field that load() should sort by (default is none)

This is overridden by selectors if applied during the load method

@return string

## getLoadQuerySelectors()

Provides additions to the ___load query for when selectors or selector string are provided

@param Selectors $selectors

@param DatabaseQuerySelect $query

@throws WireException

@return DatabaseQuerySelect

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

## loadRowsReady()

Called after rows loaded from DB but before populated to this instance

@param array $rows

## initItem()

Create a new Saveable item from a raw array ($row) and add it to $items

@param array $row

@param WireArray|null $items

@return Saveable|WireData|Wire

@since 3.0.194

## saveItemKey()

Should the given item key/field be saved in the database?

Template method used by ___save()

@param string $key

@return bool

## ___save()

Save the provided item to database

@param Saveable $item The item to save

@return bool Returns true on success, false on failure

@throws WireException

## ___delete()

Delete the provided item from the database

@param Saveable $item Item to save

@return bool Returns true on success, false on failure

@throws WireException

## ___clone()

Create and return a cloned copy of this item

If no name is specified and the new item uses a 'name' field, it will contain a number at the end to make it unique

@param Saveable $item Item to clone

@param string $name Optionally specify new name

@return bool|Saveable $item Returns the new clone on success, or false on failure

## ___find()

Find items based on Selectors or selector string

This is a delegation to the WireArray associated with this DAO.
This method assumes that all items are loaded. Desecending classes that don't load all items should
override this to the ___load() method instead.

@param Selectors|string $selectors

@return WireArray

## get()

Get an item

@param string|int $key

@return array|mixed|null|Page|Saveable|Wire|WireData

## has()

Do we have the given item or item by given key?

@param string|int|Saveable|WireData $item

@return bool

## __isset()

Isset

@param string|int $key

@return bool

## encodeData()

Encode the 'data' portion of the table.

This is a front-end to wireEncodeJSON so that it can be overridden if needed.

@param array $value

@return string

## decodeData()

Decode the 'data' portion of the table.

This is a front-end to wireDecodeJSON that it can be overridden if needed.

@param string $value

@return array

## useFuel()

Enforce no locally-scoped fuel for this class

@param bool|null $useFuel

@return bool

## ___saveReady()

***********************************************************************************
HOOKERS

## ___saveReady()

Hook that runs right before item is to be saved.

Unlike before(save), when this runs, it has already been confirmed that the item will indeed be saved.

@param Saveable $item

## ___deleteReady()

Hook that runs right before item is to be deleted.

Unlike before(delete), when this runs, it has already been confirmed that the item will indeed be deleted.

@param Saveable $item

## ___cloneReady()

Hook that runs right before item is to be cloned.

@param Saveable $item

@param Saveable $copy

## ___renameReady()

Hook that runs right before item is to be renamed.

@param Saveable $item

@param string $oldName

@param string $newName

## ___saved()

Hook that runs right after an item has been saved.

Unlike after(save), when this runs, it has already been confirmed that the item has been saved (no need to error check).

@param Saveable $item

@param array $changes

## ___added()

Hook that runs right after a new item has been added.

@param Saveable $item

## ___deleted()

Hook that runs right after an item has been deleted.

Unlike after(delete), it has already been confirmed that the item was indeed deleted.

@param Saveable $item

## ___cloned()

Hook that runs right after an item has been cloned.

@param Saveable $item

@param Saveable $copy

## ___renamed()

Hook that runs right after an item has been renamed.

@param Saveable $item

@param string $oldName

@param string $newName

## __invoke()

***********************************************************************************
OTHER

## __invoke()

Enables use of $apivar('name') or wire()->apivar('name')

@param $key

@return Wire|null

## log()

Save to activity log, if enabled in config

@param $str

@param Saveable|null Item to log

@return WireLog

## error()

Record an error

@param string $text

@param int|bool $flags See Notices::flags

@return Wire|WireSaveableItems

## __debugInfo()

debugInfo PHP 5.6+ magic method

This is used when you print_r() an object instance.

@return array

## useLazy()

Use lazy loading for this type?

@return bool

@since 3.0.194

## unsetLazy()

Remove item from lazy loading data/indexes

@param Saveable $item

@return bool
