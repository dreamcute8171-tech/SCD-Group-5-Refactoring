# Baseline Analysis – Yatzy Refactoring

## Project Description
Yatzy is a Python dice-scoring application. It calculates scores for different dice combinations.

## Identified Code Smells

1. **Duplicated Code**
   - Same dice-counting logic appears in multiple methods.
   - Technique: Extract Method.
   - Helper: `_count_dice()`.

2. **Long Method**
   - The fullHouse method contains unnecessary variables and repeated loops.
   - Technique: Extract Method and Simplify Method.

3. **Magic Numbers**
   - Values such as 6, 50, and scoring multipliers are used directly.
   - Technique: Replace Magic Number with Named Constant.

4. **Inconsistent Naming**
   - Methods use different naming styles.
   - Technique: Rename Method.

5. **Repeated Scoring Logic**
   - Number categories repeat similar calculations.
   - Technique: Extract Method.

6. **Complex Conditional Logic**
   - Pair, triple, and combination checks contain repeated conditions.
   - Technique: Decompose Conditional.

## Refactoring Goals
- Reduce duplicated code.
- Improve readability.
- Improve maintainability.
- Preserve existing external behavior.
- Verify behavior using automated tests.