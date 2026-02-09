# PageFinder

Source: `wire/core/PageFinder.php`

Inherits: `Wire`

ProcessWire PageFinder

Matches selector strings to pages


Methods:
Method: [init()](method-init.md)
Method: [initSelectors()](method-initselectors.md)
Method: [initStatus()](method-initstatus.md)
Method: [find()](method-___find.md) (hookable)
Method: [findAlt()](method-findalt.md)
Method: [findIDs()](method-findids.md)
Method: [findVerboseIDs()](method-findverboseids.md)
Method: [findParentIDs()](method-findparentids.md)
Method: [findTemplateIDs()](method-findtemplateids.md)
Method: [count()](method-count.md)
Method: [preProcessSelectors()](method-preprocessselectors.md)
Method: [preProcessFieldtypeSelector()](method-preprocessfieldtypeselector.md)
Method: [preProcessSelector()](method-preprocessselector.md)
Method: [preProcessSubSelector()](method-preprocesssubselector.md)
Method: [getQuery()](method-___getquery.md) (hookable)
Method: [getMatchQueryJSON()](method-getmatchqueryjson.md)
Method: [postProcessQuery()](method-postprocessquery.md)
Method: [whereEmptyValuePossible()](method-whereemptyvaluepossible.md)
Method: [getQueryAllowedTemplates()](method-getqueryallowedtemplates.md)
Method: [getQueryAllowedTemplatesWhere()](method-___getqueryallowedtemplateswhere.md) (hookable)
Method: [getQueryJoinPath()](method-___getqueryjoinpath.md) (hookable)
Method: [getQueryNativeField()](method-getquerynativefield.md)
Method: [getIncludeSelector()](method-getincludeselector.md)
Method: [getQueryHasParent()](method-getqueryhasparent.md)
Method: [getQueryNumChildren()](method-getquerynumchildren.md)
Method: [arrangeFields()](method-arrangefields.md)
Method: [getTotal()](method-gettotal.md)
Method: [getLimit()](method-getlimit.md)
Method: [getStart()](method-getstart.md)
Method: [getParentID()](method-getparentid.md)
Method: [getTemplatesID()](method-gettemplatesid.md)
Method: [getOptions()](method-getoptions.md)
Method: [isPageField()](method-ispagefield.md)
Method: [isRepeaterFieldtype()](method-isrepeaterfieldtype.md)
Method: [isModifierField()](method-ismodifierfield.md)
Method: [pagesColumnExists()](method-pagescolumnexists.md)
Method: [supportsLanguagePageNames()](method-supportslanguagepagenames.md)
Method: [getQueryUnknownField()](method-___getqueryunknownfield.md) (hookable)
Method: [getQueryOwnerField()](method-getqueryownerfield.md)
Method: [getPageArrayData()](method-getpagearraydata.md)
Method: [hasNativeFieldName()](method-hasnativefieldname.md)
Method: [syntaxError()](method-syntaxerror.md)

Hookable methods:
=================

- [find(Selectors|string|array $selectors, $options = array()): array|DatabaseQuerySelect](method-___find.md)
- [getQuery($selectors, array $options): DatabaseQuerySelect](method-___getquery.md)
- [getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where): string](method-___getqueryallowedtemplateswhere.md)
- [getQueryJoinPath(DatabaseQuerySelect $query, $selector): void](method-___getqueryjoinpath.md)
- [getQueryUnknownField($fieldName, array $data): bool|Field](method-___getqueryunknownfield.md) ;
- $includeMode: string
- $checkAccess: bool
