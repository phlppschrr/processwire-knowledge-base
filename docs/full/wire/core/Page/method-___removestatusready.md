# $page->___removeStatusReady($name, $value)

Source: `wire/core/Page.php`

Called when status flag is about to removed from page but not yet saved

## Example

~~~~~
$wire->addHook('Page::removeStatusReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  if($name === 'hidden' && $page->template->name === 'sitemap') {
    $page->addStatus($name);
    $e->error("Sitemap must remain hidden");
  }
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->___removeStatusReady($name, $value);
~~~~~

## Arguments

- `$name` `string` Name of the status flag to be removed, i.e. unpublished, hidden, trash, locked
- `$value` `int` Value of the status flag to be removed, a `Page::status*` constant

## Since

3.0.253
