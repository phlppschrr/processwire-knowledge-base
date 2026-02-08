# $page->___editReady(InputfieldWrapper $form)

Source: `wire/core/Page.php`

Called when this page has been loaded into the Page editor (ProcessPageEdit)

~~~~~
// hook example in /site/templates/admin.php
$wire->addHook('Page::editReady', function($e) {
  $form = $e->arguments(0);
  $f = $form->getByName('title');
  if($f) $f->notes = 'Hello World!';
});
~~~~~

## Arguments

- `$form` `InputfieldWrapper` The page editing form

## Since

3.0.253

## Details

- @todo Determine if this can also apply to the front-end editor.
