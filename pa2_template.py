

def letter_only(grade):
    if grade <= 59.4:
        return ("F")
    elif grade <= 69.4:
        return ("D")
    elif grade <= 79.4:
        return ("C")
    elif grade <= 89.4:
        return ("B")
    else:
        return ("A")
pass

def symbol_only(grade):
    if grade <= 69.4:
        return ("")
    elif grade <= 71.4:
        return ("-")
    elif grade >= 77.5 and grade <= 79.4:
        return ("+")
    elif grade <= 81.4:
        return ("-")
    elif grade >= 87.5 and grade <= 89.4:
        return ("+")
    elif grade <= 91.4:
        return ("-")
    elif grade >= 97.5:
        return ("+")
pass

def exam_pass(midterm, final):
    ''' Returns a Boolean that represents whether the midterm and final
    parameter grades result in an exam component pass according to the
    CS112 policies in Sp24.
    Assumes 0 <= midterm, final <= 100. '''
    if midterm <= 59.9 and final <=59.9:
        return (False)
    elif midterm <=59.9  and final >= 60.0:
        return (True)

def course_letter_grade(quiz, zy, lab, pa, mid, fin):
    ''' Returns the course letter grade according to the weight of one's 
    quiz, zybooks, lab, pa, midterms, and finals based off of the 
    established CS112 syllabus in Sp24.
    Assumes 0 <= quiz, zy, lab, pa, mid, fin <= 100.
    Args:
        quiz (float): Represents a students quiz grade
        quiz_percent (float): The quiz value as a decimal representing 
        the percent weight of quizzes in one's final grade

        zy (float): Represents a students zybook grade
        zy_percent (float):The zybook value as a decimal representing 
        the percent weight of zybooks in one's final grade

        lab (float): Represents a students lab grade
        lab_percent (float):The lab value as a decimal representing 
        the percent weight of labs in one's final grade

        pa (float): Represents a students pa grade
        pa_percent (float):The pa value as a decimal representing 
        the percent weight of pa in one's final grade

        mid (float): Represents a students midterm grade
        mid_percent (float):The midterm alue as a decimal representing 
        the percent weight of midterms in one's final grade

        fin (float): Represents a students final exam grade
        fin_percent (float):The final exam value as a decimal 
        representing the percent weight of the final in one's final 
        grade
        
        course_letter_grade (float): represents the course grade as a
        an overall value and is a compostite of all other args.
    Returns: 
        str: Represents the final letter grade. Possible values are
        letters F through A and can have adjacent + or - depending
        on grade
    '''
    quiz_percent = 0.03 
    zy_percent = 0.02 
    lab_percent = 0.10 
    pa_percent = 0.40 
    mid_percent = 0.20 
    fin_percent = 0.25
    if mid < fin: 
        mid = fin
    if mid <= 59.50 and fin <=59.50:
        return ("F")
    else:
        course_letter_grade = (quiz * quiz_percent + zy * zy_percent
                                + lab * lab_percent + pa * pa_percent 
                                + mid * mid_percent + fin * fin_percent)
        if course_letter_grade <= 59.4:
            return ("F")
        elif course_letter_grade <= 69.4:
            return ("D")
        elif course_letter_grade <= 71.4:
            return ("C-")
        elif course_letter_grade <= 77.4:
            return ("C")
        elif course_letter_grade >= 77.5 and course_letter_grade <= 79.4:
            return ("C+")
        elif course_letter_grade <= 81.4:
            return ("B-")
        elif course_letter_grade <= 87.4:
            return ("B")
        elif course_letter_grade >= 87.5 and course_letter_grade <= 89.4:
            return ("B+")
        elif course_letter_grade <= 91.4:
            return ("A-")
        elif course_letter_grade <= 97.4:
            return ("A")
        elif course_letter_grade >= 97.5:
            return ("A+")
        
def er_decision_tree():
    ''' Implements an interactive emergency room decision tree
    using if-else statements only '''

    if input('Cephalalgia: (Yes/No) ') == 'Yes':
        print('Non emergent')
    else:
        if input('Chest pain on effort: (Yes/No) ') == 'Yes':
            if input('Dispnea: (Yes/No) ') == 'No':
                print('Emergent')
            else:
                if input('Chest pain at rest: (Yes/No) ') == 'Yes':
                    print('Non emergent')
                else:
                    print('Emergent')
        else:
            print('Emergent')

def er_dt_mod():
    ''' Implements an interactive emergency room decision tree
    using elif clauses '''
    if input('Cephalalgia: (Yes/No) ') == 'Yes':
        print('Non emergent')
    elif input('Chest pain on effort: (Yes/No) ') == 'Yes':
        if input('Dispnea: (Yes/No) ') == 'No':
            print('Emergent')
        elif input('Chest pain at rest: (Yes/No) ') == 'Yes':
            print('Non emergent')
        else:
            print('Emergent')
    else:
        print('Emergent')
    pass