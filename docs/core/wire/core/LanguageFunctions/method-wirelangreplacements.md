# $languageFunctions->wireLangReplacements(array $values): array|string

Source: `wire/core/LanguageFunctions.php`

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

## Arguments

- `$values` `array`

## Return value

array|string

## Since

3.0.154
