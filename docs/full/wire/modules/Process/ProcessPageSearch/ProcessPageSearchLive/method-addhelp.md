# $processPageSearchLive->addHelp($group, array $examples): true

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Add help examples for when the help results are displayed

~~~~~
// handle a search of "today" to find pages modified today
$wire->addHook('ProcessPageSearchLive::findCustom', function(HookEvent $event) {
  $data = $event->arguments(0); // array
  $search = $event->object; // ProcesPageSearchLive
  if($data['help']) {
    return $search->addHelp('ID Search Help', [
      // example => description
      'today' => 'Finds pages that have been modified today',
    ]);
  }
  // ...
});
~~~~~

## Arguments

- `$group` `string` Group name for these search results
- `$examples` `array` Examples where keys are example queries and values are descriptions

## Return value

true

## Since

3.0.240
