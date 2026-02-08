# Pages::getInfoByPath()

Source: `wire/core/Pages.php`

Get verbose array of info about a given page path

This method accepts a page path (not URL) with optional language segment
prefix, additional URL segments and/or pagination number. It translates
the given path to information about what page it matches, what type of
request it would result in.

If the `response` property in the return value is 301 or 302, then the
`redirect` property will be populated with a recommend redirect path.

If given a `$path` argument of `/en/foo/bar/page3` on a site that has default
language homepage segment of `en`, a page living at `/foo/` that accepts
URL segment `bar` and has pagination enabled, it will return the following:
~~~~~
[
  'request' => '/en/foo/bar/page3',
  'response' => 200, // one of 200, 301, 302, 404, 414
  'type' => 'ok', // response type name
  'errors' => [], // array of error messages indexed by error name
  'redirect' => '/redirect/path/', // suggested path to redirect to or blank
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
  'scheme' => 'https', // blank if no scheme required, https or http if one of those is required
  'method' => 'pagesRow', // method(s) that were used to find the page
]
~~~~~


@param string $path Page path optionally including URL segments, language prefix, pagination number

@param array $options
 - `useLanguages` (bool): Allow use of multi-language page names? (default=true)
    Requires LanguageSupportPageNames module installed.
 - `useShortcuts` (bool): Allow use of shortcut methods for optimization? (default=true)
    Recommend PagePaths module installed.
 - `useHistory` (bool): Allow use historical path names? (default=true)
    Requires PagePathHistory module installed.
 - `verbose` (bool): Return verbose array of information? (default=true)
    If false, some optional information will be omitted in return value.

@return array
