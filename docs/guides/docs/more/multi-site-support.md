# Multiple-site support

Source: https://processwire.com/docs/more/multi-site-support/

## Summary

The core supports multiple sites running on the same web account and ProcessWire installation, with each site maintaining its own database and /site/ directory. This section outlines how to install multiple sites on the same ProcessWire installation using this method.

## Key Points

- The core supports multiple sites running on the same web account and ProcessWire installation, with each site maintaining its own database and /site/ directory. This section outlines how to install multiple sites on the same ProcessWire installation using this method.
- Multiple-site support implies running multiple web sites at independent domains or subdomains from the same ProcessWire installation and web hosting account.
- ProcessWire can support multiple site setups using various methods, and you'll find several techniques discussed in the forum. On this page we outline the two most common and recommended methods of supporting multiple sites.

## Sections


## Option #1: multiple sites with multiple databases

This section outlines how to install multiple sites on the same ProcessWire installation, where each site has it's own database and /site/ directory (templates, modules, etc.)


### Advantages


### Disadvantages


### How to install

Point another domain or subdomain to your current ProcessWire installation. When you access that domain or subdomain, it should load your existing ProcessWire site.


## Option #2: multiple sites from the same database

This option requires installation of the 3rd party Multisite module by Antti Peisa, or the newer 3rd party Multisite module by Soma. These modules may not be in active development at present, but are still applicable and useful starting points if you are interested in implementing this kind of multi-site support.


### Advantages


### Disadvantages


### How to install
