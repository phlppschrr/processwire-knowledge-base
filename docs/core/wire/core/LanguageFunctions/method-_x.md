# $languageFunctions->_x($text, $context, $textdomain = null): string

Source: `wire/core/LanguageFunctions.php`

Perform a language translation in a specific context

Used when two or more text strings might be the same in default language, but different in other languages.
This enables you to limit the context of the translation to a named context, like "button" or "headline" or
whatever name you decide to use.

## Example

~~~~~
echo _x('Click for more', 'button');
echo _x('Click for more', 'text-link');
~~~~~

## Usage

~~~~~
// basic usage
$string = $languageFunctions->_x($text, $context);

// usage with all arguments
$string = $languageFunctions->_x($text, $context, $textdomain = null);
~~~~~

## Arguments

- `$text` `string` Text for translation.
- `$context` `string` Name of context
- `$textdomain` (optional) `string` Textdomain for the text, may be class name, filename, or something made up by you. If omitted, a debug backtrace will attempt to determine automatically.

## Return value

- `string` Translated text or original text if translation not available.

## See Also

- __()
- _n()

## Details

- @link https://processwire.com/docs/multi-language-support/code-i18n/
