# $pageFinder->findVerboseIDs($selectors, $options = array()): array|DatabaseQuerySelect

Source: `wire/core/PageFinder.php`

Returns array of arrays with all columns in pages table indexed by page ID

## Arguments

- Selectors|string|array $selectors Selectors object, selector string or selector array
- array $options - `joinFields` (array): Names of additional fields to join (default=[]) 3.0.172+ - `joinSortfield` (bool): Include 'sortfield' in returned columns? Joined from pages_sortfields table. (default=false) 3.0.172+ - `getNumChildren` (bool): Include 'numChildren' in returned columns? Calculated in query. (default=false) 3.0.172+ - `unixTimestamps` (bool): Return created/modified/published dates as unix timestamps rather than ISO-8601? (default=false) 3.0.172+

## Return value

array|DatabaseQuerySelect

## Meta

- @since 3.0.153
