# AdminThemeFramework::___getUserNavArray()

Source: `wire/core/AdminThemeFramework.php`

Get navigation items for the “user” menu

This is hookable so that something else could add stuff to it.
See the method body for details on format used.

Supported properties/attributes as of 3.0.248:

- url (href)
- title (label text)
- target (html attr)
- icon (name of icon)
- permission (required permission)
- id (html attr)
- class (html attr)
- onclick (html attr)
- data-* (html attr)

@return array
