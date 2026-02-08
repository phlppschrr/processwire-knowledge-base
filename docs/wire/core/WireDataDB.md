# WireDataDB

Source: `wire/core/WireDataDB.php`

WireData with database storage

A WireData object that maintains its data in a database table rather than just in memory.
An example of usage is the `$page->meta()` method.

ProcessWire 3.x, Copyright 2023
https://processwire.com

## __construct()

Construct

@param int $sourceID ID of the source item this WireData is maintaining/persisting data for.

@param string $tableName Name of the table to store data in. If it does not exist, it will be created.

## get()

Get the value for a specific property/name/key

@param string $key

@return array|mixed|null

@throws WireException

## getArray()

Get all values in an associative array

@return array|mixed|null

@throws WireException

## set()

Set and save a value for a specific property/name/key

@param string $key

@param mixed $value

@return self

@throws WireException

## remove()

Remove value for a specific property/name/key

@param string $key

@return self

@throws WireException

## removeAll()

Remove all values for sourceID from the DB

@return $this

## reset()

Reset all loaded data so that it will re-load from DB on next access

@return $this

## delete()

Delete meta value or all meta values (if you specify true)

@param string|bool $name Meta property name to delete or specify boolean true for all

@return int Number of rows deleted

@throws WireException

## load()

Load a value or all values

@param string|bool $name Property name to load or boolean true to load all

@return array|mixed|null

@throws WireException

## save()

Save a value

@param string $name

@param mixed $value

@param bool $recursive

@return bool

@throws WireException

## sourceID()

Get or set the the source ID for this instance

@param int|null $id

@return int

@throws WireException

## count()

Count the number of rows this WireDataDB maintains in the database for source ID.

This implements the \Countable interface.

@return int

## copyTo()

Copy all data to a new source ID

Useful to call on the source object after a clone has been created from it.

@param int $newSourceID

@throws WireException

@return int Number of rows copied

## table()

Get the current table name

@param string $tableName

@return string

## schema()

Get DB schema in an array

@return array

## install()

Install the table

@return bool

@throws WireException

## uninstall()

Uninstall the table

@return bool

@throws WireException
