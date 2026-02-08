# $processPageSearchLive->findCustom(array $data): bool

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Hookable method to find custom search results

~~~~
// handle a search of "today" to find pages modified today
$wire->addHook('ProcessPageSearchLive::findCustom', function(HookEvent $event) {
  $data = $event->arguments(0); // array
  $search = $event->object; // ProcesPageSearchLive
  if($data['q'] === 'today') {
    $items = $event->wire()->pages->find("modified>=today, include=unpublished");
    foreach($items as $item) {
       $search->addSearchResult('Pages modified today', $item->title, $item->editUrl);
    }
  }
});
~~~~

## Usage

~~~~~
// basic usage
$bool = $processPageSearchLive->findCustom($data);

// usage with all arguments
$bool = $processPageSearchLive->findCustom(array $data);
~~~~~

## Hookable

- Hookable method name: `findCustom`
- Implementation: `___findCustom`
- Hook with: `$processPageSearchLive->findCustom()`

## Arguments

- `$data` `array` Data about the search including 'type', 'operator', 'q' (query) and more.

## Return value

- `bool` Optionally return false to stop search, making it use only results returned by this method.

## Since

3.0.240
