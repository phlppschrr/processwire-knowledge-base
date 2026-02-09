# $page->matchesDatabase($s): bool

Source: `wire/core/Page.php`

Given a selector, return whether or not this Page matches by querying the database

## Example

~~~~~
if($page->matchesDatabase("created>=today")) {
  echo "This page was created today";
}
~~~~~

## Usage

~~~~~
// basic usage
$bool = $page->matchesDatabase($s);
~~~~~

## Arguments

- `$s` `string|Selectors|array` Selector to compare against (string, Selectors object, or array).

## Return value

- `bool` Returns true if this page matches, or false if it doesn't.

## Since

3.0.225
