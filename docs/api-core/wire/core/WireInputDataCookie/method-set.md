# $wireInputDataCookie->set($key, $value, $options = array()): $this

Source: `wire/core/WireInputDataCookie.php`

Set a cookie (optionally with options)

The defaults or previously set options from an `options()` method call are used for any `$options` not specified.

## Example

~~~~~
$input->cookie->foo = 'bar'; // set with default options (expires with session)
$input->cookie->set('foo', 'bar'); // same as above
$input->cookie->set('foo', 'bar', 86400); // expire after 86400 seconds (1 day)
$input->cookie->set('foo', 'bar', [ // set with options
  'age' => 86400,
  'path' => $page->url,
  'httponly' => true,
]);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireInputDataCookie->set($key, $value);

// usage with all arguments
$result = $wireInputDataCookie->set($key, $value, $options = array());
~~~~~

## Arguments

- `$key` `string` Cookie name
- `$value` `string` Cookie value
- `$options` (optional) `array|int|string` Specify int for `age` option, string for `expire` option, or array for multiple options: - `age` (int): Max age of cookies in seconds or 0 to expire with session. For example: 3600=1 hour, 86400=1 day, 604800=1 week, 2592000=30 days, etc. Note that the default may be overridden by `$config->cookieOptions` setting from your /site/config.php file. (default=86400) - `expire` (int|string): If you prefer to use an expiration date rather than the `age` option, specify a unix timestamp (int), ISO-8601 date string, or any date string recognized by PHP’s strtotime(), like "2020-11-03" or +1 WEEK", etc. (default=null). Please note the expire option was added in 3.0.159, previous versions should use the `age` option only. - `path` (string|null): Cookie path/URL or null for PW installation’s root URL. (default=null) - `secure` (bool|null): Transmit cookies only over secure HTTPS connection? Specify true or false, or use null to auto-detect, which uses true for cookies set when HTTPS is detected. (default=null) - `httponly` (bool): When true, cookie is visible to PHP/ProcessWire only and not visible to client-side JS code. (default=false) - `fallback` (bool): If set cookie fails (perhaps due to output already sent), attempt to set at beginning of next request? (default=true) - `domain` (string|bool|null): Cookie domain, specify one of the following: `null` or blank string for current hostname [default], boolean `true` for all subdomains of current domain, `domain.com` for domain.com and *.domain.com [same as true], `www.domain.com` for www subdomain and and hostnames off of it, like dev.www.domain.com. (default=null, current hostname)

## Return value

- `$this`

## Since

3.0.141
