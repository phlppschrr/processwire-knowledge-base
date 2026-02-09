# WireTrackable

Source: `wire/core/Interfaces.php`

For classes that need to track changes made by other objects.

Methods:
- [`setTrackChanges(bool|int $trackChanges = true): $this`](method-settrackchanges.md) Turn change tracking ON or OFF
- [`trackChange(string $what, mixed $old = null, mixed $new = null): $this`](method-trackchange.md) Track a change to a property in this object
- [`isChanged(string $what = ''): bool`](method-ischanged.md) Has the given property changed?
- [`getChanges(bool $getValues = false): array`](method-getchanges.md) Return an array of properties that have changed while change tracking was on.
