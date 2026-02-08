# $pagesType->find($selectorString, $options = array()): PageArray

Source: `wire/core/PagesType.php`

Given a Selector string, return the Page objects that match in a PageArray.

## Arguments

- string $selectorString
- array $options Options to modify default behavior: - `findOne` (bool): apply optimizations for finding a single page and include pages with 'hidden' status

## Return value

PageArray

## See also

- [Pages::find()](../Pages/method-___find.md)
