# $wireSaveableItems->___saveReady(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be saved.

Unlike before(save), when this runs, it has already been confirmed that the item will indeed be saved.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___saveReady($item);

// usage with all arguments
$result = $wireSaveableItems->___saveReady(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`
