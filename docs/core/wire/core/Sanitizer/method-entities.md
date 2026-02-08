# $sanitizer->entities($str, $flags = ENT_QUOTES, $encoding = 'UTF-8', $doubleEncode = true): string

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

## Arguments

- `$str` `string` String to entity encode
- `$flags` (optional) `int|bool` See PHP htmlentities() function for flags.
- `$encoding` (optional) `string` Encoding of string (default="UTF-8").
- `$doubleEncode` (optional) `bool` Allow double encode? (default=true).

## Return value

string Entity encoded string

## See also

- [Sanitizer::entities1()](method-entities1.md)
- [Sanitizer::unentities()](method-unentities.md)
