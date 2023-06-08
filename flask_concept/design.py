from flask import Flask

design = Flask(__name__)

@design.route('/hello/<name>')
def hello_name(name):
    return 'hello %s' % name

@design.route('/list/<int:empID>')
def employe_list(empID):
    return 'Employe is %d' % empID

@design.route('/income/<float:salary>')
def emp_salary(salary):
    return 'monthly income %f' % salary

employe_list = ['Divya' , 'Anitha', 'Priya', 'Swetha']

#curl -X GET http://127.0.0.1:8000/getdetail
@design.route('/getdetail',methods =['GET'])
def detail():
    namelist = " "
    for name in employe_list:
        namelist += (name +" ")
    return namelist
#to get single name
#curl -X GET http://127.0.0.1:8000/singledata/
@design.route('/singledata/<string:name>',methods=['GET'])
def single(name):
    if name in employe_list:
        return f"employee '{name}'"
    else:
        return f"no such name in the list"


#curl -X POST http://127.0.0.1:8000/addname/
# to append new name into the list
@design.route('/addname/<string:name>',methods =['POST'])
def addname(name):
    employe_list.append(name)
    return f"new employ name is{employe_list}"

#curl -X DELETE http://127.0.0.1:8000/deletedata/
#delete name forn list
@design.route('/deletedata/<string:name>',methods=['DELETE'])
def removename(name):
    if name in employe_list:
       employe_list.remove(name)
       return f"new employ list{employe_list}"
    else:
        return f"no such name exist"


if __name__ == '__main__':
    # design.run()
     design.run(port=8000)


