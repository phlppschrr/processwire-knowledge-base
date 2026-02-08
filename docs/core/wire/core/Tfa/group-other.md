# Tfa: other

Source: `wire/core/Tfa.php`

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
