# Troubleshooting ProcessWire install or upgrade

Source: https://processwire.com/docs/start/install/troubleshooting/

## Summary

If you’ve run into an issue during installation or upgrade of ProcessWire, find out how to fix it here.

## Key Points

- If you’ve run into an issue during installation or upgrade of ProcessWire, find out how to fix it here.
- This indicates that Apache is not properly reading your .htaccess file. First we need to determine if Apache is reading your .htaccess file at all. To do this, open the .htaccess file in an editor and type in some random characters at the top, like lkjalefkjalkef and save. Load your site in your browser. You should get a "500 Error". If you do not, that means Apache is not reading your .htaccess file at all. If this is your case, contact your web host for further assistance. Or if maintaining your own server, look into the Apache *AllowOverride* directive which you may need to configure for the account in your httpd.conf file.
- If the above test did result in a 500 error, then that is good because we know your .htaccess file is at least being used. Go ahead and remove the random characters you added at the top. Now look further down in the .htaccess file for suggested changes. Specially, you will want to look at the RewriteBase directive, which is commented out (disabled) by default. You may need to enable it.

## Sections


## Troubleshooting Installation


### The homepage works but nothing else does

This indicates that Apache is not properly reading your .htaccess file. First we need to determine if Apache is reading your .htaccess file at all. To do this, open the .htaccess file in an editor and type in some random characters at the top, like lkjalefkjalkef and save. Load your site in your browser. You should get a "500 Error". If you do not, that means Apache is not reading your .htaccess file at all. If this is your case, contact your web host for further assistance. Or if maintaining your own server, look into the Apache *AllowOverride* directive which you may need to configure for the account in your httpd.conf file.


### Resolving an Apache 500 error

The presence of an Apache 500 error indicates that Apache does not like one or more of the directives in the .htaccess file. Open the .htaccess file in an editor and read the comments. Note those that indicate the term "500 NOTE" and they will provide further instructions on optional directives you can try to comment out. Test one at a time, save and reload in your browser till you determine which directive is not working with your server.


### Resolving other error messages or a blank screen

If you are getting an error message, a blank screen, or something else unexpected, see the section at the end of this document on enabling debug mode. This will enable more detailed error reporting which may help to resolve any issues.


## Troubleshooting Upgrades


### General troubleshooting upgrade tips

If you get an error message when loading your site after an upgrade, hit "reload" in your browser until the error messages disappear. It may take up to 5 reloads for ProcessWire to apply all updates.


### Enabling debug mode

Debug mode causes all errors to be reported to the screen, which can be helpful during development or troubleshooting. When in the admin, it also enables reporting of extra information in the footer. Debug mode is not intended for live or production sites, as the information reported could be a problem for security. So be sure not to leave debug mode on for any live/production sites.


### Troubleshooting a 2.x to 3.x upgrade

Before we mention anything else, if you run into any troubles with the 3.x upgrade, you may want to consider upgrading to version 2.8.x instead. It is identical to 3.x in terms of features, except that it lacks namespace support (just like 2.7). Because of that omission, version 2.8 may be more of a turn-key upgrade from 2.7 if that is your preference. You can find ProcessWire 2.8 as the processwire-legacy repository.
