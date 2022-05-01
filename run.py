import os

def addition(a,b):
	return a+b
	
def substraction(a,b):
	return a-b
	
def multiplication(a,b):
	return a*b
	
def division(a,b):
	return a/b
	
def write_report_to_file(reports_dir, report_file_name, op):
    report_file_path = os.path.join(reports_dir, report_file_name)
    with open(report_file_path, 'a') as f:
		for ops in op:
        f.write(ops)
	
	
if __name__=='__main__':
	a,b=10,2
	op1 = "Result of addition of {} and {} is : {}'.format(a,b,addition(a,b))
	op2 = "Result of addition of {} and {} is : {}'.format(a,b,substraction(a,b))
	op3 = "Result of addition of {} and {} is : {}'.format(a,b,multiplication(a,b))
	op4 = "Result of addition of {} and {} is : {}'.format(a,b,division(a,b))
	
	op =[]
	op.append(op1)
	op.append(op2)
	op.append(op3)
	op.append(op4)
	report_directory = "./reports"
	report_file_name = 'report.md'
	def write_report_to_file(reports_dir, report_file_name, op):
	
	
