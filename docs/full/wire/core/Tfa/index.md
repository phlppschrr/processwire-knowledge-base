# Tfa

Source: `wire/core/Tfa.php`

Inherits: `WireData`
Implements: `Module`, `ConfigurableModule`


Groups:
Group: [other](group-other.md)

Tfa - ProcessWire Two Factor Authentication module base class

This class is for “Tfa” modules to extend. See the TfaEmail and TfaTotp modules as examples.



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

Methods:
- [`__construct()`](method-__construct.md) Construct
- [`wired()`](method-wired.md) Called when assigned to ProcessWire instance
- [`init()`](method-init.md) Module init
- [`getTfaTypeName(): string`](method-gettfatypename.md) Get translated Tfa type name (short name)
- [`getTfaTypeTitle(): string`](method-gettfatypetitle.md) Get translated Tfa type title (longer name)
- [`getTfaTypeSummary(): string`](method-gettfatypesummary.md) Get translated Tfa type summary
- [`url(string $queryString = ''): string`](method-url.md) Get the start URL and optionally append query string
- [`redirect(string $url)`](method-redirect.md) Redirect to URL
- [`start(string $name, string $pass): bool`](method-___start.md) (hookable) Start 2-factor authentication
- [`startUser(User $user, array $settings): bool`](method-startuser.md) Start two-factor authentication for User
- [`isValidUserCode(User $user, string|int $code, array $settings): bool|int`](method-isvalidusercode.md) Return true if code is valid or false if not
- [`active(): bool`](method-active.md) Returns true if a TFA process is currently active
- [`success(): bool`](method-success.md) Returns true when TFA has successfully completed and user is now logged in
- [`getModule(?User $user = null): Tfa|null`](method-getmodule.md) Get the TFA module for given user or current session
- [`getSessionKey(bool $reset = false): string`](method-getsessionkey.md) Get a unique key that can be used in the “tfa” GET variable used by this module
- [`buildAuthCodeForm(): InputfieldForm`](method-___buildauthcodeform.md) (hookable) Build the form used for two-factor authentication
- [`render(): string`](method-___render.md) (hookable) Render the code input form
- [`process(): User|bool`](method-___process.md) (hookable) Process two-factor authentication code input
- [`getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings)`](method-___getusersettingsinputfields.md) (hookable) CONFIG *******************************************************************************************
- [`getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, array $settings)`](method-___getusersettingsinputfields.md) (hookable) Get fields needed for a user to configure and confirm TFA from their user profile
- [`getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, array $settings)`](method-___getuserenabledinputfields.md) (hookable) Get fields for when user already has TFA enabled
- [`processUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, array $settings, array $settingsPrev): array`](method-___processusersettingsinputfields.md) (hookable) Called when the user config fieldset has been processed but before $settings have been saved
- [`processUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, array $settings, array $settingsPrev): array`](method-___processuserenabledinputfields.md) (hookable) Called when the user config fieldset has been processed (for enabled user) but before $settings have been saved
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md) Module configuration
- [`sessionGet($key, $blankValue = null)`](method-sessionget.md) SESSION ******************************************************************************************
- [`sessionGet(string $key, mixed $blankValue = null): mixed|null`](method-sessionget.md) Get a session variable for this module
- [`sessionSet(string|array $key, mixed $value = null)`](method-sessionset.md) Set a session variable only for this module
- [`sessionReset(string $redirectURL = ''): false`](method-sessionreset.md) Remove all session variables set for this module
- [`autoEnableSupported(?User $user = null)`](method-autoenablesupported.md) AUTOMATIC ENABLE *******************************************************************************
- [`autoEnableSupported(?User $user = null): bool`](method-autoenablesupported.md) Does this TFA module support automatic enable?
- [`autoEnableUser(User $user, array $settings = array())`](method-autoenableuser.md) Auto-enable this TFA module for given $user
- [`getDefaultUserSettings(User $user)`](method-getdefaultusersettings.md) USER AND SETTINGS ******************************************************************************
- [`getDefaultUserSettings(User $user): array`](method-getdefaultusersettings.md) Get default/blank user settings
- [`getUserSettings(User $user): array`](method-getusersettings.md) Get TFA data for given user from user_tfa field
- [`saveUserSettings(User $user, array $settings): bool`](method-saveusersettings.md) Save TFA data for given user to user_tfa field
- [`getUser(): User`](method-getuser.md) Get current user for TFA
- [`getUserPash(User $user): string`](method-getuserpash.md) Get internal user pass hash
- [`getUserCodeHash(User $user, string $code): string`](method-getusercodehash.md) Get internal hash of given code for user
- [`initHooks()`](method-inithooks.md) HOOKS *********************************************************************************************
- [`initHooks()`](method-inithooks.md) Attach/initialize hooks used by this module
- [`hookBeforeInputfieldFormProcess(HookEvent $event)`](method-hookbeforeinputfieldformprocess.md) Hook before InputfieldForm::processInput()
- [`hookAfterInputfieldFormProcess(HookEvent $event)`](method-hookafterinputfieldformprocess.md) Hook after InputfieldForm::processInput()
- [`hookInputfieldFormRender(HookEvent $event)`](method-hookinputfieldformrender.md) Hook before InputfieldForm::render()
- [`install()`](method-___install.md) (hookable) INSTALL AND UNINSTALL *****************************************************************************
- [`install()`](method-___install.md) (hookable) Module module and other assets required to execute it
- [`uninstall()`](method-___uninstall.md) (hookable) Uninstall

HOOKABLE METHODS
