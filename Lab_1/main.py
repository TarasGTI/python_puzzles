import sys


class Helpers(object):

    def name(self):
        return "Helpful functions"

    def sum(self, numbers):
        summary = 0
        for number in numbers:
            summary += int(number)
        return int(summary)

    def is_sum_equal(self, numbers, eq_to_number):
        if sum(numbers) == int(eq_to_number):
            return True
        else:
            return False


helper = Helpers()

# Get all arguments  of script without script name (argument[0])
##input_arguments = sys.argv.pop(0)
input_arguments = [1, 33, 10, 0, 9, 3, 7, 5, 3, 9, 6, 0]
equal_to_number = 10

for argument_id, argument in enumerate(input_arguments):
    for sub_argument_id, sub_argument in enumerate(input_arguments):
        if sub_argument_id < argument_id:
            continue
        else:
            if helper.is_sum_equal([argument, sub_argument], equal_to_number):
                print(argument, "+", sub_argument)
            else:
                continue

input("Press Enter to continue...")
