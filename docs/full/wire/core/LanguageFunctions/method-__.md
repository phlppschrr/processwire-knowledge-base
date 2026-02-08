# $languageFunctions->__($text, $textdomain = null, $context = ''): string|array

Source: `wire/core/LanguageFunctions.php`

Perform a language translation

This function enables you to specify static text as the argument, and that text becomes translatable (for each language)
with ProcessWire’s built-in language translation tools. This function also works just fine if you do not have multi-language
support installed, though in that case it just returns the text that it is given.

For full documentation, please see the [Code Internationalization (i18n)](https://processwire.com/docs/multi-language-support/code-i18n/)
documentation page at ProcessWire.com.

This function is very similar to the GNU gettext `_('text');` function and essentially does the same thing, except that it is
native to ProcessWire and not using GNU gettext.

Use this `__('text')` function for common translations, use the `_x('text', 'context')` function for translations
that also require additional context, and use the `_n('singular', 'plural', $n)` function for translations that should
changed based on whether a value `$n` would require a singular or plural tense.

### Additional behaviors

- You can optionally specify a “textdomain” as the second argument. The textdomain represents the source file of the
  translation. Most often it would be the current file, so the argument can be omitted, or you can specify `__FILE__`.
  But in some cases you may want to use a translation from another file, and the textdomain argument enables you to.

- When in a class (or module) it is preferable to use `$this->_('text');` rather than `__('text');`, as it is slightly
  more efficient to do so.

- A PHP comment, i.e. `// comment` that appears somewhere after a translation call (on the same line) is used as an
  additional description for the person translating text. Another comment after that, i.e. `// comment1 // comment2`
  is used as an additional secondary note for the person translating the text.

- It is also possible to provide multiple acceptable phrases for translations, useful when making minor changes to
  an existing text where you do not want an previous translation to be abandoned. To do so, provide an array argument
  (using bracket syntax) with the multiple phrases as values, where the first is the newest phrase. This feature was
  added in ProcessWire 3.0.151. See examples below for usage details.

### Limitations

- The function call (and translatable text within it) cannot span more than one line. If your translatable text is long
  enough to require multiple lines, split them into multiple calls (like one per sentence).

- There cannot be more than one `__('text')` function call per line in the PHP code.

- The provided text argument must be one string of static text. It cannot contain PHP variables or concatenation. To populate
  dynamic values you should use PHP’s `sprintf()` (see examples below).

## Example

~~~~~~
// Standard way to make static text translatable
echo __('This is translatable text');

// Optionally specify current file as textdomain (same result as above)
echo __('This is translatable text', __FILE__);

// Specify another file as textdomain (will use translation from that file)
echo __('This is translatable text', '/site/templates/_init.php');

// Using placeholders to populate dynamic values in translatable text:
echo sprintf(__('You are reading the %s page'), $page->title);
echo sprintf(__('%d is the current page ID'), $page->id);
echo sprintf(__('Today is %1$s and the time is %2$s'), date('l'), date('g:i a'));

// Providing a description via PHP comment to translator
echo __('Welcome friend!'); // Friendly message for new users

// Providing a description AND extra note via PHP comments to translator
echo __('Welcome friend!'); // Friendly message for new users // Must be short!

// In ProcessWire 3.0.151+ you can change existing phrases without automatically
// abandoning the translations for them. To use, include both new and old phrase.
// Specify PHP array (bracket syntax required) with 2+ phrases you accept trans-
// lations for where the first is the newest/current text to translate. This array
// replaces the $text argument of this function. Must be on 1 line.
__([ 'New text', 'Old text' ]);

// The above can also be used with _x() and _n() calls as well.
_x([ 'Canada Goose', 'Canadian Goose' ], 'bird');
~~~~~

## Usage

~~~~~
// basic usage
$string = $languageFunctions->__($text);

// usage with all arguments
$string = $languageFunctions->__($text, $textdomain = null, $context = '');
~~~~~

## Arguments

- `$text` `string|array|bool` Text for translation.
- `$textdomain` (optional) `string|array` Textdomain for the text, may be class name, filename, or something made up by you. If omitted, a debug backtrace will attempt to determine it automatically.
- `$context` (optional) `string|bool|array` Name of context - DO NOT USE with this function for translation as it will not be parsed for translation. Use only with the `_x()` function, which will be parsed.

## Return value

- `string|array` Translated text or original text if translation not available. Returns array only if getting/setting options.

## See Also

- _x()
- _n()

## Details

- @link https://processwire.com/docs/multi-language-support/code-i18n/
