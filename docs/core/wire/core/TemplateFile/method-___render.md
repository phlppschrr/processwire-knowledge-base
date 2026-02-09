# $templateFile->render(): string|array

Source: `wire/core/TemplateFile.php`

Render the template: execute it and return its output

## Usage

~~~~~
// basic usage
$string = $templateFile->render();
~~~~~

## Hookable

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `$templateFile->render()`

## Hooking Before

~~~~~
$this->addHookBefore('TemplateFile::render', function(HookEvent $event) {
  $templateFile = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('TemplateFile::render', function(HookEvent $event) {
  $templateFile = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `string|array` The output of the Template File

## Exceptions

- `WireException|\Exception` Throws WireException if file not exist + any exceptions thrown by included file(s)
