# LanguageFunctions::_x()

Source: `wire/core/LanguageFunctions.php`

Perform a language translation in a specific context

Used when two or more text strings might be the same in default language, but different in other languages.
This enables you to limit the context of the translation to a named context, like "button" or "headline" or
whatever name you decide to use.

~~~~~
echo _x('Click for more', 'button');
echo _x('Click for more', 'text-link');
~~~~~


@param string $text Text for translation.

@param string $context Name of context

@param string $textdomain Textdomain for the text, may be class name, filename, or something made up by you.
  If omitted, a debug backtrace will attempt to determine automatically.

@return string Translated text or original text if translation not available.

@see __(), _n()

@link https://processwire.com/docs/multi-language-support/code-i18n/
