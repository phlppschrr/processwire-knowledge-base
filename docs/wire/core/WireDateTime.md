# WireDateTime

Source: `wire/core/WireDateTime.php`

ProcessWire Date/Time Tools ($datetime API variable)

The $datetime API variable provides helpers for working with dates/times and conversion between formats.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method string relativeTimeStr($ts, $abbreviate = false, $useTense = true)

## getDateFormats()

Return all predefined PHP date() formats for use as dates

~~~~~
// output all date formats
$formats = $datetime->getDateFormats();
echo "<pre>" . print_r($formats, true) . "</pre>";
~~~~~


@return array Returns an array of strings containing recognized date formats

## getTimeFormats()

Return all predefined PHP date() formats for use as times

~~~~~
// output all time formats
$formats = $datetime->getTimeFormats();
echo "<pre>" . print_r($formats, true) . "</pre>";
~~~~~


@return array Returns an array of strings containing recognized time formats

## stringToTimestamp()

Given a date/time string and expected format, convert it to a unix timestamp

@param string $str Date/time string

@param string $format Format of the date/time string in PHP date syntax

@return int Unix timestamp

## convertDateFormat()

Given a PHP date() format, convert it to either 'js', 'strftime' or 'regex' format


@param string $format PHP date() format

@param string $type New format to convert to: either 'js', 'strftime', or 'regex'

@return string

## date()

Format a date, using PHP date(), strftime() or other special strings (see arguments).

This is designed to work the same way as PHP's `date()` but be able to accept any common format
used in ProcessWire. This is helpful for reducing code in places where you might have logic
determining when to use `date()`, `strftime()`, `wireRelativeTimeStr()` or some other date
formatting function.

~~~~~~
// Output the current date/time in relative format
echo $datetime->date('relative');
~~~~~~

@param string|int $format Use one of the following:
 - [PHP date](http://php.net/manual/en/function.date.php) format
 - [PHP strftime](http://php.net/manual/en/function.strftime.php) format (detected by presence of a '%' somewhere in it)
 - `relative` for a relative date/time string.
 - `relative-` for a relative date/time string with no tense.
 - `rel` for an abbreviated relative date/time string.
 - `rel-` for an abbreviated relative date/time string with no tense.
 - `r` for an extra-abbreviated relative date/time string.
 - `r-` for an extra-abbreviated relative date/time string with no tense.
 - `ts` makes it return a unix timestamp
 - blank string makes it use the system date format ($config->dateFormat)
 - If given an integer and no second argument specified, it is assumed to be the second ($ts) argument.

@param int|string|null $ts Optionally specify the date/time stamp or strtotime() compatible string. If not specified, current time is used.

@return string|bool Formatted date/time, or boolean false on failure

## strtotime()

Parse about any English textual datetime description into a Unix timestamp using PHP’s strtotime()

This function behaves the same as PHP’s version except that it optionally accepts an `$options` array
and lets you specify the return value for empty or zeroed dates like 0000-00-00. If given a zero’d date
then it returns null by default (rather than throwing an error as PHP8 does). As of 3.0.238+ this method
also lets you optionally specify an input format should the given date string not be strtotime compatible.

@param string $str Date/time string

@param array|int $options Options to modify behavior, or specify int for the `baseTimestamp` option, or string for `inputFormat` option.
 - `emptyReturnValue` (int|null|false): Value to return for empty or zero-only date strings (default=null)
 - `baseTimestamp` (int|null): The timestamp which is used as a base for the calculation of relative dates.
 - `inputFormat` (string): Optional date format that given $str is in, if not strtotime() compatible. (3.0.238+)
 - `outputFormat` (string): Optionally return value in this date format rather than unix timestamp (3.0.238+)

@return false|int|null

@see https://www.php.net/manual/en/function.strtotime.php

@since 3.0.178

## strtodate()

Parse English textual datetime description into a formatted date string, or blank if not a date

@param string $str Date/time string to parse

@param string|array $format Output format to use, or array for $options.
 - Omit or boolean true for default 'Y-m-d H:i:s'.
 - Specify date format string, see [formats](https://www.php.net/manual/en/datetime.format.php).
 - Specify boolean false for unix timestamp.
 - Specify array of options.

@param array $options Can also be specified as 2nd argument. Options include:
 - `emptyReturnValue` (int|null|false): Value to return for empty or zero-only date strings (default='')
 - `baseTimestamp` (int|null): The timestamp which is used as a base for the calculation of relative dates.
 - `inputFormat` (string): Optional date format that given $str is in, if not strtotime() compatible.
 - `outputFormat` (string|bool): Format to return date string in, used only if $options specified for $format argument.
 - `format` (string|bool) Optional alias of outputFormat, used only if $options specified for $format argument.

@return string Return string, returns blank string on fail.

@since 3.0.238

## strftime()

strftime() replacement function that works in PHP 8.1+ (though not locale aware)

@param string $format

@param null|int|string $timestamp

@return string|false

@since 3.0.197

## strftimeToDateFormat()

Convert strftime() format to date() format

@param string $format

@return string

@since 3.0.197

## ___relativeTimeStr()

Given a unix timestamp (or date string), returns a formatted string indicating the time relative to now

For example:

- 2 years ago
- 3 months ago
- 1 day ago
- 30 seconds ago
- Just now
- 1 day from now
- 5 months from now
- 3 years from now

This method also supports multi-language and will output in the current user's language, so long as the
phrases in /wire/core/WireDateTime.php are translated in the language pack.

@param int|string $ts Unix timestamp or date string

@param bool|int|array $abbreviate Whether to use abbreviations for shorter strings.
 - Specify boolean TRUE for abbreviations (abbreviated where common, not always different from non-abbreviated)
 - Specify integer 1 for extra short abbreviations (all terms abbreviated into shortest possible string)
 - Specify boolean FALSE or omit for no abbreviations.
 - Specify associative array of key=value pairs of terms to use for abbreviations. The possible keys are:
	  just now, ago, from now, never, second, minute, hour, day, week, month, year, decade, seconds, minutes,
   hours, days, weeks, months, years, decades

@param bool $useTense Whether to append a tense like "ago" or "from now".
 - May be ok to disable in situations where all times are assumed in future or past.
 - In abbreviate=1 (shortest) mode, this removes the leading "+" or "-" from the string.

@return string Formatted relative time string

## elapsedTimeStr()

Render an elapsed time string

If the `$stop` argument is omitted then it is assumed to be the current time.
The maximum period used is weeks, as months and years are not fixed length periods.

~~~~~
$start = '2023-09-08 08:33:52';
$stop = '2023-09-09 10:47:23';

// Regular: 1 day 2 hours 13 minutes 31 seconds
echo $datetime->elapsedTimeStr($start, $stop);

// Abbreviated: 1 day 2 hrs 13 mins 31 secs
echo $datetime->elapsedTimeStr($start, $stop, true);

// Abbreviated with exclusions: 1 day 2 hrs
echo $datetime->elapsedTimeStr($start, $stop, true, [ 'exclude' => 'minutes seconds' ]);

// Optional 3.0.227+ usage and inclusions: 26 hours 13 minutes
echo $datetime->elapsedTimeStr($start, [ 'stop' => $stop, 'include' => 'hours minutes' ]);
~~~~~

@param int|string $start Starting timestamp or date/time string.

@param int|string|array $stop Ending timestamp or date/time string, omit for “now”, or:
 - In 3.0.227+ you may optionally substitute the `$options` array argument here. When doing so,
   all remaining arguments are ignored and the `stop` and `abbreviate` (if needed) may be
   specified in the given options array, along with any other options.

@param bool|int|array $abbreviate
 - Specify boolean FALSE for verbose elapsed time string without abbreviations (default).
 - Specify boolean TRUE for abbreviations (abbreviated where common, not always different from non-abbreviated).
 - Specify integer `1` for extra short abbreviations (all terms abbreviated into shortest possible string).
 - Specify integer `0` for digital elapsed time string like “00:01:12” referring to hours:minutes:seconds.
 - Note that when using `0` no options apply except except for `exclude[seconds]` option.

@param array $options Additional options:
 - `delimiter` (string): String to separate time periods (default=' ').
 - `getArray` (bool): Return an array of integers indexed by period name (rather than a string)? 3.0.227+
 - `exclude` (array|string): Exclude these periods, one or more of: 'seconds', 'minutes', 'hours', 'days', 'weeks' (default=[])
 - `include` (array|string): Include only these periods, one or more of: 'seconds', 'minutes', 'hours', 'days', 'weeks' (default=[]) 3.0.227+
 - Note the exclude and include options should not be used together, and the include option requires 3.0.227+.

@return string|array Returns array only if the `getArray` option is true, otherwise returns a string.

@since 3.0.129

## getPeriods()

Get named time periods

Returns regular array(s) of periods in this order:
seconds, minutes, hours, days, weeks, months, years decades

If $plural argument is null (or omitted) it instead returns an array
indexed by period name including both singular and plural periods.

@param $abbreviate
 - Specify 1 to get shortest possible abbreviations
 - Specify true to get standard/medium abbreviations
 - Specify false to get large/full terms (no abbreviations)
 - Specify associative array to get large/full terms and substitute your own

@param null|true|int $plural
 - Specify true to get plural,
 - Specify false to get singular,
 - Specify 1 to get array where [ 0 => [singulars], 1 => [plurals] ]
 - Omit (or null) to get all in an indexed array

@return array

## localizeDateText()

Localize a date's month and day names, when present

@param string $value Date that is already formated with $format

@param string $format Format that was used to format the date

@return string

## dateWords()

Get translated month/day words indexed by English words

@param string $key One of: monthNames, monthAbbrs, dayNames, dayAbbrs, meridiums

@return array
