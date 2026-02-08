# $wireSaveableItems->cloneReady(Saveable $item, Saveable $copy)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be cloned.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->cloneReady($item, $copy);

// usage with all arguments
$result = $wireSaveableItems->cloneReady(Saveable $item, Saveable $copy);
~~~~~

## Hookable

- Hookable method name: `cloneReady`
- Implementation: `___cloneReady`
- Hook with: `$wireSaveableItems->cloneReady()`

## Arguments

- `$item` `Saveable`
- `$copy` `Saveable`
