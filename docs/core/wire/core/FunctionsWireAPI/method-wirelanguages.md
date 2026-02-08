# FunctionsWireAPI::wireLanguages()

Source: `wire/core/FunctionsWireAPI.php`

Access the $languages API variable as a function

Returns the $languages API variable, or a Language object if given a language name.

~~~~
// Examples
$languages = languages(); // Languages if active, null if not
$en = languages()->getDefault();
$de = languages('de');
~~~~

@param string|int $name Optional Language name or ID for language to retrieve

@return Languages|Language|NullPage|null
