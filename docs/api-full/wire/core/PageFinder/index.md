# PageFinder

Source: `wire/core/PageFinder.php`

Inherits: `Wire`

## Summary

ProcessWire PageFinder

Common methods:
- [`init()`](method-init.md)
- [`initSelectors()`](method-initselectors.md)
- [`initStatus()`](method-initstatus.md)
- [`find()`](method-___find.md)
- [`findAlt()`](method-findalt.md)

Matches selector strings to pages


## Hookable Methods:

- [`find(Selectors|string|array $selectors, $options = array()): array|DatabaseQuerySelect`](method-___find.md)
- [`getQuery($selectors, array $options): DatabaseQuerySelect`](method-___getquery.md)
- [`getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where): string`](method-___getqueryallowedtemplateswhere.md)
- [`getQueryJoinPath(DatabaseQuerySelect $query, $selector): void`](method-___getqueryjoinpath.md)
- [`getQueryUnknownField($fieldName, array $data): bool|Field`](method-___getqueryunknownfield.md) ;
- `$includeMode: string`
- `$checkAccess: bool`

## Methods
- [`init(Selectors $selectors, array $options): array`](method-init.md) Initialize new find operation and prepare options
- [`initSelectors(Selectors $selectors, array $options): array`](method-initselectors.md) Initialize the selectors to add Page status checks
- [`initStatus(Selectors $selectors, array $options)`](method-initstatus.md) Initialize status checks
- [`find(Selectors|string|array $selectors, array $options = array()): array|DatabaseQuerySelect`](method-___find.md) (hookable) Return all pages matching the given selector.
- [`findAlt(Selectors $selectors, array $options, array $matches): array`](method-findalt.md) Perform an alternate/fallback find when first fails to match and alternate operators available
- [`findIDs(Selectors|string|array $selectors, array $options = array()): array`](method-findids.md) Same as find() but returns just a simple array of page IDs without any other info
- [`findVerboseIDs(Selectors|string|array $selectors, array $options = array()): array|DatabaseQuerySelect`](method-findverboseids.md) Returns array of arrays with all columns in pages table indexed by page ID
- [`findParentIDs(Selectors|string|array $selectors, array $options = array()): array`](method-findparentids.md) Same as findIDs() but returns the parent IDs of the pages that matched
- [`findTemplateIDs(Selectors|string|array $selectors, array $options = array()): array`](method-findtemplateids.md) Find template ID for each page — returns array of template IDs indexed by page ID
- [`count(Selectors|string|array $selectors, array $options = array()): int`](method-count.md) Return a count of pages that match
- [`preProcessSelectors(Selectors $selectors, array $options = array())`](method-preprocessselectors.md) Pre-process given Selectors object
- [`preProcessFieldtypeSelector(Selectors $selectors, Selector $selector)`](method-preprocessfieldtypeselector.md) Pre-process a selector having field name that begins with "Fieldtype"
- [`preProcessSelector(Selector $selector, Selectors $selectors, array $options, int $level = 0): bool|Selector`](method-preprocessselector.md) Pre-process the given selector to perform any necessary replacements
- [`preProcessSubSelector(Selector $selector, Selectors $parentSelectors)`](method-preprocesssubselector.md) Pre-process a Selector that has a [quoted selector] embedded within its value
- [`getQuery(Selectors $selectors, array $options): DatabaseQuerySelect`](method-___getquery.md) (hookable) Given one or more selectors, create the SQL query for finding pages.
- [`getMatchQueryJSON(DatabaseQuerySelect $q, string $tableAlias, string $subfields, string $operator, string|int|array $value): bool`](method-getmatchqueryjson.md) Get match query when data is stored in a JSON DB column (future use)
- [`postProcessQuery(DatabaseQuerySelect $parentQuery)`](method-postprocessquery.md) Post process a DatabaseQuerySelect for page finder
- [`whereEmptyValuePossible(Field $field, string $col, Selector $selector, DatabaseQuerySelect $query, string $value, string &$where): bool`](method-whereemptyvaluepossible.md) Generate SQL and modify `$query` for situations where it should be possible to match empty values
- [`getQueryAllowedTemplates(DatabaseQuerySelect $query, array $options)`](method-getqueryallowedtemplates.md) Determine which templates the user is allowed to view
- [`getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, string $where): string`](method-___getqueryallowedtemplateswhere.md) (hookable) Method that allows external hooks to add to or modify the access control WHERE conditions
- [`getQueryJoinPath(DatabaseQuerySelect $query, Selector $selector)`](method-___getqueryjoinpath.md) (hookable) Special case when requested value is path or URL
- [`getQueryNativeField(DatabaseQuerySelect $query, Selector $selector, array $fields, array $options, Selectors $selectors)`](method-getquerynativefield.md) Special case when field is native to the pages table
- [`getIncludeSelector(Selectors|string $selectors): string`](method-getincludeselector.md) Get the include|status|check_access portions from given Selectors and return selector string for them
- [`getQueryHasParent(DatabaseQuerySelect $query, Selector $selector)`](method-getqueryhasparent.md) Make the query specific to all pages below a certain parent (children, grandchildren, great grandchildren, etc.)
- [`getQueryNumChildren(DatabaseQuerySelect $query, Selector $selector): string`](method-getquerynumchildren.md) Match a number of children count
- [`arrangeFields(array $fields): array`](method-arrangefields.md) Arrange the order of field names where necessary
- [`getTotal(): int`](method-gettotal.md) Returns the total number of results returned from the last find() operation
- [`getLimit(): int`](method-getlimit.md) Returns the limit placed upon the last find() operation, or 0 if no limit was specified
- [`getStart(): int`](method-getstart.md) Returns the start placed upon the last find() operation
- [`getParentID(): int`](method-getparentid.md) Returns the parent ID, if it was part of the selector
- [`getTemplatesID(): int|null`](method-gettemplatesid.md) Returns the templates ID, if it was part of the selector
- [`getOptions(): array`](method-getoptions.md) Return array of the options provided to PageFinder, as well as those determined at runtime
- [`isPageField(string|Field $fieldName, bool $literal = false): Field|bool|string`](method-ispagefield.md) Does the given field or fieldName resolve to a field that uses Page or PageArray values?
- [`isRepeaterFieldtype(Fieldtype $fieldtype): bool`](method-isrepeaterfieldtype.md) Is the given Fieldtype for a repeater?
- [`isModifierField(string $name): string`](method-ismodifierfield.md) Is given field name a modifier that does not directly refer to a field or column name?
- [`pagesColumnExists(string $name): bool`](method-pagescolumnexists.md) Does the given column name exist in the 'pages' table?
- [`supportsLanguagePageNames(): bool`](method-supportslanguagepagenames.md) Are multi-language page names supported?
- [`getQueryUnknownField(string $fieldName, array $data): bool|Field|int`](method-___getqueryunknownfield.md) (hookable) Hook called when an unknown field is found in the selector
- [`getQueryOwnerField(string $fieldName, array $data): bool`](method-getqueryownerfield.md) Process an owner back reference selector for PageTable, Page and Repeater fields
- [`getPageArrayData(?PageArray $pageArray = null): array`](method-getpagearraydata.md) Get data that should be populated back to any resulting PageArray’s data() method
- [`hasNativeFieldName(string|array|Selector $fieldNames): bool`](method-hasnativefieldname.md) Are any of the given field name(s) native to PW system?
- [`syntaxError(string $message)`](method-syntaxerror.md) Throw a fatal syntax error
