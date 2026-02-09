# ProcessWire

Source: `wire/core/ProcessWire.php`

Inherits: `Wire`

ProcessWire API Bootstrap

Represents an instance of ProcessWire connected with a set of API variables.
This class boots a ProcessWire instance. The current ProcessWire instance is represented by the `$wire` API variable.
~~~~~
// To create a new ProcessWire instance
$wire = new ProcessWire('/server/path/', 'https://hostname/url/');
~~~~~


Default API vars (A-Z)
======================

- `$adminTheme: AdminTheme|AdminThemeFramework|null`
- `$cache: WireCache`
- `$classLoader: WireClassLoader`
- `$config: Config`
- `$database: WireDatabasePDO`
- `$datetime: WireDateTime`
- `$fieldgroups: Fieldgroups`
- `$fields: Fields`
- `$fieldtypes: Fieldtypes`
- `$files: WireFileTools`
- `$fuel: Fuel`
- `$hooks: WireHooks`
- `$input: WireInput`
- `$languages: Languages` (present only if LanguageSupport installed)
- `$log: WireLog`
- `$mail: WireMailTools`
- `$modules: Modules`
- `$notices: Notices`
- `$page: Page`
- `$pages: Pages`
- `$permissions: Permissions`
- `$process: Process|ProcessPageView`
- `$profiler: WireProfilerInterface`
- `$roles: Roles`
- `$sanitizer: Sanitizer`
- `$session: Session`
- `$templates: Templates`
- `$urls: Paths`
- `$user: User`
- `$users: Users`
- `$wire: ProcessWire`
- `$shutdown: WireShutdown`
- `$pagesVersions: PagesVersions|null`
- [`init()()`](method-init.md)
- [`ready()()`](method-ready.md)
- `@method finished(array $data)` finished(array $data)

Methods:
- [`__construct(Config|string|null $config = null, string $rootURL = '/')`](method-__construct.md) Create a new ProcessWire instance
- [`__destruct()`](method-__destruct.md) Destruct
- [`setConfig(Config $config)`](method-setconfig.md) Populate ProcessWire's configuration with runtime and optional variables
- [`setConfigDebug(Config $config): bool|int`](method-setconfigdebug.md) Determine whether debug mode should be enabled
- [`getHttpHost(Config $config): string`](method-gethttphost.md) Safely determine the HTTP host
- [`initVar(string $name, Fieldtypes|Fields|Fieldgroups|Templates|Pages|Session $value)`](method-initvar.md) Initialize the given API var
- [`setStatus(int $status, array $data = array())`](method-setstatus.md) Set the system status to one of the ProcessWire::status* constants
- [`init()`](method-___init.md) (hookable) Hookable init for anyone that wants to hook immediately before any autoload modules initialized or after all modules initialized
- [`ready()`](method-___ready.md) (hookable) Hookable ready for anyone that wants to hook immediately before any autoload modules ready or after all modules ready
- [`finished(array $data = array())`](method-___finished.md) (hookable) Hookable ready for anyone that wants to hook when the request is finished
- [`set(string $key, Wire|mixed $value, bool $lock = false): $this`](method-set.md) Set a new API variable
- [`__get(string $name): mixed`](method-__get.md) Get API var directly
- [`includeFile(string $file, array $data = array()): bool`](method-includefile.md) Include a PHP file, giving it all PW API varibles in scope
- [`__call(string $method, array $arguments): mixed`](method-__call.md) Call method
- [`getProcessWireInstanceID(): int`](method-getprocesswireinstanceid.md) Instance ID of this ProcessWire instance
- [`addInstance(ProcessWire $wire): int`](method-addinstance.md) Add a ProcessWire instance and return the instance ID
- [`getInstances(): array`](method-getinstances.md) Get all ProcessWire instances
- [`getNumInstances(): int`](method-getnuminstances.md) Return number of instances
- [`getInstance(int|null $instanceID = null): null|ProcessWire`](method-getinstance.md) Get a ProcessWire instance by ID
- [`getCurrentInstance(): ProcessWire|null`](method-getcurrentinstance.md) Get the current ProcessWire instance
- [`setCurrentInstance(ProcessWire $wire)`](method-setcurrentinstance.md) Set the current ProcessWire instance
- [`removeInstance(ProcessWire $wire)`](method-removeinstance.md) Remove a ProcessWire instance
- [`getRootPath(bool|string $rootPath = ''): string`](method-getrootpath.md) Get root path, check it, and optionally auto-detect it if not provided
- [`buildConfig(string $rootPath = '', string $rootURL = null, array $options = array()): Config`](method-buildconfig.md) Static method to build a Config object for booting ProcessWire

Constants:
- [`versionMajor`](const-versionmajor.md)
- [`versionMinor`](const-versionminor.md)
- [`versionRevision`](const-versionrevision.md)
- [`versionSuffix`](const-versionsuffix.md)
- [`indexVersion`](const-indexversion.md)
- [`htaccessVersion`](const-htaccessversion.md)
- [`statusNone`](const-statusnone.md)
- [`statusBoot`](const-statusboot.md)
- [`statusInit`](const-statusinit.md)
- [`statusReady`](const-statusready.md)
- [`statusRender`](const-statusrender.md)
- [`statusDownload`](const-statusdownload.md)
- [`statusFinished`](const-statusfinished.md)
- [`statusExited`](const-statusexited.md)
- [`statusFailed`](const-statusfailed.md)
