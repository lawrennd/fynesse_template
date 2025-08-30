# Fynesse Template Tenets

*Generated on 2025-08-30*

This document combines all individual tenet files from the Fynesse template project.

---

# Tenet: Educational Clarity Over Enterprise Complexity

**Description**: The template prioritizes learning and understanding over production-ready complexity. Students should be able to see clear patterns and understand what they're implementing without being overwhelmed by enterprise-level abstractions. This principle guides all decisions about tool selection, code structure, and feature implementation.

**Quote**: *"Teach the fundamentals clearly, not the edge cases comprehensively."*

**Examples**:
- Use simple `try/except` blocks instead of complex exception hierarchies
- Provide clear implementation guides in docstrings
- Use basic logging instead of structured logging frameworks
- Keep dependencies minimal and focused
- Show error handling patterns without complex frameworks
- Use straightforward configuration approaches

**Counter-examples**:
- Adding complex dependency injection frameworks
- Implementing enterprise-grade monitoring systems
- Using advanced design patterns that obscure the core concepts
- Adding unnecessary abstractions for "future-proofing"
- Using complex logging frameworks like structlog
- Implementing custom exception hierarchies

**Conflicts**:
- **Production vs Education**: When advanced features would help in production but confuse students
- Resolution: Prefer educational clarity, document advanced patterns separately
- **Completeness vs Simplicity**: When adding more features would be "complete" but complex
- Resolution: Focus on core concepts that students need to understand

---

# Tenet: Modern Python Practices Without Over-Engineering

**Description**: The template should follow current Python best practices and use modern tools, but avoid over-engineering solutions. Students should learn contemporary approaches without being burdened by unnecessary complexity. This ensures they learn current standards while maintaining focus on core concepts.

**Quote**: *"Use the right tool for the job, not every tool in the toolbox."*

**Examples**:
- Use Poetry for dependency management (modern, clear)
- Use pytest for testing (standard, well-documented)
- Use type hints for clarity (helps learning, not just production)
- Use `pyproject.toml` for configuration (current standard)
- Use modern Python packaging standards
- Follow PEP 8 style guidelines

**Counter-examples**:
- Adding multiple testing frameworks simultaneously
- Using experimental or unstable features
- Implementing complex CI/CD pipelines in the template
- Adding unnecessary abstractions for "flexibility"
- Using deprecated tools and practices
- Over-engineering simple solutions

**Conflicts**:
- **Simplicity vs Completeness**: When adding more tools would be "better" but more complex
- Resolution: Prefer fewer, well-chosen tools over comprehensive but complex solutions
- **Modern vs Stable**: When newer tools offer benefits but may be less stable
- Resolution: Choose modern tools that are well-established and documented

---

# Tenet: Template Structure Over Implementation Details

**Description**: The template should provide a clear structure and guidance for implementation, but not implement the actual data science work. Students should understand what to implement and where, without being given complete solutions. This principle ensures the template serves as a learning scaffold rather than a complete solution.

**Quote**: *"Show the path, don't walk it for them."*

**Examples**:
- Provide stub functions with clear docstrings
- Include implementation guides in comments
- Show error handling patterns without implementing specific data sources
- Demonstrate testing approaches with template tests
- Provide clear module structure and organization
- Include example patterns and approaches

**Counter-examples**:
- Implementing complete data loading from specific APIs
- Providing full analysis pipelines
- Including real datasets or complete solutions
- Adding domain-specific implementations
- Giving students complete working code
- Implementing specific business logic

**Conflicts**:
- **Guidance vs Solution**: When providing more examples would help but might be seen as "the answer"
- Resolution: Provide patterns and examples, not complete implementations
- **Clarity vs Completeness**: When more detail would clarify but might provide too much solution
- Resolution: Focus on structure and patterns, let students implement details
