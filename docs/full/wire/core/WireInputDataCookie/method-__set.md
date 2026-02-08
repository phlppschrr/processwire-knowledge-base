# $wireInputDataCookie->__set($key, $value)

Source: `wire/core/WireInputDataCookie.php`

Set a cookie (directly)

To set options for setting cookie, use $input->cookie->options(key, value); or $config->cookieOptions(key, value);
Note that options set from $input->cookie->options take precedence over those set to $config.

## Arguments

- string $key Cookie name
- array|float|int|null|string $value Cookie value
