# $pageimage->filenameDoesNotExist($filename): bool

Source: `wire/core/Pageimage.php`

Hook called by the size() method when a source/original filename does not exist

For the return value, override the default `false` return value and set
it to `true` in order to make it continue as if the filename did exist,
such as if your hook copied a file to $filename.

## Usage

~~~~~
// basic usage
$bool = $pageimage->filenameDoesNotExist($filename);
~~~~~

## Arguments

- `$filename` `string`

## Return value

- `bool`

## Hooking

- Hookable method name: `filenameDoesNotExist`
- Implementation: `___filenameDoesNotExist`
- Hook with: `Pageimage::filenameDoesNotExist`

### Hooking Before

~~~~~
$this->addHookBefore('Pageimage::filenameDoesNotExist', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $filename = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $filename);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pageimage::filenameDoesNotExist', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $filename = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.254
