# ProcessWire

Source: `wire/core/ProcessWire.php`

ProcessWire API Bootstrap

Represents an instance of ProcessWire connected with a set of API variables.
This class boots a ProcessWire instance. The current ProcessWire instance is represented by the `$wire` API variable.
~~~~~
// To create a new ProcessWire instance
$wire = new ProcessWire('/server/path/', 'https://hostname/url/');
~~~~~


Default API vars (A-Z)
======================

- $adminTheme: AdminTheme|AdminThemeFramework|null

- $cache: WireCache

- $classLoader: WireClassLoader

- $config: Config

- $database: WireDatabasePDO

- $datetime: WireDateTime

- $fieldgroups: Fieldgroups

- $fields: Fields

- $fieldtypes: Fieldtypes

- $files: WireFileTools

- $fuel: Fuel

- $hooks: WireHooks

- $input: WireInput

- $languages: Languages (present only if LanguageSupport installed)

- $log: WireLog

- $mail: WireMailTools

- $modules: Modules

- $notices: Notices

- $page: Page

- $pages: Pages

- $permissions: Permissions

- $process: Process|ProcessPageView

- $profiler: WireProfilerInterface

- $roles: Roles

- $sanitizer: Sanitizer

- $session: Session

- $templates: Templates

- $urls: Paths

- $user: User

- $users: Users

- $wire: ProcessWire

- $shutdown: WireShutdown

- $pagesVersions: PagesVersions|null

- [init()](method-___init.md)

- [ready()](method-___ready.md)

- [finished(array $data)](method-___finished.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [__destruct()](method-__destruct.md)
Method: [setConfig()](method-setconfig.md)
Method: [setConfigDebug()](method-setconfigdebug.md)
Method: [getHttpHost()](method-gethttphost.md)
Method: [initVar()](method-initvar.md)
Method: [setStatus()](method-setstatus.md)
Method: [init()](method-___init.md) (hookable)
Method: [ready()](method-___ready.md) (hookable)
Method: [finished()](method-___finished.md) (hookable)
Method: [set()](method-set.md)
Method: [__get()](method-__get.md)
Method: [includeFile()](method-includefile.md)
Method: [__call()](method-__call.md)
Method: [getProcessWireInstanceID()](method-getprocesswireinstanceid.md)
Method: [addInstance()](method-addinstance.md)
Method: [getInstances()](method-getinstances.md)
Method: [getNumInstances()](method-getnuminstances.md)
Method: [getInstance()](method-getinstance.md)
Method: [getCurrentInstance()](method-getcurrentinstance.md)
Method: [setCurrentInstance()](method-setcurrentinstance.md)
Method: [removeInstance()](method-removeinstance.md)
Method: [getRootPath()](method-getrootpath.md)
Method: [buildConfig()](method-buildconfig.md)

Constants:
Const: [versionMajor](const-versionmajor.md)
Const: [versionMinor](const-versionminor.md)
Const: [versionRevision](const-versionrevision.md)
Const: [versionSuffix](const-versionsuffix.md)
Const: [indexVersion](const-indexversion.md)
Const: [htaccessVersion](const-htaccessversion.md)
Const: [statusNone](const-statusnone.md)
Const: [statusBoot](const-statusboot.md)
Const: [statusInit](const-statusinit.md)
Const: [statusReady](const-statusready.md)
Const: [statusRender](const-statusrender.md)
Const: [statusDownload](const-statusdownload.md)
Const: [statusFinished](const-statusfinished.md)
Const: [statusExited](const-statusexited.md)
Const: [statusFailed](const-statusfailed.md)
