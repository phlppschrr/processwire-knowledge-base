# PageFinder

Source: `wire/core/PageFinder.php`

Inherits: `Wire`

ProcessWire PageFinder

Matches selector strings to pages


Methods:
- [`init(Selectors $selectors, array $options): array`](method-init.md)
- [`initSelectors(Selectors $selectors, array $options): array`](method-initselectors.md)
- [`initStatus(Selectors $selectors, array $options)`](method-initstatus.md)
- [`find(Selectors|string|array $selectors, array $options = array()): array|DatabaseQuerySelect`](method-___find.md) (hookable)
- [`findAlt(Selectors $selectors, array $options, array $matches): array`](method-findalt.md)
- [`findIDs(Selectors|string|array $selectors, array $options = array()): array`](method-findids.md)
- [`findVerboseIDs(Selectors|string|array $selectors, array $options = array()): array|DatabaseQuerySelect`](method-findverboseids.md)
- [`findParentIDs(Selectors|string|array $selectors, array $options = array()): array`](method-findparentids.md)
- [`findTemplateIDs(Selectors|string|array $selectors, array $options = array()): array`](method-findtemplateids.md)
- [`count(Selectors|string|array $selectors, array $options = array()): int`](method-count.md)
- [`preProcessSelectors(Selectors $selectors, array $options = array())`](method-preprocessselectors.md)
- [`preProcessFieldtypeSelector(Selectors $selectors, Selector $selector)`](method-preprocessfieldtypeselector.md)
- [`preProcessSelector(Selector $selector, Selectors $selectors, array $options, int $level = 0): bool|Selector`](method-preprocessselector.md)
- [`preProcessSubSelector(Selector $selector, Selectors $parentSelectors)`](method-preprocesssubselector.md)
- [`getQuery(Selectors $selectors, array $options): DatabaseQuerySelect`](method-___getquery.md) (hookable)
- [`getMatchQueryJSON(DatabaseQuerySelect $q, string $tableAlias, string $subfields, string $operator, string|int|array $value): bool`](method-getmatchqueryjson.md)
- [`postProcessQuery(DatabaseQuerySelect $parentQuery)`](method-postprocessquery.md)
- [`whereEmptyValuePossible(Field $field, string $col, Selector $selector, DatabaseQuerySelect $query, string $value, string &$where): bool`](method-whereemptyvaluepossible.md)
- [`getQueryAllowedTemplates(DatabaseQuerySelect $query, array $options)`](method-getqueryallowedtemplates.md)
- [`getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, string $where): string`](method-___getqueryallowedtemplateswhere.md) (hookable)
- [`getQueryJoinPath(DatabaseQuerySelect $query, Selector $selector)`](method-___getqueryjoinpath.md) (hookable)
- [`getQueryNativeField(DatabaseQuerySelect $query, Selector $selector, array $fields, array $options, Selectors $selectors)`](method-getquerynativefield.md)
- [`getIncludeSelector(Selectors|string $selectors): string`](method-getincludeselector.md)
- [`getQueryHasParent(DatabaseQuerySelect $query, Selector $selector)`](method-getqueryhasparent.md)
- [`getQueryNumChildren(DatabaseQuerySelect $query, Selector $selector): string`](method-getquerynumchildren.md)
- [`arrangeFields(array $fields): array`](method-arrangefields.md)
- [`getTotal(): int`](method-gettotal.md)
- [`getLimit(): int`](method-getlimit.md)
- [`getStart(): int`](method-getstart.md)
- [`getParentID(): int`](method-getparentid.md)
- [`getTemplatesID(): int|null`](method-gettemplatesid.md)
- [`getOptions(): array`](method-getoptions.md)
- [`isPageField(string|Field $fieldName, bool $literal = false): Field|bool|string`](method-ispagefield.md)
- [`isRepeaterFieldtype(Fieldtype $fieldtype): bool`](method-isrepeaterfieldtype.md)
- [`isModifierField(string $name): string`](method-ismodifierfield.md)
- [`pagesColumnExists(string $name): bool`](method-pagescolumnexists.md)
- [`supportsLanguagePageNames(): bool`](method-supportslanguagepagenames.md)
- [`getQueryUnknownField(string $fieldName, array $data): bool|Field|int`](method-___getqueryunknownfield.md) (hookable)
- [`getQueryOwnerField(string $fieldName, array $data): bool`](method-getqueryownerfield.md)
- [`getPageArrayData(?PageArray $pageArray = null): array`](method-getpagearraydata.md)
- [`hasNativeFieldName(string|array|Selector $fieldNames): bool`](method-hasnativefieldname.md)
- [`syntaxError(string $message)`](method-syntaxerror.md)

Hookable methods:
=================

- [`find(Selectors|string|array $selectors, $options = array()): array|DatabaseQuerySelect`](method-___find.md)
- [`getQuery($selectors, array $options): DatabaseQuerySelect`](method-___getquery.md)
- [`getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where): string`](method-___getqueryallowedtemplateswhere.md)
- [`getQueryJoinPath(DatabaseQuerySelect $query, $selector): void`](method-___getqueryjoinpath.md)
- [`getQueryUnknownField($fieldName, array $data): bool|Field`](method-___getqueryunknownfield.md) ;
- `$includeMode: string`
- `$checkAccess: bool`
