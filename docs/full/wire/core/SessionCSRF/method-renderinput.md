# $sessionCSRF->renderInput($id = ''): string

Source: `wire/core/SessionCSRF.php`

Render a form input[hidden] containing the token name and value, as looked for by hasValidToken()

## Example

~~~~~
<form method='post'>
  <input type='submit'>
  <?php echo $session->CSRF->renderInput(); ?>
</form>
~~~~~

## Usage

~~~~~
// basic usage
$string = $sessionCSRF->renderInput();

// usage with all arguments
$string = $sessionCSRF->renderInput($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

- `string`
