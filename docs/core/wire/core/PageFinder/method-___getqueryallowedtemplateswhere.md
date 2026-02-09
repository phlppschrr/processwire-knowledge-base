# $pageFinder->getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where): string

Source: `wire/core/PageFinder.php`

Method that allows external hooks to add to or modify the access control WHERE conditions

Called only if it's hooked. To utilize it, modify the $where argument in a BEFORE hook
or the $event->return in an AFTER hook.

## Usage

~~~~~
// basic usage
$string = $pageFinder->getQueryAllowedTemplatesWhere($query, $where);

// usage with all arguments
$string = $pageFinder->getQueryAllowedTemplatesWhere(DatabaseQuerySelect $query, $where);
~~~~~

## Hookable

- Hookable method name: `getQueryAllowedTemplatesWhere`
- Implementation: `___getQueryAllowedTemplatesWhere`
- Hook with: `$pageFinder->getQueryAllowedTemplatesWhere()`

## Hooking Before

~~~~~
$this->addHookBefore('PageFinder::getQueryAllowedTemplatesWhere', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $query = $event->arguments(0);
  $where = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $query);
  $event->arguments(1, $where);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PageFinder::getQueryAllowedTemplatesWhere', function(HookEvent $event) {
  $pageFinder = $event->object;

  // Get arguments
  $query = $event->arguments(0);
  $where = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$where` `string` SQL string for WHERE statement, not including the actual "WHERE"

## Return value

- `string`
