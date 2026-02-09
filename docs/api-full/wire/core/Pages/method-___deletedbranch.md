# $pages->deletedBranch(Page $page, array $options, $numDeleted)

Source: `wire/core/Pages.php`

Hook called after a a branch of pages has been deleted, called on root page of branch only

Note: this is called only on deletions that had 'recursive' option true and 1+ children.

## Usage

~~~~~
// basic usage
$result = $pages->deletedBranch($page, $options, $numDeleted);

// usage with all arguments
$result = $pages->deletedBranch(Page $page, array $options, $numDeleted);
~~~~~

## Arguments

- `$page` `Page` Page that was the root of the branch
- `$options` `array` Options passed to delete method
- `$numDeleted` `int` Number of pages deleted

## Hooking

- Hookable method name: `deletedBranch`
- Implementation: `___deletedBranch`
- Hook with: `Pages::deletedBranch`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::deletedBranch', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);
  $numDeleted = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $options);
  $event->arguments(2, $numDeleted);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::deletedBranch', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);
  $numDeleted = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.163
