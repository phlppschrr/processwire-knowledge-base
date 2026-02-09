# $page->edit($key = null, $markup = null, $modal = null): string|bool|mixed

Source: `wire/core/Page.php`

Get front-end editable output for field (requires PageFrontEdit module to be installed)

This method requires the core `PageFrontEdit` module to be installed. If it is not installed then
it returns expected output but it is not front-end editable. This method corresponds to front-end
editing Option B. See the [front-end editor docs](https://processwire.com/docs/front-end/) for more details.
If the user does not have permission to front-end edit then returned output will not be editable.

Use `$page->edit('field_name');` instead of `$page->get('field_name');` to automatically return an editable
field value when the user is allowed to edit, or a regular field value when not. When field is
editable, hovering the value shows a different icon. **The user must double-click the area to edit.**

The 2nd and 3rd arguments are typically used only if you need to override the default presentation of
the editor or provide some kind of action or button to trigger the editor. It might also be useful if
the content to edit is not visible by default. It is recommended that you specify boolean true for the
`$modal` argument when using the `$markup` argument, which makes it open the editor in a modal window,
less likely to interfere with your front-end layout.

## Example

~~~~~
// retrieve editable value if field_name is editable, or just value if not
$value = $page->edit('field_name');
~~~~~

## Usage

~~~~~
// basic usage
$string = $page->edit();

// usage with all arguments
$string = $page->edit($key = null, $markup = null, $modal = null);
~~~~~

## Hookable

- Hookable method name: `edit`
- Implementation: `___edit`
- Hook with: `$page->edit()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::edit', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $key = $event->arguments(0);
  $markup = $event->arguments(1);
  $modal = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $key);
  $event->arguments(1, $markup);
  $event->arguments(2, $modal);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::edit', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $key = $event->arguments(0);
  $markup = $event->arguments(1);
  $modal = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$key` (optional) `string|bool|null` Name of field, omit to get editor active status, or boolean true to enable editor.
- `$markup` (optional) `string|bool|null` Markup user should click on to edit $fieldName (typically omitted).
- `$modal` (optional) `bool|null` Specify true to force editable region to open a modal window (typically omitted).

## Return value

- `string|bool|mixed`

## See Also

- [https://processwire.com/docs/front-end/](https://processwire.com/docs/front-end/)

## Since

3.0.0 This method is added by a hook in PageFrontEdit and only shown in this class for documentation purposes.
