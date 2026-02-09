# $pages->found(PageArray $pages, array $details)

Source: `wire/core/Pages.php`

Hook called at the end of a $pages->find(), includes extra info not seen in the resulting PageArray

## Usage

~~~~~
// basic usage
$result = $pages->found($pages, $details);

// usage with all arguments
$result = $pages->found(PageArray $pages, array $details);
~~~~~

## Arguments

- `$pages` `PageArray` The pages that were found
- `$details` `array` Extra information on how the pages were found, including: - `pageFinder` (PageFinder): The PageFinder instance that was used. - `pagesInfo` (array): The array returned by PageFinder. - `options` (array): Options that were passed to $pages->find().

## Hooking

- Hookable method name: `found`
- Implementation: `___found`
- Hook with: `Pages::found`

### Hooking Before

~~~~~
$this->addHookBefore('Pages::found', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $pages = $event->arguments(0);
  $details = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $pages);
  $event->arguments(1, $details);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pages::found', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $pages = $event->arguments(0);
  $details = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
