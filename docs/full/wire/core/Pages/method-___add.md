# Pages::___add()

Source: `wire/core/Pages.php`

Add a new page using the given template and parent

If no page “name” is specified, one will be automatically assigned.

For an alternate interface for adding new pages, see the `$pages->new()` method.

~~~~~
// Add new page using 'skyscraper' template into Atlanta
$building = $pages->add('skyscraper', '/skyscrapers/atlanta/');

// Same as above, but with specifying a name/title as well:
$building = $pages->add('skyscraper', '/skyscrapers/atlanta/', 'Symphony Tower');

// Same as above, but with specifying several properties:
$building = $pages->add('skyscraper', '/skyscrapers/atlanta/', [
  'title' => 'Symphony Tower',
  'summary' => 'A 41-story skyscraper located at 1180 Peachtree Street',
  'height' => 657,
  'floors' => 41
]);
~~~~~


@param string|Template $template Template name or Template object

@param string|int|Page $parent Parent path, ID or Page object

@param string $name Optional name or title of page. If none provided, one will be automatically assigned.
	If you want to specify a different name and title then specify the $name argument, and $values['title'].

@param array $values Field values to assign to page (optional). If $name is omitted, this may also be 3rd param.

@return Page New page ready to populate. Note that this page has output formatting off.

@throws WireException When some criteria prevents the page from being saved.

@see Pages::new(), Pages::newPage()
