# $page->isChanged($what = ''): bool

Source: `wire/core/Page.php`

Has the Page changed since it was loaded?

To check if only a specific property on the page has changed, specify the property/field name as the first argument.
This method assumes that change tracking is enabled for the Page (as it is by default).
Pages that are new (i.e. don't yet exist in the database) always return true.

## Example

~~~~~
// Check if page has any changes
if($page->isChanged()) {
  // There are changes to this page
  $changes = $page->getChanges();
}
~~~~~

~~~~~
// When page is about to be saved, update summary when body has changed
$this->addHookBefore('Pages::saveReady', function($event) {
  $page = $event->arguments('page');
  if($page->isChanged('body')) {
    // get first 300 chars from body
    $summary = substr($page->body, 0, 300);
    // truncate to position of last period
    $period = strrpos($summary, '.');
    if($period) $summary = substr($summary, 0, $period);
    // populate to the page, so that summary is also saved
    $page->summary = $summary;
  }
});
~~~~~

## Usage

~~~~~
// basic usage
$bool = $page->isChanged();

// usage with all arguments
$bool = $page->isChanged($what = '');
~~~~~

## Arguments

- `$what` (optional) `string` If specified, only checks the given property for changes rather than the whole page.

## Return value

- `bool`

## See Also

- [Wire::setTrackChanges()](../Wire/method-settrackchanges.md)
- [Wire::getChanges()](../Wire/method-getchanges.md)
- [Wire::trackChange()](../Wire/method-trackchange.md)
