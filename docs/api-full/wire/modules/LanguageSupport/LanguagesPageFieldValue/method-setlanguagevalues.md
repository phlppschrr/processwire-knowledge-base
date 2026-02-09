# $languagesPageFieldValue->setLanguageValues(array $values, $reset = false): self

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Set multiple language values at once

## Example

~~~~~
$page->title->setLanguageValues([
 'default' => 'Hello world',
 'es' => 'Hola Mundo',
 'fr' => 'Hei maailma',
]);
~~~~~

## Usage

~~~~~
// basic usage
$result = $languagesPageFieldValue->setLanguageValues($values);

// usage with all arguments
$result = $languagesPageFieldValue->setLanguageValues(array $values, $reset = false);
~~~~~

## Arguments

- `$values` `array` Associative array of values where keys are language names or IDs.
- `$reset` (optional) `bool` Reset any languages not specified to blank? (default=false)

## Return value

- `self`

## Since

3.0.236
