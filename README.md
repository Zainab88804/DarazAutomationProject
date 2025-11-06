# 🛒 Daraz Automation Project  

## 🎯 Overview  
This project automates functional testing on [Daraz.pk](https://www.daraz.pk) using **Selenium WebDriver** with the **Page Object Model (POM)** structure.  
It demonstrates automation of product search, filters, and validation of free shipping.  

---

## 🧠 Learning Objectives  
- Learn Selenium for web automation  
- Implement search, filters, and assertions  
- Apply the Page Object Model (POM) for clean, modular test design  

---

## ⚙️ Tools & Technologies  
- **Language:** Python  
- **Framework:** Selenium WebDriver  
- **Browser:** Google Chrome  
- **Driver:** ChromeDriver  
- **Design Pattern:** Page Object Model (POM)  

---

## 🚀 Tasks Completed  
✅ Setup project with Selenium  
✅ Navigate to Daraz.pk  
✅ Search for “electronics”  
✅ Apply brand filter (Samsung)  
✅ Apply price filter (500–5000)  
✅ Count and validate products (>0)  
✅ Open first product details  
✅ Verify if free shipping is available  

---

## 🧩 Project Structure  
DarazAutomationProject/
│
├── pages/
│ ├── home_page.py
│ ├── search_results_page.py
│ └── product_page.py
│
├── tests/
│ └── test_daraz.py
│
├── README.md
└── requirements.txt


---

## 🧪 How to Run  
1️⃣ Install dependencies  
```bash
pip install selenium


2️⃣ Run the test

python -m tests.test_daraz


3️⃣ Chrome will open → search for electronics → apply filters → open product → verify free shipping

📸 Sample Output
Total products found: 40
✅ Products found successfully
✅ Opened first product.
✅ Free shipping is available!

