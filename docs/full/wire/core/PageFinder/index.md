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

Methods:
Method: [init()](method-init.md)
Method: [initSelectors()](method-initselectors.md)
Method: [initStatus()](method-initstatus.md)
Method: [___find()](method-___find.md)
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
Method: [___getQuery()](method-___getquery.md)
Method: [getMatchQueryJSON()](method-getmatchqueryjson.md)
Method: [postProcessQuery()](method-postprocessquery.md)
Method: [whereEmptyValuePossible()](method-whereemptyvaluepossible.md)
Method: [getQueryAllowedTemplates()](method-getqueryallowedtemplates.md)
Method: [___getQueryAllowedTemplatesWhere()](method-___getqueryallowedtemplateswhere.md)
Method: [___getQueryJoinPath()](method-___getqueryjoinpath.md)
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
Method: [___getQueryUnknownField()](method-___getqueryunknownfield.md)
Method: [getQueryOwnerField()](method-getqueryownerfield.md)
Method: [getPageArrayData()](method-getpagearraydata.md)
Method: [hasNativeFieldName()](method-hasnativefieldname.md)
Method: [syntaxError()](method-syntaxerror.md)
