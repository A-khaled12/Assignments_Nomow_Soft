# نظام إدارة الموظفين
# إعداد الطالب: [عبدالله خالد ابراهيم]

# كل موظف يتم تمثيله بقاموس يحتوي على:
# id, name, join_date, salary, department

employees = [
    {"id": 259, "name": "أحمد", "join_date": "1/1/2014", "salary": 50000, "department": "الخلفية"},
    {"id": 260, "name": "عمر", "join_date": "1/1/2017", "salary": 60000, "department": "الخلفية"},
    {"id": 261, "name": "ليلى", "join_date": "5/3/2018", "salary": 35000, "department": "الأمامية"},
]

# دالة لعرض جميع الموظفين
def list_employees():
    print("\n--- قائمة الموظفين ---")
    for emp in employees:
        print(f"{emp['id']} | {emp['name']} | {emp['join_date']} | {emp['department']} | {emp['salary']}")
    print("------------------------")

# دالة لإيجاد موظف حسب المعرف
def get_employee_by_id(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return None

# إضافة موظف جديد
def add_employee():
    try:
        emp_id = int(input("أدخل معرف الموظف: "))
        if get_employee_by_id(emp_id):
            print(" يوجد موظف بهذا المعرف مسبقًا!")
            return

        name = input("أدخل اسم الموظف: ")
        join_date = input("أدخل تاريخ الانضمام (مثال: 1/1/2020): ")
        salary = float(input("أدخل الراتب: "))
        department = input("أدخل القسم: ")

        new_emp = {
            "id": emp_id,
            "name": name,
            "join_date": join_date,
            "salary": salary,
            "department": department
        }

        employees.append(new_emp)
        print(" تم إضافة الموظف بنجاح!")
    except ValueError:
        print(" خطأ في الإدخال، حاول مرة أخرى.")

# تحديث بيانات موظف
def update_employee():
    emp_id = int(input("أدخل معرف الموظف لتحديثه: "))
    emp = get_employee_by_id(emp_id)
    if not emp:
        print(" لم يتم العثور على الموظف.")
        return

    print("أدخل البيانات الجديدة (اتركها فارغة إذا لا تريد التغيير):")
    name = input(f"الاسم الحالي ({emp['name']}): ") or emp['name']
    join_date = input(f"تاريخ الانضمام ({emp['join_date']}): ") or emp['join_date']
    salary_input = input(f"الراتب الحالي ({emp['salary']}): ")
    salary = float(salary_input) if salary_input else emp['salary']
    department = input(f"القسم ({emp['department']}): ") or emp['department']

    emp.update({"name": name, "join_date": join_date, "salary": salary, "department": department})
    print(" تم تحديث بيانات الموظف بنجاح.")

# حذف موظف
def delete_employee():
    emp_id = int(input("أدخل معرف الموظف لحذفه: "))
    emp = get_employee_by_id(emp_id)
    if emp:
        employees.remove(emp)
        print(" تم حذف الموظف بنجاح.")
    else:
        print(" لم يتم العثور على الموظف.")

# البحث عن موظف بالاسم أو المعرف
def search_employee():
    keyword = input("أدخل اسم أو معرف الموظف للبحث: ")
    print("\nنتائج البحث:")
    found = False
    for emp in employees:
        if keyword.lower() in emp["name"].lower() or keyword == str(emp["id"]):
            print(f"{emp['id']} | {emp['name']} | {emp['join_date']} | {emp['department']} | {emp['salary']}")
            found = True
    if not found:
        print(" لا يوجد نتائج.")

# فرز الموظفين حسب الراتب أو الاسم
def sort_employees():
    print("1. فرز حسب الاسم")
    print("2. فرز حسب الراتب")
    choice = input("اختر نوع الفرز: ")
    if choice == "1":
        sorted_list = sorted(employees, key=lambda x: x["name"])
    elif choice == "2":
        sorted_list = sorted(employees, key=lambda x: x["salary"], reverse=True)
    else:
        print(" خيار غير صحيح.")
        return
    print("\n--- بعد الفرز ---")
    for emp in sorted_list:
        print(f"{emp['id']} | {emp['name']} | {emp['salary']}")

# تجميع الموظفين حسب القسم وحساب إجمالي الرواتب
def department_salary_report():
    report = {}
    for emp in employees:
        dept = emp["department"]
        report[dept] = report.get(dept, 0) + emp["salary"]

    print("\n--- إجمالي الرواتب حسب القسم ---")
    for dept, total in report.items():
        print(f"{dept}: {total}")

# الحصول على أول وآخر موظف انضم
def joined_report():
    sorted_by_date = sorted(employees, key=lambda x: x["join_date"])
    print("\nأول موظف انضم:", sorted_by_date[0]["name"], "-", sorted_by_date[0]["join_date"])
    print("آخر موظف انضم:", sorted_by_date[-1]["name"], "-", sorted_by_date[-1]["join_date"])

# أعلى وأقل راتب
def salary_report():
    min_emp = min(employees, key=lambda x: x["salary"])
    max_emp = max(employees, key=lambda x: x["salary"])
    print("\nأقل راتب:", min_emp["name"], "-", min_emp["salary"])
    print("أعلى راتب:", max_emp["name"], "-", max_emp["salary"])

# القائمة الرئيسية
def menu():
    while True:
        print("\n--- نظام إدارة الموظفين ---")
        print("1. عرض جميع الموظفين")
        print("2. عرض موظف حسب المعرف")
        print("3. إضافة موظف")
        print("4. تحديث موظف")
        print("5. حذف موظف")
        print("6. البحث عن موظف")
        print("7. فرز الموظفين")
        print("8. تقرير الرواتب حسب القسم")
        print("9. أول وآخر موظف انضم")
        print("10. الموظف ذو الراتب الأعلى والأقل")
        print("0. خروج")

        choice = input("اختر رقم العملية: ")

        if choice == "1":
            list_employees()
        elif choice == "2":
            emp_id = int(input("أدخل معرف الموظف: "))
            emp = get_employee_by_id(emp_id)
            if emp:
                print(emp)
            else:
                print(" لم يتم العثور على الموظف.")
        elif choice == "3":
            add_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            search_employee()
        elif choice == "7":
            sort_employees()
        elif choice == "8":
            department_salary_report()
        elif choice == "9":
            joined_report()
        elif choice == "10":
            salary_report()
        elif choice == "0":
            print(" تم إنهاء البرنامج.")
            break
        else:
            print(" خيار غير صحيح، حاول مجددًا.")

# تشغيل البرنامج
menu()
