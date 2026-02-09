# $pages->touch($pages, $options = null, $type = 'modified'): bool

Source: `wire/core/Pages.php`

Update page modification time to now (or the given modification time)

This behaves essentially the same as the unix `touch` command, but for ProcessWire pages.

## Example

~~~~~
// Touch the current $page to current date/time
$pages->touch($page);

// Touch the current $page and set modification date to 2016/10/24
$pages->touch($page, "2016-10-24 00:00");

// Touch all "skyscraper" pages in "Atlanta" to current date/time
$skyscrapers = $pages->find("template=skyscraper, parent=/cities/atlanta/");
$pages->touch($skyscrapers);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $pages->touch($pages);

// usage with all arguments
$bool = $pages->touch($pages, $options = null, $type = 'modified');
~~~~~

## Hookable

- Hookable method name: `touch`
- Implementation: `___touch`
- Hook with: `$pages->touch()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::touch', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $pages = $event->arguments(0);
  $options = $event->arguments(1);
  $type = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $pages);
  $event->arguments(1, $options);
  $event->arguments(2, $type);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::touch', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $pages = $event->arguments(0);
  $options = $event->arguments(1);
  $type = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$pages` `Page|PageArray|array` May be Page, PageArray or array of page IDs (integers)
- `$options` (optional) `null|int|string|array` Omit (null) to update to now, or unix timestamp or strtotime() recognized time string, or if you do not need this argument, you may optionally substitute the $type argument here, or in 3.0.183+ you can also specify array of options here instead: - `time` (string|int|null): Unix timestamp or strtotime() recognized string to use, omit for use current time (default=null) - `type` (string): One of 'modified', 'created', 'published' (default='modified') - `user` (bool|User): True to also update modified/created user to current user, or specify User object to use (default=false)
- `$type` (optional) `string` Date type to update, one of 'modified', 'created' or 'published' (default='modified') Added 3.0.147 Skip this argument if using options array for previous argument or if using the default type 'modified'.

## Return value

- `bool` True on success, false on fail

## Exceptions

- `WireException|\PDOException` if given invalid format for $modified argument or failed database query

## Since

3.0.0
