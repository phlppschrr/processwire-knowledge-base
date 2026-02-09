# PageFieldValueInterface

Source: `wire/core/Interfaces.php`

Interface for objects that carry a Field value for a Page

Optional, but enables Page to do some of the work rather than the Fieldtype

Methods:
- [`formatted(bool|null $set = null): bool`](method-formatted.md) Get or set formatted state
- [`setPage(Page $page)`](method-setpage.md) Set the Page
- [`setField(Field $field)`](method-setfield.md) Set the Field
- [`getPage(): Page|null`](method-getpage.md) Get the page or null if not set
- [`getField(): Field|null`](method-getfield.md) Get the field or null if not set
