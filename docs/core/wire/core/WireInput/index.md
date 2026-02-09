# WireInput

Source: `wire/core/WireInput.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)
Group: [URL-segments](group-url-segments.md)
Group: [URLs](group-urls.md)

Manages the group of GET, POST, COOKIE and whitelist vars, each of which is a WireInputData object.

Provides a means to get user input from URLs, GET, POST, and COOKIE variables and more.

@link https://processwire.com/api/ref/wire-input/ Offical $input API variable Documentation




Note that properties and methods that end with numbers 1-3 above (like urlSegment1, urlSegment1(), etc.)
continue for as many numbers as the system supports, so you may go beyond 3 where supported.

Methods:
- [`__construct()`](method-__construct.md)
- [`get(string $key = '', array|string|int|callable|null $valid = null, $fallback = null): null|mixed|WireInputData`](method-get.md)
- [`post(string $key = '', array|string|int|callable|null $valid = null, $fallback = null): null|mixed|WireInputData`](method-post.md)
- [`cookie(string $key = '', array|string|int|callable|null $valid = null, $fallback = null): null|mixed|WireInputData`](method-cookie.md)
- [`whitelist(string $key = '', mixed $value = null): null|mixed|WireInputData`](method-whitelist.md)
- [`urlSegment(int|string $get = 1): string|int`](method-urlsegment.md)
- [`urlSegmentMatch(string $get, int $num = 0): string|int|bool`](method-urlsegmentmatch.md)
- [`urlSegments(): array`](method-urlsegments.md)
- [`setUrlSegment(int $num, string|null $value)`](method-seturlsegment.md)
- [`urlSegmentStr(bool|array $verbose = false, array $options = array()): string`](method-urlsegmentstr.md)
- [`pageNum(): int`](method-pagenum.md)
- [`pageNumStr(int $pageNum = 0): string`](method-pagenumstr.md)
- [`setPageNum(int $num)`](method-setpagenum.md)
- [`__get(string $key): string|int|null`](method-__get.md)
- [`url(array|bool $options = array()): string`](method-url.md)
- [`httpUrl(array|bool $options = array()): string`](method-httpurl.md)
- [`httpsUrl(array|bool $options = array()): string`](method-httpsurl.md)
- [`httpHostUrl($scheme = null, string $httpHost = ''): string`](method-httphosturl.md)
- [`canonicalUrl(array $options = array()): string`](method-canonicalurl.md)
- [`queryString(array $overrides = array()): string`](method-querystring.md)
- [`queryStringClean(array $options = array()): string`](method-querystringclean.md)
- [`scheme(): string`](method-scheme.md)
- [`requestMethod(string $method = ''): string|bool`](method-requestmethod.md)
- [`is(string $method): bool`](method-is.md)
- [`getValidInputValue(WireInputData $input, string $key, array|string|callable|mixed|null $valid, string|array|int|mixed $fallback): array|int|mixed|null|WireInputData|string`](method-getvalidinputvalue.md)
- [`filterValue(string|array $value, array $valid, bool $getArray): array|string|null`](method-filtervalue.md)
- [`sanitizeValue(string $method, string|array|null $value, bool $getArray): array|int|float|string|null`](method-sanitizevalue.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
