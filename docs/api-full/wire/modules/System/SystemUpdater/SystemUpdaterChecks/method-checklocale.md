# $systemUpdaterChecks->checkLocale(): bool

Source: `wire/modules/System/SystemUpdater/SystemUpdaterChecks.php`

Check locale setting

Warning about servers with locales that break UTF-8 strings called by basename
and other file functions, due to a long running PHP bug

## Usage

~~~~~
// basic usage
$bool = $systemUpdaterChecks->checkLocale();
~~~~~

## Return value

- `bool`
