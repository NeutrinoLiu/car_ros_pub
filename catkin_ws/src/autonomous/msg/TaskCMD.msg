# 0x00 reset reserved
# 0x01 drive_to
# 0x02 park
# 0x03 return_to_dock
# 0x04 start_clock
# 0x05 wait_at_barrier
# 0x06 wait_until
int8 task_type

float64 tox
float64 toy
int64 atTime
bool stop_flag
string name
int32 count
