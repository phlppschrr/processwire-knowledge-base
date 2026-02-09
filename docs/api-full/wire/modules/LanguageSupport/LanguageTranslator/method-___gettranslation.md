# $languageTranslator->getTranslation($textdomain, $text, $context = '', array $options = array()): string|array|false

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Implementation for the getTranslation() function - you should call getTranslation() without underscores instead.

## Usage

~~~~~
// basic usage
$string = $languageTranslator->getTranslation($textdomain, $text);

// usage with all arguments
$string = $languageTranslator->getTranslation($textdomain, $text, $context = '', array $options = array());
~~~~~

## Arguments

- `$textdomain` `string|object` Textdomain string, filename, or object.
- `$text` `string` Text in default language (EN) that needs to be converted to current language.
- `$context` (optional) `string` Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
- `$options` (optional) `array` 3.0.237+ only - `getInfo` (bool): Get verbose array of info about translation? (default=false) - `getFalse` (bool): Return false rather than default language value if translation not found? (default=false)

## Return value

- `string|array|false` Translation if available, or original EN version if translation not available. - Returns array if options[getInfo] is true. - Returns false if translation not found and options[getFalse] is true.

## Hooking

- Hookable method name: `getTranslation`
- Implementation: `___getTranslation`
- Hook with: `LanguageTranslator::getTranslation`

### Hooking Before

~~~~~
$this->addHookBefore('LanguageTranslator::getTranslation', function(HookEvent $event) {
  $languageTranslator = $event->object;

  // Get arguments
  $textdomain = $event->arguments(0);
  $text = $event->arguments(1);
  $context = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $textdomain);
  $event->arguments(1, $text);
  $event->arguments(2, $context);
  $event->arguments(3, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('LanguageTranslator::getTranslation', function(HookEvent $event) {
  $languageTranslator = $event->object;

  // Get arguments
  $textdomain = $event->arguments(0);
  $text = $event->arguments(1);
  $context = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
