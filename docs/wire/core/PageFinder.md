# PageFinder

Source: `wire/core/PageFinder.php`

ProcessWire PageFinder

Matches selector strings to pages

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

Hookable methods:
=================

@method array|DatabaseQuerySelect find(Selectors|string|array $selectors, $options = array())

@method DatabaseQuerySelect getQuery($selectors, array $options)

@method string getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where)

@method void getQueryJoinPath(DatabaseQuerySelect $query, $selector)

@method bool|Field getQueryUnknownField($fieldName, array $data);

@property string $includeMode

@property bool $checkAccess

## init()

Initialize new find operation and prepare options

@param Selectors $selectors

@param array $options

@return array Returns updated options with all present

## initSelectors()

Initialize the selectors to add Page status checks

@param Selectors $selectors

@param array $options

@return array

## initStatus()

Initialize status checks

@param Selectors $selectors

@param array $options

## ___find()

Return all pages matching the given selector.

@param Selectors|string|array $selectors Selectors object, selector string or selector array

@param array $options
 - `findOne` (bool): Specify that you only want to find 1 page and don't need info for pagination (default=false).
 - `findHidden` (bool): Specify that it's okay for hidden pages to be included in the results (default=false).
 - `findUnpublished` (bool): Specify that it's okay for hidden AND unpublished pages to be included in the
    results (default=false).
 - `findTrash` (bool): Specify that it's okay for hidden AND unpublished AND trashed pages to be included in the
    results (default=false).
 - `findAll` (bool): Specify that no page should be excluded - results can include unpublished, trash, system,
    no-access pages, etc. (default=false)
 - `getTotal` (bool|null): Whether the total quantity of matches should be determined and accessible from
    getTotal() method call.
    - null: determine automatically (default is disabled when limit=1, enabled in all other cases).
    - true: always calculate total.
    - false: never calculate total.
 - `getTotalType` (string): Method to use to get total, specify 'count' or 'calc' (default='calc').
 - `returnQuery` (bool): When true, only the DatabaseQuery object is returned by find(), for internal use. (default=false)
 - `loadPages` (bool): This is an optimization used by the Pages::find() method, but we observe it here as we
    may be able to apply some additional optimizations in certain cases. For instance, if loadPages=false, then
    we can skip retrieval of IDs and omit sort fields. (default=true)
 - `stopBeforeID` (int): Stop loading pages once a page matching this ID is found. Page having this ID will be
    excluded as well (default=0).
 - `startAfterID` (int): Start loading pages once a page matching this ID is found. Page having this ID will be
    excluded as well (default=0).
 - `reverseSort` (bool): Reverse whatever sort is specified.
 - `returnVerbose` (bool): When true, this function returns array of arrays containing page ID, parent ID,
    template ID and score. When false, returns only an array of page IDs. True is required by most usage from
    Pages class. False is only for specific cases.
 - `returnParentIDs` (bool): Return parent IDs only? (default=false, requires that 'returnVerbose' option is false).
 - `returnTemplateIDs` (bool): Return [pageID => templateID] array? [3.0.152+ only] (default=false, cannot be combined with other 'return*' options).
 - `returnAllCols` (bool): Return [pageID => [ all columns ]] array? [3.0.153+ only] (default=false, cannot be combined with other 'return*' options).
 - `allowCustom` (bool): Whether or not to allow _custom='selector string' type values (default=false).
 - `useSortsAfter` (bool): When true, PageFinder may ask caller to perform sort manually in some cases (default=false).

@return array|DatabaseQuerySelect

@throws PageFinderException

## findAlt()

Perform an alternate/fallback find when first fails to match and alternate operators available

@param Selectors $selectors

@param array $options

@param array $matches

@return array

## findIDs()

Same as find() but returns just a simple array of page IDs without any other info

@param Selectors|string|array $selectors Selectors object, selector string or selector array

@param array $options

@return array of page IDs

## findVerboseIDs()

Returns array of arrays with all columns in pages table indexed by page ID

@param Selectors|string|array $selectors Selectors object, selector string or selector array

@param array $options
 - `joinFields` (array): Names of additional fields to join (default=[]) 3.0.172+
 - `joinSortfield` (bool): Include 'sortfield' in returned columns? Joined from pages_sortfields table. (default=false) 3.0.172+
 - `getNumChildren` (bool): Include 'numChildren' in returned columns? Calculated in query. (default=false) 3.0.172+
 - `unixTimestamps` (bool): Return created/modified/published dates as unix timestamps rather than ISO-8601? (default=false) 3.0.172+

@return array|DatabaseQuerySelect

@since 3.0.153

## findParentIDs()

Same as findIDs() but returns the parent IDs of the pages that matched

@param Selectors|string|array $selectors Selectors object, selector string or selector array

@param array $options

@return array of page parent IDs

## findTemplateIDs()

Find template ID for each page — returns array of template IDs indexed by page ID

@param Selectors|string|array $selectors Selectors object, selector string or selector array

@param array $options

@return array

@since 3.0.152

## count()

Return a count of pages that match

@param Selectors|string|array $selectors Selectors object, selector string or selector array

@param array $options

@return int

@since 3.0.121

## preProcessSelectors()

Pre-process given Selectors object

@param Selectors $selectors

@param array $options

## preProcessFieldtypeSelector()

Pre-process a selector having field name that begins with "Fieldtype"

@param Selectors $selectors

@param Selector $selector

## preProcessSelector()

Pre-process the given selector to perform any necessary replacements

This is primarily used to handle sub-selections, i.e. "bar=foo, id=[this=that, foo=bar]"
and OR-groups, i.e. "(bar=foo), (foo=bar)"

@param Selector $selector

@param Selectors $selectors

@param array $options

@param int $level

@return bool|Selector Returns false if selector should be skipped over by getQuery(), returns Selector otherwise

@throws PageFinderSyntaxException

## preProcessSubSelector()

Pre-process a Selector that has a [quoted selector] embedded within its value

@param Selector $selector

@param Selectors $parentSelectors

## ___getQuery()

Given one or more selectors, create the SQL query for finding pages.

@TODO split this method up into more parts, it's too long

@param Selectors $selectors Array of selectors.

@param array $options

@return DatabaseQuerySelect

@throws PageFinderSyntaxException

## getMatchQueryJSON()

Get match query when data is stored in a JSON DB column (future use)

@param PageFinderDatabaseQuerySelect DatabaseQuerySelect $q

@param string $tableAlias

@param string $subfields

@param string $operator

@param string|int|array $value

@return bool

## postProcessQuery()

Post process a DatabaseQuerySelect for page finder

@param DatabaseQuerySelect $parentQuery

@throws WireException

## whereEmptyValuePossible()

Generate SQL and modify $query for situations where it should be possible to match empty values

This can include equals/not-equals with blank or 0, as well as greater/less-than searches that
can potentially match blank or 0.

@param Field $field

@param string $col

@param Selector $selector

@param DatabaseQuerySelect $query

@param string $value The value presumed to be blank (passed the empty() test)

@param string $where SQL where string that will be modified/appended

@return bool Whether or not the query was handled and modified

## getQueryAllowedTemplates()

Determine which templates the user is allowed to view

@param DatabaseQuerySelect $query

@param array $options

## ___getQueryAllowedTemplatesWhere()

Method that allows external hooks to add to or modify the access control WHERE conditions

Called only if it's hooked. To utilize it, modify the $where argument in a BEFORE hook
or the $event->return in an AFTER hook.

@param DatabaseQuerySelect $query

@param string $where SQL string for WHERE statement, not including the actual "WHERE"

@return string

## ___getQueryJoinPath()

Special case when requested value is path or URL

@param DatabaseQuerySelect $query

@param Selector $selector

@throws PageFinderSyntaxException

## getQueryNativeField()

Special case when field is native to the pages table

TODO not all operators will work here, so may want to add some translation or filtering

@param DatabaseQuerySelect $query

@param Selector $selector

@param array $fields

@param array $options

@param Selectors $selectors

@throws PageFinderSyntaxException

## getIncludeSelector()

Get the include|status|check_access portions from given Selectors and return selector string for them

If given $selectors lacks an include or check_access selector, then it will pull from the
equivalent PageFinder setting if present in the original initiating selector.

@param Selectors|string $selectors

@return string

## getQueryHasParent()

Make the query specific to all pages below a certain parent (children, grandchildren, great grandchildren, etc.)

@param DatabaseQuerySelect $query

@param Selector $selector

## getQueryNumChildren()

Match a number of children count

@param DatabaseQuerySelect $query

@param Selector $selector

@return string

@throws WireException

## arrangeFields()

Arrange the order of field names where necessary

@param array $fields

@return array

## getTotal()

Returns the total number of results returned from the last find() operation

If the last find() included limit, then this returns the total without the limit

@return int

## getLimit()

Returns the limit placed upon the last find() operation, or 0 if no limit was specified

@return int

## getStart()

Returns the start placed upon the last find() operation

@return int

## getParentID()

Returns the parent ID, if it was part of the selector

@return int

## getTemplatesID()

Returns the templates ID, if it was part of the selector

@return int|null

## getOptions()

Return array of the options provided to PageFinder, as well as those determined at runtime

@return array

## isPageField()

Does the given field or fieldName resolve to a field that uses Page or PageArray values?

@param string|Field $fieldName Field name or object

@param bool $literal Specify true to only allow types that literally use FieldtypePage::getMatchQuery()

@return Field|bool|string Returns Field object or boolean true (children|parent) if valid Page field, or boolean false if not

## isRepeaterFieldtype()

Is the given Fieldtype for a repeater?

@param Fieldtype $fieldtype

@return bool

## isModifierField()

Is given field name a modifier that does not directly refer to a field or column name?

@param string $name

@return string Returns normalized modifier name if a modifier or boolean false if not

## pagesColumnExists()

Does the given column name exist in the 'pages' table?

@param string $name

@return bool

## supportsLanguagePageNames()

Are multi-language page names supported?

@return bool

@since 3.0.165

## ___getQueryUnknownField()

Hook called when an unknown field is found in the selector

By default, PW will throw a PageFinderSyntaxException but that behavior can be overridden by
hooking this method and making it return true rather than false. It may also choose to
map it to a Field by returning a Field object. If it returns integer 1 then it indicates the
fieldName mapped to an API variable. If this method returns false, then it signals the getQuery()
method that it was unable to map it to anything and should be considered a fail.

@param string $fieldName

@param array $data Array of data containing the following in it:
 - `subfield` (string): First subfield
 - `subfields` (string): All subfields separated by period (i.e. subfield.tertiaryfield)
 - `fields` (array): Array of all other field names being processed in this selector.
 - `query` (DatabaseQuerySelect): Database query select object
 - `selector` (Selector): Selector that contains this field
 - `selectors` (Selectors): All the selectors

@return bool|Field|int

@throws PageFinderSyntaxException

## getQueryOwnerField()

Process an owner back reference selector for PageTable, Page and Repeater fields

@param string $fieldName Field name in "fieldName__owner" format

@param array $data Data as provided to getQueryUnknownField method

@return bool True if $fieldName was processed, false if not

@throws PageFinderSyntaxException

## getPageArrayData()

Get data that should be populated back to any resulting PageArray’s data() method

@param PageArray|null $pageArray Optionally populate given PageArray

@return array

## hasNativeFieldName()

Are any of the given field name(s) native to PW system?

This is primarily used to determine whether the getQueryNativeField() method should be called.

@param string|array|Selector $fieldNames Single field name, array of field names or pipe-separated string of field names

@return bool

## syntaxError()

Throw a fatal syntax error

@param string $message

@throws PageFinderSyntaxException
