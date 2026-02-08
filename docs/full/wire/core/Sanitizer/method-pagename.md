# $sanitizer->pageName($value, $beautify = false, $maxLength = 128, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize as a ProcessWire page name

- Page names by default support lowercase ASCII letters, digits, underscore, hyphen and period.

- Because page names are often generated from a UTF-8 title, UTF-8 to ASCII conversion will take place when `$beautify` is enabled.

- You may optionally omit the `$beautify` and/or `$maxLength` arguments and substitute the `$options` array instead.

- When substituted, the beautify and maxLength options can be specified in $options as well.

- If `$config->pageNameCharset` is "UTF8" then non-ASCII page names will be converted to punycode ("xn-") ASCII page names,
  rather than converted, regardless of `$beautify` setting.

~~~~~
$test = "Hello world!";
echo $sanitizer->pageName($test, true); // outputs: hello-world
~~~~~

## Arguments

- `$value` `string` Value to sanitize as a page name
- `$beautify` (optional) `bool|int|array` This argument accepts a few different possible values (default=false): - `true` (boolean): Make it pretty. Use this when using a pageName for the first time. - `$options` (array): You can optionally specify the $options array for this argument instead. - `Sanitizer::translate` (constant): This will make it translate non-ASCII letters based on *InputfieldPageName* module config settings. - `Sanitizer::toAscii` (constant): Convert UTF-8 characters to punycode ASCII. - `Sanitizer::toUTF8` (constant): Convert punycode ASCII to UTF-8. - `Sanitizer::okUTF8` (constant): Allow UTF-8 characters to appear in path (implied if $config->pageNameCharset is 'UTF8').
- `$maxLength` (optional) `int|array` Maximum number of characters allowed in the name. You may also specify the $options array for this argument instead.
- `$options` (optional) `array` Array of options to modify default behavior. See Sanitizer::name() method for available options, plus: - `punycodeVersion` (int): Punycode version to use with UTF-8 page names, see Sanitizer::getPunycodeVersion() method for details.

## Return value

string

## See also

- [Sanitizer::name()](method-name.md)
