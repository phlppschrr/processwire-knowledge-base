# $pagefilesManager->save()

Source: `wire/core/PagefilesManager.php`

For hooks to listen to on page save action, for file-specific operations

Executed before a page draft/published assets are moved around, when changes to files may be best to execute.

There are no arguments or return values here.
Hooks may retrieve the Page object being saved from `$event->object->page`.

## Usage

~~~~~
// basic usage
$result = $pagefilesManager->save();
~~~~~

## Hooking

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `PagefilesManager::save`

### Hooking Before

~~~~~
$this->addHookBefore('PagefilesManager::save', function(HookEvent $event) {
  $pagefilesManager = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PagefilesManager::save', function(HookEvent $event) {
  $pagefilesManager = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
