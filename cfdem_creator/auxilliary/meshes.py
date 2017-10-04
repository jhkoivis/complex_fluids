



def create_cube(xmin, xmax, ymin, ymax, zmin, zmax):
    
    od = {'vertices' : ((xmin, ymin, zmin),
                        (xmax, ymin, zmin),
                        (xmax, ymax, zmin),
                        (xmin, ymax, zmin),
                        (xmin, ymin, zmax),
                        (xmax, ymin, zmax),
                        (xmax, ymax, zmax),
                        (xmin, ymax, zmax))}

    return od

def print_cube_list(cube_list):
    
    vertice_list = []
    
    print('vertices')
    print('(')
    
    for cube in cube_list:
        for item in cube['vertices']:
            if item not in vertice_list: 
                print('\t' + str(item).replace(',', ' '))
                vertice_list.append(item)
                
    print(')\n')
    
    return vertice_list

    
def get_cube_bottom_as_indices(cube, vertice_list):
    
    bottom = []
    
    for vertex in cube['vertices'][0:4]:
        bottom.append(vertice_list.index(vertex))
        
    return bottom

def get_cube_top_as_indices(cube, vertice_list):
    
    top = []
    
    for vertex in cube['vertices'][4:8]:
        top.append(vertice_list.index(vertex))
        
    return top

def get_inlet_vertices(cube_list, vertice_list):
    
    print("""
        inlet
        {
                type patch;
                faces
                (""")
    
    for cube in cube_list:
        
        inlet_index = []
        for vertex in cube['vertices']:
            if vertex[2] == 0.2:
                inlet_index.append(vertice_list.index(vertex))
        if len(inlet_index) > 0: 
            print('\t\t\t', str(inlet_index).replace(',', ' ').replace('[','(').replace(']',')'))
    
    print('\t\t);\n\t}')
    
def get_outlet_vertices(cube_list, vertice_list):
    
    print("""
        outlet
        {
                type patch;
                faces
                (""")
    
    
    for cube in cube_list:
        
        inlet_index = []
        for vertex in cube['vertices']:
            if vertex[2] == -0.2:
                inlet_index.append(vertice_list.index(vertex))
        if len(inlet_index) > 0: 
            print('\t\t\t', str(inlet_index).replace(',', ' ').replace('[','(').replace(']',')'))    
      
    print('\t\t);\n\t}')
    
def get_constriction_vertices(cube_list, vertice_list):
    
    print("""
        constriction
        {
                type patch;
                faces
                (""")
    
    
    for cube in cube_list:
        
        inlet_index = []
        for vertex in cube['vertices']:
            if vertex[2] == 0.0:
                inlet_index.append(vertice_list.index(vertex))
        if len(inlet_index) > 0: 
            print('\t\t\t', str(inlet_index).replace(',', ' ').replace('[','(').replace(']',')'))    
      
    print('\t\t);\n\t}')






cube_list = []  

xl_1 = [-0.025, -0.0025, 0.0025, 0.025]
yl_1 = [-0.025, -0.0025, 0.0025, 0.025]
zl_1 = [0.0, 0.2]

xl_2 = [-0.0025, 0.0025]
yl_2 = [-0.0025, 0.0025]
zl_2 = [0.0, 0.2]


for xi in range(3):
    for yi in range(3):
        for zi in range(1):
            
            cube = create_cube(xl_1[xi], xl_1[xi+1], 
                               yl_1[yi], yl_1[yi+1],
                               zl_1[zi], zl_1[zi+1])

            cube_list.append(cube)
            
for xi in range(1):
    for yi in range(1):
        for zi in range(1):
            
            cube = create_cube(xl_2[xi], xl_2[xi+1], 
                               yl_2[yi], yl_2[yi+1],
                               zl_2[zi], zl_2[zi+1])

            cube_list.append(cube)            
          
                                    
vertice_list = print_cube_list(cube_list)
    
print('blocks\n(')
for cube in cube_list:
    if cube['vertices'][0][2] == -0.0001: continue
    bottom  = get_cube_bottom_as_indices(cube, vertice_list)
    top     = get_cube_top_as_indices(cube, vertice_list)
    both    = bottom.extend(top)
    indexlist = str(bottom).replace(',', ' ').replace('[','(').replace(']',')')
    print('\thex ' + indexlist + '(10 10 10) simpleGrading (1 1 1)')
print(')\n')

print('boundary\n(')

get_inlet_vertices(cube_list, vertice_list)
get_outlet_vertices(cube_list, vertice_list)
get_constriction_vertices(cube_list, vertice_list)

print(')')



