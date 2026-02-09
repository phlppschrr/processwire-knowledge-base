# PagesNames

Source: `wire/core/PagesNames.php`

Inherits: `Wire`

ProcessWire Pages Names

Pages Names
$pages->names
This class includes methods for generating and modifying page names.
While these methods are mosty for internal core use, some may at times be useful from the public API as well.
You can access methods from this class via the Pages API variable at `$pages->names()`.
~~~~~
if($pages->names()->pageNameExists('something')) {
  // A page named “something” exists
}

// generate a globally unique random page name
$name = $pages->names()->uniqueRandomPageName();
~~~~~

Methods:
Method: [__construct()](method-__construct.md)
Method: [setupNewPageName()](method-setupnewpagename.md)
Method: [hasAutogenName()](method-hasautogenname.md)
Method: [hasAdjustedName()](method-hasadjustedname.md)
Method: [isUntitledPageName()](method-isuntitledpagename.md)
Method: [nameAndNumber()](method-nameandnumber.md)
Method: [hasNumberSuffix()](method-hasnumbersuffix.md)
Method: [defaultPageNameFormat()](method-defaultpagenameformat.md)
Method: [pageNameFromFormat()](method-pagenamefromformat.md)
Method: [uniquePageName()](method-uniquepagename.md)
Method: [adjustNameLength()](method-adjustnamelength.md)
Method: [incrementName()](method-incrementname.md)
Method: [pageNameExists()](method-pagenameexists.md)
Method: [uniqueRandomPageName()](method-uniquerandompagename.md)
Method: [untitledPageName()](method-untitledpagename.md)
Method: [pageNameHasConflict()](method-pagenamehasconflict.md)
Method: [checkNameConflicts()](method-checknameconflicts.md)
