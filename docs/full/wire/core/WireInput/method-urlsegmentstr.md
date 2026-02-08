# $wireInput->urlSegmentStr($verbose = false, array $options = array()): string

Source: `wire/core/WireInput.php`

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

## Arguments

- bool|array $verbose Include pagination number (pageNum) and trailing slashes, when appropriate? (default=false) - Use this option for a more link-ready version of the URL segment string (since 3.0.106). - Optionally substitute $options argument for this argument, default for $verbose option remains false (since 3.0.155+).
- array $options Options to adjust behavior (since 3.0.106): - `segments` (array): Optionally specify URL segments to use, rather than those from current request. (default=[]) - `values` (array): Same as segments option, but associative array converted to /key1/value1/key2/value2/ segment string. (default=[]) 3.0.155+ - `pageNum` (int): Optionally specify page number to use rather than current. (default=current page number) - `page` (Page): Optionally specify Page to use for context. (default=current page) - `verbose` (bool): Verbose argument from method, applies only if $options given for $verbose argument. - *NOTE* the `pageNum` and `page` options are not applicable unless the $verbose argument is true.

## Return value

string URL segment string, i.e. `segment1/segment2/segment3` or blank if none

## See also

- [WireInput::urlSegment()](method-urlsegment.md)
