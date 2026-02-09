# $wireInput->pageNum(): int

Source: `wire/core/WireInput.php`

Return the current pagination/page number (starting from 1)

- Page numbers must be enabled in the template settings (for template used by the page).
- The current page number affects all paginated page finding operations.
- First page number is 1 (not 0).

## Example

~~~~~
// Adjust output according to page number
if($input->pageNum == 1) {
  echo $page->body;
} else {
  echo "<a href='$page->url'>Return to first page</a>";
}
~~~~~

## Usage

~~~~~
// basic usage
$int = $wireInput->pageNum();
~~~~~

## Return value

- `int` Current pagination number
