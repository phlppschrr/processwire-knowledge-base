# $pagesParents->getParents($page, array $options = array()): array|PageArray

Source: `wire/core/PagesParents.php`

Get parents for given Page and/or specific columns from them

- Return value has no exclusions for access control or status.
- Return value order is closest parent to furthest.
- This attempts to return all pages in 1 optimized query, making it potentially faster
  than other methods.
- When using `column` or `columns` options, specify only one or the other, and include
  column(s) native to pages DB table only, with 1 exception—you may specify `path` as
  a column, which will return the generated page path(s).

## Arguments

- `$page` `Page|int` Page or page ID
- `$options` (optional) `array` - `column` (string): Just return array of values from this column (use `columns` option when you need multiple columns). (default='') - `columns` (array): Return array of associative arrays containing these columns for each page (not to be combined with `column` option) - `indexBy` (string): Return array indexed by column `id` or `parent_id`, applies only if given column/columns (default='') - `includePage` (bool): Also include data for given $page in return value? (default=false) - `noHome` (bool): Omit homepage from return value (default=false) - `joinQty` (int): Number of parents to join in query before going recursive, for internal use (default=4).

## Return value

array|PageArray If given column/columns returns an array, otherwise returns a PageArray

## Since

3.0.156
