# $pageFinder->getQuery($selectors, array $options): DatabaseQuerySelect

Source: `wire/core/PageFinder.php`

Given one or more selectors, create the SQL query for finding pages.

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $pageFinder->getQuery($selectors, $options);

// usage with all arguments
$databaseQuerySelect = $pageFinder->getQuery($selectors, array $options);
~~~~~

## Arguments

- `$selectors` `Selectors` Array of selectors.
- `$options` `array`

## Return value

- `DatabaseQuerySelect`

## Hooking

- Hookable method name: `getQuery`
- Implementation: `___getQuery`
- Hook with: `PageFinder::getQuery`

### Hooking Before

~~~~~
$this->addHookBefore('PageFinder::getQuery', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $selectors = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $selectors);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PageFinder::getQuery', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $selectors = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `PageFinderSyntaxException`

## Details

- @TODO split this method up into more parts, it's too long
