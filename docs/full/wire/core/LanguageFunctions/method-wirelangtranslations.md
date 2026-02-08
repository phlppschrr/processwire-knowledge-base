# $languageFunctions->wireLangTranslations(array $values = array()): array

Source: `wire/core/LanguageFunctions.php`

Set predefined fallback translation values

These predefined translations are used when an existing translation is
not available, enabling you to provide translations programmatically.

These translations will be used if the text is not translated in the
admin. The translations are not specific to any textdomain and thus can
serve as a fallback for any file. The array you provide should be
associative, where the keys contain the text to translate, and the
values contain the translation (see examples).

The function affects behavior of future `__()`, `_x()` and `_n()` calls,
and their objected-oriented equivalents.

~~~~~
// Return 'Hola' when text is 'Hello' and 'Mundo' when text is 'World'
if($user->language->name == 'es') {
  wireLangTranslations([
    'Hello' => 'Hola',
    'World' => 'Mundo'
  ]);
}

// Setting predefined translations with context
wireLangTranslations([
  // would apply only to a _x('Search', 'nav'); call (context)
  'Search' => [ 'Buscar', 'nav' ]
]);
~~~~~

## Arguments

- `$values` (optional) `array`

## Return value

array

## Since

3.0.154 Versions 3.0.125 to 3.0.153 can use __(true, array $values);
