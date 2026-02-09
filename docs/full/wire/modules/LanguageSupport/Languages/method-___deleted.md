# $languages->deleted(Page $language)

Source: `wire/modules/LanguageSupport/Languages.php`

Hook called when a language is deleted

## Usage

~~~~~
// basic usage
$result = $languages->deleted($language);

// usage with all arguments
$result = $languages->deleted(Page $language);
~~~~~

## Arguments

- `$language` `Page`

## Hooking

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `Languages::deleted`

### Hooking Before

~~~~~
$this->addHookBefore('Languages::deleted', function(HookEvent $event) {
  $languages = $event->object;

  // Get arguments
  $language = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $language);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Languages::deleted', function(HookEvent $event) {
  $languages = $event->object;

  // Get arguments
  $language = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
