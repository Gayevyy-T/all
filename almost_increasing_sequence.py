#Given a sequence of integers as an array, 
#determine whether it is possible to obtain a strictly 
#increasing sequence by removing no more than one element from the array.
def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True

    def IncreasingSequence(test_sequence):
        if len(test_sequence) == 2:
            if test_sequence[0] < test_sequence[1]:
                return True
        else:
            for i in range(0, len(test_sequence)-1):
                if test_sequence[i] >= test_sequence[i+1]:
                    return False
                else:
                    pass
            return True

    for i in range(0, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            test_seq1 = sequence[:i] + sequence[i + 1:]
            test_seq2 = sequence[:i + 1] + sequence[i + 2:]
            print(test_seq1)
            print(test_seq2)
            if IncreasingSequence(test_seq1) == True:
                print("True")
                return True
            elif IncreasingSequence(test_seq2) == True:
                print("True")
                return True
            else:
                print("False")
                return False

#sequence = [10, 1, 2, 3, 4, 5]#true
sequence = [1, 4, 10, 4, 2] #false
almostIncreasingSequence(sequence)

#============================MY VERSION=============================================
def almostIncreasingSequence(sequence):
    x = 0
    for index in range(0, len(sequence) - 1):
        if sequence[index] < sequence[index + 1]:
            x += 0
        else:
            x += 1
            try:
                if sequence[index] is sequence[0]:
                    continue
                elif sequence[index - 1] < sequence[index + 1]:
                    continue
                elif sequence[index] < sequence[index + 2]:
                    continue
                else:
                    x += 1
            except:
                pass
    if x <= 1:
        return True
    return False
        

#sequence = [1, 2, 5, 3, 5]  #expected --> true
#sequence = [1, 2, 1, 2]     #expected --> false
#sequence = [1, 2, 3, 4, 3, 6] #expected --> true
print(almostIncreasingSequence(sequence))

