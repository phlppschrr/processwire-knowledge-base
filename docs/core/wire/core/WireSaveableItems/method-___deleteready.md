# $wireSaveableItems->___deleteReady(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be deleted.

Unlike before(delete), when this runs, it has already been confirmed that the item will indeed be deleted.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___deleteReady($item);

// usage with all arguments
$result = $wireSaveableItems->___deleteReady(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`
