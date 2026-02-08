# $wireSaveableItems->cloned(Saveable $item, Saveable $copy)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been cloned.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->cloned($item, $copy);

// usage with all arguments
$result = $wireSaveableItems->cloned(Saveable $item, Saveable $copy);
~~~~~

## Hookable

- Hookable method name: `cloned`
- Implementation: `___cloned`
- Hook with: `$wireSaveableItems->cloned()`

## Arguments

- `$item` `Saveable`
- `$copy` `Saveable`
