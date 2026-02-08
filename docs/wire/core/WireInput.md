# WireInput

Source: `wire/core/WireInput.php`

Manages the group of GET, POST, COOKIE and whitelist vars, each of which is a WireInputData object.

Provides a means to get user input from URLs, GET, POST, and COOKIE variables and more.

@link https://processwire.com/api/ref/wire-input/ Offical $input API variable Documentation




Note that properties and methods that end with numbers 1-3 above (like urlSegment1, urlSegment1(), etc.)
continue for as many numbers as the system supports, so you may go beyond 3 where supported.

## other

@property WireInputData $post POST variables

@property WireInputData $get GET variables

@property WireInputDataCookie $cookie COOKIE variables

@property WireInputData $whitelist Whitelisted variables

## URL-segments

@property array|string[] $urlSegments Retrieve all URL segments (array). This requires url segments are enabled on the template of the requested page. You can turn it on or off under the url tab when editing a template.

@property string $urlSegmentStr Alias of urlSegmentsStr

@property string $urlSegment1 First URL segment

@property string $urlSegment2 Second URL segment

@property string $urlSegment3 Third URL segment, and so on...

@property string $urlSegmentLast Last URL segment (since 3.0.155)

@property string $urlSegmentFirst Alias of $urlSegment1 (since 3.0.155)

@method string|int|bool urlSegment1($get = '') Same as urlSegment() method but apply only to 1st URL segment. (since 3.0.155)

@method string|int|bool urlSegment2($get = '') Same as urlSegment() method but apply only to 2nd URL segment. (since 3.0.155)

@method string|int|bool urlSegment3($get = '') Same as urlSegment() method but apply only to 3rd URL segment. (since 3.0.155)

@method string|int|bool urlSegmentLast($get = '') Same as urlSegment() method but apply only to last URL segment. (since 3.0.155)

@method string|int|bool urlSegmentFirst($get = '') Same as urlSegment() method but apply only to first URL segment. (since 3.0.155)

## URLs

@property int $pageNum Current page number (where 1 is first)

@property string $url Current requested URL including page numbers and URL segments, excluding query string.

@property string $httpUrl Like $url but includes the scheme/protcol and hostname.

@property string $queryString Current query string

@property string $scheme Current scheme/protcol, i.e. http or https

## __construct()

Construct

## get()

Retrieve a named GET variable value, or all GET variables (from URL query string)

Always sanitize (and validate where appropriate) any values from user input.

The following optional features are available in ProcessWire version 3.0.125 and newer:

- Provide a sanitization method as the 2nd argument to include sanitization.
- Provide an array of valid values as the 2nd argument to limit input to those values.
- Provide a callback function that receives the value and returns a validated value.
- Provide a fallback value as the 3rd argument to use if value not present or invalid.
- Append “[]” to the 1st argument to always force return value to be an array, i.e “colors[]”.

Note that the `$valid` and `$fallback` arguments are only applicable if a `$key` argument is provided.

~~~~~
// Retrieve a "q" GET variable, sanitize and output
// Example request URL: domain.com/path/to/page/?q=TEST
$q = $input->get('q'); // retrieve value
$q = $sanitizer->text($q); // sanitize input as 1-line text
echo $sanitizer->entities($q); // sanitize for output, outputs "TEST"

// You can also combine $input and one $sanitizer call, replacing
// the "text" method call with any $sanitizer method:
$q = $input->get->text('q');

// like the previous example, but specify sanitizer method as second argument (3.0.125+):
$q = $input->get('q', 'text');

// if you want more than one sanitizer, specify multiple in a CSV string (3.0.125+):
$q = $input->get('q', 'text,entities');

// you can provide a whitelist array of allowed values instead of a sanitizer method (3.0.125+):
$color = $input->get('color', [ 'red', 'blue', 'green' ]);

// an optional 3rd argument lets you specify a fallback value to use if valid value not present or
// empty in input, and it will return this value rather than null/empty (3.0.125+):
$qty = $input->get('qty', 'int', 1); // return 1 if no qty provided
$color = $input->get('color', [ 'red', 'blue', 'green' ], 'red'); // return red if no color selected

// you may optionally provide a callback function to sanitize/validate with (3.0.125+):
$isActive = $input->get('active', function($val) { return $val ? true : false; });
~~~~~

@param string $key Name of GET variable you want to retrieve.
 - If populated, returns the value corresponding to the key or NULL if it doesn’t exist.
 - If blank, returns reference to the WireDataInput containing all GET vars.

@param array|string|int|callable|null $valid Omit for no validation/sanitization, or provide one of the following (3.0.125+ only):
 - String name of Sanitizer method to to sanitize value with before returning it.
 - CSV string of multiple sanitizer names to process the value, in order.
 - Array of allowed values (aka whitelist), where input value must be one of these, otherwise null (or fallback value) will returned.
   Values in the array may be any string or integer.
 - Callback function to sanitize and validate the value.
 - Integer if a specific number is the only allowed value other than fallback value (i.e. like a checkbox toggle).

@param mixed|null Optional fallback value to return if input value is not present or does not validate (3.0.125+ only).

@return null|mixed|WireInputData Returns one of the following:
 - If given no `$key` argument, returns `WireInputData` with all unsanitized GET vars.
 - If given no `$valid` argument, returns unsanitized value or NULL if not present.
 - If given a Sanitizer name for `$valid` argument, returns value sanitized with that Sanitizer method (3.0.125+).
 - If given an array of allowed values for `$valid` argument, returns value from that array if it was in the input, or null if not (3.0.125+).
 - If given a callable function for `$valid` argument, returns the value returned by that function (3.0.125+).
 - If given a `$fallback` argument, returns that value when it would otherwise return null (3.0.125+).

@throws WireException if given unknown Sanitizer method for $valid argument

## post()

Retrieve a named POST variable value, or all POST variables

Always sanitize (and validate where appropriate) any values from user input.

The following optional features are available in ProcessWire version 3.0.125 and newer:

- Provide a sanitization method as the 2nd argument to include sanitization.
- Provide an array of valid values as the 2nd argument to limit input to those values.
- Provide a callback function that receives the value and returns a validated value.
- Provide a fallback value as the 3rd argument to use if value not present or invalid.
- Append “[]” to the 1st argument to always force return value to be an array, i.e “colors[]”.

Note that the `$valid` and `$fallback` arguments are only applicable if a `$key` argument is provided.


~~~~~
// Retrieve a "comments" POST variable, sanitize and output it
$comments = $input->post('comments');
$comments = $sanitizer->textarea($comments); // sanitize input as multi-line text with no HTML
echo $sanitizer->entities($comments); // sanitize for output

// You can also combine $input and one $sanitizer call like this,
// replacing "text" with name of any $sanitizer method:
$comments = $input->post->textarea('comments');

// like the previous example, but specify sanitizer method as second argument (3.0.125+):
$comments = $input->post('comments', 'textarea');

// if you want more than one sanitizer, specify multiple in a CSV string (3.0.125+):
$comments = $input->post('comments', 'textarea,entities');

// you can provide a whitelist array of allowed values instead of a sanitizer method (3.0.125+):
$color = $input->post('color', [ 'red', 'blue', 'green' ]);

// an optional 3rd argument lets you specify a fallback value to use if valid value not present or
// empty in input, and it will return this value rather than null/empty (3.0.125+):
$qty = $input->post('qty', 'int', 1); // return 1 if no qty provided
$color = $input->post('color', [ 'red', 'blue', 'green' ], 'red'); // return red if no color selected

// you may optionally provide a callback function to sanitize/validate with (3.0.125+):
$isActive = $input->post('active', function($val) { return $val ? true : false; });
~~~~~

@param string $key Name of POST variable you want to retrieve.
 - If populated, returns the value corresponding to the key or NULL if it doesn't exist.
 - If blank, returns reference to the WireDataInput containing all POST vars.

@param array|string|int|callable|null $valid Omit for no validation/sanitization, or provide one of the following:
 - String name of Sanitizer method to to sanitize value with before returning it.
 - CSV string of multiple sanitizer names to process the value, in order.
 - Array of allowed values (aka whitelist), where input value must be one of these, otherwise null (or fallback value) will returned.
   Values in the array may be any string or integer.
 - Callback function to sanitize and validate the value.
 - Integer if a specific number is the only allowed value other than fallback value (i.e. like a checkbox toggle).

@param mixed|null Optional Fallback value to return if input value is not present or does not validate.

@return null|mixed|WireInputData Returns one of the following:
 - If given no `$key` argument, returns `WireInputData` with all unsanitized POST vars.
 - If given no `$valid` argument, returns unsanitized value or NULL if not present.
 - If given a Sanitizer name for `$valid` argument, returns value sanitized with that Sanitizer method (3.0.125+).
 - If given an array of allowed values for `$valid` argument, returns value from that array if it was in the input, or null if not (3.0.125+).
 - If given a callable function for `$valid` argument, returns the value returned by that function (3.0.125+).
 - If given a `$fallback` argument, returns that value when it would otherwise return null (3.0.125+).

@throws WireException if given unknown Sanitizer method for $valid argument

## cookie()

Retrieve a named COOKIE variable value or all COOKIE variables

Please see the [cookie API reference page](https://processwire.com/api/ref/wire-input-data-cookie/) for
additional documentation on how to get and set cookies and cookie options.

~~~~~
// setting cookies
$input->cookie->foo = 'bar'; // set with default options (expires with session)
$input->cookie->set('foo', 'bar'); // same as above
$input->cookie->set('foo', 'bar', 86400); // expire after 86400 seconds (1 day)
$input->cookie->set('foo', 'bar', [ 'age' => 86400, 'path' => $page->url ]);

// getting cookies
$val = $input->cookie->foo;
$val = $input->cookie->get('foo'); // same as above
$val = $input->cookie->text('foo'); // get and use text sanitizer

// removing cookies
$input->cookie->remove('foo');

// getting cookie options
$array = $input->cookie->options();
print_r($array); // see all options

// setting cookie options (to use in next $input->cookie->set call)
$input->cookie->options('age', 86400); // set default age to 1 day
$input->cookie->options([ // set multiple options
  'age' => 86400,
  'path' => $page->url,
  'domain' => 'www.domain.com',
]);

// setting default options (in /site/config.php):
$config->cookieOptions = [
  'age' => 604800, // 1 week
  'httponly' => true, // make visible to PHP but not JS
   // and so on
];
~~~~~

Cookies are a form of user input, so always sanitize (and validate where appropriate) any values.

The following optional features are available in ProcessWire version 3.0.125 and newer:

- Provide a sanitization method as the 2nd argument to include sanitization.
- Provide an array of valid values as the 2nd argument to limit input to those values.
- Provide a callback function that receives the value and returns a validated value.
- Provide a fallback value as the 3rd argument to use if value not present or invalid.
- Append “[]” to the 1st argument to always force return value to be an array, i.e “colors[]”.

Note that the `$valid` and `$fallback` arguments are only applicable if a `$key` argument is provided.
See the `WireInput::get()` method for usage examples (get method works the same as cookie method).

@param string $key Name of the COOKIE variable you want to retrieve.
 - If populated, returns the value corresponding to the key or NULL if it doesn't exist.
 - If blank, returns reference to the WireDataInput containing all COOKIE vars.

@param array|string|int|callable|null $valid Omit for no validation/sanitization, or provide one of the following:
 - String name of Sanitizer method to to sanitize value with before returning it.
 - CSV string of multiple sanitizer names to process the value, in order.
 - Array of allowed values (aka whitelist), where input value must be one of these, otherwise null (or fallback value) will returned.
   Values in the array may be any string or integer.
 - Callback function to sanitize and validate the value.
 - Integer if a specific number is the only allowed value other than fallback value (i.e. like a checkbox toggle).

@param mixed|null Optional Fallback value to return if input value is not present or does not validate.

@return null|mixed|WireInputData Returns one of the following:
 - If given no `$key` argument, returns `WireInputData` with all unsanitized COOKIE vars.
 - If given no `$valid` argument, returns unsanitized value or NULL if not present.
 - If given a Sanitizer name for `$valid` argument, returns value sanitized with that Sanitizer method (3.0.125+).
 - If given an array of allowed values for `$valid` argument, returns value from that array if it was in the input, or null if not (3.0.125+).
 - If given a callable function for `$valid` argument, returns the value returned by that function (3.0.125+).
 - If given a `$fallback` argument, returns that value when it would otherwise return null (3.0.125+).

@throws WireException if given unknown Sanitizer method for $valid argument

## whitelist()

Get or set a whitelist variable

Whitelist variables are used by modules and templates and assumed to be sanitized.
Only place variables in the whitelist that you have already sanitized.

The whitelist is a list of variables specifically set by the application as sanitized for use elsewhere in the application.
This whitelist is not specifically used by ProcessWire unless you populate it from your templates or the API.
When populated, it is used by the MarkupPagerNav module (for instance) to ensure that sanitized query string (GET) variables
are maintained across paginations.

~~~~~
// Retrieve a GET variable, sanitize/validate it, and populate to whitelist
$limit = (int) $input->get('limit');
if($limit < 10 || $limit > 100) $limit = 25; // validate
$input->whitelist('limit', $limit);
~~~~~
~~~~~
// Retrieve a variable from the whitelist
$limit = $input->whitelist('limit');
~~~~~

@param string $key Whitelist variable name that you want to get or set.
 - If $key is blank, it assumes you are asking to return the entire whitelist.
 - If $key and $value are populated, it adds the value to the whitelist.
 - If $key is an array, it adds all the values present in the array to the whitelist.
 - If $value is omitted, it assumes you are asking for a value with $key, in which case it returns it.

@param mixed $value Value you want to set (if setting a value). See explanation for the $key param.

@return null|mixed|WireInputData Returns whitelist variable value if getting a value (null if it doesn't exist).

## urlSegment()

Retrieve matching URL segment number or pattern

In all ProcessWire versions  this method accepts a 1-based index and returns the
corresponding URL segment, where 1 is first URL segment, 2 is second, etc.

In ProcessWire versions 3.0.155 and newer, this method also does the following:

- If given a negative number, it will retrieve from the end of the URL segments.
  For example, if given -1 it will return the last URL segment, -2 will return second
  to last, and so on.

- If given a full URL segment (i.e. “foo”) it will return the 1-based index at which that
  segment exists, or 0 if not present.

- If given URL segment followed by equals sign, i.e. “foo=” it will return the next URL
  segment that comes after it. If equals sign comes before URL segment, i.e. “=bar”, it
  will return the URL segment that came before it. This lets you create “key=value”
  type relationships with URL segments. For example, an argument of “foo=” would return
  the segment “bar” when applied to URL /path/to/page/foo/bar/.

- If given a wildcard string, it will return the first matching URL segment. For example,
  the wildcard string `foo-*` would match the first URL segment to begin with “foo-”,
  so any of these segments would match & be returned: `foo-bar`, `foo-12345`, `foo-baz123`.
  A wildcard string of `*bar` would match anything ending with “bar”, i.e. it would match
  and return `foo-bar`, `foobar`, `baz_123bar`, etc.

- If given a wildcard string with parenthesis in it, then only the portion in parenthesis
  is returned for the first matching URL segment. For example, `foo-(*)` would match the
  URL segment `foo-baz123` and would return just the `baz123` portion.

- If given a regular expression (PCRE regex), the behavior is the same as with wildcards,
  except that your regex is used to perform the match. If there are capturing parenthesis
  in the regex then the first captured text is returned rather than the whole URL segment.
  To specify a regex, choose one of the following characters as your opening and closing
  delimiters: `/`, `!`, `%`, `#`, `@`.

- If you want to focus any of the above options upon a URL segment at a specific index,
  then you can append the index number to the method name. For example, if you want it to
  just focus on URL segment #1, then call `$input->urlSegment1(…)`, or for URL segment #2
  you would call `$input->urlSegment2(…)`, and so on.

Please also note the following about URL segments:

- URL segments must be enabled in the template settings (for template used by the page).
- When using index numbers, note that it is 1-based. There is no 0 index for URL segments.
- If no arguments are provided, it assumes you ar asking for the first (1) URL segment.
- The maximum segments allowed can be adjusted in your `$config->maxUrlSegments` setting.
- URL segments are populated by ProcessWire automatically on each request.
- URL segments are already sanitized as page names.
- Strongly recommended: throw a 404 when encountering URL segments you do not recognize.

~~~~~
// Get first URL segment and use it to determine output
$action = $input->urlSegment(1);
if($action == 'photos') {
  // display photos
} else if($action == 'map') {
  // display map
} else if(strlen($action)) {
  // unknown action, throw a 404
  throw new Wire404Exception();
} else {
  // default or display main page
}

// All following examples require PW 3.0.155+.

// Examples 1-5 below assume current URL is /path/to/page/foo/bar
// and that /foo/bar is the URL segments portion of the URL.

// 1. Check if URL segment “foo” is present
if($input->urlSegment('foo')) {
  // “foo” is present as a URL segment
}

// 2. Get index of matching URL segment
if($input->urlSegment('foo') === 1) {
  // “foo” is first URL segment
}

// 3. Get last URL segment
if($input->urlSegment(-1) === 'bar') {
  // “bar” is last URL segment
}

// 4. Get next URL segment
$next = $input->urlSegment('foo='); // returns 'bar'

// 5. Get previous URL segment
$prev = $input->urlSegment('=bar'); // returns 'foo'

// Examples 6-8 below assume current URL is /path/to/page/sort-date/
// where /sort-date/ is the URL segment.

// 6. Match URL segment using wildcard
$sort = $input->urlSegment('sort-*');
if($sort === 'sort-title') {
  // sort by title
} else if($sort === 'sort-date') {
  // sort by date
} else if(strlen($sort)) {
  // unknown sort value, throw 404 or fallback to default
} else {
  // no sort specified, use default
}

// 7. Match using wildcard and parenthesis
$sort = $input->urlSegment('sort-(*)');
if($sort === 'title') {
  // sort by title
} else if($sort === 'date') {
  // sort by date
} else if(strlen($sort)) {
  // unknown sort value, throw 404?
} else {
  // no sort specified, use default
}

// 8. Match using regular expression
$sort = $input->urlSegment('/^sort-(.+)$/');
if($sort === 'title') {
  // same if statement as example 5...
}

// 9. Similar goal to above but with URL /path/to/page/sort/date/
// that uses separate segment for sort value, which is a good
// example of using the “next” segment feature:
$sort = $input->urlSegment('sort=');
if($sort === 'title') {
  // sort by title
} else if($sort === 'date') {
  // sort by date
} else if($sort === '-date') {
  // reverse sort by date
} else {
  // no sort specified, use default
}
~~~~~


@param int|string $get Specify one of the following
 - Omit argument to simply return 1st URL segment.
 - Positive integer of n’th URL segment where first is 1.
 - Negative integer of URL segment to match from end where last is -1. (3.0.155+)
 - Full URL segment string to return index for, if present (or 0 if not). (3.0.155+)
 - Full URL segment with equals sign before or after it, to return segment before or after it. (3.0.155+)
 - Wildcard string to match, as described in method description and examples. (3.0.155+)
 - Regular expression string to match, as described in method description and examples. (3.0.155+)

@return string|int Returns one of the following:
 - URL segment at requested index or blank string if not present.
 - Index (integer) of matching URL segment when given entire segment to match, or 0 when there is no match. (3.0.155+)
 - Matching URL segment when given wildcard string or regular expression. (3.0.155+)
 - Portion of matching URL segment when given wildcard or regex with parenthesis around pattern to match. (3.0.155+)

@see WireInput::urlSegmentStr()

## urlSegmentMatch()

Handles find/match logic for URL segment methods

@param string $get URL segment match string

@param int $num Limit only to this URL segment number (default=0 to indicate ignore)

@return string|int|bool

@since 3.0.155

## urlSegments()

Retrieve array of all URL segments

- URL segments must be enabled in the template settings (for template used by the page).
- The maximum segments allowed can be adjusted in your `$config->maxUrlSegments` setting.
- URL segments are populated by ProcessWire automatically on each request.
- URL segments are already sanitized as page names.


@return array Returns an array of strings, or an empty array if no URL segments available.

## setUrlSegment()

Set a URL segment value

- This is typically only used by the core.
- To unset, specify NULL as the value.


@param int $num Number of this URL segment (1 based)

@param string|null $value Value to set, or NULL to unset.

## urlSegmentStr()

Get the string of URL segments separated by slashes

- Note that return value lacks leading or trailing slashes.
- URL segments must be enabled in the template settings (for template used by the page).
- The maximum segments allowed can be adjusted in your `$config->maxUrlSegments` setting.
- URL segments are populated by ProcessWire automatically on each request.
- URL segments are already sanitized as page names.
- The URL segment string can also be accessed by property: `$input->urlSegmentStr`.

~~~~~
// Adjust output according to urlSegmentStr
// In this case our urlSegmentStr is 2 URL segments
$s = $input->urlSegmentStr();
if($s == 'photos/large') {
  // show large photos
} else if($s == 'photos/small') {
  // show small photos
} else if($s == 'map') {
  // show map
} else if(strlen($s)) {
  // something we don't recognize
  throw new Wire404Exception();
} else {
  // no URL segments present, do some default behavior
  echo $page->body;
}
~~~~~


@param bool|array $verbose Include pagination number (pageNum) and trailing slashes, when appropriate? (default=false)
 - Use this option for a more link-ready version of the URL segment string (since 3.0.106).
 - Optionally substitute $options argument for this argument, default for $verbose option remains false (since 3.0.155+).

@param array $options Options to adjust behavior (since 3.0.106):
 - `segments` (array): Optionally specify URL segments to use, rather than those from current request. (default=[])
 - `values` (array): Same as segments option, but associative array converted to /key1/value1/key2/value2/ segment string. (default=[]) 3.0.155+
 - `pageNum` (int): Optionally specify page number to use rather than current. (default=current page number)
 - `page` (Page): Optionally specify Page to use for context. (default=current page)
 - `verbose` (bool): Verbose argument from method, applies only if $options given for $verbose argument.
 - *NOTE* the `pageNum` and `page` options are not applicable unless the $verbose argument is true.

@return string URL segment string, i.e. `segment1/segment2/segment3` or blank if none

@see WireInput::urlSegment()

## pageNum()

Return the current pagination/page number (starting from 1)

- Page numbers must be enabled in the template settings (for template used by the page).
- The current page number affects all paginated page finding operations.
- First page number is 1 (not 0).

~~~~~
// Adjust output according to page number
if($input->pageNum == 1) {
  echo $page->body;
} else {
  echo "<a href='$page->url'>Return to first page</a>";
}
~~~~~


@return int Current pagination number

## pageNumStr()

Return the string that represents the page number URL segment

Returns blank when page number is 1, since page 1 is assumed when no pagination number present in URL.

This is the string that gets appended to the URL and typically looks like `page123`,
but can be changed by modifying the `$config->pageNumUrlPrefix` setting, or specifying
language-specific page number settings in the LanguageSupportPageNames module.


@param int $pageNum Optionally specify page number to use (default=0, which means use current page number)

@return string

@since 3.0.106

## setPageNum()

Set the current page number.

- This is typically used only by the core.
- Note that the first page should be 1 (not 0).


@param int $num

## __get()

Retrieve the get, post, cookie or whitelist vars using a direct reference, i.e. $input->cookie

Can also be used with URL segments, i.e. $input->urlSegment1, $input->urlSegment2, $input->urlSegment3, etc.
And can also be used for $input->pageNum.

@param string $key

@return string|int|null

## url()

Get the URL that initiated the current request, including URL segments and page numbers

- This should be the same as `$page->url` except that it includes URL segments and page numbers, when present.

- Note that this does not include query string unless requested (see arguments).

- WARNING: if query string requested, it can contain undefined/unsanitized user input. If you use it for output
  make sure that you entity encode first (by running through `$sanitizer->entities()` for instance).

~~~~~~
$url = $input->url();
$url = $sanitizer->entities($url); // entity encode for output
echo "You accessed this page at: $url";
~~~~~~


@param array|bool $options Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array:
 - `withQueryString` (bool): Include the query string as well? (if present, default=false)
 - `page` (Page): Page object to use, if different from $page (default=$page)
 - `pageNum` (int): Override current pagination number with this one, 1 to exclude pageNum, 0 for no override (default=0). 3.0.169+

@return string

@see WireInput::httpUrl(), Page::url()

## httpUrl()

Get the http URL that initiated the current request, including scheme, URL segments and page numbers

- This should be the same as `$page->httpUrl` except that it includes URL segments and page numbers, when present.

- Note that this does not include query string unless requested (see arguments).

- WARNING: if query string requested, it can contain undefined/unsanitized user input. If you use it for output
  make sure that you entity encode first (by running through `$sanitizer->entities()` for instance).

~~~~~~
$url = $input->httpUrl();
$url = $sanitizer->entities($url); // entity encode for output
echo "You accessed this page at: $url";
~~~~~~


@param array|bool $options Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array:
 - `withQueryString` (bool): Include the query string as well? (if present, default=false)
 - `page` (Page): Page object to use, if different from $page (default=$page)

@return string

@see WireInput::url(), Page::httpUrl()

## httpsUrl()

Same as httpUrl() method but always uses https scheme, rather than current request scheme

See httpUrl() method for argument and usage details.


@param array|bool $options Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array:
 - `withQueryString` (bool): Include the query string as well? (if present, default=false)
 - `page` (Page): Page object to use, if different from $page (default=$page)

@return string

@see WireInput::httpUrl()

## httpHostUrl()

Get current scheme and URL for hostname without any path or query string

For example: `https://www.domain.com`


@param string|bool|null Optionally specify this argument to force a particular scheme (rather than using current):
 - boolean true or string "https" to force “https”
 - boolean false or string "http" to force “http”
 - string with some other scheme you want to use
 - blank string or "//" for no scheme, i.e. URL begins with "//" which refers to current scheme.
 - omit argument or null to use current request scheme (default behavior).

@param string $httpHost HTTP host to use or leave blank for current host

@return string

## canonicalUrl()

Generate canonical URL for current page and request

Canonical URL includes full scheme, hostname, path and optionally:
URL segments, page numbers and query string.


@param array $options
 - `scheme` (string|bool): Scheme "https", "http", or omit to auto-detect (default='').
 - `host` (string): Hostname or omit to use current http host (default='').
 - `page` (Page): Page to use for URL or omit for current Page (default=$page).
 - `urlSegments` (array|string|bool): True to include current URL segments, false to disable,
    or specify array or string of URL segments to use (default=true).
 - `notSegments` (array|string): Full URL segments or patterns (wildcard or regex) to exclude
    from canonical URL (default=[])
 - `pageNum` (bool|int): True to include current page/pagination number, false to disable,
    or specify pagination number (int) to use (default=true).
 - `queryString` (bool|string|array): True to use current whitelist query string, false to disable,
    or specify array of query string vars, or actual query string as string (default=true).
 - `language` (bool|Language): True for current language, false to force default or no language,
    or specify Language object to use that language. (default=true)

@return string

@since 3.0.155

## queryString()

Return the unsanitized query string that was part of this request, or blank if none

Note that the returned query string is not sanitized, so if you use it in any output
be sure to run it through `$sanitizer->entities()` first. An optional assoc array
param can be used to add new GET params or override existing ones.


@param array $overrides Optional assoc array for overriding or adding GET params

@return string Returns the unsanitized query string

@see WireInput::queryStringClean()

## queryStringClean()

Return a cleaned query string that was part of this request, or blank if none

Note: it is recommended that you always specify $options with this method as the defaults
may or may not be consistent with your needs.


@param array $options
 - `values` (array): Optional associative array of [name=value] to use in query string rather than current GET vars. (default=[])
 - `overrides` (array): Array of values to override or add to current request values. (default=[])
 - `validNames` (array): Only include query string variables with these names, and omit any others. (default=[])
 - `maxItems` (int): Maximum number of variables/items to include in the query string or 0 for no max. (default=20)
 - `maxLength` (int): Max overall length of returned query string or 0 for no max. (default=1024)
 - `maxNameLength` (int): Max length of any “name” in the “name=value” portion of a query string or 0 for no max. (default=50)
 - `maxValueLength` (int): Max length of any “value” in the “name=value” portion of a query string or 0 for no max. (default=255)
 - `maxArrayDepth` (int): Maximum depth for arrays, or 0 to disallow arrays. (default=0)
 - `maxArrayItems` (int): Maximum number of items allowed in arrays or 0 for no max. (default=20)
 - `associative` (bool): Allow associative arrays? (default=false)
 - `sanitizeName` (string): Sanitize query string variable names with this sanitizer method or blank to ignore. (default='fieldName')
 - `sanitizeValue` (string): Sanitize query string variable values with this sanitizer method or blank to ignore. (default='line')
 - `sanitizeRemove` (bool): Remove any variables from query string that are changed as the result of sanitization? (default=true)
 - `entityEncode` (bool): Should returned query string be entity encoded for HTML output? (default=true)
 - `encType` (int): Use PHP_QUERY_RFC3986 for spaces encoded to '%20' or PHP_QUERY_RFC1738 for spaces as '+'. (default=PHP_QUERY_RFC3986)
 - `separator` (string): Character(s) that separate each “name=value” in query string. (default='&')

@return string

@since 3.0.167

## scheme()

Return the current access scheme/protocol

Note that this is only useful for http/https, as we don't detect other schemes.


@return string Return value is either "https" or "http"

## requestMethod()

Return the current request method (i.e. GET, POST, etc.) or blank if not known

Possible return values are:
- GET
- POST
- HEAD
- PUT
- DELETE
- OPTIONS
- or blank if not known

@param string $method Optionally enter the request method to return bool if current method matches

@return string|bool

@since 3.0.39

## is()

Is the current request of the specified type?

This is a more readable/shorter alias of `$input->requestMethod('type')` for syntax convenience.
Internally, it determines the request type without accessing any input data, so it is efficient.

~~~~~
// The following are equivalent:
$isPost = $input->is('post');
$isPost = $input->requestMethod('post');
~~~~~

@param string $method Specify one of: post, get, head, put, delete, options, patch (not case sensitive)

@return bool

@since 3.0.145

## getValidInputValue()

Provides the implementation for get/post/cookie method validation and fallback features

@param WireInputData $input

@param string $key Name of variable to pull from $input

@param array|string|callable|mixed|null $valid String containing name of Sanitizer method, or array of allowed values.

@param string|array|int|mixed $fallback Return this value rather than null if input value is not present or not valid.

@return array|int|mixed|null|WireInputData|string

@throws WireException if given unknown Sanitizer method or some other invalid arguments.

## filterValue()

Filter value against given $valid whitelist

@param string|array $value

@param array $valid Whitelist of valid values

@param bool $getArray Filter to allow multiple values (array)?

@return array|string|null

@throws WireException If given a multidimensional array for $valid argument

## sanitizeValue()

Sanitize the given value with the given method(s)

@param string $method Sanitizer method name or CSV string of sanitizer method names

@param string|array|null $value

@param bool $getArray

@return array|int|float|string|null

@throws WireException If given unknown sanitizer method

## __debugInfo()

debugInfo PHP 5.6+ magic method

This is used when you print_r() an object instance.

@return array
