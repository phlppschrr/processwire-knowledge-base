# $languagesPageFieldValue->setLanguageValues(array $values, $reset = false): self

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Set multiple language values at once

~~~~~
$page->title->setLanguageValues([
 'default' => 'Hello world',
 'es' => 'Hola Mundo',
 'fr' => 'Hei maailma',
]);
~~~~~

## Arguments

- array $values Associative array of values where keys are language names or IDs.
- bool $reset Reset any languages not specified to blank? (default=false)

## Return value

self

## Meta

- @since 3.0.236
