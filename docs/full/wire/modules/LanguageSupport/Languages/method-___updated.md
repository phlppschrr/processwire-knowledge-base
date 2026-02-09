# $languages->updated(Page $language, $what)

Source: `wire/modules/LanguageSupport/Languages.php`

Hook called when a language is added or deleted

## Usage

~~~~~
// basic usage
$result = $languages->updated($language, $what);

// usage with all arguments
$result = $languages->updated(Page $language, $what);
~~~~~

## Hookable

- Hookable method name: `updated`
- Implementation: `___updated`
- Hook with: `$languages->updated()`

## Hooking Before

~~~~~
$this->addHookBefore('Languages::updated', function(HookEvent $event) {
  $languages = $event->object;

  // Get arguments
  $language = $event->arguments(0);
  $what = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $language);
  $event->arguments(1, $what);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Languages::updated', function(HookEvent $event) {
  $languages = $event->object;

  // Get arguments
  $language = $event->arguments(0);
  $what = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$language` `Page`
- `$what` `string` What occurred? ('added' or 'deleted')
