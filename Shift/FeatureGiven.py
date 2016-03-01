from Data import KinshipContext
from ZipfHypothesis import KinshipLexicon
from Model.Primitives import *
from LOTlib.Evaluation.Eval import primitive

# Info1's Family Tree

Info1_obj = ['Info1', 'A1', 'A2', 'a1', 'a2']

FM_Info1 = [
    ['Info1', 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
     1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    ['A1', 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
     0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
     1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    ['A2', 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    ['a1', 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0,
     1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0,
     1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    ['a2', 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0,
     0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0,
     0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    
distance2 = {'Info1': 1, 'A1': 4, 'A2': 3, 'a1': 2, 'a2': 1}

Info1_tree_context = KinshipContext(Info1_obj,
                                      ['null'], FM_Info1, distance=distance2, ego='Info1')


# Info2 Family Tree
Info2_obj = ['Info2', 'B1', 'B2', 'b1', 'b2', 'b3', 'b4', 'b5']

FM_Info2 = [['Info2', 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
             ['B1', 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
             ['B2', 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
             ['b1', 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
             ['b2', 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             ['b3', 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
             ['b4', 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
             ['b5', 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]]

distance = {'Info2': 1, 'B1': 8, 'B2': 7, 'b1': 6, 'b2': 5, 'b3': 4, 'b4': 3, 'b5': 2}


Info2_tree_context = KinshipContext(Info2_obj,
                                       ['null'],FM_Info2, distance=distance, ego='Info2')

# Original Tree

original_obj = ['George', 'Lucille', 'Oscar', 'Michael', 'Gob', 'Lindsay', 'Buster', 'Tobias', 'GeorgeMichael', 'Maebe',
                'Annyong']

# Skin, Hair, Facial, Height, Weight, Age, BRF, F0, HairLength
#  3	 6	 2	3	3      3    2 	 2      4
FM_original = [['George', 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
               ['Lucille', 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               ['Oscar', 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
               ['Michael', 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
               ['Gob', 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
               ['Lindsay', 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
               ['Buster', 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
               ['Tobias', 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
               ['GeorgeMichael', 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               ['Maebe', 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
               ['Annyong', 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0]]

distance3 = {'Annyong': 1,
             'Maebe': 2,
             'GeorgeMichael': 3,
             'Buster': 4,
             'Tobias': 6,
             'Lindsay': 5,
             'Gob': 7,
             'Michael': 8,
             'Oscar': 9,
             'Lucille': 10,
             'George': 11
            }

original_tree_context = KinshipContext(original_obj,
                                       [('null', 'james', 'Luna'), ('null', 'james', 'harry'),
                                        ('null', 'Lily', 'Luna'),
                                        ('null', 'Lily', 'harry'), ('null', 'harry', 'Mellissa'),
                                        ('null', 'harry', 'salem'),
                                        ('null', 'harry', 'Sabrina'), ('null', 'Hermione', 'Mellissa'),
                                        ('null', 'Hermione', 'salem'), ('null', 'Hermione', 'Sabrina'),
                                        ('null', 'Mellissa', 'fabio'), ('null', 'Mellissa', 'Clarice'),
                                        ('null', 'joey', 'fabio'),
                                        ('null', 'joey', 'Clarice'), ('null', 'salem', 'gary'),
                                        ('null', 'salem', 'Amanda'),
                                        ('null', 'Zelda', 'gary'), ('null', 'Zelda', 'Amanda'),
                                        ('null', 'Sabrina', 'Katniss'),
                                        ('null', 'Sabrina', 'peeta'), ('null', 'Sabrina', 'Prue'),
                                        ('null', 'frodo', 'Katniss'),
                                        ('null', 'frodo', 'peeta'), ('null', 'frodo', 'Prue'),
                                        ('null', 'fred', 'ron'),
                                        ('null', 'fred', 'Hermione'), ('null', 'Anne', 'ron'),
                                        ('null', 'Anne', 'Hermione'),
                                        ('null', 'gandalf', 'Eowyn'), ('null', 'gandalf', 'aragorn'),
                                        ('null', 'Galadriel', 'Eowyn'), ('null', 'Galadriel', 'aragorn'),
                                        ('null', 'aragorn', 'merry'), ('null', 'aragorn', 'Leia'),
                                        ('null', 'aragorn', 'frodo'),
                                        ('null', 'Arwen', 'merry'), ('null', 'Arwen', 'Leia'),
                                        ('null', 'Arwen', 'frodo'),
                                        ('null', 'merry', 'Rose'), ('null', 'merry', 'sam'),
                                        ('null', 'Brandy', 'Rose'),
                                        ('null', 'Brandy', 'sam'), ('null', 'Leia', 'luke'),
                                        ('null', 'Leia', 'Padme'),
                                        ('null', 'han', 'luke'), ('null', 'han', 'Padme'),
                                        ('null', 'elrond', 'legolas'),
                                        ('null', 'elrond', 'Arwen'), ('null', 'Celebrindal', 'legolas'),
                                        ('null', 'Celebrindal', 'Arwen'), ('null', 'james', 'Lily'),
                                        ('null', 'Lily', 'james'),
                                        ('null', 'harry', 'Hermione'), ('null', 'Hermione', 'harry'),
                                        ('null', 'Mellissa', 'joey'), ('null', 'joey', 'Mellissa'),
                                        ('null', 'salem', 'Zelda'),
                                        ('null', 'Zelda', 'salem'), ('null', 'Sabrina', 'frodo'),
                                        ('null', 'frodo', 'Sabrina'),
                                        ('null', 'fred', 'Anne'), ('null', 'Anne', 'fred'),
                                        ('null', 'gandalf', 'Galadriel'),
                                        ('null', 'Galadriel', 'gandalf'), ('null', 'aragorn', 'Arwen'),
                                        ('null', 'Arwen', 'aragorn'), ('null', 'merry', 'Brandy'),
                                        ('null', 'Brandy', 'merry'),
                                        ('null', 'Leia', 'han'), ('null', 'han', 'Leia'),
                                        ('null', 'elrond', 'Celebrindal'),
                                        ('null', 'Celebrindal', 'elrond')], FM_original, distance=distance3,
                                       ego='peeta')

# Not sure what I'm supposed to replace this with. New matrix to replace original_tree_context?
the_context = original_tree_context

@primitive
def feature_(key, num, context):
    do = set()
    for person in context.features:
        if num == int(person[key]):
            do.add(person[0])
    return do


from LOTlib.Grammar import Grammar

char_grammar = Grammar()

char_grammar.add_rule('START', '', ['CHAR'], 1.0)

# SET THEORETIC
char_grammar.add_rule('CHAR', 'union_', ['CHAR', 'CHAR'], 1.0)
char_grammar.add_rule('CHAR', 'complement_', ['CHAR', 'C'], 1.0)
char_grammar.add_rule('CHAR', 'intersection_', ['CHAR', 'CHAR'], 1.0)
char_grammar.add_rule('CHAR', 'setdifference_', ['CHAR', 'CHAR'], 1.0)

char_grammar.add_rule('CHAR', 'feature_', ['KEY', 'NUM', 'C'], float(len(the_context.features[0])-1))

for f in xrange(len(the_context.features[0])-1):
    char_grammar.add_rule('KEY', str(f+1), None, 1.0)

char_grammar.add_rule('NUM', '1', None, 1.0)
char_grammar.add_rule('NUM', '0', None, 1.0)



# DEFINING GRAMMAR
def_grammar = Grammar()

def_grammar.add_rule('START', '', ['DEF'], 1.0)

# TREE
def_grammar.add_rule('DEF', 'nulls_of_', ['DEF', 'C'], 1.0)
def_grammar.add_rule('DEF', 'children_of_', ['DEF', 'C'], 1.0)
def_grammar.add_rule('DEF', 'nulls_of_', ['DEF', 'C'], 1.0)

# SET THEORETIC
def_grammar.add_rule('DEF', 'union_', ['DEF', 'DEF'], 1.0)
def_grammar.add_rule('DEF', 'complement_', ['DEF', 'C'], 1.0)
def_grammar.add_rule('DEF', 'intersection_', ['DEF', 'DEF'], 1.0)
def_grammar.add_rule('DEF', 'setdifference_', ['DEF', 'DEF'], 1.0)

# GENDER
def_grammar.add_rule('DEF', 'female_', ['DEF'], 1.0)
def_grammar.add_rule('DEF', 'male_', ['DEF'], 1.0)

def_grammar.add_rule('DEF', 'X', None, 100.0)
