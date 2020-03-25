'''
Created on 24 mar. 2020 г.

@author: maxx
'''


class Finder(object):
    '''
    This class make precomputations in constructor:
    self.list_of_strings - contains copy of the input list
    
    self.dict_of_count_letters - dict where keys are the lengths of the strings from the self.list_of_strings
        vals are the sets of the indexes in self.list_of_strings
    example:
    {1: set(1,2),
    2: set(3)}
    
    self.dict_precalc_values - dict where keys are the unique letters from self.list_of_strings
        vals are the new dicts 
            keys are counts how much the letter contains in the string from the each of self.list_of_strings
            vals are the sets of the indexes in self.list_of_strings
    example:
    { 'a' : {1:set(1,2), 2:set(3)}, 
    'b':{2:set(3)}}
    
    '''

    def __init__(self, input_string_list):
        '''
        Constructor
        I can append parameter "deep_copy", but I'm not sure if this is necessary. Need to look at the full task.
        '''
        # append simple checks of the input parameter types
        if not isinstance(input_string_list, list) or not all(isinstance(val, str) for val in input_string_list):
            raise TypeError('type should be list of strings')
        
        #initial defines
        self.list_of_strings = input_string_list
        self.dict_of_count_letters = {}
        self.dict_precalc_values = {}
        
        #iterate over each string by index
        for idx in range(len(self.list_of_strings)):
            # calculating self.dict_of_count_letters - dict {length: set(indexes)}
            if len(self.list_of_strings[idx]) in self.dict_of_count_letters:
                self.dict_of_count_letters[len(self.list_of_strings[idx])].add(idx)
            else:
                self.dict_of_count_letters[len(self.list_of_strings[idx])] = {idx}

            #get unique letters with counts
            temp_dict = self.get_uniq_count(self.list_of_strings[idx])
                            
            for key, val in temp_dict.items():
                #first init self.dict_precalc_values for each uniq letter
                #to have possibility to work with self.dict_precalc_values[key] as dict below
                if key not in self.dict_precalc_values:
                    self.dict_precalc_values[key] = {}

                #storing the index of the string from self.list_of_strings
                if val in self.dict_precalc_values[key]:
                    self.dict_precalc_values[key][val].add(idx)
                else:
                    self.dict_precalc_values[key][val] = {idx}
        
    def get_uniq_count(self, in_str):
        '''
        return dict where the keys are the unique letters
            the vals are the count of occurrences
        '''
        temp_dict = {}
        for letter in in_str:
            temp_dict[letter] = temp_dict.get(letter, 0) + 1;
        return temp_dict
        
    def find(self, in_str):
        '''
        The function will return all strings from the init list that
        contain the exact same characters as the string `in_str`.
        '''
        #first stage - get all indexes contains the same length
        if len(in_str) in self.dict_of_count_letters:
            result_set = self.dict_of_count_letters[len(in_str)]
        else:
            # input string differ from any by length
            return []
        
        #getting dict of the unique letters for in_str
        temp_dict = self.get_uniq_count(in_str)
                
        for letter, count in temp_dict.items():
            # the set of indexes are limited for each letter
            result_set &= self.dict_precalc_values.get(letter, {}).get(count, set())
            if not result_set:
                #finish loop earlier if discrepancy was presented
                return []
        # converting result set to the list
        return [self.list_of_strings[idx] for idx in result_set]
                
        
