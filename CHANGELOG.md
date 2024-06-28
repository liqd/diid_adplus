# Changelog

All notable changes to this project will be documented in this file.

Since version v2306 the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
This project (not yet) adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2406.2

### Changed

- rebased on aplus v2406.4

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
