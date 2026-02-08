# $languageFunctions->_n($textSingular, $textPlural, $count, $textdomain = null): string

Source: `wire/core/LanguageFunctions.php`

Perform a language translation with singular and plural versions

## Example

~~~~~
$items = array(...);
$qty = count($items);
echo _n('Found one item', 'Found multiple items', $qty);
echo sprintf(_n('Found one item', 'Found %d items', $qty), $qty);
~~~~~

## Usage

~~~~~
// basic usage
$string = $languageFunctions->_n($textSingular, $textPlural, $count);

// usage with all arguments
$string = $languageFunctions->_n($textSingular, $textPlural, $count, $textdomain = null);
~~~~~

## Arguments

- `$textSingular` `string` Singular version of text (when there is 1 item)
- `$textPlural` `string` Plural version of text (when there are multiple items or 0 items)
- `$count` `int` Quantity of items, should be 0 or more.
- `$textdomain` (optional) `string` Textdomain for the text, may be class name, filename, or something made up by you. If omitted, a debug backtrace will attempt to determine automatically.

## Return value

- `string` Translated text or original text if translation not available.

## See Also

- __()
- _x()

## Details

- @link https://processwire.com/docs/multi-language-support/code-i18n/
