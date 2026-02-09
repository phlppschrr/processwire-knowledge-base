# $inputfieldWrapper->renderInputfield(Inputfield $inputfield, $renderValueMode = false): string

Source: `wire/core/InputfieldWrapper.php`

Render output for an individual Inputfield

This method takes care of all the pre-and-post requisites needed for rendering an Inputfield
among a group of Inputfields. It is used by the `InputfieldWrapper::render()` method for each
Inputfield present in the children.

## Usage

~~~~~
// basic usage
$string = $inputfieldWrapper->renderInputfield($inputfield);

// usage with all arguments
$string = $inputfieldWrapper->renderInputfield(Inputfield $inputfield, $renderValueMode = false);
~~~~~

## Arguments

- `$inputfield` `Inputfield` The Inputfield to render.
- `$renderValueMode` (optional) `bool` Specify true if we are only rendering values (default=false).

## Return value

- `string` Rendered output

## Hooking

- Hookable method name: `renderInputfield`
- Implementation: `___renderInputfield`
- Hook with: `InputfieldWrapper::renderInputfield`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldWrapper::renderInputfield', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Get arguments
  $inputfield = $event->arguments(0);
  $renderValueMode = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $inputfield);
  $event->arguments(1, $renderValueMode);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldWrapper::renderInputfield', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Get arguments
  $inputfield = $event->arguments(0);
  $renderValueMode = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
