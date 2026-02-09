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
- [`__construct(Pages $pages)`](method-__construct.md)
- [`init(string $path, array $options)`](method-init.md)
- [`get(string $path, array $options = array()): array`](method-get.md)
- [`getPage(string $path, array $options = array()): NullPage|Page`](method-getpage.md)
- [`getPagesRow(array $parts): array|null`](method-getpagesrow.md)
- [`applyPagesRow(array $parts, array|null $row): string`](method-applypagesrow.md)
- [`getPathParts(string $path): array`](method-getpathparts.md)
- [`getPathPartsLanguage(array &$parts): Language|null`](method-getpathpartslanguage.md)
- [`getBlankResult(array $result = array())`](method-getblankresult.md)
- [`getBlankResult(array $result = array()): array`](method-getblankresult.md)
- [`applyResultTemplate(string $path): bool`](method-applyresulttemplate.md)
- [`applyResultHome()`](method-applyresulthome.md)
- [`applyResultLanguage(string $path): string`](method-applyresultlanguage.md)
- [`applyResultPageNum(array &$parts)`](method-applyresultpagenum.md)
- [`finishResult(string|bool $path): array`](method-finishresult.md)
- [`getShortcut($path)`](method-getshortcut.md)
- [`getShortcut(string $path): bool`](method-getshortcut.md)
- [`getShortcutRoot(string $path): bool`](method-getshortcutroot.md)
- [`getShortcutExcludeRoot(string $path): bool`](method-getshortcutexcluderoot.md)
- [`getShortcutPagePaths(string &$path): bool`](method-getshortcutpagepaths.md)
- [`getShortcutGlobalUnique(string &$path): bool`](method-getshortcutglobalunique.md)
- [`getShortcutPageNum(string &$path): array`](method-getshortcutpagenum.md)
- [`getPathHistory(string $path): bool`](method-getpathhistory.md)
- [`pageNumUrlSegment(int $pageNum, string $langName = 'default'): string`](method-pagenumurlsegment.md)
- [`pageNumUrlPrefixes(): array`](method-pagenumurlprefixes.md)
- [`isHomePath(string $path): bool`](method-ishomepath.md)
- [`pageNameToUTF8(string $name): string`](method-pagenametoutf8.md)
- [`pageNameToAscii(string $name): string`](method-pagenametoascii.md)
- [`getResultTemplate(): null|Template`](method-getresulttemplate.md)
- [`isResultInAdmin(): bool`](method-isresultinadmin.md)
- [`strlen(string $str): int`](method-strlen.md)
- [`addMethod(string $name, int|bool $code, string $note = '')`](method-addmethod.md)
- [`getHomepage(): Page`](method-gethomepage.md)
- [`addResultError(string $name, string $message, bool $force = false)`](method-addresulterror.md)
- [`addResultNote(string $message)`](method-addresultnote.md)
- [`pagePathsModule(): bool|PagePaths`](method-pagepathsmodule.md)
- [`pagePathHistoryModule(): PagePathHistory|bool`](method-pagepathhistorymodule.md)
- [`setResultLanguage(int|string|Language $language, string $segment = '')`](method-setresultlanguage.md)
- [`setResultLanguageSegment(string $segment)`](method-setresultlanguagesegment.md)
- [`setResultLanguageStatus(int|bool $status)`](method-setresultlanguagestatus.md)
- [`getPageLanguageStatus(int $pageId, int $languageId): int`](method-getpagelanguagestatus.md)
- [`languages(bool $getArray = false): Languages|Language[]`](method-languages.md)
- [`language(string|int|Language $value): Language|null`](method-language.md)
- [`languageSegment(string|int|Language $language): string`](method-languagesegment.md)
- [`segmentLanguage(string $segment, bool $getLanguageId = false): Language|null|int`](method-segmentlanguage.md)
- [`languageName(int|string|Language $language): string`](method-languagename.md)
- [`languageNames(): array`](method-languagenames.md)
- [`languageId(int|string|Language $language): int`](method-languageid.md)
- [`updatePathForLanguage(string $path, string $langName = ''): string`](method-updatepathforlanguage.md)
- [`addLanguageSegment(string $path, string|Language|int $language): string`](method-addlanguagesegment.md)
- [`removeLanguageSegment(string $path): string`](method-removelanguagesegment.md)
- [`finishResultRedirectPageNum($response, &$result)`](method-finishresultredirectpagenum.md)
- [`finishResultRedirectPageNum(int $response, &$result): int`](method-finishresultredirectpagenum.md)
