# $page->___addStatusReady($name, $value)

Source: `wire/core/Page.php`

Called when new status flag about to be added to page but not yet saved

## Example

~~~~~
$wire->addHook('Page::addStatusReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  if($name === 'unpublished' && $page->id === 1) {
    $page->removeStatus($name);
    $e->error("We do not allow unpublish of homepage");
  }
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->___addStatusReady($name, $value);
~~~~~

## Arguments

- `$name` `string` Name of the status flag to be added, i.e. unpublished, hidden, trash, locked
- `$value` `int` Value of the status flag to be added, a `Page::status*` constant

## Since

3.0.253
