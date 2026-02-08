# Fieldgroups

Source: `wire/core/Fieldgroups.php`

ProcessWire Fieldgroups

Maintains collections of Fieldgroup object instances and represents the `$fieldgroups` API variable.
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.
$fieldgroups

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method Fieldgroup clone(Saveable $item, $name = '')

@method int saveContext(Fieldgroup $fieldgroup)

@method array getExportData(Fieldgroup $fieldgroup)

@method array setImportData(Fieldgroup $fieldgroup, array $data)

@method void fieldRemoved(Fieldgroup $fieldgroup, Field $field)

@method void fieldAdded(Fieldgroup $fieldgroup, Field $field)

## init()

Init

## getLoadQuery()

Get the DatabaseQuerySelect to perform the load operation of items

@param Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

@return DatabaseQuerySelect

## ___load()

Load all the Fieldgroups from the database

The loading is delegated to WireSaveableItems.
After loaded, we check for any 'global' fields and add them to the Fieldgroup, if not already there.

@param WireArray $items

@param Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

@return WireArray Returns the same type as specified in the getAll() method.

## getAll()

Per WireSaveableItems interface, return all available Fieldgroup instances

@return FieldgroupsArray

## getWireArray()

@return WireArray|FieldgroupsArray

## makeBlankItem()

Per WireSaveableItems interface, create a blank instance of a Fieldgroup

@return Fieldgroup

## getTable()

Per WireSaveableItems interface, return the name of the table that Fieldgroup instances are stored in

@return string

## getLookupTable()

Per WireSaveableItemsLookup interface, return the name of the table that Fields are linked to Fieldgroups

@return string

## getNumTemplates()

Get the number of templates using the given fieldgroup.

Primarily used to determine if the Fieldgroup is deleteable.

@param Fieldgroup $fieldgroup

@return int

## getTemplates()

Given a Fieldgroup, return a TemplatesArray of all templates using the Fieldgroup

@param Fieldgroup $fieldgroup

@return TemplatesArray

## getFieldNames()

Get all field names used by given fieldgroup

Use this when you want to identify the field names (or IDs) without loading the fieldgroup or fields in it.

@param string|int|Fieldgroup $fieldgroup Fieldgroup name, ID or object

@return array Returned array of field names indexed by field ID

@since 3.0.194

## ___save()

Save the Fieldgroup to DB

If fields were removed from the Fieldgroup, then track them down and remove them from the associated field_* tables

@param Saveable $item Fieldgroup to save

@return bool True on success, false on failure

@throws WireException

## ___delete()

Delete the given fieldgroup from the database

Also deletes the references in fieldgroups_fields table

@param Saveable|Fieldgroup $item

@return bool

@throws WireException

## deleteField()

Delete the entries in fieldgroups_fields for the given Field

@param Field $field

@return bool

## ___clone()

Create and return a cloned copy of this item

If the new item uses a 'name' field, it will contain a number at the end to make it unique

@param Saveable $item Item to clone

@param string $name

@return Fieldgroup|false $item Returns the new clone on success, or false on failure

## ___saveContext()

Save contexts for all fields in the given fieldgroup

@param Fieldgroup $fieldgroup

@return int Number of field contexts saved

## ___getExportData()

Export config data for the given fieldgroup

@param Fieldgroup $fieldgroup

@return array

## ___setImportData()

Given an export data array, import it back to the class and return what happened

Changes are not committed until the item is saved

@param Fieldgroup $fieldgroup

@param array $data

@return array Returns array(
	[property_name] => array(
		'old' => 'old value',	// old value, always a string
		'new' => 'new value',	// new value, always a string
		'error' => 'error message or blank if no error'
	)

@throws WireException if given invalid data

## ___fieldAdded()

Hook called when field has been added to fieldgroup


@param Fieldgroup $fieldgroup

@param Field $field

@since 3.0.193

## ___fieldRemoved()

Hook called when field has been removed from fieldgroup


@param Fieldgroup $fieldgroup

@param Field $field

@since 3.0.193
