#一个函数负责处理打印设计工作
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+ current_design)
        completed_models.append(current_design)

#一个函数概述打印了哪些设计
def describe_completed_designs(completed_models):
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)