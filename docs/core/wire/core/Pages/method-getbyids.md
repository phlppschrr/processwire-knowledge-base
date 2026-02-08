# Pages::getByIDs()

Source: `wire/core/Pages.php`

Given array or CSV string of Page IDs, return a PageArray


@param array|string|WireArray $ids Any one of the following:
 - Single page ID (string or int)
 - Array of page IDs
 - Comma or pipe-separated string of page IDs
 - Array of associative arrays having id and templates_id: [ [ 'id' => 1, 'templates_id' => 2], [ 'id' => 3, 'templates_id' => 4 ] ]

@param array $options Options to affect behavior. The 'template' option is recommended when you have this info available.
- `template` (Template|int|string): Template object, name or ID to use for loaded pages. (default=null)
- `parent` (Page|int|string): Parent Page object, ID, or path to use for loaded pages. (default=null)
- `cache` (bool): Place loaded pages in memory cache? (default=true)
- `getFromCache` (bool): Allow use of previously cached pages in memory (rather than re-loading it from DB)? (default=true)
- `getNumChildren` (bool): Specify false to disable retrieval and population of 'numChildren' Page property. (default=true)
- `getOne` (bool): Specify true to return just one Page object, rather than a PageArray. (default=false)
- `autojoin` (bool): Allow use of autojoin option? (default=true)
- `joinFields` (array): Autojoin the field names specified in this array, regardless of field settings (requires autojoin=true). (default=empty)
- `joinSortfield` (bool): Whether the 'sortfield' property will be joined to the page. (default=true)
- `findTemplates` (bool): Determine which templates will be used (when no template specified) for more specific autojoins. (default=true)
- `pageClass` (string): Class to instantiate Page objects with. Leave blank to determine from template. (default=auto-detect)
- `pageArrayClass` (string): PageArray-derived class to store pages in (when 'getOne' is false). (default=PageArray)
- `pageArray` (PageArray|null): Populate this existing PageArray rather than creating a new one. (default=null)
- `page` (Page|null): Existing Page object to populate (also requires the getOne option to be true). (default=null)

@return PageArray|Page Returns PageArray unless the getOne option was specified in which case a Page is returned.

@since 3.0.156 Previous versions can use $pages->getById() for similar behavior
