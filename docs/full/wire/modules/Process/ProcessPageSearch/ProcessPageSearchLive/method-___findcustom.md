# ProcessPageSearchLive::___findCustom()

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


@param array $data Data about the search including 'type', 'operator', 'q' (query) and more.

@return bool Optionally return false to stop search, making it use only results returned by this method.

@since 3.0.240
