# $pageArray->getSelectors($getString = false): Selectors|string|null

Source: `wire/core/PageArray.php`

Return the Selectors that led to this PageArray, or null if not set/applicable.

Use this to retrieve the Selectors that were used to find this group of pages,
if dealing with a PageArray that originated from a database operation.

~~~~~
$products = $pages->find("template=product, featured=1, sort=-modified, limit=10");
echo $products->getSelectors(); // outputs the selector above
~~~~~

## Arguments

- `$getString` (optional) `bool` Specify true to get selector string rather than Selectors object (default=false) added in 3.0.142

## Return value

Selectors|string|null Returns Selectors object if available, or null if not. Always return string if $getString argument is true.
