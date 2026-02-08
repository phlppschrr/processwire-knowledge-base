# SessionCSRF::renderInput()

Source: `wire/core/SessionCSRF.php`

Render a form input[hidden] containing the token name and value, as looked for by hasValidToken()

~~~~~
<form method='post'>
  <input type='submit'>
  <?php echo $session->CSRF->renderInput(); ?>
</form>
~~~~~


@param int|string|null $id Optional unique ID for this token

@return string
