# $wireInputDataCookie->get($key, $options = array()): string|int|float|array|null

Source: `wire/core/WireInputDataCookie.php`

Get a cookie value

Gets a previously set cookie value or null if cookie not present or expired.
Cookies are a type of user input, so always sanitize (and validate where appropriate) any values.

~~~~~
$val = $input->cookie->foo;
$val = $input->cookie->get('foo'); // same as above
$val = $input->cookie->text('foo'); // get and use text sanitizer
~~~~~

## Arguments

- string $key Name of cookie to get
- array|int|string $options Options not currently used, but available for descending classes or future use

## Return value

string|int|float|array|null $value
