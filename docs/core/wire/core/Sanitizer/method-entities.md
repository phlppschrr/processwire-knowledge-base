# Sanitizer::entities()

Source: `wire/core/Sanitizer.php`

Entity encode a string for output

Wrapper for PHP's `htmlentities()` function that contains typical ProcessWire usage defaults

The arguments used here are identical to those for
[PHP's htmlentities](http://www.php.net/manual/en/function.htmlentities.php) function,
except that the ProcessWire defaults for encoding quotes and using UTF-8 are already populated.

~~~~~
$test = "ain't <em>nothing</em> perfect but our brokenness";
echo $sanitizer->entities($test);
// result: ain&apos;t &lt;em&gt;nothing&lt;/em&gt; perfect but our brokenness
~~~~~


@param string $str String to entity encode

@param int|bool $flags See PHP htmlentities() function for flags.

@param string $encoding Encoding of string (default="UTF-8").

@param bool $doubleEncode Allow double encode? (default=true).

@return string Entity encoded string

@see Sanitizer::entities1(), Sanitizer::unentities()
