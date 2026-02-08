# PagesType::find()

Source: `wire/core/PagesType.php`

Given a Selector string, return the Page objects that match in a PageArray.

@param string $selectorString

@param array $options Options to modify default behavior:
 - `findOne` (bool): apply optimizations for finding a single page and include pages with 'hidden' status

@return PageArray

@see Pages::find()
