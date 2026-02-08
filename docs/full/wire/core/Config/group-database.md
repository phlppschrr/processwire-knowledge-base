# Config: database

Source: `wire/core/Config.php`

@property string $dbHost Database host

@property string $dbName Database name

@property string $dbUser Database user

@property string $dbPass Database password

@property string $dbPort Database port (default=3306)

@property string $dbCharset Default is 'utf8' but 'utf8mb4' is also supported.

@property string $dbEngine Database engine (MyISAM or InnoDB)

@property string $dbSocket Optional DB socket config for sites that need it.

@property bool $dbCache Whether to allow MySQL query caching.

@property bool $dbLowercaseTables Force any created field_* tables to be lowercase.

@property string $dbPath MySQL database exec path (Path to mysqldump)

@property array $dbOptions Any additional driver options to pass as $options argument to "new PDO(...)".

@property array $dbSqlModes Set or adjust SQL mode per MySQL version, where array keys are MySQL version and values are SQL mode command(s).

@property int $dbQueryLogMax Maximum number of queries WireDatabasePDO will log in memory, when debug mode is enabled (default=1000).

@property string $dbInitCommand Database init command, for PDO::MYSQL_ATTR_INIT_COMMAND. Note placeholder {charset} gets replaced with $config->dbCharset.

@property bool $dbStripMB4 When dbEngine is not utf8mb4 and this is true, we will attempt to remove 4-byte characters (like emoji) from inserts when possible. Note that this adds some overhead.

@property array|null $dbReader Configuration values for read-only database connection (if available). @since 3.0.175
