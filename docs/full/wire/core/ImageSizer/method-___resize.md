# $imageSizer->resize($targetWidth, $targetHeight = 0): bool

Source: `wire/core/ImageSizer.php`

Resize the image proportionally to the given width/height

## Usage

~~~~~
// basic usage
$bool = $imageSizer->resize($targetWidth);

// usage with all arguments
$bool = $imageSizer->resize($targetWidth, $targetHeight = 0);
~~~~~

## Hookable

- Hookable method name: `resize`
- Implementation: `___resize`
- Hook with: `$imageSizer->resize()`

## Hooking Before

~~~~~
$this->addHookBefore('ImageSizer::resize', function(HookEvent $event) {
  $imageSizer = $event->object;

  // Get arguments
  $targetWidth = $event->arguments(0);
  $targetHeight = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $targetWidth);
  $event->arguments(1, $targetHeight);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ImageSizer::resize', function(HookEvent $event) {
  $imageSizer = $event->object;

  // Get arguments
  $targetWidth = $event->arguments(0);
  $targetHeight = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$targetWidth` `int` Target width in pixels, or 0 for proportional to height
- `$targetHeight` (optional) `int` Target height in pixels, or 0 for proportional to width. Optional-if not specified, 0 is assumed.

## Return value

- `bool` True if the resize was successful, false if not

## Exceptions

- `WireException` when not enough memory to load image or missing required data
