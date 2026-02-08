# WireArray::each()

Source: `wire/core/WireArray.php`

Perform an action upon each item in the WireArray

This is typically used to execute a function for each item, or to build a string
or array from each item.

~~~~~
// Generate navigation list of page children:
echo $page->children()->each(function($child) {
  return "<li><a href='$child->url'>$child->title</a></li>";
});

// If 2 arguments specified to custom function(), 1st is the key, 2nd is the value
echo $page->children()->each(function($key, $child) {
  return "<li><a href='$child->url'>$key: $child->title</a></li>";
});

// Same as above using different method (template string):
echo $page->children()->each("<li><a href='{url}'>{title}</a></li>");

// If WireArray used to hold non-object items, use only {key} and/or {value}
echo $items->each('<li>{key}: {value}</li>');

// Get an array of all "title" properties
$titles = $page->children()->each("title");

// Get array of "title" and "url" properties. Returns an array
// containing an associative array for each item with "title" and "url"
$properties = $page->children()->each(["title", "url"]);
~~~~~


@param callable|string|array|null $func Accepts any of the following:
1. Callable function that each item will be passed to as first argument. If this
   function returns a string, it will be appended to that of the other items and
   the result returned by this each() method.
2. Markup or text string with variable {tags} within it where each {tag} resolves
   to a property in each item. This each() method will return the concatenated result.
3. A property name (string) common to items in this WireArray. The result will be
   returned as an array.
4. An array of property names common to items in this WireArray. The result will be
   returned as an array of associative arrays indexed by property name.

@return array|null|string|WireArray Returns one of the following (related to numbers above):
  - `$this` (1a): WireArray if given a function that has no return values (if using option #1 in arguments).
  - `string` (1b): Containing the concatenated results of all function calls, if your function
    returns strings (if using option #1 in arguments).
  - `string` (2): Returns the processed and concatenated result (string) of all items in your
    template string (if using option #2 in arguments).
  - `array` (3): Returns regular PHP array of the property values for each item you requested
    (if using option #3 in arguments).
  - `array` (4): Returns an array of associative arrays containing the property values for each item
    you requested (if using option #4 in arguments).

@see WireArray::implode(), WireArray::explode()
