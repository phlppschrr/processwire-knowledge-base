# Config: database

Source: `wire/core/Config.php`

- $dbHost: string Database host
- $dbName: string Database name
- $dbUser: string Database user
- $dbPass: string Database password
- $dbPort: string Database port (default=3306)
- $dbCharset: string Default is 'utf8' but 'utf8mb4' is also supported.
- $dbEngine: string Database engine (MyISAM or InnoDB)
- $dbSocket: string Optional DB socket config for sites that need it.
- $dbCache: bool Whether to allow MySQL query caching.
- $dbLowercaseTables: bool Force any created field_* tables to be lowercase.
- $dbPath: string MySQL database exec path (Path to mysqldump)
- [$dbOptions: array](method-dboptions.md) Any additional driver options to pass as $options argument to "new PDO(...)".
- [$dbSqlModes: array](method-dbsqlmodes.md) Set or adjust SQL mode per MySQL version, where array keys are MySQL version and values are SQL mode command(s).
- $dbQueryLogMax: int Maximum number of queries WireDatabasePDO will log in memory, when debug mode is enabled (default=1000).
- $dbInitCommand: string Database init command, for PDO::MYSQL_ATTR_INIT_COMMAND. Note placeholder {charset} gets replaced with $config->dbCharset.
- $dbStripMB4: bool When dbEngine is not utf8mb4 and this is true, we will attempt to remove 4-byte characters (like emoji) from inserts when possible. Note that this adds some overhead.
- $dbReader: array|null Configuration values for read-only database connection (if available). @since 3.0.175
