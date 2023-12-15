class DetectionBuffer:
    def __init__(self, size=5):
        self.size = size
        self.buffer = []

    def add_detection(self, detection):
        if len(self.buffer) >= self.size:
            self.buffer.pop(0)  # Remove the oldest element
        self.buffer.append(detection)  # Add new detection to the end

    def get_detections(self):
        return self.buffer

    def flag_signal(self, threshold=2, object_name='Cap'):
        """
        Checks if the number of 1s in the buffer meets or exceeds a certain threshold.
        Only then it flags a signal.
        """
        return self.buffer.count(object_name) >= threshold


def notification_buffer(buffer_temp,not_flagged_counter):
    if buffer_temp.flag_signal():
        # print("Signal flagged")
        if not_flagged_counter > 2:
            # print(buffer_temp.get_detections())  # Shows the current state of the buffer
            msg='SENT_NOTIFICATION!!!' # 'Notice' #
        else:
            msg = None
        not_flagged_counter = 0  # Reset the counter when flagged
    else:
        # print("Signal not flagged")
        # print(not_flagged_counter)
        not_flagged_counter += 1
        # print(not_flagged_counter)
        msg = None
    return not_flagged_counter, msg
