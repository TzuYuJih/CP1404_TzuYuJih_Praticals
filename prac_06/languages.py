from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

programming_language_list = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for i in programming_language_list:
    if i.is_dynamic():
        print(i.field)