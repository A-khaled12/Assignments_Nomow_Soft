
from datetime import datetime

class Employee:
    # قائمة لتخزين كل الموظفين (محاكاة قاعدة بيانات)
    employees = []
    _auto_id = 1  # رقم متزايد تلقائيًا

    def __init__(self, data: dict):
        """
        هنا نستقبل قاموس يحتوي بيانات الموظف
        مثال: {"emp_id": "E101", "name": "أحمد", "join_date": "1/1/2020", "salary": 50000}
        """
        self.id = Employee._auto_id
        Employee._auto_id += 1

        self.emp_id = data.get("emp_id")
        self.name = data.get("name")
        # تحويل التاريخ من نص إلى كائن تاريخ
        self.join_date = datetime.strptime(data.get("join_date"), "%d/%m/%Y").date()
        self.salary = float(data.get("salary", 0))
        self.department = data.get("department")

    # --- إنشاء موظف جديد ---
    @classmethod
    def create(cls, data: dict):
        # التحقق من أن emp_id غير مكرر
        for emp in cls.employees:
            if emp.emp_id == data.get("emp_id"):
                print(" معرف الموظف موجود مسبقًا!")
                return None
        obj = cls(data)
        obj.save()
        print(" تم إنشاء الموظف بنجاح!")
        return obj

    # --- حفظ الموظف (إضافة إلى القائمة) ---
    def save(self):
        Employee.employees.append(self)

    # --- تحديث بيانات موظف ---
    @classmethod
    def update(cls, emp_id, data: dict):
        emp = cls.find(emp_id)
        if not emp:
            print(" لم يتم العثور على الموظف.")
            return
        for key, value in data.items():
            if value:  # نتجاهل القيم الفارغة
                if key == "join_date":
                    value = datetime.strptime(value, "%d/%m/%Y").date()
                setattr(emp, key, value)
        print(" تم تحديث بيانات الموظف.")

    # --- حذف موظف ---
    @classmethod
    def delete(cls, emp_id):
        emp = cls.find(emp_id)
        if emp:
            cls.employees.remove(emp)
            print(" تم حذف الموظف.")
        else:
            print(" لم يتم العثور على الموظف.")

    # --- البحث عن موظف ---
    @classmethod
    def find(cls, emp_id):
        for emp in cls.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    # --- عرض جميع الموظفين مع البحث والفرز ---
    @classmethod
    def list(cls):
        data = cls.employees.copy()

        # --- البحث ---
        search_choice = input("هل ترغب في البحث؟ (نعم/لا): ").lower()
        if search_choice == "نعم":
            term = input("أدخل مصطلح البحث (emp_id أو الاسم): ").lower()
            data = [emp for emp in data if term in emp.emp_id.lower() or term in emp.name.lower()]

        # --- الفرز ---
        sort_choice = input("هل ترغب في الفرز؟ (نعم/لا): ").lower()
        if sort_choice == "نعم":
            sort_field = input("فرز حسب (emp_id / name / join_date / salary): ")
            try:
                data.sort(key=lambda x: getattr(x, sort_field))
            except AttributeError:
                print(" حقل فرز غير صحيح!")

        print("\n--- قائمة الموظفين ---")
        for emp in data:
            print(f"{emp.id} | {emp.emp_id} | {emp.name} | {emp.join_date} | {emp.department} | {emp.salary}")
        print("------------------------")

# ------------------------------------------------------

# اختبار النظام
if __name__ == "__main__":
    # إنشاء بعض الموظفين للتجربة
    Employee.create({"emp_id": "E101", "name": "أحمد", "join_date": "01/01/2014", "salary": 50000, "department": "الخلفية"})
    Employee.create({"emp_id": "E102", "name": "ليلى", "join_date": "05/03/2018", "salary": 35000, "department": "الأمامية"})
    Employee.create({"emp_id": "E103", "name": "عمر", "join_date": "01/01/2017", "salary": 60000, "department": "الخلفية"})

    while True:
        print("\n--- نظام إدارة الموظفين ---")
        print("1. عرض جميع الموظفين")
        print("2. إضافة موظف جديد")
        print("3. تحديث موظف")
        print("4. حذف موظف")
        print("0. خروج")
        choice = input("اختر رقم العملية: ")

        if choice == "1":
            Employee.list()
        elif choice == "2":
            data = {
                "emp_id": input("معرف الموظف: "),
                "name": input("الاسم: "),
                "join_date": input("تاريخ الانضمام (يوم/شهر/سنة): "),
                "salary": input("الراتب: "),
                "department": input("القسم: ")
            }
            Employee.create(data)
        elif choice == "3":
            emp_id = input("أدخل معرف الموظف لتحديثه: ")
            data = {
                "name": input("الاسم الجديد (أو اتركه فارغ): "),
                "join_date": input("تاريخ الانضمام الجديد (أو اتركه فارغ): "),
                "salary": input("الراتب الجديد (أو اتركه فارغ): "),
                "department": input("القسم الجديد (أو اتركه فارغ): ")
            }
            Employee.update(emp_id, data)
        elif choice == "4":
            emp_id = input("أدخل معرف الموظف لحذفه: ")
            Employee.delete(emp_id)
        elif choice == "0":
            print(" تم إنهاء البرنامج.")
            break
        else:
            print(" خيار غير صحيح، حاول مجددًا.")
