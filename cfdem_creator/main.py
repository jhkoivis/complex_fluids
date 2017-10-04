
import cfdem_creator

cc = cfdem_creator.Cfdem_creator()  

a = ('fix', 'm4', 'all', 'property/global', 
     'coefficientFriction', 'peratomtypepair','2',
     '0.13', '0.13', '0.13', '0.13')

b = ('fix', 'm4', 'all', 'property/global', 
     'coefficientFriction', 'peratomtypepair','2',
     '0.15', '0.15', '0.15', '0.15')

cc.replace_liggghts_command('dem.init', a, b)


cc.create_blockMeshDict()    
cc.create_liggghts_inputs()





