# WireDateTime

Source: `wire/core/WireDateTime.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Date/Time Tools ($datetime API variable)

The $datetime API variable provides helpers for working with dates/times and conversion between formats.

Methods:
- [`getDateFormats(): array`](method-getdateformats.md)
- [`getTimeFormats(): array`](method-gettimeformats.md)
- [`stringToTimestamp(string $str, string $format): int`](method-stringtotimestamp.md)
- [`convertDateFormat(string $format, string $type): string`](method-convertdateformat.md)
- [`date(string|int $format = '', int|string|null $ts = null): string|bool`](method-date.md)
- [`strtotime(string $str, array|int $options = array()): false|int|null`](method-strtotime.md)
- [`strtodate(string $str, string|array $format = true, array $options = array()): string`](method-strtodate.md)
- [`strftime(string $format, null|int|string $timestamp = null): string|false`](method-strftime.md)
- [`strftimeToDateFormat(string $format): string`](method-strftimetodateformat.md)
- [`relativeTimeStr(int|string $ts, bool|int|array $abbreviate = false, bool $useTense = true): string`](method-___relativetimestr.md) (hookable)
- [`elapsedTimeStr(int|string $start, int|string|array $stop = null, bool|int|array $abbreviate = false, array $options = array()): string|array`](method-elapsedtimestr.md)
- [`getPeriods($abbreviate, null|true|int $plural = null): array`](method-getperiods.md)
- [`localizeDateText(string $value, string $format): string`](method-localizedatetext.md)
- [`dateWords(string $key): array`](method-datewords.md)
