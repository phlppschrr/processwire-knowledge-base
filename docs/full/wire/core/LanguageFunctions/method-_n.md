# LanguageFunctions::_n()

Source: `wire/core/LanguageFunctions.php`

Perform a language translation with singular and plural versions

~~~~~
$items = array(...);
$qty = count($items);
echo _n('Found one item', 'Found multiple items', $qty);
echo sprintf(_n('Found one item', 'Found %d items', $qty), $qty);
~~~~~


@param string $textSingular Singular version of text (when there is 1 item)

@param string $textPlural Plural version of text (when there are multiple items or 0 items)

@param int $count Quantity of items, should be 0 or more.

@param string $textdomain Textdomain for the text, may be class name, filename, or something made up by you.
  If omitted, a debug backtrace will attempt to determine automatically.

@return string Translated text or original text if translation not available.

@see __(), _x()

@link https://processwire.com/docs/multi-language-support/code-i18n/
