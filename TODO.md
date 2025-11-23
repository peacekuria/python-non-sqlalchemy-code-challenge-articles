# TODO - Refactor many_to_many.py to match tests and finalize deliverables

1. Rename class attribute `_all_authors` in Author to `all`.
2. Rename class attribute `_all_magazines` in Magazine to `all`.
3. Rename class attribute `_all_articles` in Article to `all`.
4. Ensure all methods referencing those class attributes use the new `all`.
5. Verify all validations and property setters/getters work correctly.
6. Test with existing pytest tests under lib/testing/ for articles, authors, magazines.
7. Correct any test failures related to these changes.
8. Confirm meeting all deliverables:
    - Initializers and properties
    - Object relationships
    - Aggregate and association methods
    - Proper exception handling for invalid input
9. Optionally, refactor code/comments for beginner-friendly clarity.

Once complete, run:
```bash
pytest lib/testing/
```
to verify passing tests.
