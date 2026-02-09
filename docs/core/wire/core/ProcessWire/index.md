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
- [`__construct(Config|string|null $config = null, string $rootURL = '/')`](method-__construct.md)
- [`__destruct()`](method-__destruct.md)
- [`setConfig(Config $config)`](method-setconfig.md)
- [`setConfigDebug(Config $config): bool|int`](method-setconfigdebug.md)
- [`getHttpHost(Config $config): string`](method-gethttphost.md)
- [`initVar(string $name, Fieldtypes|Fields|Fieldgroups|Templates|Pages|Session $value)`](method-initvar.md)
- [`setStatus(int $status, array $data = array())`](method-setstatus.md)
- [`init()`](method-___init.md) (hookable)
- [`ready()`](method-___ready.md) (hookable)
- [`finished(array $data = array())`](method-___finished.md) (hookable)
- [`set(string $key, Wire|mixed $value, bool $lock = false): $this`](method-set.md)
- [`__get(string $name): mixed`](method-__get.md)
- [`includeFile(string $file, array $data = array()): bool`](method-includefile.md)
- [`__call(string $method, array $arguments): mixed`](method-__call.md)
- [`getProcessWireInstanceID(): int`](method-getprocesswireinstanceid.md)
- [`addInstance(ProcessWire $wire): int`](method-addinstance.md)
- [`getInstances(): array`](method-getinstances.md)
- [`getNumInstances(): int`](method-getnuminstances.md)
- [`getInstance(int|null $instanceID = null): null|ProcessWire`](method-getinstance.md)
- [`getCurrentInstance(): ProcessWire|null`](method-getcurrentinstance.md)
- [`setCurrentInstance(ProcessWire $wire)`](method-setcurrentinstance.md)
- [`removeInstance(ProcessWire $wire)`](method-removeinstance.md)
- [`getRootPath(bool|string $rootPath = ''): string`](method-getrootpath.md)
- [`buildConfig(string $rootPath = '', string $rootURL = null, array $options = array()): Config`](method-buildconfig.md)

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
