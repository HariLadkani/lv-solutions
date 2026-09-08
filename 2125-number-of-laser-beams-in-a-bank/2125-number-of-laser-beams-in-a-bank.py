class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_row_devices = 0
        res = 0

        ROWS, COLS = len(bank), len(bank[0])

        for row in range(ROWS):
            curr_device_count = 0
            for col in range(COLS):
                if bank[row][col] == '1':
                    curr_device_count += 1
            
            if curr_device_count > 0:
                res += curr_device_count * last_row_devices
                last_row_devices = curr_device_count

        return res
                  
