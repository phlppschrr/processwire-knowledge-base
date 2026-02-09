# $wireMailTools->new($options = array()): WireMail

Source: `wire/core/WireMailTools.php`

Get a new WireMail instance for sending email

Note: The `$options` argument added in 3.0.123, previous versions had no $options argument.

## Example

~~~~~
$message = $mail->new();
$message->to('user@domain.com')->from('you@company.com');
$message->subject('Mail Subject')->body('Mail Body Text')->bodyHTML('Body HTML');
$numSent = $message->send();
~~~~~

## Usage

~~~~~
// basic usage
$wireMail = $wireMailTools->new();

// usage with all arguments
$wireMail = $wireMailTools->new($options = array());
~~~~~

## Hookable

- Hookable method name: `new`
- Implementation: `___new`
- Hook with: `$wireMailTools->new()`

## Hooking Before

~~~~~
$this->addHookBefore('WireMailTools::new', function(HookEvent $event) {
  $wireMailTools = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireMailTools::new', function(HookEvent $event) {
  $wireMailTools = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$options` (optional) `array|string` Optional settings to override defaults, or string for `module` option: - `module` (string): Class name of WireMail module you want to use rather than auto detect, or 'WireMail' to force using default PHP mail. If requested module is not available, it will fall-back to one that is (or PHP mail), so check class name of returned value if there is any doubt about what WireMail module is being used. - You may also specify: subject, from, fromName, to, toName, subject or any other WireMail property and it will be populated.

## Return value

- `WireMail`
