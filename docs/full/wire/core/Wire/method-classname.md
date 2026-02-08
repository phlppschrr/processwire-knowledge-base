# Wire::className()

Source: `wire/core/Wire.php`

Return this object’s class name

By default, this method returns the class name without namespace. To include the namespace, call it
with boolean true as the first argument.

~~~~~
echo $page->className(); // outputs: Page
echo $page->className(true); // outputs: ProcessWire\Page
~~~~~


@param array|bool|null $options Specify boolean `true` to return class name with namespace, or specify an array of
 one or more options:
	- `lowercase` (bool): Specify true to make it return hyphenated lowercase version of class name (default=false).
	- `namespace` (bool): Specify true to include namespace from returned class name (default=false).
	- *Note: The lowercase and namespace options may not both be true at the same time.*

@return string String with class name
