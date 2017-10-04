
import os


class Cfdem_creator:
    
    parameter_dict = {}
    
    def __init__(self):
        
        exec(open("./cfdem_settings.py").read(), globals())
        self.parameter_dict = settings

    def create_directories(self): 
        for dir in self.parameter_dict['folder_list']: os.makedirs(dir, 
                                                            
                                                                   exist_ok = True)

    def _write_string(self, outfile, key, value, indents = 0):
        outfile.write('\n')
        for i in range(indents): outfile.write('\t')
        outfile.write(key + ' ' + value + ';\n')
        

    def _write_dictionary(self, outfile, dictionary, 
                          key_requirement   = None, 
                          key_remove      = None,
                          indents       = 0):
        
        for key, value in dictionary.items():
            
            use_key = True
            
            if not key_requirement == None:
                if not key_requirement in key:
                    use_key = False

            write_key = key
            if not key_remove == None:
                write_key = key.replace(key_remove, '') 
            
            if write_key[0] == '_': use_key = False
            
            if use_key:
            
                if value == None:
                    outfile.write('\n' + write_key + '\n(\n);\n') 
                
                # write string         
                if value.__class__ == 'string'.__class__:
                    new_indents = indents
                    if indents > 0: new_indents = indents + 1
                    self._write_string(outfile, write_key, value, indents = new_indents)
            
                # write tuple
                if value.__class__ == (1,2).__class__:
                    new_indents = indents
                    if indents > 0: new_indents = indents + 1
                    self._write_tuple(outfile, write_key, value, indents = new_indents)
                    
                if value.__class__ == {}.__class__:
                    new_indents = indents
                    if indents > 0: new_indents = indents + 1
                    self._write_dictionary(outfile, value, key_requirement = None, 
                                           key_remove = None, indents = new_indents)
                    
                      #  (outfile, write_key, value, indents = new_indents)

                # write length one tuple
                #if value.__class__ == (1,2).__class__ and :
        outfile.write('\n')       


    def _write_tuple(self, outfile, key, tuple, 
                     indents            = 0,
                     write_liggghts     = False,
                     write_key          = True):
        
        if key == None:
            write_key           = False
        
        if indents == 0: outfile.write('\n')
        for i in range(indents): outfile.write('\t')
        if write_key: outfile.write(key + '\n')   
        for i in range(indents): outfile.write('\t')
        if write_key: outfile.write('(\n')
        
        for item in tuple:
            
            for i in range(indents + 1): outfile.write('\t')
            
            # keyword tuple contains tuples (vectors)
            if item.__class__ == (1,2).__class__: 
                
                if write_liggghts:
                    outstr = ''
                    for tuple_item in item:
                        outstr = outstr + tuple_item + ' '
                else:
                    outstr = str(item).replace(',', ' ')
                  
                outfile.write(outstr + '\n')
            
            # keyword tuple contains strings
            if item.__class__ == 'string'.__class__:
                outfile.write(item + '\n')
                
            # keyword tuple contains dictionary
            if item.__class__ == {}.__class__:
                outfile.write('{\n')
                self._write_dictionary(outfile, item, indents = indents + 1)
                for i in range(indents + 1): outfile.write('\t')
                outfile.write('}\n')
            
            
            
                
        
        
        for i in range(indents): outfile.write('\t')
        
        if write_key: outfile.write(');\n')
        
        
    
    def create_blockMeshDict(self):
        
        self.create_directories()
        
        outfile = open(self.parameter_dict['cfd.system.blockMeshDict._location'], 'w')
        
        self._write_dictionary(outfile, self.parameter_dict, 
                               key_requirement  = 'cfd.system.blockMeshDict.', 
                               key_remove       = 'cfd.system.blockMeshDict.', 
                               indents          = 0)
        
#         for key, value in self.parameter_dict.items():
#             
#             if value == None:
#                outfile.write('\n' + key.replace('cfd.system.blockMeshDict.', '') + '\n(\n);\n') 
#             
#             if not 'cfd.system.blockMeshDict.' in key: continue
#             
#             if 'cfd.system.blockMeshDict._' in key: continue
#             
#             if value.__class__ == 'string'.__class__:
#                 outfile.write(key.replace('cfd.system.blockMeshDict.', '') + ' ' + value + ';\n')
#         
#             if value.__class__ == (1,2).__class__:
#                 self._write_tuple(outfile, key.replace('cfd.system.blockMeshDict.', ''), value)
#                 
        outfile.close()
        
    
    def create_liggghts_inputs(self):
        
        self.create_directories()    
        
        outfile = open(self.parameter_dict['dem.in_liggghts_init._location'], 'w')
        
        self._write_tuple(outfile, None, 
                          self.parameter_dict['dem.init'],
                          indents           = 0,
                          write_liggghts    = True)
        
    def replace_liggghts_command(self,
                                 main_key, 
                                 to_be_replaced = None,
                                 replace_with   = None):
        
        new_lt = []
        
        for lt in self.parameter_dict[main_key]:
            
            if lt == to_be_replaced:
                new_lt.append(replace_with)
                print('replaced:\n\t%s\nwith:\n\t%s' % (str(lt), 
                                                        str(replace_with)))
            else: 
                new_lt.append(lt)
        
        self.parameter_dict[main_key] = tuple(new_lt)
        
        
    
#if __name__ == '__main___':
 
        
        





