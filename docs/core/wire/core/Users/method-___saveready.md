# $users->saveReady(Page $page): array

Source: `wire/core/Users.php`

Hook called just before a user is saved

## Usage

~~~~~
// basic usage
$array = $users->saveReady($page);

// usage with all arguments
$array = $users->saveReady(Page $page);
~~~~~

## Arguments

- `$page` `Page` The user about to be saved

## Return value

- `array` Optional extra data to add to pages save query.

## Hooking

- Hookable method name: `saveReady`
- Implementation: `___saveReady`
- Hook with: `Users::saveReady`

### Hooking Before

~~~~~
$this->addHookBefore('Users::saveReady', function(HookEvent $event) {
  $users = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Users::saveReady', function(HookEvent $event) {
  $users = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
