# PagesPathFinder

Source: `wire/core/PagesPathFinder.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Path Finder

Common methods:
- [`init()`](method-init.md)
- [`get()`](method-get.md)
- [`getPage()`](method-getpage.md)
- [`getPagesRow()`](method-getpagesrow.md)
- [`applyPagesRow()`](method-applypagesrow.md)

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

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`init(string $path, array $options)`](method-init.md) Init for new get()
- [`get(string $path, array $options = array()): array`](method-get.md) Get verbose array of info about a given page path
- [`getPage(string $path, array $options = array()): NullPage|Page`](method-getpage.md) Given a path, get a Page object or NullPage if not found
- [`getPagesRow(array $parts): array|null`](method-getpagesrow.md) Find a row for given $parts in pages table
- [`applyPagesRow(array $parts, array|null $row): string`](method-applypagesrow.md) Apply a found pages table row to the $result and return corresponding path
- [`getPathParts(string $path): array`](method-getpathparts.md) Prepare $path and convert to array of $parts
- [`getPathPartsLanguage(array &$parts): Language|null`](method-getpathpartslanguage.md) Get language that path is in and apply it to result
- [`getBlankResult(array $result = array())`](method-getblankresult.md) RESULT ********************************************************************************
- [`getBlankResult(array $result = array()): array`](method-getblankresult.md) Build blank result/return value array
- [`applyResultTemplate(string $path): bool`](method-applyresulttemplate.md) Update paths for template info like urlSegments and pageNum and populate urls property
- [`applyResultHome()`](method-applyresulthome.md) Apply result for homepage match
- [`applyResultLanguage(string $path): string`](method-applyresultlanguage.md) Identify and populate language information in result
- [`applyResultPageNum(array &$parts)`](method-applyresultpagenum.md) Identify and populate pagination number from $result['urlSegments']
- [`finishResult(string|bool $path): array`](method-finishresult.md) Finish result/return value
- [`getShortcut($path)`](method-getshortcut.md) SHORTCUTS *****************************************************************************
- [`getShortcut(string $path): bool`](method-getshortcut.md) Attempt to match path to page using shortcuts and return true if shortcut found
- [`getShortcutRoot(string $path): bool`](method-getshortcutroot.md)
- [`getShortcutExcludeRoot(string $path): bool`](method-getshortcutexcluderoot.md) Find out if we can early exit 404 based on the root segment
- [`getShortcutPagePaths(string &$path): bool`](method-getshortcutpagepaths.md) Find a shortcut using the PagePaths module
- [`getShortcutGlobalUnique(string &$path): bool`](method-getshortcutglobalunique.md) Attempt to match a page with status 'unique' or having parent_id=1
- [`getShortcutPageNum(string &$path): array`](method-getshortcutpagenum.md) Identify shortcut pagination info
- [`getPathHistory(string $path): bool`](method-getpathhistory.md) Attempt to match page path from PagePathHistory module
- [`pageNumUrlSegment(int $pageNum, string $langName = 'default'): string`](method-pagenumurlsegment.md) Get page number segment with given pageNum and and in given language name
- [`pageNumUrlPrefixes(): array`](method-pagenumurlprefixes.md) Get pageNum URL prefixes indexed by language name
- [`isHomePath(string $path): bool`](method-ishomepath.md) Does given path refer to homepage?
- [`pageNameToUTF8(string $name): string`](method-pagenametoutf8.md) Convert ascii page name to UTF-8
- [`pageNameToAscii(string $name): string`](method-pagenametoascii.md) Convert UTF-8 page name to ascii
- [`getResultTemplate(): null|Template`](method-getresulttemplate.md) Get template used by page found in result or null if not yet known
- [`isResultInAdmin(): bool`](method-isresultinadmin.md) Is matched result in admin?
- [`strlen(string $str): int`](method-strlen.md) Get string length, using mb_strlen() if available, strlen() if not
- [`addMethod(string $name, int|bool $code, string $note = '')`](method-addmethod.md) Add method debug info (verbose mode)
- [`getHomepage(): Page`](method-gethomepage.md) Get homepage
- [`addResultError(string $name, string $message, bool $force = false)`](method-addresulterror.md) Add named error message to result
- [`addResultNote(string $message)`](method-addresultnote.md) Add note to result
- [`pagePathsModule(): bool|PagePaths`](method-pagepathsmodule.md) Get optional PathPaths module instance if it is installed, false if not
- [`pagePathHistoryModule(): PagePathHistory|bool`](method-pagepathhistorymodule.md) Get optional PagePathHistory module instance if it is installed, false if not
- [`setResultLanguage(int|string|Language $language, string $segment = '')`](method-setresultlanguage.md) Set result language by name or ID
- [`setResultLanguageSegment(string $segment)`](method-setresultlanguagesegment.md) Set result language segment
- [`setResultLanguageStatus(int|bool $status)`](method-setresultlanguagestatus.md) Set result language status
- [`getPageLanguageStatus(int $pageId, int $languageId): int`](method-getpagelanguagestatus.md) Get value from page status column
- [`languages(bool $getArray = false): Languages|Language[]`](method-languages.md) Return Languages if installed w/languageSupportPageNames module or blank array if not
- [`language(string|int|Language $value): Language|null`](method-language.md) Given a value return corresponding language
- [`languageSegment(string|int|Language $language): string`](method-languagesegment.md) Return homepage name segment used by given language
- [`segmentLanguage(string $segment, bool $getLanguageId = false): Language|null|int`](method-segmentlanguage.md) Return language identified by homepage name segment
- [`languageName(int|string|Language $language): string`](method-languagename.md) Return name for given language id or object
- [`languageNames(): array`](method-languagenames.md) Return all language names indexed by language id
- [`languageId(int|string|Language $language): int`](method-languageid.md) Return language id for given value (language name, name column or home segment)
- [`updatePathForLanguage(string $path, string $langName = ''): string`](method-updatepathforlanguage.md) Update given path for result language and return it
- [`addLanguageSegment(string $path, string|Language|int $language): string`](method-addlanguagesegment.md) Add language segment
- [`removeLanguageSegment(string $path): string`](method-removelanguagesegment.md) Remove any language segments present on given path
- [`finishResultRedirectPageNum($response, &$result)`](method-finishresultredirectpagenum.md) ADDITIONAL/HELPER LOGIC ***************************************************************
- [`finishResultRedirectPageNum(int $response, &$result): int`](method-finishresultredirectpagenum.md) Update result for cases where a redirect was determined that involved pagination
