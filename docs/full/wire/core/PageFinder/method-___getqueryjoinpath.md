# $pageFinder->getQueryJoinPath(DatabaseQuerySelect $query, $selector)

Source: `wire/core/PageFinder.php`

Special case when requested value is path or URL

## Usage

~~~~~
// basic usage
$result = $pageFinder->getQueryJoinPath($query, $selector);

// usage with all arguments
$result = $pageFinder->getQueryJoinPath(DatabaseQuerySelect $query, $selector);
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$selector` `Selector`

## Hooking

- Hookable method name: `getQueryJoinPath`
- Implementation: `___getQueryJoinPath`
- Hook with: `PageFinder::getQueryJoinPath`

### Hooking Before

~~~~~
$this->addHookBefore('PageFinder::getQueryJoinPath', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $query = $event->arguments(0);
  $selector = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $query);
  $event->arguments(1, $selector);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PageFinder::getQueryJoinPath', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $query = $event->arguments(0);
  $selector = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `PageFinderSyntaxException`
