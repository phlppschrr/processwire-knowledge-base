# PagesPathFinder

Source: `wire/core/PagesPathFinder.php`

Inherits: `Wire`

ProcessWire Pages Path Finder

Pages Path Finder
$pages->pathFinder
Enables finding pages by path, optionally with URL segments, pagination numbers, language prefixes, etc.
This is built for use by the PagesRequest class and ProcessPageView module, but can also be useful from the public API.
The most useful method is the `get()` method which returns a verbose array of information about the given path.
Methods in this class should be acessed from `$pages->pathFinder()`, i.e.
~~~~~
$result = $pages->pathFinder()->get('/en/foo/bar/page3');
~~~~~
Note that PagesPathFinder does not perform any access control checks, so if using this class then validate access
afterwards when appropriate.


@todo:
Determine how to handle case where this class is called before
LanguageSupport module has been loaded (for multi-language page names)

Methods:
Method: [__construct()](method-__construct.md)
Method: [init()](method-init.md)
Method: [get()](method-get.md)
Method: [getPage()](method-getpage.md)
Method: [getPagesRow()](method-getpagesrow.md)
Method: [applyPagesRow()](method-applypagesrow.md)
Method: [getPathParts()](method-getpathparts.md)
Method: [getPathPartsLanguage()](method-getpathpartslanguage.md)
Method: [getBlankResult()](method-getblankresult.md)
Method: [getBlankResult()](method-getblankresult.md)
Method: [applyResultTemplate()](method-applyresulttemplate.md)
Method: [applyResultHome()](method-applyresulthome.md)
Method: [applyResultLanguage()](method-applyresultlanguage.md)
Method: [applyResultPageNum()](method-applyresultpagenum.md)
Method: [finishResult()](method-finishresult.md)
Method: [getShortcut()](method-getshortcut.md)
Method: [getShortcut()](method-getshortcut.md)
Method: [getShortcutRoot()](method-getshortcutroot.md)
Method: [getShortcutExcludeRoot()](method-getshortcutexcluderoot.md)
Method: [getShortcutPagePaths()](method-getshortcutpagepaths.md)
Method: [getShortcutGlobalUnique()](method-getshortcutglobalunique.md)
Method: [getShortcutPageNum()](method-getshortcutpagenum.md)
Method: [getPathHistory()](method-getpathhistory.md)
Method: [pageNumUrlSegment()](method-pagenumurlsegment.md)
Method: [pageNumUrlPrefixes()](method-pagenumurlprefixes.md)
Method: [isHomePath()](method-ishomepath.md)
Method: [pageNameToUTF8()](method-pagenametoutf8.md)
Method: [pageNameToAscii()](method-pagenametoascii.md)
Method: [getResultTemplate()](method-getresulttemplate.md)
Method: [isResultInAdmin()](method-isresultinadmin.md)
Method: [strlen()](method-strlen.md)
Method: [addMethod()](method-addmethod.md)
Method: [getHomepage()](method-gethomepage.md)
Method: [addResultError()](method-addresulterror.md)
Method: [addResultNote()](method-addresultnote.md)
Method: [pagePathsModule()](method-pagepathsmodule.md)
Method: [pagePathHistoryModule()](method-pagepathhistorymodule.md)
Method: [setResultLanguage()](method-setresultlanguage.md)
Method: [setResultLanguageSegment()](method-setresultlanguagesegment.md)
Method: [setResultLanguageStatus()](method-setresultlanguagestatus.md)
Method: [getPageLanguageStatus()](method-getpagelanguagestatus.md)
Method: [languages()](method-languages.md)
Method: [language()](method-language.md)
Method: [languageSegment()](method-languagesegment.md)
Method: [segmentLanguage()](method-segmentlanguage.md)
Method: [languageName()](method-languagename.md)
Method: [languageNames()](method-languagenames.md)
Method: [languageId()](method-languageid.md)
Method: [updatePathForLanguage()](method-updatepathforlanguage.md)
Method: [addLanguageSegment()](method-addlanguagesegment.md)
Method: [removeLanguageSegment()](method-removelanguagesegment.md)
Method: [finishResultRedirectPageNum()](method-finishresultredirectpagenum.md)
Method: [finishResultRedirectPageNum()](method-finishresultredirectpagenum.md)
