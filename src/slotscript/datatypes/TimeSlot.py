class TimeSlot:
    def __init__(self, start_time: str, end_time: str, slots: int):
        self.start_time = start_time
        self.end_time = end_time
        self.slots = slots

    @classmethod
    def convert_from_line(cls, line: list[str]):
        full_line = " ".join(line)
        time_range, slots = full_line.split("=>")
        start_time, end_time = time_range.split("-")
        return cls(start_time, end_time, int(slots))
