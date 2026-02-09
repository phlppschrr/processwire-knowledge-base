# $wireInput->urlSegment($get = 1): string|int

Source: `wire/core/WireInput.php`

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

## Example

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

```php

```
~~~~~

## Usage

~~~~~
// basic usage
$string = $wireInput->urlSegment();

// usage with all arguments
$string = $wireInput->urlSegment($get = 1);
~~~~~

## Arguments

- `$get` (optional) `int|string` Specify one of the following - Omit argument to simply return 1st URL segment. - Positive integer of n’th URL segment where first is 1. - Negative integer of URL segment to match from end where last is -1. (3.0.155+) - Full URL segment string to return index for, if present (or 0 if not). (3.0.155+) - Full URL segment with equals sign before or after it, to return segment before or after it. (3.0.155+) - Wildcard string to match, as described in method description and examples. (3.0.155+) - Regular expression string to match, as described in method description and examples. (3.0.155+)

## Return value

- `string|int` Returns one of the following: - URL segment at requested index or blank string if not present. - Index (integer) of matching URL segment when given entire segment to match, or 0 when there is no match. (3.0.155+) - Matching URL segment when given wildcard string or regular expression. (3.0.155+) - Portion of matching URL segment when given wildcard or regex with parenthesis around pattern to match. (3.0.155+)

## See Also

- [WireInput::urlSegmentStr()](method-urlsegmentstr.md)
