---
id: "educational-clarity"
title: "Educational Clarity Over Enterprise Complexity"
created: "2025-08-30"
last_updated: "2025-08-30"
version: "1.0"
tags:
- tenet
- education
- simplicity
---

# Tenet: Educational Clarity Over Enterprise Complexity

*Description*: The template prioritises learning and understanding over production-ready complexity. Students should be able to see clear patterns and understand what they're implementing without being overwhelmed by enterprise-level abstractions. This principle guides all decisions about tool selection, code structure, and feature implementation.

*Quote*: *"Teach the fundamentals clearly, not the edge cases comprehensively."*

*Examples*:
- Use simple `try/except` blocks instead of complex exception hierarchies
- Provide clear implementation guides in docstrings
- Use basic logging instead of structured logging frameworks
- Keep dependencies minimal and focused
- Show error handling patterns without complex frameworks
- Use straightforward configuration approaches

*Counter-examples*:
- Adding complex dependency injection frameworks
- Implementing enterprise-grade monitoring systems
- Using advanced design patterns that obscure the core concepts
- Adding unnecessary abstractions for "future-proofing"
- Using complex logging frameworks like structlog
- Implementing custom exception hierarchies

*Conflicts*:
- *Production vs Education*: When advanced features would help in production but confuse students
- Resolution: Prefer educational clarity, document advanced patterns separately
- *Completeness vs Simplicity*: When adding more features would be "complete" but complex
- Resolution: Focus on core concepts that students need to understand
