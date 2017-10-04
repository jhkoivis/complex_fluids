


settings = \
{
    
'root_directory'                        : ['./case'],
'folder_list'                           : ['cfd',
                                           'cfd/system',
                                           'dem'],

'cfd.system.blockMeshDict._location'    : 'cfd/system/blockMeshDict',

'dem.in_liggghts_init._location'           : 'dem/in.liggghts_init',
'dem.in_liggghts_run._location'            : 'dem/in.liggghts_run',       


############################################################
# cfd/system/blockMeshDict
############################################################

'cfd.system.blockMeshDict.FoamFile'     : 
{
    'version'   : '2.0',
    'format'    : 'ascii',
    'class'     : 'dictionary',
    'object'    : 'blockMeshDict'
},

'cfd.system.blockMeshDict.convertToMeters' : 
'1.0',

'cfd.system.blockMeshDict.vertices' : 
(
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0.1),
    (1, 0, 0.1),
    (1, 1, 0.1),
    (0, 1, 0.1)
),
                               
'cfd.system.blockMeshDict.blocks' : 
(
    'hex',
    (0, 1, 2, 3, 4, 5, 6, 7),
    (20, 20, 1),
    'simpleGrading',
    (1, 1, 1,)
),

'cfd.system.blockMeshDict.edges' :
None,

'cfd.system.blockMeshDict.boundary' : 
(
    'movingWall',
        {'type'     : 'wall',
         'faces'    : ((3, 7, 6, 2),)},
    'fixedWalls',
        {'type'     : 'wall',
         'faces'    : ((0, 4, 7, 3),
                       (2, 6, 5, 1),
                       (1, 5, 4, 0))},
    'frontAndBack',
        {'type'     : 'empty',
         'faces'    : ((0, 3, 2, 1),
                       (4, 5, 6, 7))},
),        
##################################                              
'cfd.blockMeshDict.mergePatchPairs' : """
(
);
""",

##########################################################################3

'dem.init' : 
(
    ('units'        , 'si'),
    ('atom_style'   , 'sphere'),
    ('atom_modify'  , 'map array'),
    ('boundary'     , 'f f f'),
    ('newton'       , 'off'),
    ('communicate'  , 'single vel yes'),
    
    ('region'       , 'domain block -0.05 0.05 -0.05 0.05 -0.25 0.25 units box'),
    ('create_box'   , '2 domain'),

    ('neighbor'     , '0.0015 bin'),
    ('neigh_modify' , 'every 1 check no'),
    
    ('fix'          , 'm1'
                    , 'all'   
                    , 'property/global' 
                    , 'youngsModulus'
                    , 'peratomtype' 
                    , '1.0e7'
                    , '1.0e7'),
                    
    ('fix'          , 'm2'
                    , 'all'
                    , 'property/global'
                    , 'poissonsRatio'
                    , 'peratomtype'
                    , '0.2'
                    , '0.2'),
    
    ('fix'          , 'm3'
                    , 'all'
                    , 'property/global'
                    , 'coefficientRestitution'
                    , 'peratomtypepair'
                    , '2'
                    , '0.9'
                    , '0.9'
                    , '0.9'
                    , '0.9'),
                    
    ('fix'          , 'm4'
                    , 'all'
                    , 'property/global'
                    , 'coefficientFriction'
                    , 'peratomtypepair'
                    , '2'
                    , '0.13'
                    , '0.13'
                    , '0.13'
                    , '0.13'),

    ('fix'          , 'pts'
                    , 'all'
                    , 'particletemplate/sphere'
                    , '939193'
                    , 'atom_type'
                    , '1'
                    , 'density'
                    , 'constant'
                    , '2500'
                    , 'radius'
                    , 'gaussian'
                    , 'number'
                    , '0.0005'
                    , '0.00005'),
                    
    ('fix'          , 'pdd'
                    , 'all'
                    , 'particledistribution/discrete'
                    , '67867967'
                    , '1'
                    , 'pts'
                    , '1.0'),
    
    ('fix'          , 'region'
                    , 'factory'
                    , 'cylinder'
                    , 'z'
                    , '0'
                    , '0'
                    , '0.02379'
                    , '0.198'
                    , '0.203'
                    , 'units'
                    , 'box'),
    
    ('fix'          , 'ins'
                    , 'all'
                    , 'insert/rate/region'
                    , 'seed'
                    , '15485863'
                    , 'distributiontemplate'
                    , 'pdd'
                    , 'nparticles'
                    , '400000'
                    , 'particlerate'
                    , '400000'
                    , 'insert_every'
                    , '1000'
                    , 'overlapcheck'
                    , 'yes'
                    , 'vel'
                    , 'constant'
                    , '0.'
                    , '0.'
                    , '-1.0'
                    , 'region'
                    , 'factory'
                    , 'ntry_mc'
                    , '100000'),
    
    ('fix'          , 'cad1'
                    , 'all'
                    , 'mesh/surface'
                    , 'file' 
                    , '../DEM/hopper.stl'
                    , 'type'
                    , '2'
                    , 'scale'
                    , '0.1'),
                    
    ('fix'          , 'geometry'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'mesh'
                    , 'n_meshes'
                    , '1'
                    , 'meshes'
                    , 'cad1'),

    ('fix'          , 'stopper'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'zplane'
                    , '0.0'),
                    
    ('fix'          , 'rod'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'zcylinder'
                    , '0.001'
                    , '0.0'
                    , '0.0'),
                    
    ('fix'          , 'bwall2'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'zplane'
                    , '0.25'),
                    
    ('fix'          , 'bwall3'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'xplane'
                    , '-0.05'),
                    
    ('fix'          , 'bwall4'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'xplane'
                    , '0.05'),
                    
    ('fix'          , 'bwall5'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'yplane'
                    , '-0.05'),
                    
    ('fix'          , 'bwall6'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'yplane'
                    , '0.05'),
                    
    ('pair_style'   , 'gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'),

    ('pair_coeff'   , '*'
                    , '*'),

    ('fix'          , 'integrate'
                    , 'all'
                    , 'nve/sphere'),
    
    ('fix'          , 'grav'
                    , 'all'
                    , 'gravity'
                    , '9.81'
                    , 'vector'
                    , '0.0'
                    , '0.0'
                    , '-1.0'),

    ('timestep'     , '0.000005'),

    ('thermo_style' , 'custom'
                    , 'step'
                    , 'atoms'
                    , 'ke'
                    , 'cpu'),
                    
    ('thermo'       , '10000'),
    
    ('thermo_modify',   'norm'
                    ,    'no'
                    ,   'lost'
                    ,   'ignore'),

    ('fix'          , 'ctg'
                    , 'all'
                    , 'check/timestep/gran'
                    , '1'
                    , '0.01'
                    , '0.01'),
    
    ('run'          , '1'),
    
    ('unfix'        , 'ctg'),
    

    ('region'       , 'topregion'
                    , 'block'
                    , '-0.05'
                    , '0.05'
                    , '-0.05'
                    , '0.05'
                    , '0.0'
                    , '0.25'),

    ('variable'     , 'nh'
                    , 'equal'
                    , '"count(all,topregion)"'),
                    
    ('variable'     , 'nhtime'
                    , 'equal'
                    , 'time'),

    ('fix'          , 'dhprint'
                    , 'all'
                    , 'print'
                    , '100'
                    , '"${nhtime} ${nh}"'
                    , 'append'
                    , 'time_vs_N.txt'),

    ('dump'         , 'dumpstl'
                    , 'all'
                    , 'stl'
                    , '100000'
                    , 'dump*.stl'),
                    
    ('dump'         , 'dmp'
                    , 'all'
                    , 'custom'
                    , '100000'
                    , 'dump*.hopper'
                    , 'id'
                    , 'type'
                    , 'type'
                    , 'x'
                    , 'y'
                    , 'z'
                    , 'ix'
                    , 'iy'
                    , 'iz'
                    , 'vx'
                    , 'vy'
                    , 'vz'
                    , 'fx'
                    , 'fy'
                    , 'fz'
                    , 'omegax'
                    , 'omegay'
                    , 'omegaz'
                    , 'radius'),

    ('run'          , '300000'
                    , 'upto'),
                    
    ('write_restart', 'liggghts_init.restart')),

###############################################################
# DEM/in.liggghts_run
###############################################################

'dem.run' : 
(
    ('units'        , 'si'),
    ('atom_style'   , 'sphere'),
    ('atom_modify'  , 'map array'),
    ('boundary'     , 'f f f'),
    ('newton'       , 'off'),
    ('communicate'  , 'single vel yes'),
    
    ('read_restart' , '../DEM/liggghts_init.restart'),

    ('neighbor'     , '0.0015 bin'),
    ('neigh_modify' , 'every 1 check no'),
    
    ('fix'          , 'm1'
                    , 'all'   
                    , 'property/global' 
                    , 'youngsModulus'
                    , 'peratomtype' 
                    , '1.0e7'
                    , '1.0e7'),
                    
    ('fix'          , 'm2'
                    , 'all'
                    , 'property/global'
                    , 'poissonsRatio'
                    , 'peratomtype'
                    , '0.2'
                    , '0.2'),
    
    ('fix'          , 'm3'
                    , 'all'
                    , 'property/global'
                    , 'coefficientRestitution'
                    , 'peratomtypepair'
                    , '2'
                    , '0.9'
                    , '0.9'
                    , '0.9'
                    , '0.9'),
                    
    ('fix'          , 'm4'
                    , 'all'
                    , 'property/global'
                    , 'coefficientFriction'
                    , 'peratomtypepair'
                    , '2'
                    , '0.13'
                    , '0.13'
                    , '0.13'
                    , '0.13'),
    
    ('fix'          , 'cad1'
                    , 'all'
                    , 'mesh/surface'
                    , 'file' 
                    , '../DEM/hopper.stl'
                    , 'type'
                    , '2'
                    , 'scale'
                    , '0.1'),
                    
    ('fix'          , 'geometry'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'mesh'
                    , 'n_meshes'
                    , '1'
                    , 'meshes'
                    , 'cad1'),

    ('fix'          , 'stopper'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'zplane'
                    , '0.0'),
                    
    ('fix'          , 'rod'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'zcylinder'
                    , '0.001'
                    , '0.0'
                    , '0.0'),
                    
    ('fix'          , 'bwall2'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'zplane'
                    , '0.25'),
                    
    ('fix'          , 'bwall3'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'xplane'
                    , '-0.05'),
                    
    ('fix'          , 'bwall4'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'xplane'
                    , '0.05'),
                    
    ('fix'          , 'bwall5'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'yplane'
                    , '-0.05'),
                    
    ('fix'          , 'bwall6'
                    , 'all'
                    , 'wall/gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'
                    , 'primitive'
                    , 'type'
                    , '2'
                    , 'yplane'
                    , '0.05'),
                    
    ('pair_style'   , 'gran'
                    , 'model'
                    , 'hertz'
                    , 'tangential'
                    , 'history'),

    ('pair_coeff'   , '*'
                    , '*'),
                    
    ('fix'          , 'cfd'
                    , 'all'
                    , 'couple/cfd'
                    , 'couple_every'
                    , '100'
                    , 'mpi'),
                    
    ('fix'          , 'cfd2'
                    , 'all'
                    , 'couple/cfd/force/implicit'),

    ('fix'          , 'integrate'
                    , 'all'
                    , 'nve/sphere'),
    
    ('fix'          , 'grav'
                    , 'all'
                    , 'gravity'
                    , '9.81'
                    , 'vector'
                    , '0.0'
                    , '0.0'
                    , '-1.0'),

    ('timestep'     , '0.000004'),

    ('thermo_style' , 'custom'
                    , 'step'
                    , 'atoms'
                    , 'ke'
                    , 'cpu'),
                    
    ('thermo'       , '10000'),
    
    ('thermo_modify',   'norm'
                    ,    'no'
                    ,   'lost'
                    ,   'ignore'),

    ('fix'          , 'ctg'
                    , 'all'
                    , 'check/timestep/gran'
                    , '1'
                    , '0.01'
                    , '0.01'),
    
    ('run'          , '1'),
    
    ('unfix'        , 'ctg'),
    

    ('region'       , 'topregion'
                    , 'block'
                    , '-0.05'
                    , '0.05'
                    , '-0.05'
                    , '0.05'
                    , '0.0'
                    , '0.25'),

    ('variable'     , 'nh'
                    , 'equal'
                    , '"count(all,topregion)"'),
                    
    ('variable'     , 'nhtime'
                    , 'equal'
                    , 'time'),

    ('fix'          , 'dhprint'
                    , 'all'
                    , 'print'
                    , '100'
                    , '"${nhtime} ${nh}"'
                    , 'append'
                    , 'time_vs_N.txt'),

    ('dump'         , 'dumpstl'
                    , 'all'
                    , 'stl'
                    , '100000'
                    , 'dump*.stl'),
                    
    ('dump'         , 'dmp'
                    , 'all'
                    , 'custom'
                    , '100000'
                    , 'dump*.hopper'
                    , 'id'
                    , 'type'
                    , 'type'
                    , 'x'
                    , 'y'
                    , 'z'
                    , 'ix'
                    , 'iy'
                    , 'iz'
                    , 'vx'
                    , 'vy'
                    , 'vz'
                    , 'fx'
                    , 'fy'
                    , 'fz'
                    , 'omegax'
                    , 'omegay'
                    , 'omegaz'
                    , 'radius'),

    ('unfix'        , 'stopper'),
    
    ('unfix'        , 'rod'),
    
    ('run'          , '1')),
    
#########################################################
# end DEM/in.liggghts_run
#########################################################
}
         