# $processPageSearchLive->___getDefaultPageSearchFields(): array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Get the names of fields that should be used when searching pages

Hook this from /site/templates/admin.php to modify what gets searched.
This overrides the setting specified interactively in the ProcessPageSearch module settings.

## Example

~~~~~
$wire->addHookAfter('ProcessPageSearchLive::getDefaultPageSearchFields', function(HookEvent $e) {
  $e->return = [ 'title', 'subtitle', 'categories.title' ];
});
~~~~~

## Usage

~~~~~
// basic usage
$array = $processPageSearchLive->___getDefaultPageSearchFields();
~~~~~

## Return value

- `array`

## Since

3.0.242
