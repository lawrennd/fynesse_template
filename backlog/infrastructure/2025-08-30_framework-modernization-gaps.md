---
id: "2025-08-30_framework-modernization-gaps"
title: "Framework Modernization: Address Gaps and Outdated Approaches"
status: "Proposed"
priority: "High"
created: "2025-08-30"
last_updated: "2025-08-30"
owner: "Development Team"
dependencies: []
related: []
---

# Task: Framework Modernization - Address Gaps and Outdated Approaches

Note: this is a template implementation where most core functions raise `NotImplementedError`. It is just a skeleton, not fully functional
Where possible we can implement basic functionality with proper abstractions. But leave user choice in place. Modules include `access.py`, `assess.py`, `address.py`. 

## Description

The Fynesse framework template has several significant gaps and uses outdated approaches that need to be addressed for modern Python development practices. This task identifies and prioritizes the key areas requiring modernization.

## Acceptance Criteria

- [x] Replace deprecated `nose` testing framework with modern `pytest`
- [ ] Update Python packaging from `setup.py` to modern standards (`pyproject.toml`)
- [x] Add stubs for comprehensive test suite
- [x] Modernize dependency management and version specifications (Poetry with pyproject.toml)
- [x] Add type hints throughout the codebase
- [x] Implement proper error handling and logging
- [x] Add CI/CD pipeline configuration
- [ ] Update Python version requirements to current standards
- [x] Add proper documentation and API references

## Implementation Notes

### Critical Issues Identified

#### 1. **Outdated Testing Framework**
- **Problem**: Uses `nose` testing framework which is deprecated (last release 2015)
- **Impact**: Tests don't run, no test coverage, broken CI/CD
- **Solution**: Migrate to `pytest` with proper test structure
- **Files affected**: `access_tests.py`, `assess_tests.py`, `address_tests.py`

#### 2. **Missing Test Implementation**
- **Problem**: Test files reference non-existent `fynesse/tests/` directory
- **Impact**: No actual test stubs, framework untested
- **Solution**: Create any tests of framework that can be run before use builds on skeleton. Create snesible test stubs
- **Required**: Unit test stubs, integration test stubs, data validation test stubs

#### 3. **Outdated Python Packaging**
- **Problem**: Uses `setup.py` instead of modern `pyproject.toml`
- **Impact**: Deprecated approach, harder dependency management
- **Solution**: Migrate to `pyproject.toml` with modern build system
- **Benefits**: Better dependency resolution, modern tooling support

#### 4. **Missing Modern Python Features**
- **Problem**: No type hints, limited error handling, no logging
- **Impact**: Poor developer experience, hard to maintain
- **Solution**: Add type hints, proper error handling, logging system
- **Benefits**: Better IDE support, easier debugging, maintainability

#### 5. **Configuration Management Issues**
- **Problem**: Basic YAML config with hardcoded paths and limited validation
- **Impact**: Fragile configuration, poor error messages
- **Solution**: Implement robust config management with validation
- **Files**: `config.py`, `defaults.yml`

#### 6. **Missing Development Tools**
- **Problem**: No linting, formatting, or code quality tools
- **Impact**: Inconsistent code style, potential bugs
- **Solution**: Add `black`, `flake8`, `mypy`, pre-commit hooks
- **Benefits**: Consistent code quality, automated checks

#### 7. **Outdated Dependencies**
- **Problem**: Dependencies not pinned, potential compatibility issues
- **Impact**: Reproducible builds, security vulnerabilities
- **Solution**: Pin dependencies, add security scanning
- **Tools**: `pip-tools`, `safety`, `bandit`

### Priority Order

1. **High Priority** (Critical for functionality):
   - Replace nose with pytest
   - Implement basic test suite
   - Fix configuration system

2. **Medium Priority** (Important for maintainability):
   - Add type hints
   - Implement proper error handling
   - Add logging system

3. **Low Priority** (Nice to have):
   - Modernize packaging
   - Add development tools
   - Implement CI/CD

## Related

- Framework modernization
- Testing infrastructure
- Python packaging standards
- Development tooling

## Progress Updates

### 2025-08-30
Task created with comprehensive analysis of framework gaps and outdated approaches.

### 2025-08-30 (Update)
- ✅ Replaced deprecated `nose` testing framework with modern `pytest`
- ✅ Created comprehensive test suite with 43 test stubs across all modules
- ✅ Added `pytest.ini` configuration with coverage reporting
- ✅ Created `pyproject.toml` with modern packaging standards
- ✅ Removed redundant `requirements.txt` (pyproject.toml is single source of truth)
- ✅ Fixed module documentation and docstrings
- ✅ All tests now passing (43/43)
- ✅ Individual test runners working for each module
- ✅ Development tools installed and working (black, mypy, flake8)
- ✅ Migrated to Poetry for superior dependency management
- ✅ Code formatted with black for consistent style
- ✅ Added comprehensive type hints to core modules
- ✅ Added types-PyYAML dependency for proper type checking
- ✅ Added basic error handling and logging for educational use
