# WireArray::find()

Source: `wire/core/WireArray.php`

Find all items in this WireArray that match the given selector.

This is non destructive and returns a brand new WireArray.

~~~~~
// Find all items with a title property containing the word "foo"
$matches = $items->find("title%=foo");
if($matches->count()) {
  echo "Found $matches->count items";
} else {
  echo "Sorry, no items were found";
}
~~~~~


@param string|array|Selectors $selector

@return WireArray
