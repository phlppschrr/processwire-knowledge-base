# $functionsWireAPI->wireLanguages($name = ''): Languages|Language|NullPage|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $languages API variable as a function

Returns the $languages API variable, or a Language object if given a language name.

~~~~
// Examples
$languages = languages(); // Languages if active, null if not
$en = languages()->getDefault();
$de = languages('de');
~~~~

## Arguments

- `$name` (optional) `string|int` Optional Language name or ID for language to retrieve

## Return value

Languages|Language|NullPage|null
