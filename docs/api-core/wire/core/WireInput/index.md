# WireInput

Source: `wire/core/WireInput.php`

Inherits: `Wire`

## Summary

Manages the group of GET, POST, COOKIE and whitelist vars, each of which is a WireInputData object.

Common methods:
- [`setLazy()`](method-setlazy.md)
- [`get()`](method-get.md)
- [`post()`](method-post.md)
- [`cookie()`](method-cookie.md)
- [`whitelist()`](method-whitelist.md)

Groups:
Group: [other](group-other.md)
Group: [URL-segments](group-url-segments.md)
Group: [URLs](group-urls.md)

Provides a means to get user input from URLs, GET, POST, and COOKIE variables and more.

@link https://processwire.com/api/ref/wire-input/ Offical `$input` API variable Documentation




Note that properties and methods that end with numbers 1-3 above (like urlSegment1, urlSegment1(), etc.)
continue for as many numbers as the system supports, so you may go beyond 3 where supported.

## Methods
- [`__construct()`](method-__construct.md) Construct
- [`get(string $key = '', array|string|int|callable|null $valid = null, $fallback = null): null|mixed|WireInputData`](method-get.md) Retrieve a named GET variable value, or all GET variables (from URL query string)
- [`post(string $key = '', array|string|int|callable|null $valid = null, $fallback = null): null|mixed|WireInputData`](method-post.md) Retrieve a named POST variable value, or all POST variables
- [`cookie(string $key = '', array|string|int|callable|null $valid = null, $fallback = null): null|mixed|WireInputData`](method-cookie.md) Retrieve a named COOKIE variable value or all COOKIE variables
- [`whitelist(string $key = '', mixed $value = null): null|mixed|WireInputData`](method-whitelist.md) Get or set a whitelist variable
- [`urlSegment(int|string $get = 1): string|int`](method-urlsegment.md) Retrieve matching URL segment number or pattern
- [`urlSegmentMatch(string $get, int $num = 0): string|int|bool`](method-urlsegmentmatch.md) Handles find/match logic for URL segment methods
- [`urlSegments(): array`](method-urlsegments.md) Retrieve array of all URL segments
- [`setUrlSegment(int $num, string|null $value)`](method-seturlsegment.md) Set a URL segment value
- [`urlSegmentStr(bool|array $verbose = false, array $options = array()): string`](method-urlsegmentstr.md) Get the string of URL segments separated by slashes
- [`pageNum(): int`](method-pagenum.md) Return the current pagination/page number (starting from 1)
- [`pageNumStr(int $pageNum = 0): string`](method-pagenumstr.md) Return the string that represents the page number URL segment
- [`setPageNum(int $num)`](method-setpagenum.md) Set the current page number.
- [`__get(string $key): string|int|null`](method-__get.md) Retrieve the get, post, cookie or whitelist vars using a direct reference, i.e. `$input->cookie`
- [`url(array|bool $options = array()): string`](method-url.md) Get the URL that initiated the current request, including URL segments and page numbers
- [`httpUrl(array|bool $options = array()): string`](method-httpurl.md) Get the http URL that initiated the current request, including scheme, URL segments and page numbers
- [`httpsUrl(array|bool $options = array()): string`](method-httpsurl.md) Same as httpUrl() method but always uses https scheme, rather than current request scheme
- [`httpHostUrl($scheme = null, string $httpHost = ''): string`](method-httphosturl.md) Get current scheme and URL for hostname without any path or query string
- [`canonicalUrl(array $options = array()): string`](method-canonicalurl.md) Generate canonical URL for current page and request
- [`queryString(array $overrides = array()): string`](method-querystring.md) Return the unsanitized query string that was part of this request, or blank if none
- [`queryStringClean(array $options = array()): string`](method-querystringclean.md) Return a cleaned query string that was part of this request, or blank if none
- [`scheme(): string`](method-scheme.md) Return the current access scheme/protocol
- [`requestMethod(string $method = ''): string|bool`](method-requestmethod.md) Return the current request method (i.e. GET, POST, etc.) or blank if not known
- [`is(string $method): bool`](method-is.md) Is the current request of the specified type?
- [`getValidInputValue(WireInputData $input, string $key, array|string|callable|mixed|null $valid, string|array|int|mixed $fallback): array|int|mixed|null|WireInputData|string`](method-getvalidinputvalue.md) Provides the implementation for get/post/cookie method validation and fallback features
- [`filterValue(string|array $value, array $valid, bool $getArray): array|string|null`](method-filtervalue.md) Filter value against given `$valid` whitelist
- [`sanitizeValue(string $method, string|array|null $value, bool $getArray): array|int|float|string|null`](method-sanitizevalue.md) Sanitize the given value with the given method(s)
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
