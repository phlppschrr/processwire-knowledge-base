# Tfa

Source: `wire/core/Tfa.php`

Tfa - ProcessWire Two Factor Authentication module base class

This class is for “Tfa” modules to extend. See the TfaEmail and TfaTotp modules as examples.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com


USAGE
~~~~~~
$tfa = new Tfa();

if($tfa->success()) {
  $session->redirect('after/login/url/');

} else if($tfa->active()) {
  echo $tfa->render();

} else if($input->post('submit_login')) {
  $name = $input->post('name');
  $pass = $input->post('pass');
  $tfa->start($name, $pass);

  // the start() method performs a redirect if TFA is active for the user
  // place your regular code to login user here, which will be used if TFA is not active for the user

} else {
  // render login form
}
~~~~~~

SETTINGS

TEXT LABELS

HOOKABLE METHODS

## other

@property int $codeLength Required length for authentication code (default=6)

@property int $codeExpire Codes expire after this many seconds (default=180)

@property int $codeType Type of TFA code to use, see codeType constants (default=0, which is Tfa::codeTypeDigits)

@property string $startUrl URL we are operating from (default='./')

@property int $rememberDays Number of days to "remember this browser", 0 to disable option, or -1 for no limit? (default=0)

@property array $rememberFingerprints Fingerprints to remember: agent,agentVL,accept,scheme,host,ip,fwip (default=agentVL,accept,scheme,host)

@property array $formAttrs Form <form> element attributes

@property array $inputAttrs Code <input> element attributes

@property array $submitAttrs Submit button attributes

@property bool $showCancel Show a cancel link under authentication code form? (default=true)

@property string $autoType Automatic/force TFA type (module name) to use when user doesn’t already have TFA enabled (default='')

@property array $autoRoleIDs Role IDs to enforce $autoType or blank for all roles, applies only if $autoType set (default=[])

@property string $cancelMarkup Markup to use for the cancel link that appears under auth code form, must have {url} and {label} placeholders.

@property string $cancelLabel Label to use for Cancel link (default='Cancel', translatable)

@property string $configureLabel Indicates that TFA needs to be configured

@property string $enabledLabel Indicates TFA enabled

@property string $enabledDescLabel Describes enabled TFA and how to change settings

@property string $expiredCodeLabel Expired code error

@property string $fieldTfaTypeLabel Select 2-factor auth type

@property string $fieldTfaTypeDescLabel Description of 2-factor auth type

@property string $inputLabel Label for code <input> element

@property string $invalidCodeLabel Invalid code error

@property string $maxAttemptsLabel Max attempts error

@property string $rememberLabel Label for "remember this browser" option

@property string $rememberSuccessLabel Indicates that browser has been saved/remembered for n days.

@property string $rememberSkipLabel Indicates that code entry was skipped because browser is remembered

@property string $rememberClearLabel Clear remembered browsers

@property string $rememberClearedLabel Message after remembered browsers cleared

@property string $sendCodeErrorLabel Error creating or sending code

@property string $submitLabel Label for submit button

@property string $timeLimitLabel Time limit reached error

@method bool start($name, $pass)

@method InputfieldForm buildAuthCodeForm()

@method string render()

@method User|bool process()

@method void getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings)

@method void getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings)

@method array processUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev)

@method array processUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings, $settingsPrev)

@method install()

@method uninstall()

## __construct()

Construct

## wired()

Called when assigned to ProcessWire instance

## init()

Module init

## getTfaTypeName()

Get translated Tfa type name (short name)

When a module implements this, it should not make a a parent::getTfaTypeName() call.

@return string

@since 3.0.160

## getTfaTypeTitle()

Get translated Tfa type title (longer name)

This is generally the same or similar to the module title, though in a $this->_('…'); call
so that it is translatable. When a module implements this, it should not make a
parent::getTfaTypeLabel() call.

@return string

@since 3.0.160

## getTfaTypeSummary()

Get translated Tfa type summary

This is generally the same or similar to the module summary, though in a $this->_('…'); call
so that it is translatable. When a module implements this, it should not make a
parent::getTfaTypeLabel() call.

@return string

@since 3.0.160

## url()

Get the start URL and optionally append query string

@param string $queryString

@return string

## redirect()

Redirect to URL

@param string $url

## ___start()

Start 2-factor authentication

On successful authentication of user, this method performs a redirect to the next step.
If user does not exist, they are not allowed to login, or fails to authenticate, this method
returns a boolean false. If user does not have 2FA enabled, or is remembered from a previous
TFA login, then this method returns true, but user still needs to be authenticated.

If preferred, you can ignore the return value, as this method will perform redirects whenever
it needs to move on to the next 2FA step.

@param string $name

@param string $pass

@return bool

## startUser()

Start two-factor authentication for User

Modules must implement this method unless they do not need to generate or send
authentication codes to the user. Below are details on how to implement this
method:

A. For modules that generate and validate their own authentication codes:
   1. Generate an authentication code for user
   2. Save the code to session
   3. Send the code to the user via whatever TFA channel is used
   4. Call parent::startUser($user)
   5. Return true (if no errors)

B. For modules that use an external service to generate, send and validate codes:
   1. Call on the external service to generate and the code to user
   2. Call parent::startUser($user)
   3. Return true (if no errors)

C. Modules that do not generate or send codes, but only validate them (i.e. TOTP):
   You can omit implementation, leaving just the built-in one below.
   But if you do implement it, make sure you call the parent::startUser($user).

@param User $user

@param array $settings Settings configured by user

@return bool True on success, false on fail

## isValidUserCode()

Return true if code is valid or false if not

Modules MUST implement this method.

@param User $user

@param string|int $code

@param array $settings User configured TFA settings

@return bool|int Returns true if valid, false if not, or optionally integer 0 if code was valid but is now expired

@throws WireException

## active()

Returns true if a TFA process is currently active

- This method should be called if $tfa->success() returns false.
- If this method returns true, you should `echo $tfa->render()` which will
  render the auth code form.
- If this method returns false and login/pass submitted, then call `$tfa->start()`,
  or if login not submitted, then render login form.

@return bool

## success()

Returns true when TFA has successfully completed and user is now logged in

Note that this method functions as part of the TFA flow control and will
perform redirects during processing.

@return bool

## getModule()

Get the TFA module for given user or current session

@param User|null $user Optionally specify user

@return Tfa|null

## getSessionKey()

Get a unique key that can be used in the “tfa” GET variable used by this module

@param bool $reset Reset to new key?

@return string

## ___buildAuthCodeForm()

Build the form used for two-factor authentication

This form typically appears on the screen after the user has submitted their login info

At minimum it must have an Inputfield with name “tfa_code”

@return InputfieldForm

## ___render()

Render the code input form

“Please enter your authentication code to complete login”

@return string

## ___process()

Process two-factor authentication code input

This method processes the submission of the form containing “tfa_code”.
Note that this method will perform redirects as needed.

@return User|bool Returns logged-in user object on successful code completion, or false on fail

## ___getUserSettingsInputfields()

CONFIG *******************************************************************************************

## ___getUserSettingsInputfields()

Get fields needed for a user to configure and confirm TFA from their user profile

This method should be implemented by each TFA module. It is only used when the user has selected
a TFA type and submitted form, but has not yet configured the TFA type.

@param User $user

@param InputfieldWrapper $fieldset

@param array $settings

## ___getUserEnabledInputfields()

Get fields for when user already has TFA enabled

This method does not need to be implemented by TFA modules unless they want to add something to it.

@param User $user

@param InputfieldWrapper $fieldset

@param array $settings

## ___processUserSettingsInputfields()

Called when the user config fieldset has been processed but before $settings have been saved

@param User $user

@param InputfieldWrapper $fieldset

@param array $settings Associative array of new/current settings after processing

@param array $settingsPrev Associative array of previous settings

@return array Return $newSettings array (modified as needed)

## ___processUserEnabledInputfields()

Called when the user config fieldset has been processed (for enabled user) but before $settings have been saved

@param User $user

@param InputfieldWrapper $fieldset

@param array $settings Associative array of new/current settings after processing

@param array $settingsPrev Associative array of previous settings

@return array Return $newSettings array (modified as needed)

## getModuleConfigInputfields()

Module configuration

@param InputfieldWrapper $inputfields

## sessionGet()

SESSION ******************************************************************************************

## sessionGet()

Get a session variable for this module

@param string $key

@param mixed $blankValue Optionally provide replacement blank value if session var does not exist.

@return mixed|null

## sessionSet()

Set a session variable only for this module

Optionally set several variables at once by specifying just $key as an associative array.

@param string|array $key

@param mixed $value

## sessionReset()

Remove all session variables set for this module

@param string $redirectURL Optionally redirect to URL after reset

@return false

## autoEnableSupported()

AUTOMATIC ENABLE *******************************************************************************

## autoEnableSupported()

Does this TFA module support automatic enable?

Automatic enable means a TFA module can be enabled for a user without their input.
This can be supported by a module like TfaEmail when/if we already have the user’s email,
but cannot be supported by a module like TfaTotp which requires manual setup by user.

Modules that support auto-enable must implement this method to return true. Modules
that do not support it can ignore this method, as the default returns false.

@param User|null $user Specify user to also confirm it is supported for given user.
  Omit to test if the module supports it in general.

@return bool

@since 3.0.160

## autoEnableUser()

Auto-enable this TFA module for given $user

Automatic enable means a TFA module can be enabled for a user without their input.

This method throws WireException for all error conditions, so you may want to call the
`autoEnableSupported($user)` method first.

@param User $user User to auto-enable this Tfa module for.

@param array $settings This argument can be omitted in public API usage, but should be specified
  by Tfa modules in parent::autoEnableForUser() call, containing any needed settings.

@throws WireException on all error conditions

@since 3.0.160

## getDefaultUserSettings()

USER AND SETTINGS ******************************************************************************

## getDefaultUserSettings()

Get default/blank user settings

Descending modules should implement this method.

@param User $user

@return array

## getUserSettings()

Get TFA data for given user from user_tfa field

@param User $user

@return array

@throws WireException

## saveUserSettings()

Save TFA data for given user to user_tfa field

@param User $user

@param array $settings

@return bool

@throws WireException

## getUser()

Get current user for TFA

@return User

## getUserPash()

Get internal user pass hash

This is used to represent a user + pass hash in a temporary session value.
It helps to identify if a user’s password changed between the time they
authenticated and the time they submitted the authentication code. While
it seems extremely unlikely, I think we have to cover this, just in case.

@param User $user

@return string

@since 3.0.160

## getUserCodeHash()

Get internal hash of given code for user

This is used to identify and invalidate a previously used authentication code,

@param User $user

@param string $code

@return string

@since 3.0.160

## initHooks()

HOOKS *********************************************************************************************

## initHooks()

Attach/initialize hooks used by this module

## hookBeforeInputfieldFormProcess()

Hook before InputfieldForm::processInput()

@param HookEvent $event

## hookAfterInputfieldFormProcess()

Hook after InputfieldForm::processInput()

This method grabs data from the TFA related fields added by our render() hooks,
and saves them in the user’s “tfa_type” field “settings” column.

@param HookEvent $event

## hookInputfieldFormRender()

Hook before InputfieldForm::render()

This method adds the fields configured in getUserSettingsInputfields() and adds
them to the form being rendered, but only if the form already has a field
named “tfa_type”. It also pulls the settings stored in that field, and
populates the module-specific configuration fields.

@param HookEvent $event

## ___install()

INSTALL AND UNINSTALL *****************************************************************************

## ___install()

Module module and other assets required to execute it

Please note: Tfa modules with their own install method must also call parent::___install()

## ___uninstall()

Uninstall

Please note: Tfa modules with their own uninstall method must also call parent::___uninstall()
