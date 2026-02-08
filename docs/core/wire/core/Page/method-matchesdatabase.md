# Page::matchesDatabase()

Source: `wire/core/Page.php`

Given a selector, return whether or not this Page matches by querying the database

~~~~~
if($page->matchesDatabase("created>=today")) {
  echo "This page was created today";
}
~~~~~


@param string|Selectors|array $s Selector to compare against (string, Selectors object, or array).

@return bool Returns true if this page matches, or false if it doesn't.

@since 3.0.225
