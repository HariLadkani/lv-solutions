class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        '''
        0   0   1   0   1   1    
        0   0   0   1   2   4  operations left
        0   0   0   1   1   2 balls left

       11   8   5   3   1   0  operations right     
       3    3   2   2   1   0    balls right



        0   0   1   1   1   1    
        0   0   0   1   3   6  operations
        0   0   0   1   2   3 balls

        operation[i] = balls[i-1] + operations[i-1] + (1 if boxes[i-1] == 1 else 0)
        balls[i] = balls[i-1] + (1 if boxes[i-1] == 1 else 0)

        '''
        res = []
        def get_operations(input_boxes):
            balls, operations = [0], [0]
        

            for i in range(1, len(input_boxes)):
                total_balls = balls[i-1] + (1 if input_boxes[i-1] == '1' else 0)
                balls.append(total_balls)
                total_operations = balls[i-1] + operations[i-1] + (1 if input_boxes[i-1] == '1' else 0)
                operations.append(total_operations)

            return operations

        left_operations = get_operations(boxes)
        right_operations = get_operations(boxes[::-1])
        right_operations.reverse()

        for left, right in zip(left_operations, right_operations):
            res.append(left+right)

        return res
        