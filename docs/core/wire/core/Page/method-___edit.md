# Page::___edit()

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

~~~~~
// retrieve editable value if field_name is editable, or just value if not
$value = $page->edit('field_name');
~~~~~


@param string|bool|null $key Name of field, omit to get editor active status, or boolean true to enable editor.

@param string|bool|null $markup Markup user should click on to edit $fieldName (typically omitted).

@param bool|null $modal Specify true to force editable region to open a modal window (typically omitted).

@return string|bool|mixed

@see https://processwire.com/docs/front-end/

@since 3.0.0 This method is added by a hook in PageFrontEdit and only shown in this class for documentation purposes.
