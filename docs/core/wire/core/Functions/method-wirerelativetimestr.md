# $functions->wireRelativeTimeStr($ts, $abbreviate = false, $useTense = true): string

Source: `wire/core/Functions.php`

Given a unix timestamp (or date string), returns a formatted string indicating the time relative to now

Examples: “1 day ago”, “30 seconds ago”, “just now”, etc.

This is the procedural version of `$datetime->relativeTimeStr()`.

Based upon: http://www.php.net/manual/en/function.time.php#89415

## Arguments

- int|string $ts Unix timestamp or date string
- bool|int|array $abbreviate Whether to use abbreviations for shorter strings. - Specify boolean TRUE for abbreviations (abbreviated where common, not always different from non-abbreviated) - Specify integer 1 for extra short abbreviations (all terms abbreviated into shortest possible string) - Specify boolean FALSE or omit for no abbreviations. - Specify associative array of key=value pairs of terms to use for abbreviations. The possible keys are: just now, ago, from now, never, second, minute, hour, day, week, month, year, decade, seconds, minutes, hours, days, weeks, months, years, decades
- bool $useTense Whether to append a tense like “ago” or “from now”, May be ok to disable in situations where all times are assumed in future or past. In abbreviate=1 (shortest) mode, this removes the leading "+" or "-" from the string.

## Return value

string

## See also

- [WireDateTime::relativeTimeStr()](../WireDateTime/method-___relativetimestr.md)
