# PagesPathFinder

Source: `wire/core/PagesPathFinder.php`

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

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

@todo:
Determine how to handle case where this class is called before
LanguageSupport module has been loaded (for multi-language page names)

## __construct()

Construct

@param Pages $pages

## init()

Init for new get()

@param string $path

@param array $options

## get()

Get verbose array of info about a given page path

This method accepts a page path (not URL) with optional language segment
prefix, additional URL segments and/or pagination number. It translates
the given path to information about what page it matches, what type of
request it would result in.

If the `response` property in the return value is 301 or 302, then the
`redirect` property will be populated with a recommend redirect path.

Please access this method from `$pages->pathFinder()->get('…');`

Below is an example when given a `$path` argument of `/en/foo/bar/page3`
on a site that has default language homepage segment of `en`, a page living
at `/foo/` that accepts URL segment `bar` and has pagination enabled;
~~~~~
$array = $pages->pathFinder()->get('/en/foo/bar/page3');
~~~~~
~~~~~
[
  'request' => '/en/foo/bar/page3',
  'response' => 200, // one of 200, 301, 302, 404, 414
  'type' => 'ok', // response type name
  'errors' => [], // array of error messages indexed by error name
  'redirect` => '/redirect/path/', // suggested path to redirect to or blank
  'page' => [
     'id' => 123, // ID of the page that was found
     'parent_id' => 456,
     'templates_id' => 12,
     'status' => 1,
     'name' => 'foo',
  ],
  'language' => [
     'name' => 'default', // name of language detected
     'segment' => 'en', // segment prefix in path (if any)
     'status' => 1, // language status where 1 is on, 0 is off
   ],
  'parts' => [ // all the parts of the path identified
    [
      'type' => 'language',
      'value' => 'en',
      'language' => 'default'
    ],
    [
      'type' => 'pageName',
      'value' => 'foo',
      'language' => 'default'
    ],
    [
      'type' => 'urlSegment',
      'value' => 'bar',
      'language' => ''
    ],
    [
      'type' => 'pageNum',
      'value' => 'page3',
      'language' => 'default'
    ],
  ],
  'urlSegments' => [ // URL segments identified in order
     'bar',
  ],
  'urlSegmentStr' => 'bar', // URL segment string
  'pageNum' => 3, // requested pagination number
  'pageNumPrefix' => 'page', // prefix used in pagination number
  'scheme' => 'https', // blank if no scheme required, 'https' or 'http' if one of those is required
  'method' => 'pagesRow', // method(s) that were used to find the page
]
~~~~~

@param string $path Page path optionally including URL segments, language prefix, pagination number

@param array $options
 - `useLanguages` (bool): Allow use of multi-language page names? (default=true)
    Requires LanguageSupportPageNames module installed.
 - `useHistory` (bool): Allow use historical path names? (default=true)
    Requires PagePathHistory module installed.
 - `verbose` (bool): Return verbose array of information? (default=true)
    If false, some optional information will be omitted in return value.

@return array

@see PagesPathFinder::getPage()

## getPage()

Given a path, get a Page object or NullPage if not found

This method is like the `get()` method except that it returns a `Page`
object rather than an array. It sets a `_pagePathFinder` property to the
returned Page, which is an associative array containing the same result
array returned by the `get()` method.

Please access this method from `$pages->pathFinder()->getPage('…');`

@param string $path

@param array $options

@return NullPage|Page

@see PagesPathFinder::get()

## getPagesRow()

Find a row for given $parts in pages table

@param array $parts

@return array|null

## applyPagesRow()

Apply a found pages table row to the $result and return corresponding path

@param array $parts

@param array|null $row

@return string Path string

## getPathParts()

Prepare $path and convert to array of $parts

If language segment detected then remove it and populate language to result

@param string $path

@return array

## getPathPartsLanguage()

Get language that path is in and apply it to result

@param array $parts

@return Language|null

## getBlankResult()

RESULT ********************************************************************************

## getBlankResult()

Build blank result/return value array

@param array $result Optionally return blank result merged with this one

@return array

## applyResultTemplate()

Update paths for template info like urlSegments and pageNum and populate urls property

@param string $path

@return bool

## applyResultHome()

Apply result for homepage match

## applyResultLanguage()

Identify and populate language information in result

@param string $path

@return string $path Path is updated as needed

## applyResultPageNum()

Identify and populate pagination number from $result['urlSegments']

@param array $parts

## finishResult()

Finish result/return value

@param string|bool $path Path string or boolean false when 404

@return array

## getShortcut()

SHORTCUTS *****************************************************************************

## getShortcut()

Attempt to match path to page using shortcuts and return true if shortcut found

@param string $path

@return bool Return true if shortcut found and result ready, false if not

## getShortcutRoot()

@param string $path

@return bool

## getShortcutExcludeRoot()

Find out if we can early exit 404 based on the root segment

Unlike other shortcuts, this one is an exclusion shortcut:
Returns false if the root segment matched and further analysis should take place.
Returns true if root segment is not in this site and 404 should be the result.

@param string $path

@return bool

## getShortcutPagePaths()

Find a shortcut using the PagePaths module

@param string $path

@return bool Returns true if found, false if not installed or not found

## getShortcutGlobalUnique()

Attempt to match a page with status 'unique' or having parent_id=1

This method only proceeds if the path contains no slashes, meaning it is 1-level from root.

@param string $path

@return bool

## getShortcutPageNum()

Identify shortcut pagination info

Returns found pagination number, or 1 if first pagination.
Extracts the pagination segment from the path.

@param string $path

@return array of [ pageNum, pageNumPrefix ]

## getPathHistory()

Attempt to match page path from PagePathHistory module

@param string $path

@return bool

## pageNumUrlSegment()

Get page number segment with given pageNum and and in given language name

@param int $pageNum

@param string $langName

@return string

## pageNumUrlPrefixes()

Get pageNum URL prefixes indexed by language name

@return array

## isHomePath()

Does given path refer to homepage?

@param string $path

@return bool

## pageNameToUTF8()

Convert ascii page name to UTF-8

@param string $name

@return string

## pageNameToAscii()

Convert UTF-8 page name to ascii

@param string $name

@return string

## getResultTemplate()

Get template used by page found in result or null if not yet known

@return null|Template

## isResultInAdmin()

Is matched result in admin?

@return bool

## strlen()

Get string length, using mb_strlen() if available, strlen() if not

@param string $str

@return int

## addMethod()

Add method debug info (verbose mode)

@param string $name

@param int|bool $code

@param string $note

## getHomepage()

Get homepage

@return Page

## addResultError()

Add named error message to result

@param string $name

@param string $message

@param bool $force Force add even if not in verbose mode? (default=false)

## addResultNote()

Add note to result

@param string $message

## pagePathsModule()

Get optional PathPaths module instance if it is installed, false if not

@return bool|PagePaths

## pagePathHistoryModule()

Get optional PagePathHistory module instance if it is installed, false if not

@return PagePathHistory|bool

## setResultLanguage()

Set result language by name or ID

@param int|string|Language $language

@param string $segment

## setResultLanguageSegment()

Set result language segment

@param string $segment

## setResultLanguageStatus()

Set result language status

@param int|bool $status

## getPageLanguageStatus()

Get value from page status column

@param int $pageId

@param int $languageId

@return int

## languages()

Return Languages if installed w/languageSupportPageNames module or blank array if not

@param bool $getArray Force return value as an array indexed by language name

@return Languages|Language[]

## language()

Given a value return corresponding language

@param string|int|Language $value

@return Language|null

## languageSegment()

Return homepage name segment used by given language

@param string|int|Language $language

@return string

## segmentLanguage()

Return language identified by homepage name segment

@param string $segment

@param bool $getLanguageId

@return Language|null|int

## languageName()

Return name for given language id or object

@param int|string|Language $language

@return string

## languageNames()

Return all language names indexed by language id

@return array

## languageId()

Return language id for given value (language name, name column or home segment)

@param int|string|Language $language

@return int

## updatePathForLanguage()

Update given path for result language and return it

@param string $path

@param string $langName

@return string

## addLanguageSegment()

Add language segment

@param string $path

@param string|Language|int $language

@return string

## removeLanguageSegment()

Remove any language segments present on given path

@param string $path

@return string

## finishResultRedirectPageNum()

ADDITIONAL/HELPER LOGIC ***************************************************************

## finishResultRedirectPageNum()

Update result for cases where a redirect was determined that involved pagination

Most of the logic here allows for the special case of admin URLs, which work with either
a custom pageNumUrlPrefix or the original/default one. This is a helper for the
finishResult() method.

@param int $response

@var array $result

@return int

@since 3.0.198
