

user_info = []

# 定义功能界面

def info_print():
    print('请选择功能--------------')
    print('1,添加学员')
    print('2,删除学员')
    print('3,修改学员')
    print('4,查询学员')
    print('5,显示所有学员')
    print('6,退出系统')
    print('-'*20)


# 添加用户
def add_info():
    """
    添加用户
    :return:
    """
    new_id = input('输入用户id')
    new_name = input('输入用户姓名')
    new_tel = input('输入用户手机号')

    global user_info

    for user in user_info:
        if new_name == user['name']:
            print(f'用户名{new_name}以及存在')
            return

    user_dict = {}

    user_dict['id'] = new_id
    user_dict['name'] = new_name
    user_dict['tel'] = new_tel
    user_info.append(user_dict)

def del_info():
    """
    删除用户
    :return:
    """
    user_name = input("请输入姓名")
    global user_info
    for user in user_info:
        if user_name == user['name']:
            user_info.remove(user)
            break
    else:
        print(f'用户{user_name}不存在')


def update_info():
    """
    更新用户信息
    :return:
    """
    user_name = input("输入学员信息")
    global user_info
    for user in user_info:
        if user_name == user['name']:
            tel = input('输入学员新手机号')
            user['tel'] = tel
            print("修改成功")
            break
    else:
        print("学员不存在")

def search_info():
    """
    查询学员信息
    :return:
    """
    user_name = input("输入学员信息")
    global user_info
    for user in user_info:
        if user_name == user['name']:
            print(user)
    else:
        print(f'学员{user_name}不存在')

def print_all():
    """
    显示所有学员信息
    :return:
    """
    for user in user_info:
        print(f'id:{user["id"]},name:{user["name"]},tel:{user["tel"]}')




while True:
# 1.显示功能界面
    info_print()

# 2.用户输入功能序号
    user_num = int(input('请选择序号'))

# 3.按照用户输入的功能序号，执行不同的功能
    if 1 == user_num:
        add_info()
    elif 2 == user_num:
        del_info()
    elif 3 == user_num:
        update_info()
    elif 4 == user_num:
        search_info()
    elif 5 == user_num:
        print_all()
    elif 6 == user_num:
        exit_flag = input('你确实要退出系统吗，yes/no')
        if 'yes' == exit_flag:
            break
    else:
        print('输入有误')

