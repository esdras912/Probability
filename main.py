
import math
import matplotlib.pyplot as plt
from numpy import mat
import seaborn as sns
from seaborn.palettes import color_palette
import random
cordenades_info = {'q0' : [(-3,3),6,-1] ,'q1': [(4,-6), 6,1],'q2': [(3,-5), 6,1], 'q3': [(7,-1), 4,1], 'q4': [(-6,7), 6,-1],'q5': [(2,6), 6,-1], 'q6': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q6': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q7': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q8': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q9': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q10': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q11': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q12': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q13': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
'q14': [(random.randint(0,12),random.randint(0,12)), random.randint(1,10),random.choice([-1,1])],
}



def get_components(cordenades_info,q_iter, affected_iter):
    n = q_iter
    affected_n = affected_iter


    boolean_val_q = [bool_val[2] for bool_val in list(cordenades_info.values())]
    coordenades =  [dot[0] for dot in list(cordenades_info.values())] 
    values_q = [val[1] for val in list(cordenades_info.values())]




    x_axis = [x[0] for x in coordenades]
    y_axis = [y[1] for y in coordenades]


    try:
        affected_q = coordenades[affected_n]
    except IndexError:
        return [0,0]
    x_axis_dots = [x_axis[n], affected_q[0]]
    y_axis_dots = [y_axis[n], affected_q[1]]
    components_x = abs(x_axis_dots[0] - x_axis_dots[1]) 
    components_y = abs(y_axis_dots[0] - y_axis_dots[1]) 


    x_direction,y_direction = 0,0
    if boolean_val_q[n] != boolean_val_q[affected_n]:
        f_status = -1
    else:
        f_status = 1


    if f_status == -1:
        if x_axis[n] < affected_q[0]:
            x_direction = -1

        elif x_axis[n] > affected_q[0]:    
            x_direction = 1

        if y_axis[n] < affected_q[1]:
            y_direction = -1

        elif y_axis[n] > affected_q[1]: 
            y_direction = 1




    if f_status == 1:
            if x_axis[n] < affected_q[0]:
                x_direction = 1

            elif x_axis[n] > affected_q[0]:   
                x_direction = -1

            if y_axis[n] < affected_q[1]:
                y_direction = 1

            elif y_axis[n] > affected_q[1]:
                y_direction = -1


    path_x = [affected_q[0], x_axis[n],x_axis[n]] 
    path_y = [affected_q[1], affected_q[1], y_axis[n]]
    

    distance =   components_x**2 + components_y**2   
    distance = math.sqrt(distance)


    place_grid = 0
    if x_direction == 1 and y_direction == 1:
        place_grid = 1
    elif x_direction == -1 and y_direction == 1:
        place_grid = 2
    elif x_direction == -1 and y_direction == -1:
        place_grid = 3
    elif x_direction == 1 and y_direction == 1:
        place_grid = 4



    q_affected = values_q[affected_n] ; q_2 = values_q[n]
    k = 8.9874e9

    Fe = (k *((q_affected / 1e6) * (q_2 / 1e6))) / (distance * 1e9)

    print(f"Fe = {Fe}N")

    new_component_y = ((components_y/distance) * values_q[n]) * y_direction
    new_component_x = math.sqrt( (values_q[n]**2) - (new_component_y**2)) * x_direction


    provisional_dot_x = affected_q[0] + new_component_x
    provisional_dot_y = affected_q[1] + new_component_y




    new_path_x = [affected_q[0],provisional_dot_x]
    new_path_y = [affected_q[1], provisional_dot_y]

    

    new_components_path_x = [affected_q[0], provisional_dot_x, affected_q[0],affected_q[0]]
    new_components_path_y = [affected_q[1],affected_q[1],affected_q[1], provisional_dot_y]

   
    plt.grid()
    
    sns.scatterplot(x = x_axis,y = y_axis, color = 'red')
    plt.savefig("plot.png")
    
    return [new_component_x,new_component_y]



cyles_input = 12
cycle = 0
while cycle <= cyles_input:

    current_sum_x = []
    current_sum_y = []
    for q in range(len(cordenades_info)):
        key_affected = f'q{q}'
        for a in range(len(cordenades_info)):
                try: 
                    dif = get_components(cordenades_info,q,a)
                    current_sum_x.append(dif[0])
                    current_sum_y.append(dif[1])
                except ZeroDivisionError:
                    pass
        
        if a == len(cordenades_info) -1 :
            cordenades_info[key_affected][0] = (sum(current_sum_x), sum(current_sum_y))
            
        
    coordenades = [dot[0] for dot in cordenades_info.values()]

    
    x = [x[0] for x in coordenades]
    y = [y[1] for y in coordenades]
    plt.grid()
    sns.set_style("dark")
    sns.scatterplot(x = x, y =y)
    plt.savefig(f"./plots/ciclo{cycle}.png")
    cycle += 1

    plt.clf()
    








# def get_cordenades_info(cordenades_info, required_Data = 0):

    
#     boolean_val_q = [bool_val[2] for bool_val in list(cordenades_info.values())]
#     coordenades =  [dot[0] for dot in list(cordenades_info.values())] 
#     values_q = [val[1] for val in list(cordenades_info.values())]

#     x_axis = [x[0] for x in coordenades]
#     y_axis = [y[1] for y in coordenades]

#     if required_Data == 'bool':
#         return boolean_val_q

#     elif required_Data == 'dots':
#         return coordenades

#     elif required_Data == 'values':
#         return values_q

#     elif required_Data == 'x' or required_Data == 'X':
#         return x_axis

#     elif required_Data == 'Y' or required_Data == 'y':
#         return y_axis



# process_completed = False
# affected_iter = 0; q_iter = 0

# getting_components_process = False
# components_for_current_q_x = []
# components_for_current_q_y = []
# time_to_graph = False
# info_iter = 0
# while process_completed == False:

#     try:
#         key_acces_affected = f'q{affected_iter}'

#         current_affected_q = cordenades_info[key_acces_affected]
#     except KeyError:
#         getting_components_process = None
#         time_to_graph = True
#         process_completed == True


#     try:
#         key_acces_q = f'q{q_iter}'
#         current_q_to_compare = cordenades_info[key_acces_q]

#     except KeyError:
#         if q_iter < len(cordenades_info) -1:
#             q_iter += 1
#         affected_iter += 1
#         q_iter = 0
#         getting_components_process = True



#     if getting_components_process == False:
#         try:
#             current_components = get_components(cordenades_info,q_iter,affected_iter)
#             components_for_current_q_x.append(current_components[0])
#             components_for_current_q_y.append(current_components[1])
#             q_iter += 1


#         except ZeroDivisionError :
#             q_iter += 1

#     elif getting_components_process == True:

#         new_component_x_for_affected_q = sum(components_for_current_q_x)
#         new_component_y_for_affected_q = sum(components_for_current_q_y)

#         new_dot_for_x_affected_q = get_cordenades_info(cordenades_info,'x')[q_iter] + new_component_x_for_affected_q
#         new_dot_for_y_affected_q = get_cordenades_info(cordenades_info,'y')[q_iter] + new_component_y_for_affected_q

#         key_acces = f'q{info_iter}'
#         try:
#             cordenades_info[key_acces][0] = (new_dot_for_x_affected_q,new_dot_for_y_affected_q)
#             info_iter += 1
#         except KeyError:
#             pass
#         getting_components_process = False
#         q_iter =0
        
    
#     if time_to_graph == True:
#         x_axis = get_cordenades_info(cordenades_info,'x')
#         y_axis = get_cordenades_info(cordenades_info,'y')
#         plt.grid()
#         sns.scatterplot(x_axis,y_axis)
#         plt.savefig("amogus.png")
#         getting_components_process = None
#         time_to_graph == False
#         process_completed =  True


#     else:
#         pass



    
