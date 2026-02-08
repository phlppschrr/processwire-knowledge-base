# LanguageFunctions

Source: `wire/core/LanguageFunctions.php`

ProcessWire Language Functions

Provides GetText-like language translation functions to ProcessWire.

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

## __()

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


@param string|array|bool $text Text for translation.

@param string|array $textdomain Textdomain for the text, may be class name, filename, or something made up by you.
  If omitted, a debug backtrace will attempt to determine it automatically.

@param string|bool|array $context Name of context - DO NOT USE with this function for translation as it will not be parsed for translation.
  Use only with the `_x()` function, which will be parsed.

@return string|array Translated text or original text if translation not available. Returns array only if getting/setting options.

@see _x(), _n()

@link https://processwire.com/docs/multi-language-support/code-i18n/

## _x()

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

## _n()

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

## wireLangEntityEncode()

Set entity encoding state for language translation function calls

The function affects behavior of future `__()`, `_x()` and `_n()` calls.

The following can be used for the `$value` argument:

- `true` (bool): Entity encoding ON
- `false` (bool): Entity encoding OFF
- `1` (int): Entity encode only if not already
- `null` (null): Entity encoding undefined

To get current entity encoding state, call this function with no arguments.


@param bool|int|string|null $value

@return bool|int|string|null

@since 3.0.154 Versions 3.0.125 to 3.0.153 can use __(true, 'entityEncode', $value);

## wireLangTranslations()

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


@param array $values

@return array

@since 3.0.154 Versions 3.0.125 to 3.0.153 can use __(true, array $values);

## wireLangReplacements()

Set global translation replacement values

This option enables you to replace text sent to translation calls
like `__('text')` with your own replacement text. This is similar
to the `wireLangTranslations()` function except that it applies
regardless of whether or not a translation is available for the
phrase. It overrides rather than serves as a fallback.

This function works whether ProcessWire multi-language support is
installed or not, so it can also be useful for selectively replacing
phrases in core or modules.

Note that this applies globally to all translations that match,
regardless of language. As a result, you would typically surround
this in an if() statement to make sure you are in the desired state
before you apply the replacements.

The function affects behavior of future `__()`, `_x()` and `_n()`
calls, as well as their object-oriented equivalents.

This function should ideally be called from a /site/init.php file
(before PW has booted) to ensure that your replacements will be
available to any translation calls. However, it can be called from
anywhere you’d like, so long as it is before the translation calls
that you are looking to replace.

~~~~~
// The following example replaces the labels of all the Tabs in the
// Page editor (and anywhere else labels used):

wireLangReplacements([
  'Content' => 'Data',
  'Children' => 'Family',
  'Settings' => 'Details',
  'Delete' => 'Trash',
  'View' => 'See',
]);

// If you wanted to be sure the above replacements applied only
// to the Page editor, then you would place it in /site/ready.php
// or /site/templates/admin.php and surround with an if() statement:

if($page->process == 'ProcessPageEdit') {
  wireLangReplacements([
    'Content' => 'Data', // and so on
  ]);
}

// To make the replacement apply only for a specific _x() context, specify the
// translated value in an array with text first and context second, like the
// following example that replaces 'URL' with 'Path' when the context call
// specifed 'relative-url' as context, i.e. _x('URL', 'relative-url');

wireLangReplacements([
  'URL' => [ 'Path', 'relative-url' ],
]);
~~~~~


@param array $values

@return array|string

@since 3.0.154
