# 🛒 Ecommerce Superstore Sales Analysis

## 📌 وصف المشروع
هذا المشروع يهدف إلى تحليل بيانات مبيعات متجر إلكتروني ضخم بهدف استخراج أهم المؤشرات التي تساعد في:
- فهم الأداء العام للمبيعات والأرباح.
- تحديد أكثر الفئات والفئات الفرعية مبيعًا.
- معرفة أعلى العملاء إنفاقًا.
- تحديد المدن الأكثر مساهمة في المبيعات.
تم تنفيذ التحليل باستخدام مكتبات **Pandas** و **Matplotlib** و **Seaborn** في Python لعمل الرسوم البيانية والتصورات البصرية.

---

## 🛠️ الخطوات المتبعة في التحليل
1. **تحميل البيانات** من ملف CSV وفحص الأعمدة والأنواع.
2. **تنظيف البيانات**:
   - تحويل الأعمدة لتواريخ (`Order Date`, `Ship Date`).
   - ملء القيم المفقودة في `Postal Code` بـ "not found".
3. **التحليل الاستكشافي (EDA)**:
   - إحصائيات وصفية.
   - عدد القيم الفريدة للأعمدة النصية.
4. **التحليل البصري**:
   - إجمالي المبيعات والأرباح.
   - المبيعات حسب الفئة الرئيسية والفئة الفرعية.
   - العملاء الأعلى إنفاقًا.
   - تطور المبيعات عبر السنوات.
   - المدن الأكثر مبيعات.

---

## 📊 أهم النتائج
- **إجمالي المبيعات:** `12,642,501.91 USD`  
- **إجمالي الأرباح:** ` 1,467,457.29 USD`  
- أكثر فئة مبيعًا: `face supplies`  
- أكثر مدينة مبيعًا: `New York City`  
- أكثر عميل إنفاقًا: `Tom Ashbrook`

---

## 🖼️ أمثلة من الرسوم البيانية
### 1. إجمالي المبيعات والأرباح
![Sales_vs_Profit](https://github.com/kareemgamal74/ecommerce-superstore-analysis/blob/main/Figure_1.png?raw=true)

### 2. المبيعات حسب الفئة
![Sales_by_Category]((https://github.com/kareemgamal74/ecommerce-superstore-analysis/blob/main/Figure_2.png?raw=true))

### 3. المدن الأكثر مبيعات
![Top_10_Cities]((https://github.com/kareemgamal74/ecommerce-superstore-analysis/blob/main/Figure_6.png?raw=true))

---

## 📂 الملفات المرفقة
- `Global_Superstore2.csv` → ملف البيانات.
- `import pandas as pd.py` → كود التحليل.
- `images/` → صور الرسوم البيانية.

---

## 📌 المتطلبات
لتشغيل الكود، يجب تثبيت المكتبات التالية:
```bash
pip install pandas matplotlib seaborn

