# $pageFinder->___find($selectors, array $options = array()): array|DatabaseQuerySelect

Source: `wire/core/PageFinder.php`

Return all pages matching the given selector.

## Usage

~~~~~
// basic usage
$array = $pageFinder->___find($selectors);

// usage with all arguments
$array = $pageFinder->___find($selectors, array $options = array());
~~~~~

## Arguments

- `$selectors` `Selectors|string|array` Selectors object, selector string or selector array
- `$options` (optional) `array` - `findOne` (bool): Specify that you only want to find 1 page and don't need info for pagination (default=false). - `findHidden` (bool): Specify that it's okay for hidden pages to be included in the results (default=false). - `findUnpublished` (bool): Specify that it's okay for hidden AND unpublished pages to be included in the results (default=false). - `findTrash` (bool): Specify that it's okay for hidden AND unpublished AND trashed pages to be included in the results (default=false). - `findAll` (bool): Specify that no page should be excluded - results can include unpublished, trash, system, no-access pages, etc. (default=false) - `getTotal` (bool|null): Whether the total quantity of matches should be determined and accessible from getTotal() method call. - null: determine automatically (default is disabled when limit=1, enabled in all other cases). - true: always calculate total. - false: never calculate total. - `getTotalType` (string): Method to use to get total, specify 'count' or 'calc' (default='calc'). - `returnQuery` (bool): When true, only the DatabaseQuery object is returned by find(), for internal use. (default=false) - `loadPages` (bool): This is an optimization used by the Pages::find() method, but we observe it here as we may be able to apply some additional optimizations in certain cases. For instance, if loadPages=false, then we can skip retrieval of IDs and omit sort fields. (default=true) - `stopBeforeID` (int): Stop loading pages once a page matching this ID is found. Page having this ID will be excluded as well (default=0). - `startAfterID` (int): Start loading pages once a page matching this ID is found. Page having this ID will be excluded as well (default=0). - `reverseSort` (bool): Reverse whatever sort is specified. - `returnVerbose` (bool): When true, this function returns array of arrays containing page ID, parent ID, template ID and score. When false, returns only an array of page IDs. True is required by most usage from Pages class. False is only for specific cases. - `returnParentIDs` (bool): Return parent IDs only? (default=false, requires that 'returnVerbose' option is false). - `returnTemplateIDs` (bool): Return [pageID => templateID] array? [3.0.152+ only] (default=false, cannot be combined with other 'return*' options). - `returnAllCols` (bool): Return [pageID => [ all columns ]] array? [3.0.153+ only] (default=false, cannot be combined with other 'return*' options). - `allowCustom` (bool): Whether or not to allow _custom='selector string' type values (default=false). - `useSortsAfter` (bool): When true, PageFinder may ask caller to perform sort manually in some cases (default=false).

## Return value

- `array|DatabaseQuerySelect`

## Exceptions

- `PageFinderException`
