# Playwright Test Report

**Report date:** 2026-11-09  
**Project:** QA Practice Site ecommerce tests  
**Overall status:** 1 failed, 5 passed

## Results

| Test case | Result | Details |
|---|---|---|
| Valid login | Passed | Demo credentials logged in successfully. |
| Invalid login | Passed | The expected invalid-credentials message appeared. |
| Add one item to cart | Passed | Cart count became `1`. |
| Add one item to favorites | Passed | The first product's favorite icon changed to its active state. |
| Search for Laptop | Failed | The ecommerce page has no search box; the requested search cannot run. |
| Sort by price, low to high | Passed | Product prices were sorted in ascending order. |

## Report file

The self-contained pytest HTML report is `report.html` in the project folder.
