# CommentFormCustom

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFormCustom.php`

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

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

## getFormMarkup()

Get form markup

To set form markup use the markup in this method as your starting point and set your custom markup with this:
~~~~~
$markup = "...your custom form markup...";
$commentForm->markup('form', $markup);
~~~~~

@return string

## applyIf()

Apply an {if.name} ... {endif.name} statement

@param string $name Property name for if statement

@param bool $value If true the contents of the {if...} statement will stay, if false it will be removed

@param string $out

@return mixed|string

## renderForm()

Custom markup form render

@param string $id

@param string $class

@param array $attrs

@param array $labels

@param array $inputValues

@return string
