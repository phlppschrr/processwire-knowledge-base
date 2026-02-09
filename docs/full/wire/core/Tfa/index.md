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
Method: [__construct()](method-__construct.md)
Method: [wired()](method-wired.md)
Method: [init()](method-init.md)
Method: [getTfaTypeName()](method-gettfatypename.md)
Method: [getTfaTypeTitle()](method-gettfatypetitle.md)
Method: [getTfaTypeSummary()](method-gettfatypesummary.md)
Method: [url()](method-url.md)
Method: [redirect()](method-redirect.md)
Method: [start()](method-___start.md) (hookable)
Method: [startUser()](method-startuser.md)
Method: [isValidUserCode()](method-isvalidusercode.md)
Method: [active()](method-active.md)
Method: [success()](method-success.md)
Method: [getModule()](method-getmodule.md)
Method: [getSessionKey()](method-getsessionkey.md)
Method: [buildAuthCodeForm()](method-___buildauthcodeform.md) (hookable)
Method: [render()](method-___render.md) (hookable)
Method: [process()](method-___process.md) (hookable)
Method: [getUserSettingsInputfields()](method-___getusersettingsinputfields.md) (hookable)
Method: [getUserSettingsInputfields()](method-___getusersettingsinputfields.md) (hookable)
Method: [getUserEnabledInputfields()](method-___getuserenabledinputfields.md) (hookable)
Method: [processUserSettingsInputfields()](method-___processusersettingsinputfields.md) (hookable)
Method: [processUserEnabledInputfields()](method-___processuserenabledinputfields.md) (hookable)
Method: [getModuleConfigInputfields()](method-getmoduleconfiginputfields.md)
Method: [sessionGet()](method-sessionget.md)
Method: [sessionGet()](method-sessionget.md)
Method: [sessionSet()](method-sessionset.md)
Method: [sessionReset()](method-sessionreset.md)
Method: [autoEnableSupported()](method-autoenablesupported.md)
Method: [autoEnableSupported()](method-autoenablesupported.md)
Method: [autoEnableUser()](method-autoenableuser.md)
Method: [getDefaultUserSettings()](method-getdefaultusersettings.md)
Method: [getDefaultUserSettings()](method-getdefaultusersettings.md)
Method: [getUserSettings()](method-getusersettings.md)
Method: [saveUserSettings()](method-saveusersettings.md)
Method: [getUser()](method-getuser.md)
Method: [getUserPash()](method-getuserpash.md)
Method: [getUserCodeHash()](method-getusercodehash.md)
Method: [initHooks()](method-inithooks.md)
Method: [initHooks()](method-inithooks.md)
Method: [hookBeforeInputfieldFormProcess()](method-hookbeforeinputfieldformprocess.md)
Method: [hookAfterInputfieldFormProcess()](method-hookafterinputfieldformprocess.md)
Method: [hookInputfieldFormRender()](method-hookinputfieldformrender.md)
Method: [install()](method-___install.md) (hookable)
Method: [install()](method-___install.md) (hookable)
Method: [uninstall()](method-___uninstall.md) (hookable)

HOOKABLE METHODS
