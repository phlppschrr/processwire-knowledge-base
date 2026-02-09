# $wireSaveableItemsLookup->getLookupField()

Source: `wire/core/WireSaveableItemsLookup.php`

If a lookup table should be left joined, this method returns the name of the array field in $data that contains multiple values

i.e. roles_permissions becomes permissions_id if getTable() returns roles
Does not need to be overridden unless the table naming structure doesn't follow existing logic.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItemsLookup->getLookupField();
~~~~~
