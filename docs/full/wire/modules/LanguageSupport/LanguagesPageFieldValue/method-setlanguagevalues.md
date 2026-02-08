# LanguagesPageFieldValue::setLanguageValues()

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Set multiple language values at once

~~~~~
$page->title->setLanguageValues([
 'default' => 'Hello world',
 'es' => 'Hola Mundo',
 'fr' => 'Hei maailma',
]);
~~~~~

@param array $values Associative array of values where keys are language names or IDs.

@param bool $reset Reset any languages not specified to blank? (default=false)

@return self

@since 3.0.236
