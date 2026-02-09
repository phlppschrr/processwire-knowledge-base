# WireInputDataCookie

Source: `wire/core/WireInputDataCookie.php`

Inherits: `WireInputData`

Provides methods for managing cookies via the $input->cookie API variable

Enables getting, setting and removing cookies from the ProcessWire API using `$input->cookie`.


- Whether getting or setting, cookie values are always strings.
- Values retrieved from `$input->cookie` are user input (like PHP’s $_COOKIE) and need to be sanitized and validated by you.
- When removing/unsetting cookies, the path, domain, secure, and httponly options must be the same as when the cookie was set,
  as a result, it’s good to have these things predefined in `$config->cookieOptions` rather than setting during runtime.
- Note that this class does not manage PW’s session cookies.

~~~~~
// setting cookies
$input->cookie->foo = 'bar';
$input->cookie->set('foo', 'bar'); // same as above
$input->cookie['foo'] = 'bar'; // same as above

// setting cookies, with options
$input->cookie->set('foo', 'bar', 86400); // live for 1 day
$input->cookie->options('age', 3600); // any further set() cookies live for 1 hour (3600s)
$input->cookie->set('foo', 'bar'); // uses setting from above options() call

// getting cookies
$bar = $input->cookie->foo;
$bar = $input->cookie['foo']; // same as above
$bar = $input->cookie('foo'); // same as above
$bar = $input->cookie->get('foo'); // same as above
$bar = $input->cookie->text('foo'); // sanitize with text() sanitizer

// removing cookies
unset($input->cookie->foo);
$input->cookie->remove('foo'); // same as above
$input->cookie->set('foo', null); // same as above
$input->cookie->removeAll(); // remove all cookies

// to modify default cookie settings, add this to your /site/config.php file and edit:
$config->cookieOptions = [

  // Max age of cookies in seconds or 0 to expire with session
  // 3600=1 hour, 86400=1 day, 604800=1 week, 2592000=30 days, etc.
  'age' => 604800,

  // Cookie path/URL or null for PW installation’s root URL
  'path' => null,

  // Cookie domain: null for current hostname, true for all subdomains of current domain,
  // domain.com for domain and all subdomains (same as true), www.domain.com for www subdomain
  // and additional hosts off www subdomain (i.e. dev.www.domain.com)
  'domain' => null,

  // Transmit cookies only over secure HTTPS connection?
  // Specify true, false, or null to auto-detect (uses true for cookies set when HTTPS).
  'secure' => null,

  // Cookie SameSite value: When set to “Lax” cookies are preserved on GET requests to this site
  // originated from external links. May also be “Strict” or “None”. The 'secure' option is
  // required for “None”. Default value is “Lax”. Available in PW 3.0.178+.
  'samesite' => 'Lax',

  // Make cookies accessible by HTTP (ProcessWire/PHP) only?
  // When true, cookie is http/server-side only and not visible to client-side JS code.
  'httponly' => false,

  // If set cookie fails (perhaps due to output already sent),
  // attempt to set at beginning of next request?
  'fallback' => true,
];
~~~~~

Methods:
- [`__construct(array &$input = array(), bool $lazy = false)`](method-__construct.md)
- [`options(string|array|null $key = null, string|array|int|float|null $value = null): string|array|int|float|null|$this`](method-options.md)
- [`__set(string $key, array|float|int|null|string $value)`](method-__set.md)
- [`get(string $key, array|int|string $options = array()): string|int|float|array|null`](method-get.md)
- [`set(string $key, string $value, array|int|string $options = array()): $this`](method-set.md)
- [`remove(string $key): WireInputDataCookie|WireInputData|$this`](method-remove.md)
- [`removeAll(): $this|WireInputData`](method-removeall.md)
- [`allowSetCookie(string $name): bool`](method-allowsetcookie.md)
