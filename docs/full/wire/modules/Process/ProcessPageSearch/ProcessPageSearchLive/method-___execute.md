# $processPageSearchLive->execute($getJSON = true): string|array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Execute live search and return JSON result

## Usage

~~~~~
// basic usage
$string = $processPageSearchLive->execute();

// usage with all arguments
$string = $processPageSearchLive->execute($getJSON = true);
~~~~~

## Arguments

- `$getJSON` (optional) `bool` Get results as JSON string? Specify false to get array instead.

## Return value

- `string|array`

## Hooking

- Hookable method name: `execute`
- Implementation: `___execute`
- Hook with: `ProcessPageSearchLive::execute`

### Hooking Before

~~~~~
$this->addHookBefore('ProcessPageSearchLive::execute', function(HookEvent $event) {
  $processPageSearchLive = $event->object;

  // Get arguments
  $getJSON = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $getJSON);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ProcessPageSearchLive::execute', function(HookEvent $event) {
  $processPageSearchLive = $event->object;

  // Get arguments
  $getJSON = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
