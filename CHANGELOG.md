# Changelog

All notable changes to this project will be documented in this file.

Since version v2306 the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
This project (not yet) adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2406.3
### Changed

- update a4 to aplus-v2406.3
- use magic as fallback to detect image filetype if MIMEImage fails to detect
  it.

## v2406.2

### Added
- modules diagrams
- added pytest-mock to dev dependencies (currently only used in forks)

### Fixed
- fixed outdated telephone number in error templates
- fixed linting errors and reformat the modified templates
- disable password help text provided by django-allauth on login form

### Changed

- changed link on error templates from hardcoded value to page root
- docs structure
- make insight migration a bit faster

## v2406.1

### Changed

- rebased on aplus v2406.2
- update djangosaml2 to v 1.9.3

### Fixed

- add account logout view to allowed urls during saml signup. Fixes aborting
  the saml signup not being possible (#6).

## v2312.1

### Changed

- rebase on aplus ef2f03409e0b1f5c6d097909d6f37cf305b4f048
- update djangosaml2 to 1.8.0

## v2306.2

### Added

- a check for user registration in settings

### Changed

- translations
- Notifications checkbox during registration is now unchecked by default
