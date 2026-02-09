# WireDateTime

Source: `wire/core/WireDateTime.php`

Inherits: `Wire`

## Summary

ProcessWire Date/Time Tools (`$datetime` API variable)

Common methods:
- [`getDateFormats()`](method-getdateformats.md)
- [`getTimeFormats()`](method-gettimeformats.md)
- [`stringToTimestamp()`](method-stringtotimestamp.md)
- [`formatDate()`](method-formatdate.md)
- [`convertDateFormat()`](method-convertdateformat.md)

Groups:
Group: [other](group-other.md)

The `$datetime` API variable provides helpers for working with dates/times and conversion between formats.

## Methods
- [`getDateFormats(): array`](method-getdateformats.md) Return all predefined PHP date() formats for use as dates
- [`getTimeFormats(): array`](method-gettimeformats.md) Return all predefined PHP date() formats for use as times
- [`stringToTimestamp(string $str, string $format): int`](method-stringtotimestamp.md) Given a date/time string and expected format, convert it to a unix timestamp
- [`convertDateFormat(string $format, string $type): string`](method-convertdateformat.md) Given a PHP date() format, convert it to either 'js', 'strftime' or 'regex' format
- [`date(string|int $format = '', int|string|null $ts = null): string|bool`](method-date.md) Format a date, using PHP date(), strftime() or other special strings (see arguments).
- [`strtotime(string $str, array|int $options = array()): false|int|null`](method-strtotime.md) Parse about any English textual datetime description into a Unix timestamp using PHP’s strtotime()
- [`strtodate(string $str, string|array $format = true, array $options = array()): string`](method-strtodate.md) Parse English textual datetime description into a formatted date string, or blank if not a date
- [`strftime(string $format, null|int|string $timestamp = null): string|false`](method-strftime.md) strftime() replacement function that works in PHP 8.1+ (though not locale aware)
- [`strftimeToDateFormat(string $format): string`](method-strftimetodateformat.md) Convert strftime() format to date() format
- [`relativeTimeStr(int|string $ts, bool|int|array $abbreviate = false, bool $useTense = true): string`](method-___relativetimestr.md) (hookable) Given a unix timestamp (or date string), returns a formatted string indicating the time relative to now
- [`elapsedTimeStr(int|string $start, int|string|array $stop = null, bool|int|array $abbreviate = false, array $options = array()): string|array`](method-elapsedtimestr.md) Render an elapsed time string
- [`getPeriods($abbreviate, null|true|int $plural = null): array`](method-getperiods.md) Get named time periods
- [`localizeDateText(string $value, string $format): string`](method-localizedatetext.md) Localize a date's month and day names, when present
- [`dateWords(string $key): array`](method-datewords.md) Get translated month/day words indexed by English words
