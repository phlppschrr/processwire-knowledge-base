# $wireCache->maintenance($obj = null): bool

Source: `wire/core/WireCache.php`

Cache maintenance removes expired caches

Should be called as part of a regular maintenance routine and after page/template save/deletion.
ProcessWire already calls this automatically, so you don’t typically need to call this method on your own.

## Arguments

- Template|Page|null|bool Item to run maintenance for or, if not specified, general maintenance is performed. General maintenance only runs once per request. Specify boolean true to force general maintenance to run.

## Return value

bool
