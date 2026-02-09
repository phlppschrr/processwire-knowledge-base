# WireTrackable

Source: `wire/core/Interfaces.php`

For classes that need to track changes made by other objects.

Methods:
- [`setTrackChanges(bool|int $trackChanges = true): $this`](method-settrackchanges.md)
- [`trackChange(string $what, mixed $old = null, mixed $new = null): $this`](method-trackchange.md)
- [`isChanged(string $what = ''): bool`](method-ischanged.md)
- [`getChanges(bool $getValues = false): array`](method-getchanges.md)
