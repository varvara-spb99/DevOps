import pickle
from hw14_1v import Employee
f = open('/home/varya/Documents/homework/E1.pickle', 'rb')
E1 = pickle.load(f)
f.close()
E1.print_salary_info()