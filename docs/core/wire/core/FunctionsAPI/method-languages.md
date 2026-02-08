# $functionsAPI->languages($name = ''): Languages|Language|NullPage|null

Source: `wire/core/FunctionsAPI.php`

Access all installed languages in multi-language environment ($languages API variable as a function)

Returns the `$languages` API variable, or a `Language` object if given a language name or ID.

~~~~
$languages = languages(); // Languages if active, null if not
$en = languages()->getDefault(); // Get default language
$de = languages()->get('de'); // Get another language
$de = languages('de'); // Get another language (shorcut syntax)
~~~~

## Arguments

- `$name` (optional) `string|int` Optional Language name or ID for language to retrieve

## Return value

Languages|Language|NullPage|null

## See also

- Languages
- Languages::get()
- Language
