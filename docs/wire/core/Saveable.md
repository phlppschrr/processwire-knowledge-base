# Saveable

Source: `wire/core/Interfaces.php`

For classes that are saved to a database or disk.

Item must have a gettable/settable 'id' property for this interface as well

## other

@property int $id

@property string $name

## save()

Save the object's current state to database.

## getTableData()

Get an array of this item's saveable data, should match exact with the table it saves in

@return array
