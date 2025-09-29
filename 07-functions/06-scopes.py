
global_variable = 'Soy Global'

def outer_function():
    eclosing_variable = 'Soy Eclosing'
    
    def inner_function():
        local_variable = 'Soy Local'
        
        print(global_variable)
        print(eclosing_variable)
        print(local_variable)
    inner_function()
outer_function()
