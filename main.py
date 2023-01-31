import sys
class Helpers(object):
    def name(self):
        return "Helpfull functions"
    def sum(self, numbers):
        summary = 0
        for number in numbers:
            summary += number
        return summary
    def is_sum_equal(self, numbers, eq_to_number ):
        if sum(numbers) == eq_to_number:
            return True
        else:
            return False

helper = Helpers()

# Get all arguments  of script without script name (argument[0])
input_arguments = sys.argv.pop(0)

#####Debug shit
###print(summaryOfTwo.sum([1,7,10,11]))
print(str(sys.argv), file=sys.stdout)
print(len(sys.argv), file=sys.stdout)

input("Press Enter to continue...")