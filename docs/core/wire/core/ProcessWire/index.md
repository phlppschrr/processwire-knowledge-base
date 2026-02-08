# ProcessWire

Source: `wire/core/ProcessWire.php`

ProcessWire API Bootstrap

Represents an instance of ProcessWire connected with a set of API variables.
This class boots a ProcessWire instance. The current ProcessWire instance is represented by the `$wire` API variable.
~~~~~
// To create a new ProcessWire instance
$wire = new ProcessWire('/server/path/', 'https://hostname/url/');
~~~~~

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

Default API vars (A-Z)
======================

@property AdminTheme|AdminThemeFramework|null $adminTheme

@property WireCache $cache

@property WireClassLoader $classLoader

@property Config $config

@property WireDatabasePDO $database

@property WireDateTime $datetime

@property Fieldgroups $fieldgroups

@property Fields $fields

@property Fieldtypes $fieldtypes

@property WireFileTools $files

@property Fuel $fuel

@property WireHooks $hooks

@property WireInput $input

@property Languages $languages (present only if LanguageSupport installed)

@property WireLog $log

@property WireMailTools $mail

@property Modules $modules

@property Notices $notices

@property Page $page

@property Pages $pages

@property Permissions $permissions

@property Process|ProcessPageView $process

@property WireProfilerInterface $profiler

@property Roles $roles

@property Sanitizer $sanitizer

@property Session $session

@property Templates $templates

@property Paths $urls

@property User $user

@property Users $users

@property ProcessWire $wire

@property WireShutdown $shutdown

@property PagesVersions|null $pagesVersions

@method init()

@method ready()

@method finished(array $data)

Methods:
Method: [__construct()](method-__construct.md)
Method: [__destruct()](method-__destruct.md)
Method: [setConfig()](method-setconfig.md)
Method: [setConfigDebug()](method-setconfigdebug.md)
Method: [getHttpHost()](method-gethttphost.md)
Method: [initVar()](method-initvar.md)
Method: [setStatus()](method-setstatus.md)
Method: [___init()](method-___init.md)
Method: [___ready()](method-___ready.md)
Method: [___finished()](method-___finished.md)
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
