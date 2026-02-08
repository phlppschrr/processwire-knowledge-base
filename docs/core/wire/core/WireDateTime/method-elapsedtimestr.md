# $wireDateTime->elapsedTimeStr($start, $stop = null, $abbreviate = false, array $options = array()): string|array

Source: `wire/core/WireDateTime.php`

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

## Arguments

- `$start` `int|string` Starting timestamp or date/time string.
- `$stop` (optional) `int|string|array` Ending timestamp or date/time string, omit for “now”, or: - In 3.0.227+ you may optionally substitute the `$options` array argument here. When doing so, all remaining arguments are ignored and the `stop` and `abbreviate` (if needed) may be specified in the given options array, along with any other options.
- `$abbreviate` (optional) `bool|int|array` - Specify boolean FALSE for verbose elapsed time string without abbreviations (default). - Specify boolean TRUE for abbreviations (abbreviated where common, not always different from non-abbreviated). - Specify integer `1` for extra short abbreviations (all terms abbreviated into shortest possible string). - Specify integer `0` for digital elapsed time string like “00:01:12” referring to hours:minutes:seconds. - Note that when using `0` no options apply except except for `exclude[seconds]` option.
- `$options` (optional) `array` Additional options: - `delimiter` (string): String to separate time periods (default=' '). - `getArray` (bool): Return an array of integers indexed by period name (rather than a string)? 3.0.227+ - `exclude` (array|string): Exclude these periods, one or more of: 'seconds', 'minutes', 'hours', 'days', 'weeks' (default=[]) - `include` (array|string): Include only these periods, one or more of: 'seconds', 'minutes', 'hours', 'days', 'weeks' (default=[]) 3.0.227+ - Note the exclude and include options should not be used together, and the include option requires 3.0.227+.

## Return value

string|array Returns array only if the `getArray` option is true, otherwise returns a string.

## Since

3.0.129
