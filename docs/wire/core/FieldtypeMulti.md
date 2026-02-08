# FieldtypeMulti

Source: `wire/core/FieldtypeMulti.php`

ProcessWire FieldtypeMulti

Interface and some functionality for Fieldtypes that can contain multiple values.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com



To support automatic “order by” sorting: The `$useOrderByCols` property of this Fieldtype must be set to boolean true,
indicating that the Fieldtype supports sorting. The actual columns to order by are an array of 'col' or '-col' specified
with the Field object in an $orderByCols property (array).

To support pagination: Both the `$useOrderByCols` and the `$usePagination` properties of this Fieldtype must be set to
boolean true, indicating the Fieldtype supports pagination (and sorting). When enabled, the wakeupValue() method will receive
pagination information in the value it is given. All other aspects of pagination must be handled by the individual Fieldtype.

## other

@method bool savePageFieldRows(Page $page, Field $field, $value)

@method int deletePageFieldRows(Page $page, Field $field, $value)

## multiValueSeparator

Separator for multi values when using GROUP_CONCAT()

TODO sanitize set() values from ever containing this separator

## getDatabaseSchema()

Modify the default schema provided by Fieldtype to include a 'sort' field, and integrate that into the primary key.

@param Field $field

@return array

## ___getSelectorInfo()

Return array with information about what properties and operators can be used with this field

@param Field $field

@param array $data Array of extra data, when/if needed

@return array

## ___getCompatibleFieldtypes()

Get an array of Fieldtypes that are compatible with this one (i.e. ones the user may change the type to)

@param Field $field Just in case it's needed

@return Fieldtypes|null

## getBlankValue()

Per Fieldtype interface, return a blank value of this Fieldtype

@param Page $page

@param Field $field

@return WireArray

## sanitizeValue()

Per the Fieldtype interface, sanitize the combined value for use in a Page

In this case, make sure that it's a WireArray (able to hold multiple values)

@param Page $page

@param Field $field

@param mixed $value

@return WireArray

## ___wakeupValue()

Process the value to convert it from array to whatever object it needs to be

@param Page $page

@param Field $field

@param array $value

@return WireArray

## ___sleepValue()

Given an 'awake' value, as set by wakeupValue, convert the value back to a basic type for storage in DB.

FieldtypeMulti::savePageField expects values as an array, so we convert the $value object to an array

Note that FieldtypeMulti is designed around potentially supporting more than just the 'data' field in
the table, so other fieldtypes may want to override this and return an array of associative arrays containing a 'data' field
and any other fields that map to the table. i.e. $values[] = array('data' => $data, 'description' => $description), etc.
See FieldtypePagefiles module class for an example of this.

@param Page $page

@param Field $field

@param WireArray $value

@return array

## ___savePageField()

Per the Fieldtype interface, Save the given Field from the given Page to the database

Because the number of values may have changed, this method plays it safe and deletes all the old values
and reinserts them as new.

@param Page $page

@param Field $field

@return bool

@throws \PDOException|WireException|WireDatabaseQueryException on failure

## ___loadPageField()

Load the given page field from the database table and return the value.

- Return NULL if the value is not available, or array when it is.
- Return the value as it exists in the database (as an array), without further processing.
- This is intended only to be called by Page objects on an as-needed basis.
- Typically this is only called for fields that don't have 'autojoin' turned on.
- Any actual conversion of the value should be handled by the `Fieldtype::wakeupValue()` method.

If pagination is active, the following extra properties are populated to the returned array value:

- `_pagination_limit` (int): The specified limit of items per pagination.
- `_pagination_start` (int): The starting index of the pagination.
- `_pagination_total` (int): The total number of items across all paginations.


@param Page $page Page object to save.

@param Field $field Field to retrieve from the page.

@return array|null

## getLoadQuery()

Return the query used for loading all parts of the data from this field.


@param Field $field

@param DatabaseQuerySelect $query

@return DatabaseQuerySelect

@throws WireException

## getLoadQueryWhere()

Apply a where condition to a load query (used by getLoadQuery method)

@param Field $field

@param DatabaseQuerySelect $query

@param string $col The column name

@param string $operator The comparison operator

@param mixed $value The value to find

@return DatabaseQuery $query

@throws WireException if given invalid or unrecognized arguments

## setupPageFieldRows()

Prepare rows for save or delete

@param Page $page

@param Field $field

@param $value

@return WireArray

@throws WireException

## lockForWriting()

Lock field table for writing

@param Field $field

@return bool

## unlockForWriting()

Unlock for writing

@return bool

## getMaxColumnValue()

Get max value of column for given Page and Field or boolean false (or specified $noValue) if no rows present

@param Page $page

@param Field $field

@param string $column

@param int|bool $noValue Return this value if there are no rows to count from (default=false)

@return int|bool|mixed

@throws WireException

@since 3.0.154

## getLoadQueryAutojoin()

Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.

@param Field $field

@param DatabaseQuerySelect $query

@return DatabaseQuerySelect|NULL

## getMatchQuery()

Get the query that matches a Fieldtype table's data with a given value

Possible template method: If overridden, children should NOT call this parent method.

@param PageFinderDatabaseQuerySelect $query

@param string $table The table name to use

@param string $subfield Name of the field (typically 'data', unless selector explicitly specified another)

@param string $operator The comparison operator

@param mixed $value The value to find

@return PageFinderDatabaseQuerySelect|DatabaseQuerySelect $query

## ___getConfigInputfields()

Get Inputfields for advanced settings of the Field and Fieldtype

Inputfields returned from this appear under the "Advanced" tab rather than the "Details" tab,
in the Field editor.

In most cases, you will want to implement the getConfigInputfields() or getConfigArray() rather than this method.

NOTE: Inputfields with a name that starts with an underscore, i.e. "_myname" are assumed to be for runtime
use and are NOT stored in the database.


@param Field $field

@return InputfieldWrapper
