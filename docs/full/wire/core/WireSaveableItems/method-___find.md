# $wireSaveableItems->___find($selectors): WireArray

Source: `wire/core/WireSaveableItems.php`

Find items based on Selectors or selector string

This is a delegation to the WireArray associated with this DAO.
This method assumes that all items are loaded. Desecending classes that don't load all items should
override this to the ___load() method instead.

## Usage

~~~~~
// basic usage
$items = $wireSaveableItems->___find($selectors);
~~~~~

## Arguments

- `$selectors` `Selectors|string`

## Return value

- `WireArray`
