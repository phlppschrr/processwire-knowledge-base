# CommentFormCustom

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFormCustom.php`

Inherits: `CommentForm`

CommentFormCustom

CommentForm with 100% customizable form markup

~~~~~~
$form = $page->comments->getCommentForm([
  'className' => 'CommentFormCustom',
]);

$formMarkup = "
  <form class='{form.class}' action='{form.action}' method='{form.method}' {form.attrs}>
    ...copy/paste what's in the getFormMarkup() method for a starting point...
  </form>
";

$form->markup('form', $formMarkup);
$form->labels('submit', 'Submit Feedback');
$form->labels('notify', 'Email Me');

// form notifications
$form->markup('notification', "<div class='uk-alert {class}'>{message}</div>");
$form->classes('success', 'uk-alert-success');
$form->classes('pending', 'uk-alert-warning');
$form->classes('error', 'uk-alert-danger');

echo $form->render();
~~~~~~

Methods:
Method: [getFormMarkup()](method-getformmarkup.md)
Method: [applyIf()](method-applyif.md)
Method: [renderForm()](method-renderform.md)
