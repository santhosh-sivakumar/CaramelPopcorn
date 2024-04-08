class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while(True):

            if (len(sandwiches) == 0) and (len(students) == 0):
                return 0

            if(sandwiches[0] in students):
                if(sandwiches[0] == students[0]):
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    tmp = students[0]
                    students.pop(0)
                    students.append(tmp)
            else:
                break

        return len(students)