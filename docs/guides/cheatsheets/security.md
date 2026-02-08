# Security Checklist

Source: https://processwire.com/docs/security/file-permissions/
Source: https://processwire.com/docs/security/admin/
Source: https://processwire.com/docs/security/web-hosting/
Source: https://processwire.com/docs/security/migration/
Source: https://processwire.com/docs/security/remove-unnecessary-files/
Source: https://processwire.com/docs/security/sessions/
Source: https://processwire.com/docs/security/third-party-modules/
Source: https://processwire.com/docs/security/template-files/
Source: https://processwire.com/docs/security/two-factor-authentication/

## Checklist

- ProcessWire security: file permissions: Getting your file permissions right is one of the most important factors in maintaining the security of your ProcessWire installation, particularly in non-dedicated/shared environments
- ProcessWire security: securing your admin control panel: Information about the design and purpose of the admin environment and how to protect it. Overview of securing your admin, preventing attacks, SSL certificates, tracking logins, enabling 2FA, managing page edit access and other security best practices
- ProcessWire security: web hosting: When possible, your production sites running ProcessWire (or any CMS) should ideally be in a dedicated environment. This doesn't necessarily mean a dedicated server…
- ProcessWire security: migrating to production: Unless the production server is a completely dedicated environment, don't assume that what was safe on your development server will also be safe on the production server
- ProcessWire security: remove unnecessary files: ProcessWire comes with several files that you will no longer need after installation
- ProcessWire security: database driven sessions: Database-driven sessions offer potentially better security since the session information is not stored on the file system
- ProcessWire security: third party modules: We can vouch for the security of the code that we write in the ProcessWire core, but we can't vouch for the security of third party modules. Follow these guidelines to maximize your security with third party modules
- ProcessWire security: template files: While ProcessWire handles a lot of the common security considerations before your template files are even loaded, you should also follow security best practices within your template files as you would in any other PHP framework
- 2-factor authentication: Two-factor (or multi-factor) authentication gives you an extra layer of account security relative to just using a password. ProcessWire versions 3.0.109 and newer include core support for two-factor authentication
