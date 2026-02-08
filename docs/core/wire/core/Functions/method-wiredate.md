# $functions->wireDate($format = '', $ts = null): string|bool

Source: `wire/core/Functions.php`

Format a date, using PHP date(), strftime() or other special strings (see arguments).

This is designed to work the same wa as PHP’s `date()` but be able to accept any common format
used in ProcessWire. This is helpful in reducing code in places where you might have logic
determining when to use `date()`, `strftime()`, or `wireRelativeTimeStr()`.

This is the procedural version of the `$datetime->date()` method.

~~~~~
echo wireDate('Y-m-d H:i:s'); // Outputs: 2019-01-20 06:48:11
echo wireDate('relative', '2019-01-20 06:00'); // Outputs: 48 minutes ago
~~~~~

## Arguments

- string|int $format Use any PHP date() or strftime() format, or one of the following: - `relative` for a relative date/time string. - `relative-` for a relative date/time string with no tense. - `rel` for an abbreviated relative date/time string. - `rel-` for an abbreviated relative date/time string with no tense. - `r` for an extra-abbreviated relative date/time string. - `r-` for an extra-abbreviated relative date/time string with no tense. - `ts` makes it return a unix timestamp. - Specify blank string to make it use the system date format ($config->dateFormat) . - If given an integer and no second argument specified, it is assumed to be the second ($ts) argument.
- int|string|null $ts Optionally specify the date/time stamp or strtotime() compatible string. If not specified, current time is used.

## Return value

string|bool Formatted date/time, or boolean false on failure
