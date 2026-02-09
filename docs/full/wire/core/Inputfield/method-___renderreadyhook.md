# $inputfield->renderReadyHook(?Inputfield $parent = null, $renderValueMode = false)

Source: `wire/core/Inputfield.php`

Hookable version of renderReady(), not called unless 'renderReadyHook' is hooked

Hook this method instead if you want to hook renderReady().

## Usage

~~~~~
// basic usage
$result = $inputfield->renderReadyHook();

// usage with all arguments
$result = $inputfield->renderReadyHook(?Inputfield $parent = null, $renderValueMode = false);
~~~~~

## Hookable

- Hookable method name: `renderReadyHook`
- Implementation: `___renderReadyHook`
- Hook with: `$inputfield->renderReadyHook()`

## Hooking Before

~~~~~
$this->addHookBefore('Inputfield::renderReadyHook', function(HookEvent $event) {
  $inputfield = $event->object;

  // Get arguments
  $parent = $event->arguments(0);
  $renderValueMode = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $parent);
  $event->arguments(1, $renderValueMode);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Inputfield::renderReadyHook', function(HookEvent $event) {
  $inputfield = $event->object;

  // Get arguments
  $parent = $event->arguments(0);
  $renderValueMode = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$parent` (optional) `Inputfield|null`
- `$renderValueMode` (optional) `bool`
