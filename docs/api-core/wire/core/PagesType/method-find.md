# $pagesType->find($selectorString, $options = array()): PageArray

Source: `wire/core/PagesType.php`

Given a Selector string, return the Page objects that match in a PageArray.

## Usage

~~~~~
// basic usage
$items = $pagesType->find($selectorString);

// usage with all arguments
$items = $pagesType->find($selectorString, $options = array());
~~~~~

## Arguments

- `$selectorString` `string`
- `$options` (optional) `array` Options to modify default behavior: - `findOne` (bool): apply optimizations for finding a single page and include pages with 'hidden' status

## Return value

- `PageArray`

## See Also

- [Pages::find()](../Pages/method-___find.md)
