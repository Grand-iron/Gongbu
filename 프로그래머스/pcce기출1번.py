def solution(video_len, pos, op_start, op_end, commands):
    video_len_mm = int(video_len[0:2])
    video_len_ss = int(video_len[3:5])
    pos_mm = int(pos[0:2])
    pos_ss = int(pos[3:5])
    op_start_mm = int(op_start[0:2])
    op_start_ss = int(op_start[3:5])
    op_end_mm = int(op_end[0:2])
    op_end_ss = int(op_end[3:5])
    
    for command in commands:
        if (op_start_mm < pos_mm < op_end_mm) or \
           (pos_mm == op_start_mm and pos_ss >= op_start_ss) or \
           (pos_mm == op_end_mm and pos_ss <= op_end_ss):
            pos_mm = op_end_mm
            pos_ss = op_end_ss
        
        # Check if exceeds video length
        if pos_mm > video_len_mm or (pos_mm == video_len_mm and pos_ss >= video_len_ss):
            pos_mm = video_len_mm
            pos_ss = video_len_ss
            
        if command == 'prev':
            if pos_ss < 10:
                if pos_mm > 0:
                    pos_mm -= 1
                    pos_ss = 60 - (10 - pos_ss)
                else:
                    pos_mm = 0
                    pos_ss = 0
            else:
                pos_ss -= 10
        else:  # 'next'
            if pos_ss + 10 >= 60:
                pos_mm += 1
                pos_ss = (pos_ss + 10) - 60
            else:
                pos_ss += 10
        
        # Check if within the operation range
        if (op_start_mm < pos_mm < op_end_mm) or \
           (pos_mm == op_start_mm and pos_ss >= op_start_ss) or \
           (pos_mm == op_end_mm and pos_ss <= op_end_ss):
            pos_mm = op_end_mm
            pos_ss = op_end_ss
        
        # Check if exceeds video length
        if pos_mm > video_len_mm or (pos_mm == video_len_mm and pos_ss >= video_len_ss):
            pos_mm = video_len_mm
            pos_ss = video_len_ss

    # Format the output
    answer = f"{pos_mm:02}:{pos_ss:02}"
    return answer
