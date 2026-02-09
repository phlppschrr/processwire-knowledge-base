# $pagesType->new(array $options = []): Page

Source: `wire/core/PagesType.php`

Create new instance of this page type

## Usage

~~~~~
// basic usage
$page = $pagesType->new();

// usage with all arguments
$page = $pagesType->new(array $options = []);
~~~~~

## Hookable

- Hookable method name: `new`
- Implementation: `___new`
- Hook with: `$pagesType->new()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesType::new', function(HookEvent $event) {
  $pagesType = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagesType::new', function(HookEvent $event) {
  $pagesType = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$options` (optional) `array`

## Return value

- `Page`

## Since

3.0.249
