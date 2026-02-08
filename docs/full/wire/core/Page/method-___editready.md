# $page->___editReady(InputfieldWrapper $form)

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
$result = $page->___editReady($form);

// usage with all arguments
$result = $page->___editReady(InputfieldWrapper $form);
~~~~~

## Arguments

- `$form` `InputfieldWrapper` The page editing form

## Since

3.0.253

## Details

- @todo Determine if this can also apply to the front-end editor.
