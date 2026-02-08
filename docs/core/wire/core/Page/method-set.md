# Page::set()

Source: `wire/core/Page.php`

Set the value of a page property

You can set properties to a page using either `$page->set('property', $value);` or `$page->property = $value;`.

~~~~~
// Set the page title using set() method
$page->set('title', 'About Us');

// Set the page title directly (equivalent to the above)
$page->title = 'About Us';
~~~~~


@param string $key Name of property to set

@param mixed $value Value to set

@return Page|WireData Reference to this Page

@see __set

@throws WireException
