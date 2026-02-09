# $pageimage->createdVariation(Pageimage $image, array $data)

Source: `wire/core/Pageimage.php`

Hook called after successful creation of image variation

## Usage

~~~~~
// basic usage
$result = $pageimage->createdVariation($image, $data);

// usage with all arguments
$result = $pageimage->createdVariation(Pageimage $image, array $data);
~~~~~

## Arguments

- `$image` `Pageimage` The variation image that was created
- `$data` `array` Verbose associative array of data used to create the variation

## Hooking

- Hookable method name: `createdVariation`
- Implementation: `___createdVariation`
- Hook with: `Pageimage::createdVariation`

### Hooking Before

~~~~~
$this->addHookBefore('Pageimage::createdVariation', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $image = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $image);
  $event->arguments(1, $data);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pageimage::createdVariation', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $image = $event->arguments(0);
  $data = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.180
