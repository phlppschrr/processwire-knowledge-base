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
- [`__construct()`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`init()`](method-init.md)
- [`getTfaTypeName(): string`](method-gettfatypename.md)
- [`getTfaTypeTitle(): string`](method-gettfatypetitle.md)
- [`getTfaTypeSummary(): string`](method-gettfatypesummary.md)
- [`url(string $queryString = ''): string`](method-url.md)
- [`redirect(string $url)`](method-redirect.md)
- [`start(string $name, string $pass): bool`](method-___start.md) (hookable)
- [`startUser(User $user, array $settings): bool`](method-startuser.md)
- [`isValidUserCode(User $user, string|int $code, array $settings): bool|int`](method-isvalidusercode.md)
- [`active(): bool`](method-active.md)
- [`success(): bool`](method-success.md)
- [`getModule(?User $user = null): Tfa|null`](method-getmodule.md)
- [`getSessionKey(bool $reset = false): string`](method-getsessionkey.md)
- [`buildAuthCodeForm(): InputfieldForm`](method-___buildauthcodeform.md) (hookable)
- [`render(): string`](method-___render.md) (hookable)
- [`process(): User|bool`](method-___process.md) (hookable)
- [`getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings)`](method-___getusersettingsinputfields.md) (hookable)
- [`getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, array $settings)`](method-___getusersettingsinputfields.md) (hookable)
- [`getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, array $settings)`](method-___getuserenabledinputfields.md) (hookable)
- [`processUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, array $settings, array $settingsPrev): array`](method-___processusersettingsinputfields.md) (hookable)
- [`processUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, array $settings, array $settingsPrev): array`](method-___processuserenabledinputfields.md) (hookable)
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md)
- [`sessionGet($key, $blankValue = null)`](method-sessionget.md)
- [`sessionGet(string $key, mixed $blankValue = null): mixed|null`](method-sessionget.md)
- [`sessionSet(string|array $key, mixed $value = null)`](method-sessionset.md)
- [`sessionReset(string $redirectURL = ''): false`](method-sessionreset.md)
- [`autoEnableSupported(?User $user = null)`](method-autoenablesupported.md)
- [`autoEnableSupported(?User $user = null): bool`](method-autoenablesupported.md)
- [`autoEnableUser(User $user, array $settings = array())`](method-autoenableuser.md)
- [`getDefaultUserSettings(User $user)`](method-getdefaultusersettings.md)
- [`getDefaultUserSettings(User $user): array`](method-getdefaultusersettings.md)
- [`getUserSettings(User $user): array`](method-getusersettings.md)
- [`saveUserSettings(User $user, array $settings): bool`](method-saveusersettings.md)
- [`getUser(): User`](method-getuser.md)
- [`getUserPash(User $user): string`](method-getuserpash.md)
- [`getUserCodeHash(User $user, string $code): string`](method-getusercodehash.md)
- [`initHooks()`](method-inithooks.md)
- [`initHooks()`](method-inithooks.md)
- [`hookBeforeInputfieldFormProcess(HookEvent $event)`](method-hookbeforeinputfieldformprocess.md)
- [`hookAfterInputfieldFormProcess(HookEvent $event)`](method-hookafterinputfieldformprocess.md)
- [`hookInputfieldFormRender(HookEvent $event)`](method-hookinputfieldformrender.md)
- [`install()`](method-___install.md) (hookable)
- [`install()`](method-___install.md) (hookable)
- [`uninstall()`](method-___uninstall.md) (hookable)

HOOKABLE METHODS
