# CommentForm

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentForm.php`

Inherits: `Wire`
Implements: `CommentFormInterface`

Default/example implementation of the CommentFormInterface

Generates a user input form for comments, processes comment input, and saves to the page

@see CommentArray::renderForm()

Methods:
- [`__construct(Page $page, CommentArray $comments, array $options = array())`](method-__construct.md)
- [`setOptions(array $options)`](method-setoptions.md)
- [`getOptions(): array`](method-getoptions.md)
- [`arrayOption(string $property, string|array $name = '', string|null $value = null): string|array`](method-arrayoption.md)
- [`labels(string $name, string|null $value = null): string`](method-labels.md)
- [`attrs(string $name, string|null $value = null): string`](method-attrs.md)
- [`classes(string $name, string|null $value = null): string`](method-classes.md)
- [`markup(string $name, string|null $value = null): string`](method-markup.md)
- [`presets(string $name, string|null $value = null): string`](method-presets.md)
- [`setAttr(string $attr, string $value)`](method-setattr.md)
- [`setLabel(string $label, string $value)`](method-setlabel.md)
- [`renderSuccess(?Comment $comment = null): string`](method-rendersuccess.md)
- [`render(): string`](method-render.md)
- [`renderForm(string $id, string $class, array $attrs, array $labels, array $inputValues): string`](method-renderform.md)
- [`renderFormNormal(string $id, string $class, array $attrs, array $labels, array $inputValues): string`](method-renderformnormal.md)
- [`renderFormThread(string $id, string $class, array $attrs, array $labels, array $inputValues): string`](method-renderformthread.md)
- [`renderNotifyOptions(): string`](method-rendernotifyoptions.md)
- [`processInput(): Comment|bool`](method-processinput.md)
- [`getPostedComment()`](method-getpostedcomment.md)
