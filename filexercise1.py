with open('salary.txt','r') as rf:
    with open('Newsalary.txt', 'a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name}\'s salary is {salary} ")



