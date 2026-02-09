# $wireInputDataCookie->__set($key, $value)

Source: `wire/core/WireInputDataCookie.php`

Set a cookie (directly)

To set options for setting cookie, use $input->cookie->options(key, value); or $config->cookieOptions(key, value);
Note that options set from $input->cookie->options take precedence over those set to $config.

## Usage

~~~~~
// basic usage
$result = $wireInputDataCookie->__set($key, $value);
~~~~~

## Arguments

- `$key` `string` Cookie name
- `$value` `array|float|int|null|string` Cookie value
