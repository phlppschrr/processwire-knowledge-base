# Page::matches()

Source: `wire/core/Page.php`

Given a selector, return whether or not this Page matches using runtime/memory comparison

~~~~~
if($page->matches("created>=" . strtotime("today"))) {
  echo "This page was created today";
}
~~~~~


@param string|Selectors|array $s Selector to compare against (string, Selectors object, or array).

@return bool Returns true if this page matches, or false if it doesn't.
