# WirePaginatable

Source: `wire/core/Interfaces.php`

Interface that indicates the object supports its items being paginated

## setTotal()

Set the total number of items, if more than are in the WireArray.

@param int $total

@return $this

## getTotal()

Get the total number of items in all paginations of the WireArray.

If no limit used, this returns total number of items currently in the WireArray.

@return int

## setLimit()

Set the limit that was used in pagination.

@param int $numLimit

@return $this

## getLimit()

Get the limit that was used in pagination.

If no limit set, then return number of items currently in this WireArray.

@return int

## setStart()

Set the starting offset that was used for pagination.

@param int $numStart;

@return $this

## getStart()

Get the starting offset that was used for pagination.

@return int
