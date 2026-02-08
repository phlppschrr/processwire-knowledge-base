# $wireInput->canonicalUrl(array $options = array()): string

Source: `wire/core/WireInput.php`

Generate canonical URL for current page and request

Canonical URL includes full scheme, hostname, path and optionally:
URL segments, page numbers and query string.

## Usage

~~~~~
// basic usage
$string = $wireInput->canonicalUrl();

// usage with all arguments
$string = $wireInput->canonicalUrl(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` - `scheme` (string|bool): Scheme "https", "http", or omit to auto-detect (default=''). - `host` (string): Hostname or omit to use current http host (default=''). - `page` (Page): Page to use for URL or omit for current Page (default=$page). - `urlSegments` (array|string|bool): True to include current URL segments, false to disable, or specify array or string of URL segments to use (default=true). - `notSegments` (array|string): Full URL segments or patterns (wildcard or regex) to exclude from canonical URL (default=[]) - `pageNum` (bool|int): True to include current page/pagination number, false to disable, or specify pagination number (int) to use (default=true). - `queryString` (bool|string|array): True to use current whitelist query string, false to disable, or specify array of query string vars, or actual query string as string (default=true). - `language` (bool|Language): True for current language, false to force default or no language, or specify Language object to use that language. (default=true)

## Return value

- `string`

## Since

3.0.155
