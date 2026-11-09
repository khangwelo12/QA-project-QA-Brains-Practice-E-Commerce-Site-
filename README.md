# QA-project-QA-Brains-Practice-E-Commerce-Site-
QA Brains Practice E-Commerce Site  QA Project 

Project: QA Brains Practice E-Commerce Site  
URL: https://practice.qabrains.com/ecommerce-site  
Framework: Playwright + Python + pytest  
Date: November 06, 2026  
Author: Netshisumbewa Khangwelo

 Simulated Environment Assumptions
- Base URL: https://practice.qabrains.com/ecommerce-site
- All locators are example / placeholder** values (replace with real ones after inspecting the live site)
- Example locators used in code:
  - Login: `id="username"`, `id="password"`, `id="loginBtn"`
  - Add to Cart: `css=".add-to-cart-btn"`
  - Cart count: `id="cart-count"`
  - Search: `id="search-input"`
  - Sort: `id="sort-select"`
  - Favorites heart: `css=".favorite-icon"`

How to Run the Tests
1. `pip install -r requirements.txt`
2. `pytest tests/ -v --headed`          # visual mode
3. `pytest tests/ -v --headed --slowmo=500` 
4. For CI/headless: `pytest tests/ -v`

## Test Coverage (5 Critical Workflows)
1. Login (valid & invalid)
2. Add to Cart
3. Search + Sort
4. Favorites
5. Checkout

Best Practices Followed
- Page Object Model
- Explicit waits via Playwright auto-waiting
- pytest fixtures for setup/teardown
- Clear comments & docstrings
- Screenshot on failure
