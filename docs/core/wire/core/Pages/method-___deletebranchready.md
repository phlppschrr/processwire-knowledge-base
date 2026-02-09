# $pages->deleteBranchReady(Page $page, array $options)

Source: `wire/core/Pages.php`

Hook called before a branch of pages is about to be deleted, called on root page of branch only

Note: this is called only on deletions that had 'recursive' option true and 1+ children.

## Usage

~~~~~
// basic usage
$result = $pages->deleteBranchReady($page, $options);

// usage with all arguments
$result = $pages->deleteBranchReady(Page $page, array $options);
~~~~~

## Arguments

- `$page` `Page` Page that was deleted
- `$options` `array` Options passed to delete method

## Hooking

- Hookable method name: `deleteBranchReady`
- Implementation: `___deleteBranchReady`
- Hook with: `Pages::deleteBranchReady`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::deleteBranchReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::deleteBranchReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.163
