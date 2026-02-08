# Sanitizer::hyphenCase()

Source: `wire/core/Sanitizer.php`

Convert string to be all hyphenated-lowercase (aka kabab-case, hyphen-case, dash-case, etc.)

For example, "Hello World" or "helloWorld" becomes "hello-world".


@param string $value

@param array $options
 - `hyphen` (string): Character to use as the hyphen (default='-')
 - `allow` (string): Characters to allow or range of characters to allow, for placement in regex (default='a-z0-9').
 - `allowUnderscore` (bool): Allow underscores? (default=false)

@return string
