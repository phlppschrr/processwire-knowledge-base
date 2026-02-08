# Page::___editReady()

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


@param InputfieldWrapper $form The page editing form

@todo Determine if this can also apply to the front-end editor.

@since 3.0.253
