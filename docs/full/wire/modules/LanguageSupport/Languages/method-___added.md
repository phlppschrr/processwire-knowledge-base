# $languages->added(Page $language)

Source: `wire/modules/LanguageSupport/Languages.php`

Hook called when a language is added

## Usage

~~~~~
// basic usage
$result = $languages->added($language);

// usage with all arguments
$result = $languages->added(Page $language);
~~~~~

## Hookable

- Hookable method name: `added`
- Implementation: `___added`
- Hook with: `$languages->added()`

## Hooking Before

~~~~~
$this->addHookBefore('Languages::added', function(HookEvent $event) {
  $languages = $event->object;

  // Get arguments
  $language = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $language);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Languages::added', function(HookEvent $event) {
  $languages = $event->object;

  // Get arguments
  $language = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$language` `Page`
