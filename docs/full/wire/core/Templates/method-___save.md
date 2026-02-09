# $templates->save(Saveable $item): bool

Source: `wire/core/Templates.php`

Save a Template

## Example

~~~~~
$templates->save($template);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $templates->save($item);

// usage with all arguments
$bool = $templates->save(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$templates->save()`

## Hooking Before

~~~~~
$this->addHookBefore('Templates::save', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Templates::save', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Saveable|Template` Template to save

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
