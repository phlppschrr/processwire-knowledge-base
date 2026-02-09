# $imageSizerEngineGD->imSaveReady($im, $filename): bool

Source: `wire/core/ImageSizerEngineGD.php`

Called before saving of image, returns true if save should proceed, false if not

Also Creates a webp file when settings indicate it should.

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->imSaveReady($im, $filename);
~~~~~

## Arguments

- `$im` `resource`
- `$filename` `string` Source filename

## Return value

- `bool`

## Hooking

- Hookable method name: `imSaveReady`
- Implementation: `___imSaveReady`
- Hook with: `ImageSizerEngineGD::imSaveReady`

### Hooking Before

~~~~~
$this->addHookBefore('ImageSizerEngineGD::imSaveReady', function(HookEvent $event) {
  $imageSizerEngineGD = $event->object;

  // Get arguments
  $im = $event->arguments(0);
  $filename = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $im);
  $event->arguments(1, $filename);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ImageSizerEngineGD::imSaveReady', function(HookEvent $event) {
  $imageSizerEngineGD = $event->object;

  // Get arguments
  $im = $event->arguments(0);
  $filename = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
