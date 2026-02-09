# $page->getFields(): FieldsArray

Source: `wire/core/Page.php`

Returns a FieldsArray of all Field objects in the context of this Page

Unlike $page->fieldgroup (or its alias $page->fields), the fields returned from
this method are in the context of this page/template. Meaning returned Field
objects may have some properties that are different from the Field outside of
the context of this page.

## Usage

~~~~~
// basic usage
$fieldsArray = $page->getFields();
~~~~~

## Return value

- `FieldsArray` of Field objects
