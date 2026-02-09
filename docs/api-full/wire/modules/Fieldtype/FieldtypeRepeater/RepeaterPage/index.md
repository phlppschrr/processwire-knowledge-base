# RepeaterPage

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPage.php`

Inherits: `Page`

## Summary

RepeaterPage represents an individual repeater page item

Common methods:
- [`setForPage()`](method-setforpage.md)
- [`getForPage()`](method-getforpage.md)
- [`setForField()`](method-setforfield.md)
- [`getForField()`](method-getforfield.md)
- [`getForRoot()`](method-getforroot.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`setForPage(Page $forPage): $this`](method-setforpage.md) Set the page that owns this repeater item
- [`getForPage(): Page`](method-getforpage.md) Return the page that this repeater item is for
- [`setForField(Field $forField): $this`](method-setforfield.md) Set the field that owns this repeater item
- [`getForField(): Field|null`](method-getforfield.md) Return the field that this repeater item belongs to
- [`getForRoot(string $get = ''): array|Page|Field`](method-getforroot.md) For nested repeaters, returns the root level forPage and forField in an array
- [`getForFieldRoot(): Field`](method-getforfieldroot.md) For nested repeaters, return the root-level field that this repeater item belongs to
- [`getForPageRoot(): Page`](method-getforpageroot.md) For nested repeaters, return the root-level non-repeater page that this repeater item belongs to
- [`get(string $key): int|mixed|null`](method-get.md) Get property
- [`getDepth(): int`](method-getdepth.md) Get depth
- [`setDepth(int $depth)`](method-setdepth.md) Set depth
- [`isPublic(): bool`](method-ispublic.md) Is this page public?
- [`isReady(): bool`](method-isready.md) Is this a ready page?
- [`getAccessTemplate($type = 'view'): $this`](method-getaccesstemplate.md) Track a change to a property in this object
