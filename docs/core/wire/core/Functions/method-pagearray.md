# $functions->PageArray($items = array()): PageArray

Source: `wire/core/Functions.php`

Create new PageArray, add given $items (pages) to it, and return it

This is the same as creating a `new PageArray()` and then adding items to it with separate `add()` calls,
except that this function enables you to do it all in one shot.

## Example

~~~~~
$a = PageArray(); // create empty PageArray
$a = PageArray($page); // create PageArray with one page
$a = PageArray([ $page1, $page2, $page3 ]); // create PageArray with multiple items
~~~~~

## Usage

~~~~~
// basic usage
$items = $functions->PageArray();

// usage with all arguments
$items = $functions->PageArray($items = array());
~~~~~

## Arguments

- `$items` (optional) `array|PageArray`

## Return value

- `PageArray`

## Since

3.0.123
