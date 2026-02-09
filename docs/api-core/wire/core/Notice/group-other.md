# Notice: other

Source: `wire/core/Notice.php`

- `$text: string|object|array` Text or value of notice
- `$class: string` Class of notice
- `$timestamp: int` Unix timestamp of when the notice was generated
- [`$flags: int`](method-flags.md) Bitmask using any of the Notice::constants
- `@property-read $flagsArray Current flags as an array where indexes are int flags and values are flag names (since 3.0.149)` `$flagsArray` Current flags as an array where indexes are int flags and values are flag names (since 3.0.149)
- `@property-read $flagsStr Current flags as string of flag names (since 3.0.149)` `$flagsStr` Current flags as string of flag names (since 3.0.149)
- `$icon: string` Name of icon to use with Notice
- `$idStr: string` Unique ID string for Notice
- `$qty: int` Number of times this Notice was added.
