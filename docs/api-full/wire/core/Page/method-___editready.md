# $page->editReady(InputfieldWrapper $form)

Source: `wire/core/Page.php`

Called when this page has been loaded into the Page editor (ProcessPageEdit)

## Example

~~~~~
// hook example in /site/templates/admin.php
$wire->addHook('Page::editReady', function($e) {
  $form = $e->arguments(0);
  $f = $form->getByName('title');
  if($f) $f->notes = 'Hello World!';
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->editReady($form);

// usage with all arguments
$result = $page->editReady(InputfieldWrapper $form);
~~~~~

## Arguments

- `$form` `InputfieldWrapper` The page editing form

## Hooking

- Hookable method name: `editReady`
- Implementation: `___editReady`
- Hook with: `Page::editReady`

### Hooking Before

~~~~~
$this->addHookBefore('Page::editReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $form = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $form);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::editReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $form = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253

## Details

- @todo Determine if this can also apply to the front-end editor.
