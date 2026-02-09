# $pagefiles->clone(Pagefile $item, array $options = array()): Pagefile|bool

Source: `wire/core/Pagefiles.php`

Duplicate the Pagefile and add to this Pagefiles instance

After duplicating a file, you must follow up with a save of the page containing it.
Otherwise the file is marked for deletion.

## Usage

~~~~~
// basic usage
$pagefile = $pagefiles->clone($item);

// usage with all arguments
$pagefile = $pagefiles->clone(Pagefile $item, array $options = array());
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$pagefiles->clone()`

## Hooking Before

~~~~~
$this->addHookBefore('Pagefiles::clone', function(HookEvent $event) {
  $pagefiles = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pagefiles::clone', function(HookEvent $event) {
  $pagefiles = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Pagefile` Pagefile item to duplicate
- `$options` (optional) `array` Options to modify default behavior: - `action` (string): Specify "append", "prepend", "after", "before" or blank to only return Pagefile. (default="after") - `pagefiles` (Pagefiles): Pagefiles instance file should be duplicated to. (default=$this)

## Return value

- `Pagefile|bool` Returns new Pagefile or boolean false on fail
